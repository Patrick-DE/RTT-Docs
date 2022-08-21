
## [[Find Web Server]]
Scan internal network
* Screenshot a single website  
> gowitness single https://www.google.com/
* Screenshot a cidr using 20 threads  
> gowitness scan --cidr 192.168.0.0/24 --threads 20
* Scan based on Nessus scan
> .\gowitness-2.4.0-windows-amd64.exe nessus -f .\ScanniSceneroni_xm6g2a.nessus
* Scan based on URL/IP file
> .\gowitness-2.4.0-windows-amd64.exe file -f '.\External Pentesting\urls.txt'
* Screenshot open http services from an namp file  
> gowitness nmap -f nmap.xml --open --service-contains http
* Run the report server  
> gowitness report serve

```meta
phases: 02,06
requirements: 
results: 
opsec: true
oss: #linux
source: https://github.com/sensepost/gowitness
description: Pictures of webservers
undetected: 
```
