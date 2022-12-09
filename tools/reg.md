
## [[PowerShell Logging]]
#get_powershell_logging
```ps
reg query HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Policies\Microsoft\Windows\PowerShell\Transcription
 
reg query HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Policies\Microsoft\Windows\PowerShell\ModuleLogging

reg query HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging

reg query HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\PowerShellCore\Transcription
"EnableTranscripting"=dword:00000001
"OutputDirectory"="c:\\windows\\temp\\pstranscripts"

reg query HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\PowerShell\Transcription
"EnableTranscripting"=dword:00000001
"OutputDirectory"="c:\\windows\\temp\\pstranscripts"
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
oss: #win
source: Windows
description: Registry query stuff
```
