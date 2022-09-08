# OneDrive
Steps:
* Install OneDrive from [here](https://hansbrender.com/all-onedrive-versions/)
* Create your payload
* Clone metadata from ColorAdapterClient.dll from C:\Windows\System32\ onto your payload  
* Create the file %localappdata%\Microsoft\OneDrive\ColorAdapterClient.dll  

❗ Use DLL proxying against crashing  

| dll | working | not working |
| --- | ------- | ----------- |
| SspiCli.dll| 20H2 | |
| iertutil.dll| 20H2 | |
| ncrypt.dll| 20H2 | |
| CRYPTBASE.DLL| 20H2 | |
| CRYPTSP.dll| 20H2 | |
| profapi.dll| 20H2 | |
| OneDriveTelemetryExperimental.dll| 20H2 | |
| FileSyncTelemetryExtensions.dll| 20H2 | |
| version.dll| 20H2 | 21H1-19043 |


## Tools
########
########


```meta
ttp: T1000
requirements: 
results: persistence
description: Get Persistence via OneDrive DLL hijacking
```
