# OneDrive
Path: %localappdata%\Microsoft\OneDrive  
Try to load ColorAdapterClient.dll at startup located in C:\Windows\System32\ on win  
Can hijack dll by creating %localappdata%\Microsoft\OneDrive\ColorAdapterClient.dll  

❗ Use DLL proxying against crashing  

| dll | working | not working |
| --- | ------- | ----------- |
| SspiCli.dll| 1909 | |
| iertutil.dll| 1909 | |
| ncrypt.dll| 1909 | |
| CRYPTBASE.DLL| 1909 | |
| CRYPTSP.dll| 1909 | |
| profapi.dll| 1909 | |
| OneDriveTelemetryExperimental.dll| 1909 | |
| FileSyncTelemetryExtensions.dll| 1909 | |
| version.dll| 1909 | 21H1-19043 |


## Tools
########
########


```meta
ttp: T1000
requirements: 
results: persistence
description: Get Persistence via OneDrive DLL hijacking
```
