# Golden Tickets
A Golden Ticket is a forged TGT. In comparison to a Silver Ticket, which impersonates a single service or a single machine, a Golden Ticket can be used to impersonate either a choosen user, service, or machine.

* Create silver tickets: [[Mimikatz#Create silver ticket]]
* Create golden tickets: [[Mimikatz#Create golden ticket]]

## Detection
Network:
- Lifetime with mimikatz is abnormal 10 years

Windows logs:
- Seeing 4769's _without_ a prior 4768.
  It's not possible to request a TGS without a TGT. No record of a TGT being issued -> forged offline.
- Alert on 4769's for sensitive users such as the default domain administrator account.


## Tools
########
########


```meta
ttp: T1558.001
requirements: krbtgt
results: ticket
description: Extract kerberos ticket from memory
```