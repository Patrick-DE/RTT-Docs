# Net

## [[Local User+Groups]]
1. Create User:
    ```bash
    net user nviso Nv1so12345! /ADD /DOMAIN
    ```
2. List local / domain groups
    ```bash
    net group /domain

    Gruppenkonten für \\dc1.testdomain.local
    -------------------------------------------------------------------------------
    *$7O...
    *Abteilung_....
    *Domänen-Admins
    
    net localgroup [group (Remote Dektop Users)]
    ```
1. Add User to domain /local group
    ```sh
    net group "Domänen-Admins" nviso /add /domain

    net localgroup "Remote Desktop Users" nviso /add
    net localgroup "Administrators" nviso /add
    ```

## [[Domain Controller]]
From domain joined device  
>net group "domain controllers" /domain
>nslookup dc-01
>net time

## [[Web Proxies]]
``````beacon
beacon> getuid
[*] You are EDU\john

beacon> run net user john /domain
The request will be processed at a domain controller for domain edu.evil.corp.
[...snip...]

Global Group memberships     *Domain Users         *Roaming Users        
                             *Developers           *Proxy Users
``````



```meta
requirements: 
results: 
opsec: 
oss: #win
source: 
description: 
```