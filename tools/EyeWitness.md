This is tool capable of identifying (and taking screenshots of) web apps from a list of targets.

## [[Find Web Server]]
Local Scan (does not work)
>./EyeWitness.py --localscan 192.168.1.0/24

Scan with multiple IPs received from NMAP
```sh
cat /root/targets.txt
10.10.17.71
10.10.1.20
10.10.17.68

proxychains4 ./EyeWitness.py --web -f /root/targets.txt -d /root/edu --no-dns --no-prompt

Starting Web Requests (3 Hosts)
Attempting to screenshot http://10.10.17.71
[*] WebDriverError when connecting to http://10.10.17.71
Attempting to screenshot http://10.10.1.20
[proxychains] Strict chain  ...  127.0.0.1:1080  ...  10.10.1.20:80  ...  OK
Attempting to screenshot http://10.10.17.68
[*] WebDriverError when connecting to http://10.10.17.68
Finished in 12.967030048370361 seconds
```

```meta
requirements: 
results: 
oss: #py, #exe
source: https://github.com/FortyNorthSecurity/EyeWitness
description: EyeWitness is designed to take screenshots of websites provide some server header info, and identify default credentials if known.
```