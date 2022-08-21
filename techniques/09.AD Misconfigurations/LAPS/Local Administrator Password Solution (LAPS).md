# Local Administrator Password Solution (LAPS)
When machines are build with a golden image to ensure consistency and compliance every machine receives the same password for each user.

LAPS by Microsoft is a solution to manage credentials of the local administrator (RID 500 or custom) account on every machine. It ensures that the password for each account is different, random, and automatically changed on a defined schedule. 

The process:
1.  The Active Directory schema has two new attributes to computer objects, called `ms-Mcs-AdmPwd` and `ms-Mcs-AdmPwdExpirationTime`.
2.  By default, only a Domain Admin can read the `AdmPwd` attribute. Each computer can update these attributes on its own object.
3.  Rights to read `AdmPwd` can be delegated (users, groups etc).
4.  GPOs are ususally used to deploy LAPS (or SCCM) and its configuration.
6.  On `gpupdate`, the LAPS will check the machines `AdmPwdExpirationTime` attribute. If the received time is passed, it will generate a new password 
and updates the `AdmPwd` attribute.

## Identify
* Via files
  > ls C:\Program Files\LAPS\CSE
* Via GPO guessing [[PowerView#Get GPOs filter with name]]
  The config can be dumped like this [[Dump GPOs]]
* Via searching for computers with ``ms-Mcs-AdmPwdExpirationTime`` [[PowerView#Search computers with property]]
* [[BloodHound#Local Administrator Password Solution (LAPS)]]


## Modify
If LAPS PowerShell cmdlets are installed
```beacon
beacon> powershell Get-Command *AdmPwd*

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Cmdlet          Find-AdmPwdExtendedRights                          5.0.0.0    AdmPwd.PS
Cmdlet          Get-AdmPwdPassword                                 5.0.0.0    AdmPwd.PS
Cmdlet          Reset-AdmPwdPassword                               5.0.0.0    AdmPwd.PS
Cmdlet          Set-AdmPwdAuditing                                 5.0.0.0    AdmPwd.PS
Cmdlet          Set-AdmPwdComputerSelfPermission                   5.0.0.0    AdmPwd.PS
Cmdlet          Set-AdmPwdReadPasswordPermission                   5.0.0.0    AdmPwd.PS
Cmdlet          Set-AdmPwdResetPasswordPermission                  5.0.0.0    AdmPwd.PS
Cmdlet          Update-AdmPwdADSchema                              5.0.0.0    AdmPwd.PS
```

```meta
ttp: T1000
requirements:
results: 
description: 
```