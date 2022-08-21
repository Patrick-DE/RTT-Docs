
## [[User enum]]
Enumerate users present on a system
```
proxychains rpcclient 10.0.1.10 -U testuser -P pw
enumdomusers
```

Enumerate the user
`queryuser testuser`


Enumerate the current users privs
`enumprivs`



```meta
requirements: 
results: 
opsec: 
oss: #linux 
source: https://www.mankier.com/1/rpcclient
description: tool for executing client side MS-RPC functions
```