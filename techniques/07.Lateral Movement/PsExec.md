# PsExec

## Detection
To build a detection, the following markers can be used:
-   File creation.
-   Service installed.
-   Process start.

Cobalt Strike has a few default behaviours that we can profile:
-   It uses the same name for the service and the exe.
-   The name is a random alphanumeric string of length 7.
-   The service binary is always dropped into `C:\Windows`.

Furthermore, `psexec` and `psexec64` are the only `jump` methods that will perform a process migration automatically (by default into `rundll32.exe`) in order to delete the binary. It's parent process will be the service binary and would result in a further process create event.
With psexec/64, the service filename is always a UNC path (e.g. `\\srv1\ADMIN$\fe80480.exe`). 

`psexec_psh` will execute PowerShell via `%COMSPEC%` (resulting in the command line interpreter, usually `cmd.exe`).
If psexec_psh is used, the filepath will be `%COMSPEC% /b /c start /b /min powershell -nop -w hidden -encodedcommand ba`.

>event.module : sysmon and event.type : creation and event.category : file and file.extension : exe and file.directory : "C:\\Windows"

Find the associated service.

>event.provider : "Service Control Manager" and message : "A service was installed"


## Tools
########
########


```meta
ttp: T1000
requirements: 
results: admin
description: Get Persistence via Teams DLL hijacking
```