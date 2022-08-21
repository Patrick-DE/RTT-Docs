# Constrained Delegation
More secure method of [[Unconstrained Delegation]].
TGTs of users are no longer cached, but it allows to request a TGS for another user with its own TGT.
 ![](/Images/Pasted%20image%2020220316164953.png)

It can only act on behalf of a user to the **cifs** service on **WKSTN2**. With CIFS file shares can be listed, files can be uploaded and downloaded, and the Service Control Manager ([[PsExec]]) can be controlled.

To perform the delegation, we need TGT of the principal (machine or user) trusted for delegation. We can extract:
- from a machine (`Rubeus dump`) 
- using the NTLM / AES keys and ask for the TGT ([[eKeys]] + [[Rubeus#Request TGT and inject into sacrificial process]]).


## Alternate Service Name
Even if the service for a specific workstation is not usefull, it can be changed via `/altservice` in [[Rubeus]] since its not being validated in s4u.


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```