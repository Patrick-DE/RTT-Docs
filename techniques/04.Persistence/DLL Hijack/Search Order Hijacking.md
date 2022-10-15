# Search Order Hijacking

There are many ways an adversary can hijack DLL loads.
* Plant malicious DLLs in a directory that will be searched before the location of a legitimate library, causing Windows to load the malicious DLL. Often this location is the current working directory of the program.
* Remote DLL preloading attacks occur when a program sets its current directory to a remote location such as a Web share before loading a DLL.
* Attackers can also directly modify the search order via DLL redirection, which after being enabled (in the Registry and creation of a redirection file) may cause a program to load a different DLL.
* Priv Esc: If a search order-vulnerable program is configured to run at a higher privilege level, then the adversary-controlled DLL will also be executed at the higher level. To reduce suspician configure the malicious DLLs to also load the legitimate DLLs they were meant to impersonate.

## Safe DLL Search Mode
Disallow loading of remote DLLs. This is included by default in Windows Server 2012+ and is available by patch for XP+ and Server 2003+.
Enable Safe DLL Search Mode to force search for system DLLs in directories with greater restrictions (e.g. %SYSTEMROOT%)to be used before local directory DLLs (e.g. a user's home directory).

GPO  
The Safe DLL Search Mode can be enabled via Group Policy at Computer Configuration > Policies > Administrative Templates > MSS (Legacy): MSS: (SafeDllSearchMode) > Enable Safe DLL search mode.

Registry  
The associated Windows Registry key for this is located at:
`HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\SafeDLLSearchMode`


## Tools
########
########

```meta
ttp: T1574.001
requirements: 
results: persistence
description: Side-loading takes advantage of the DLL search order used by the loader by positioning both the victim application and malicious payload(s) alongside each other.
```
