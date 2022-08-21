## Installation
```sh
git clone https://github.com/thewhiteh4t/FinalRecon.git
cd FinalRecon
pip3 install -r requirements.txt
```

## [[Passive Reconnaissance]]
```sh
python3 finalrecon.py -h
usage: finalrecon.py [-h] [--headers] [--sslinfo] [--whois] [--crawl] [--full]
                     url

FinalRecon - OSINT Tool for All-In-One Web Recon | v1.0.0

positional arguments:
  url         Target URL

optional arguments:
  -h, --help  show this help message and exit
  --headers   Get Header Information
  --sslinfo   Get SSL Certificate Information
  --whois     Get Whois Lookup
  --crawl     Crawl Target Website
  --full      Get Full Analysis, Test All Available Options

# Check headers
python3 finalrecon.py --headers <url>

# Check ssl Certificate
python3 finalrecon.py --sslinfo <url>

# Check whois Information
python3 finalrecon.py --whois <url>

# Crawl Target
python3 finalrecon.py --crawl <url>

# full scan
python3 finalrecon.py --full <url>
```


```meta
requirements: 
results: 
opsec: 
oss: #py
source: https://github.com/thewhiteh4t/FinalRecon
description: FinalRecon is an automatic web reconnaissance tool written in python. Goal of FinalRecon is to provide an overview of the target in a short amount of time while maintaining the accuracy of results. Instead of executing several tools one after another it can provide similar results keeping dependencies small and simple.
```

