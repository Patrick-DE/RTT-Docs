# Steal Token
The `steal_token` command will impersonate the access token of the target process. Like `make_token`, only for network, not local actions.

This command opens a handle to another users target process in order to duplicate and impersonate the access token, and therefore requires local admin privileges.
``````beacon
beacon> ls \\srv2\c$
[-] could not open \\srv2\c$\*: 5

beacon> steal_token 3320
[+] Impersonated EDU\doe

beacon> ls \\srv2\c$

 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
 dir     05/10/2022 04:11:30   $Recycle.Bin
 dir     05/10/2022 03:23:44   Boot
 ``````

## Tools
########
########


```meta
ttp: T1558
requirements: admin
results: 
description: 
```
