# GPRegistryPolicyParser

## [[Group Policy (GPO)]]
`Parse-PolFile` from the [GPRegistryPolicyParser](https://github.com/PowerShell/GPRegistryPolicyParser) package can be used to convert this file into human-readable format.
```beacon
PS C:\Users\Administrator\Desktop> Parse-PolFile .\Registry.pol

KeyName     : Software\Policies\Microsoft Services\AdmPwd
ValueName   : PasswordComplexity
ValueType   : REG_DWORD
ValueLength : 4
ValueData   : 3    <-- Password contains uppers, lowers and numbers (4 would also include specials)

KeyName     : Software\Policies\Microsoft Services\AdmPwd
ValueName   : PasswordLength
ValueType   : REG_DWORD
ValueLength : 4
ValueData   : 14   <-- Password length is 14

KeyName     : Software\Policies\Microsoft Services\AdmPwd
ValueName   : PasswordAgeDays
ValueType   : REG_DWORD
ValueLength : 4
ValueData   : 7    <-- Password is changed every 7 days

KeyName     : Software\Policies\Microsoft Services\AdmPwd
ValueName   : AdminAccountName
ValueType   : REG_SZ
ValueLength : 14
ValueData   : lapsadmin   <-- The name of the local admin account to manage

KeyName     : Software\Policies\Microsoft Services\AdmPwd
ValueName   : AdmPwdEnabled
ValueType   : REG_DWORD
ValueLength : 4
ValueData   : 1   <-- LAPS is enabled
```


```meta
requirements: 
results: 
opsec: 
oss: #win
source: https://github.com/PowerShell/GPRegistryPolicyParser
description: These cmdlets will allow you to work with .POL files, which contain the registry keys enacted by Group Policy.
```
