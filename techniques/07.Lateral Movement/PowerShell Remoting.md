# PowerShell Remoting

## Detection
There are multiple steps to this technique that can be used to detect.  We can look for **egress** network connections with a destination port of **5985**.

>event.module : sysmon and event.type : connection and network.direction : egress and destination.port : 5985

There's the process start event for `wsmprovhost.exe` (with an `-Embedding` parameter in the command line arguments).

>event.module : sysmon and event.type : process_start and process.command_line : "C:\\Windows\\system32\\wsmprovhost.exe -Embedding"

PowerShell logging will also provide the script block and/or transactional log, which reveals which code/commands were executed. Use the `process.pid` field from the previous query to find its associated script block.

>event.module : powershell and winlog.process.pid: 2984


## Tools
########
########


```meta
ttp: T1000
requirements: admin
results: 
description: 
```
