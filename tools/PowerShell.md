

## [[LSA Protection]]
`Get-WinEvent -FilterHashtable @{ LogName='system'; Id='12' ; ProviderName='Microsoft-Windows-Wininit' }`

## [[RDP]]
`Get-WinEvent -FilterHashtable @{ LogName='Microsoft-Windows-TerminalServices-RDPClient/Operational'; id='1024' } | select timecreated, message | ft -AutoSize -Wrap`

## [[COM Hijacking]]
List COM objects
`gwmi Win32_COMSetting | ? {$_.progid } | sort | ft ProgId,Caption,InprocServer32`

List COM Object Methods for WScript.Shell.1
`$o = [activator]::CreateInstance([type]::GetTypeFromProgID(("WScript.Shell.1"))) | gm`

## [[Unquoted Service Path]]
Get ACLs of services
```cmd
powershell Get-Acl -Path "C:\Program Files\Vuln Services" | fl
  
Path   : Microsoft.PowerShell.Core\FileSystem::C:\Program Files\Vuln Services
Owner  : BUILTIN\Administrators
Group  : wkstn1\None
Access : CREATOR OWNER Allow  FullControl
 NT AUTHORITY\SYSTEM Allow  FullControl
 BUILTIN\Administrators Allow  FullControl
 BUILTIN\Users Allow  Write, ReadAndExecute, Synchronize
 NT SERVICE\TrustedInstaller Allow  FullControl
 APPLICATION PACKAGE AUTHORITY\ALL APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
 APPLICATION PACKAGE AUTHORITY\ALL RESTRICTED APPLICATION PACKAGES Allow  ReadAndExecute, Synchronize
```

```meta
requirements: 
results: 
opsec: 
oss: #win
source: 
description: PowerShell
```