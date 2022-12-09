
Returns 0 if disabled.
`$(Get-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\Windows NT\DNSClient" -name EnableMulticast).EnableMulticast`

If it returns an error then it is not set.
`Get-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\Windows NT\DNSClient" -name EnableMulticast`


## Tools
########
########

```meta
ttp: T1557.001
requirements: 
results: 
description: Identify weaknesses on the local system
```
