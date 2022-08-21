# Unconstrained Delegation
Delegation: User or a service acting on behalf of another user to another service
Example: User authenticates to a front-end web application that serves a back-end database. The front-end application needs to authenticate to the back-end database (using Kerberos) as user.
 ![](/Images/Pasted%20image%2020220316153112.png)

If unconstrained delegation: KDC includes a copy of the user’s TGT inside the TGS.
Example: 
1. User accesses the Web Server, it extracts the user's TGT from the TGS and caches it in memory.
2. When the Web Server needs to access the DB Server on behalf of that user, it uses cached TGT to request a TGS for the database service.
3. The caching is **always** being done, also on normal auth. ->Compromise a machine with unconstrained delegation and extract any TGTs.

## Exploit
1. [[Rubeus#Unconstrained Delegation]] can be used to monitor for new TGTs cached on the machine.
2. [[Kerberos/Printer Bug]]


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```