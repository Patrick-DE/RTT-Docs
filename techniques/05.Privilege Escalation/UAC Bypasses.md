# UAC Bypasses
This technique enables and attacker from **Medium** to **High Integrity** without prompting for consent.

By default, applications will run in **Medium** Integrity context. Even if local administrators launch the Command Prompt "normally" it is not possible to execute privileged functions.

The default setting is **Prompt for consent for non-Windows binaries**, but you can configure them to the following states, top to bottom reducing security:
* Prompt for credentials
* Prompt for consent
* Prompt for consent for non-Windows binaries 
* Elevate without prompting

[[Seatbelt]] can be used to query the configuration applied to a machine.
Cobalt Strike has some [[UAC-Bypass]] included.


## Tools
########
########


```meta
ttp: T1000
requirements: 
results: admin
description: UAC bypass to elevate from medium into a high integrity process
```