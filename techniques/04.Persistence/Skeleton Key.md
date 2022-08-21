# Skeleton Key
The Skeleton Key must be used on Domain Controllers where as LSASS will be patched to allow any user to be authenticated with the password `mimikatz` (their real passwords still work too).

⛔ The skeleton key cannot be removed unless the domain controller is rebooted and it can cause side effects such as replication issues.

## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
``` 