# Process Monitor

## [[COM Hijacking]]
Find COM hijacks
[Process Monitor](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon) shows real-time file system, registry and process activity and is very useful in finding different types of privilege escalation primitives.

Due to the sheer number of events generated, filtering is essential to find the ones of interest. We're looking for:

-   **RegOpenKey** operations.
-   where the _Result_ is **NAME NOT FOUND**.
-   and the _Path_ ends with **InprocServer32**.
 ![](/Images/Hunting-com.png)

Verify that the entry does exist in HKLM, but not in HKCU.
>Get-Item -Path "HKLM:\Software\Classes\CLSID\{AB8902B4-09CA-4bb6-B78D-A8F59079A8D5}\InprocServer32"


```meta
requirements: 
results: 
oss: #win, #linux
source: https://docs.microsoft.com/en-us/sysinternals/downloads/procmon
description: Process Monitor is an advanced monitoring tool for Windows that shows real-time file system, Registry and process/thread activity.
```