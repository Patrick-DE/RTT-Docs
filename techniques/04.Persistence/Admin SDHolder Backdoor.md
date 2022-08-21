# Admin SDHolder Backdoor
The **AdminSDHolder** is a DACL template used to protect sensitive principals from modification. Within 60 minutes, you will find modified entries to be restored. Protected objects include Enterprise & Domain Admins, Schema Admins, Backup Operators and krbtgt.

The AdminSDHolder attribute itself is not protected so if we modify the DACL on it, those changes will be replicated again.

[[PowerView#Assign rights AdminSDHolder]]


## Tools
########
########

```meta
ttp: T1000
requirements:
results: 
description: 
```