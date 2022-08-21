# Aged Domains

## Purpose
Domains with short lifespan (generally less than 30 days) are often marked as high risk and blocked at clients. Further domains are categorized in different categories such as finance but also phishing. Uncategorised domains or with category 'placeholder' are also considered high risk. 

OPSEC WARNING!: If possible, immediately request a new category, do not check the category beforehand! Otherwise your site is categorised anyways with 'uncategorised' instead of immediately what you want it to be. There is a chance that reassigning categories are verified by analysts. This increases the chance of the domain being categorised as something like 'placeholder' (which is a blocked category at some banks) 

There are four ways to get a domain that will not be blocked by web categorization filters:
* age and categorize a new domain
* buy an expired domain with still a category assigned
* use high trust domain as redirector (f.e. phishingdomain.azureedges.net)
* buy a “subdomain.eu.com” domain (eu.com is not an official top level domain so many solutions look for the age and categorization to eu.com instead of subdomain.eu.com)

## Buy an expired domain with still a category assigned
The previous method takes time (at least 30 days) to work. When a domain is needed in a shorter period, it is often better to buy an expired domain. The downside is that we have less control over how the domain will look like. 

When domains expire, often web categorization services are not updated quickly enough. By buying a domain that has just expired, but is still seen as valid and trusted by these services, we can set this up in a short time.

The following three steps will take care of this: 
* check for an expired domain on expireddomains.net (you will need to make a bogus account)
* check if a category of ‘financial'/’business'/'technology'/… is still assigned to it by the desired web categorization service (see table above)
* buy it on Eurodns

## use high trust domain as redirector
TODO: To be worked out

## Buy a “subdomain.eu.com” domain
eu.com is not an official top level domain so many solutions look for the age and categorization to eu.com instead of subdomain.eu.com 

By default you will get
* age = 26 years
* category = portal/search engine/web hosting (or something similar based on vendor)

Just always check if the security solution you are up against is also checking things this way

This trick does not work against
* umbrella client

## Tools
########
########


```meta
ttp: T1583.001
internal: false
requirements: 
results: 
description: Buying ages domains in order to bypass trust based network filtering
```