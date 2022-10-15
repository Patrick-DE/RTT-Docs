# Bypassing Antivirus (AV)

## Show Detected Threads
`Get-MpThreatDetection` is a Windows Defender cmdlet that can also show detected threats.
```beacon
beacon> remote-exec winrm dc-1 Get-MpThreatDetection | select ActionSuccess, DomainUser, ProcessName, Resources

ActionSuccess  : True
DomainUser     : 
ProcessName    : Unknown
Resources      : {file:_C:\Windows\v34gs462.exe, file:_\\dc-1\ADMIN$\v34gs462.exe}
PSComputerName : dc-1

ActionSuccess  : True
DomainUser     : EDU\patrick
ProcessName    : C:\Windows\System32\wsmprovhost.exe
Resources      : {amsi:_C:\Windows\System32\wsmprovhost.exe}
PSComputerName : dc-1
```

## Cobalt Strike Kits
- [[Artifact Kit]]
- [[Resource Kit]]
- Elevate Kit
- Persistence Kit
- Mimikatz Kit
- Sleep Mask Kit
- Thread Stack Spoofer


## Tools
########
########


```meta
ttp: TA0005
requirements:
results: 
description: 
```