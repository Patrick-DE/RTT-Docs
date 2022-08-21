# Search Order Hijacking
There are many ways an adversary can hijack DLL loads.
* Plant malicious DLLs in a directory that will be searched before the location of a legitimate library, causing Windows to load the malicious DLL. Often this location is the current working directory of the program.
* Remote DLL preloading attacks occur when a program sets its current directory to a remote location such as a Web share before loading a DLL.
* Attackers can also directly modify the search order via DLL redirection, which after being enabled (in the Registry and creation of a redirection file) may cause a program to load a different DLL.
* Priv Esc: If a search order-vulnerable program is configured to run at a higher privilege level, then the adversary-controlled DLL will also be executed at the higher level. To reduce suspician configure the malicious DLLs to also load the legitimate DLLs they were meant to impersonate.


## Tools
########
########

```meta
ttp: T1574.001
requirements: 
results: persistence
description: Side-loading takes advantage of the DLL search order used by the loader by positioning both the victim application and malicious payload(s) alongside each other.
```