# Proxychains

## [[SOCKS Proxy]]
1. Change configuration:
   ```bash
    nano /etc/proxychains.conf
    - comment out the last line
    + Socks5 127.0.0.1 8080
    ```
2. Use proxychains:
    `proxychains4 nmap -sT -p- 10.0.0.0/24`


```meta
requirements: 
results: 
oss: #linux
source: https://github.com/haad/proxychains
description: Proxies traffix through the netter
```