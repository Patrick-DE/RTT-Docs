## Redirect TCP traffic
```
socat TCP4-LISTEN:80,fork TCP4:<REMOTE>:80
```


```meta
phases: 00
requirements: 
results: 
oss: #linux, #win
source: http://www.dest-unreach.org/socat/
description: 
```