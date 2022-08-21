# Make Token
The Cobalt Strike command `make_token` uses the [LogonUserA](https://docs.microsoft.com/en-gb/windows/win32/api/winbase/nf-winbase-logonusera) to get a process handle with the users token. For that it requires the username, domain and plaintext password and the logon type **LOGON32_LOGON_NEW_CREDENTIALS**.

From MS:
> This logon type allows the caller to clone its current token and specify new credentials for outbound connections. The new logon session has the same local identifier but uses different credentials for other network connections.

The local identifier stays the same since it uses the own token!  
* `getuid` stays  **EDU\john**
* network connections use new user token
* no local admin privs are required
* To revert the token, use `rev2self`.

``````beacon
beacon> getuid
[*] You are EDU\john
beacon> ls \\srv2\c$
[-] could not open \\srv2\c$\*: 5
beacon> make_token EDU\doe Passw0rd1
[+] Impersonated EDU\john
beacon> ls \\srv2\c$

 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
 dir     05/10/2022 04:11:30   $Recycle.Bin
 dir     05/10/2022 03:23:44   Boot
 ``````


## Detection
* Event `4624: An account was successfully logged on` with Logon Type: `LOGON32_LOGON_NEW_CREDENTIALS` (type `9`).  
>event.code: 4624 and winlog.event_data.LogonType: 9
* Windows commands such as RunAs will also generate the same event.
* Records contain the user who ran the command, the user they're impersonating, and the process it was run from.


## Tools
########
########


```meta
ttp: T1000
requirements: admin
results: 
description: 
```