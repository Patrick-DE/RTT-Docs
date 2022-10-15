# Silver Ticket
A Silver Ticket is a forged TGS, signed using the secret material (RC4/AES keys) of a machine account. You may forge a TGS for any user to any service on a specific machine. This access will remain until the computer account password changes, which is every 30 days by default.

#OPSEC Silver and [[Golden Ticket]] can be generated "offline" and imported into your session. This saves executing Mimikatz on the target. Generating both silver and golden tickets can be done with [[Mimikatz#Create silver ticket]].

## Tools
########
########


```meta
ttp: T1558.002
requirements: krbtgt
results: ticket
description: Extract kerberos ticket from memory
```