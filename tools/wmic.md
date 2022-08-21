
## [[Unquoted Service Path]]
List of every service and the path
```cmd
wmic service get name, pathname
Name                                      PathName
ALG                                       C:\Windows\System32\alg.exe
AppVClient                                C:\Windows\system32\AppVClient.exe
AmazonSSMAgent                            "C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe"
[...snip...]
Vuln-Service-1                            C:\Program Files\Vuln Services\Service 1.exe
```

```meta
requirements: 
results: 
opsec: 
oss: #win
source: 
description: VBA Obfuscation Tools combined with an MS office document generator
undetected: 
```
