
## [[PowerShell Logging]]
#get_powershell_logging
```ps
reg query HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Policies\Microsoft\Windows\PowerShell\Transcription
 
reg query HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Policies\Microsoft\Windows\PowerShell\ModuleLogging

reg query HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging
```

## [[PowerShell-Version]]
```ps
reg query HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\1\PowershellEngine /v PowershellVersion

reg query HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\3\PowershellEngine /v PowershellVersion

Get-ItemPropertyValue HKLM:\SOFTWARE\Microsoft\PowerShell\*\PowerShellEngine
-Name PowerShellVersion
```

```meta
requirements: 
results: 
opsec: 
oss: #win
source: Windows
description: Registry query stuff
```