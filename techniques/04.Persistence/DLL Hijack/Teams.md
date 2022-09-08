# Teams
Path: %localappdata%\Microsoft\Teams\current\  
❗ Use DLL proxying against crashing  

| dll | working | not working |
| --- | ------- | ----------- |
| ncrypt.dll | even without proxying |  |
| CRYPTBASE.DLL |  |  |
| CRYPTSP.dll |  |  |
| crypt32.dll |  |  |
| MSASN1.dll |  |  |
| wintrust.dll |  |  |
| winnlsres.dll |  |  | 
| MSVCP140_CLR0400.dll |  |  |
| version.dll | 21H1-19043 |  |

## Tools
########
########


```meta
ttp: T1000
requirements: 
results: persistence
description: Get Persistence via Teams DLL hijacking
```
