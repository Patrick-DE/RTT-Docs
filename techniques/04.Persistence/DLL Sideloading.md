# DLL Sideloading
Side-loading uses the DLL search order by positioning both the victim application and malicious payload next to each other. Adversaries often use side-loading as a means of hiding their tracks through  legitimate, trusted processes avoiding detection. In order to further evade detection payloads may additionally be encrypted/packed until the in memory execution.

## Tools
########
########

```meta
ttp: T1574.002
requirements: 
results: persistence
description: Side-loading takes advantage of the DLL search order used by the loader by positioning both the victim application and malicious payload(s) alongside each other.
```