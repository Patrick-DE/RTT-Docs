#pip install bs4 requests datefinder PyPDF2 PyCryptodome
import datetime
import io
import os
import pathlib
import re
from time import sleep
from typing import List
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
import PyPDF2
from dateutil import parser
import datefinder
import random
import json
from aptTypes import APT, exclusion_list

class DateQuery:
    def __init__ (self, query):
        self.query = query
        self.session = self.setupSession()


    def setupSession(self):
        user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14'
        headers = {'User-Agent': user_agent,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}

        se = requests.Session()
        se.headers.update(headers) 
        return se


    def getRequest(self, url, raw=False, cookies = {}):
        try:
            response = self.session.get(url, cookies=cookies)
        except Exception as ex:
            print(ex.message)
            pass

        sc = response.status_code
        if sc != 200:
            raise Exception({"status":sc, "message":"getRequest| HTTP status code {} opening {}".format(sc, url)})    
        
        if raw:
            return response.content
        else:
            return response.text
 
    
    def validateDate(self, date):
        if date == None:
            return None
        newDate = parser.parse(date).date()
        if newDate >= datetime.datetime.now().date():
            return None
        if newDate < datetime.date(2000,1,1):
            return None
        return date


    def googleScrape(self):
        cookies = {"CONSENT":"PENDING+981",
                "SIDCC": "AP8dLtzMp7W0W-BdsEvSL_ca55H54TPD2_HPDtJFJgfo85l5K_AQINBlWXeHcup-0uypbpv3iw",
                "SID": "WQg0c6LKN9gC8anqOwGbentmIMgfzkWtcAclaGT5AW1hglXQiiXzObGzuJLADAGI4HAcfQ.",
                "SOCS":"CAISHAgCEhJnd3NfMjAyMzA1MDItMF9SQzEaAmVuIAEaBgiA1NuiBg",
                "NID":"511=CbhAagpUj_i3LKqcOP6Pp4AYlDC-AibiHRQxvVqUWd-zHQtdyCGxedEzlH_EE5srqlWFuWGrKMZ8EmGvnexks6eSRSZOSbIAZIT4HCm8OvzBILHkk8EI5U9dAJXPZoA5utn3GzNXvXUUbtvW0YSLfzFmWNsvrFKYmZ4Ssvk7Cb8fhrseFlEfsWESR67HD1tkOyeQgW0TU-kXx_B2DHRfIuQKWX5LTskOnTDnnt_ROnMmG6EfdHTnvLaU64gb6IntwEPESC66E8d6TviZ9tNLlAz5fCcLjWpi-9c"}
        
        text = self.getRequest("https://www.google.com/search?q={}&num=1".format(self.query), False, cookies)
        try:
            date = re.search(r"<span class=\".*\">(\d{2}\.\d{2}\.\d{4})</span>", text).group(1)
            return date
        except Exception as ex:
            if hasattr(ex, "name") and ex.name == "group":
                return None
            print("googleScrape| Error: {}".format(ex))
            return None
    
    
    def extractFromURL(self):
        try:
            date = re.search(r"(\d{4}/\d{2})", self.query).group(1).split("/")
            return "01.{}.{}".format(date[1],date[0])
        except:
            return None
    

    def extractFromPDF(self):
        # Fetch the PDF file from the URL
        content = self.getRequest(self.query, True)

        # on web.archive.org the PDF is iframed so fetch the correct URL
        if "web.archive.org" in self.query:
            soup = BeautifulSoup(content, "html.parser")
            meta_tag = soup.find("iframe", id="playback")
            if meta_tag:
                content = self.getRequest(meta_tag["src"], True)
        # sanity check
        if not b'%PDF-1.' == content[:7]:
            raise Exception({"status":500, "message":"extractFromPDF| PDF magic bytes missing for {}".format(self.query)}) 
          
        pdf_file = io.BytesIO(content)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        try:
            date = pdf_reader.metadata.creation_date.strftime('%d.%m.%Y')
        except:
            try:
                date = datetime.datetime.strptime(pdf_reader.metadata.creation_date_raw, 'D:%Y%m%d%H%M%S').strftime('%d.%m.%Y')
            except:
                return None
        return date
    
    
    def fuzzyDateSearch(self):
        date_string = None

        text = self.getRequest(self.query)
        if not text:
            return None
        
        soup = BeautifulSoup(text, "html.parser")

        # Look for publication date in <meta> tags
        meta_tag = soup.find("meta", {"property": "article:published_time"})
        if meta_tag:
            date_string = parser.parse(meta_tag["content"]).strftime('%d.%m.%Y')
        if date_string == None:
            meta_tag = soup.find("meta", {"property": "og:article:published_time"})
            if meta_tag:
                date_string = parser.parse(meta_tag["content"]).strftime('%d.%m.%Y')
        if date_string == None:
            time_tag = soup.find("time", {"itemprop": "datePublished"})
            if time_tag:
                date_string = time_tag["datetime"]
        if date_string == None:
            txt = soup.get_text()
            try:
                dates = list(datefinder.find_dates(txt))
            except Exception as ex:
                print(ex.message)
                return None

            if dates and len(dates) > 0:
                date_string = dates[0].strftime("%d.%m.%Y")
        
        if date_string:
            return date_string
        else:
            return None


def getWebsiteDate(query):
        if query == "":
            return None
        
        q = DateQuery(query)
        date = None

        if pathlib.Path(query).suffix == ".pdf":
            date = q.validateDate(q.extractFromPDF())
        if date == None:
            date = q.validateDate(q.googleScrape())
        if date == None:
            date = q.validateDate(q.extractFromURL())
        if date == None:
            date = q.validateDate(q.fuzzyDateSearch())

        if date:
            print("{}: {}".format(date,query))
            return date
        else:
            print("No date found for {}".format(query))
            return None


f = open('date_mapping.json')
date_mapping: dict = json.load(f)
f.close()

def getReleaseDate():
    f = open('apts.json')
    apt_list: List[APT] = json.load(f)
    f.close()

    ac = len(apt_list)
    for apt in apt_list:
        ac = ac - 1
        tc = len(apt["techniques"])
        for technique in apt["techniques"]:
            tc = tc - 1
            rc = len(technique["group_ref"])
            for ref in technique["group_ref"]:
                rc = rc - 1 
                if ref["date"] != None:
                    continue

                # add to exclusion list if not resolvable or wrong urls
                if ref["url"] in exclusion_list:
                    continue

                # build up a mapping to only query a website once and else fill
                if ref["url"] in date_mapping:
                    ref["date"] = date_mapping[ref["url"]]
                    continue

                try:
                    ref["date"] = getWebsiteDate(ref["url"])
                    date_mapping[ref["url"]] = ref["date"]
                except Exception as ex:
                    eex = ex.args[0]
                    if "message" in eex:
                        print(eex["message"])
                    else:
                        print(eex)
                    if "status" in eex:
                        date_mapping[ref["url"]] = str(eex["status"])

                    # f = open("apts.json", "w")
                    # json.dump([apt for apt in apt_list], f, indent=2)
                    # f.close()
                    # f = open ("date_mapping.json", "w")
                    # json.dump(date_mapping, f, indent=2)
                    # f.close()

                    if "status" in eex and eex["status"] == 429:
                        exit(code=-1)
                    continue
                    
                s = random.randint(10,60)
                print("{}/{}/{}: Sleeping {} seconds".format(ac, tc, rc, s))
                sleep(s)


    f = open ("date_mapping.json", "w")
    json.dump(date_mapping, f, indent=2)
    f.close()
    
    f = open("apts.json", "w")
    json.dump([apt for apt in apt_list], f, indent=2)
    f.close()

getReleaseDate()