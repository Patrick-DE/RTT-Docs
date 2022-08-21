# SharpHound

## [[Domain]]
All information
> SharpHound.exe -c All --randomfilenames --memcache -d <domain> --throttle 10000 --jitter 10 --zippassword "RT2022!" --ldapusername <user> --ldappassword "<pw>" --domaincontroller <ip> --excludedcs

#opsec: use --stealth, but that removes:
* LoggedOn
* DCOM
* RPD
* PSRemote
* LocalAdmin

Additionally to snapshot
> SharpHound.exe -c "Container, LocalGroup, GPOLocalGroup, Session, LoggedOn, RDP, DCOM" --randomfilenames --memcache -d <domain> --throttle 10000 --jitter 10 --stealth --zippassword "RT2022!" --ldapusername <user> --ldappassword "<pw>" --domaincontroller <ip>

## [[Domain Controller]]
Get DC via Trust
>SharpHound -c DcOnly -d evil.external


## [[One-Way (Inbound)]]
Get Trust of domain
>SharpHound -c Trusts -d evil.external


```meta
requirements: 
results: 
opsec: 
oss: #win
source: https://github.com/BloodHoundAD/SharpHound
description: Ingestor for Bloodhound
```