# OneDrive
OneDrive.exe is located at %localappdata%\Microsoft\OneDrive
Try to load ColorAdapterClient.dll at startup located in C:\Windows\System32\ on win
Can hijack dll by creating %localappdata%\Microsoft\OneDrive\ColorAdapterClient.dll
With DLL proxying against crashing

These are some of the dll working as of november 2021:  
Path: "C:\Users\AppData\Local\Microsoft\OneDrive\"  
* SspiCli.dll
* iertutil.dll
* ncrypt.dll
* CRYPTBASE.DLL
* CRYPTSP.dll
* profapi.dll
* OneDriveTelemetryExperimental.dll
* FileSyncTelemetryExtensions.dll




## Tools
########
########


```meta
ttp: T1000
requirements: 
results: persistence
description: Get Persistence via OneDrive DLL hijacking
```