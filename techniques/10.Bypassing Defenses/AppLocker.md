# AppLocker
AppLocker  executables, libraries and scripts that are on a system. AppLocker can restrict the execution based on rules defined for the following categories:
* Executable
* Windows Installer
* Script
* Packaged App
* DLLs

These rules can have the following status:
* enforced  
* audit only
* none

**If enforced** everything within that category is blocked. Rules can then be added to allow principals to execute files. The rules themselves can be defined based on file attributes such as path, publisher or hash. AppLocker has a set of default allow rules such as, "allow everyone to execute anything within `C:\Windows\*`".
![](/Images/Pasted%20image%2020220323165007.png)
Custom rules can be applied to block especially ["LOLBAS's"](https://lolbas-project.github.corp/).

Bypassing AppLocker is based on the rules defined
1.  Executing untrusted code via trusts LOLBAS's.
2.  Finding writeable directories within "trusted" paths.
3.  By default, AppLocker is not even applied to Administrators.

ℹ️ By default `C:\Windows` is a trusted location which is being exploited by Cobalt Strike's `jump psexec[64]`.
Uploading into `C:\Windows` requires elevated privileges, but there are places like `C:\Windows\Tasks` that are writeable by standard users. These areas are useful in cases where you have access to a machine (e.g. in an assumed breach scenario), and need to break out of AppLocker to run post-ex tooling.

⚠️DLL enforcement very rarely enabled due to the additional load it can put on a system, and the amount of testing required to ensure nothing will break.


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```