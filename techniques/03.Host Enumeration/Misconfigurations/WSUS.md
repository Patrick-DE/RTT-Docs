
1. Gather infos
>reg query HKLM\Software\Policies\Microsoft\Windows\WindowsUpdate /v WUServer
2. Needs to be 1
>HKLM\Software\Policies\Microsoft\Windows\WindowsUpdate\AU /v UseWUServer

## Tools
########
########

```meta
ttp: T1546
requirements: 
results: 
description: Identify if the Windows Update Service is running via the insecure protocol http
```