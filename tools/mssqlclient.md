# mssqlclient.py

## [[MS SQL Servers]]
```bash
proxychains python3 /usr/local/bin/mssqlclient.py -windows-auth EDU/john@10.10.1.20

ProxyChains-3.1 (http://proxychains.sf.net)
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation

Password:
|S-chain|-<>-127.0.0.1:1080-<><>-10.10.1.20:1433-<><>-OK
[*] Encryption required, switching to TLS
[*] ENVCHANGE(DATABASE): Old Value: master, New Value: master
[*] ENVCHANGE(LANGUAGE): Old Value: , New Value: us_english
[*] ENVCHANGE(PACKETSIZE): Old Value: 4096, New Value: 16192
[*] INFO(SRV1): Line 1: Changed database context to 'master'.
[*] INFO(SRV1): Line 1: Changed language setting to us_english.
[*] ACK: Result: 1 - Microsoft SQL Server (130 19162)
[<>] Press help for extra shell commands
SQL> select @@servername;

SRV1
```


```meta
requirements: 
results: 
oss: #linux 
source: Impacket
description: Interact with MSSQL DB
```