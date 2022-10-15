
If active, plain-text passwords are stored in LSASS (Local Security Authority Subsystem Service).
> reg query HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential


## Tools
########
########

```meta
ttp: T1003
requirements: 
results: credential.plaintext
description: Identify if WDigest is still enabled, allowing an attacker to steal plaintext credentials
```