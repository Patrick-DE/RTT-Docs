
# Commands
```cmd
REM List all alias
    wmic alias list brief
REM Information about the OS
    wmic computersystem list full
REM Available volumes
    wmic volume list brief
```

Domain Controller
Entry: Technique
Tool: Header
-> 

Entry: Technique
Tool: Tag

## [[Domain]]
```cmd
Domain DC and Information
wmic NTDOMAIN GET DomainControllerAddress,DomainName,Roles

List all users
wmic /NAMESPACE:\\root\directory ldap PATH ds_user GET ds_samaccountname

Get all groups
wmic /NAMESPACE:\\root\directory ldap PATH ds_group GET ds_samaccountname

Members of Domain Admins Group
wmic path win32_groupuser where (groupcomponent="win32_group.name='domain admins',domain =='YOURDOMAINHERE'")

List all computers
wmic /NAMESPACE: root directory ldap PATH ds_computer GET
ds_samaccountname
```

## [[Local User+Groups]]
Get local user accounts
```cmd
wmic useraccount list
```

## [[Windows Update]]
List Updates
```cmd
wmic qfe list brief
```

## [[AV-EDR]]
List Antivirus
```cmd
wmic /namespace:\\root\securitycenter2 path antivirusproduct GET displayName, productState, pathToSignedProductExe
```

## [[Sensitive Files]]
Search files containing 'password' in the name
```cmd
wmic DATAFILE where "drive='C:' AND Name like '%password%'" GET Name,readable,size /VALUE
```

## [[Unquoted Service Path]]
List of every service and the path
```cmd
wmic service get name, pathname
Name                                      PathName
ALG                                       C:\Windows\System32\alg.exe
AppVClient                                C:\Windows\system32\AppVClient.exe
AmazonSSMAgent                            "C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe"
[...snip...]
Vuln-Service-1                            C:\Program Files\Vuln Services\Service 1.exe
```


```meta
requirements: 
results: 
opsec: 
oss: #win
source: 
description: VBA Obfuscation Tools combined with an MS office document generator
undetected: 
```
