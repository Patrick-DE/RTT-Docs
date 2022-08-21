# Kerberoasting
Services run on a machine under the context of a user account. These accounts are either local to the machine (LocalSystem, LocalService, NetworkService) or are domain accounts (e.g. `DOMAIN\mssql`).

A Service Principal Name (SPN) is a unique id of a service instance. SPNs are configured on the User Object and used by [[Kerberos]] to match a service instance to a logon account.

Part of the TGS returned by the KDC is encrypted with a secret derived from the password of the user account running that service. By Kerberoasting a TGS is requested for the user running that service which can be cracked offline to reveal the users plain-text passwords.

Process:
1. Identify users with:
- [[BloodHound#Kerberoasting]]
- [[ADSearch#Identify kerberoastable users]]
2. [[Rubeus]] can be used to perform the kerberoasting.
- [[Rubeus#Kerberoasting]]
- [[Rubeus#Targeted Kerberoasting]]
3. Cracking
- [[Hashcat#Cracking krb5tgs]]

## Detection
When a TGS is requested, Windows event `4769 - A Kerberos service ticket was requested` is generated.

You can find them in Kibana with:
>event.code: 4769

>event.code: 4769 and winlog.event_data.ServiceName : svc_xxx


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```