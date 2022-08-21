# Resource Based Constrained Delegation (RBCD)
1. Non-privileged account on a Windows 10 machine
2. Privileges to write the `msDS-AllowedToActOnBehalfOfOtherIdentity` attribute on a domain controller
3. Create a new computer account due to the default MachineAccountQuota = 10
4. Set the msDS-AllowedToActOnBehalfOfOtherIdentity attribute to contain a security descriptor with the computer account from step 3
5. Leverage Rubeus to abuse resource-based constrained delegation

sources:
- https://stealthbits.com/blog/resource-based-constrained-delegation-abuse/
- https://www.ired.team/offensive-security-experiments/active-directory-kerberos-abuse/resource-based-constrained-delegation-ad-computer-object-take-over-and-privilged-code-execution


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```