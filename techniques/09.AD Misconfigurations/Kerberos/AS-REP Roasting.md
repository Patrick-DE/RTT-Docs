# AS-RER Roasting
If a user does not have [[Kerberos]] pre-authentication enabled, an AS-REP can be requested for that user, and part of the reply can be cracked offline to recover their plaintext password.

 ![](/Images/AS-REP Roast.png)

Process:
1. [[BloodHound#AS-REP Roasting]]
2. [[ADSearch#Identify as-rep roastable user]]
3. [[Hashcat#Cracking krb5asrep]]

## Tools
########
########


```meta
ttp: T1558.004
requirements:
results: 
description: 
```