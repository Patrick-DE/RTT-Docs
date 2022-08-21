# PowerShell Remoting

## Detection
When binaries are executed via WMI (using process call create), it will be a child of `WmiPrvSE.exe`. So a process create event where **WmiPrvSE** is the parent will be suspicious. This would also be the case if you use WMI to execute a PowerShell one-liner.

>event.module: sysmon and event.type : process_start and process.parent.name : WmiPrvSE.exe


## Tools
########
########


```meta
ttp: T1000
requirements: wmi, ticket
results: localuser, localadmin, admin
description: Get Persistence via Teams DLL hijacking
```