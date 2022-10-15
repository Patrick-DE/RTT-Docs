# SMB Relay

## Idea
1. Attacker selects target
2. Victim authenticates to attacker
3. Attacker forwards the authentication attempt to the target
4. Attacker receives the challenge
5. Attacker sends back challenge to the victim
6. Victim sents encrypted challenge to attacker
7. Attacker sends the challenge and authenticates

Note: this works only if the “Network security: LAN Manager authentication level” is set to “Send LM & NTLM responses” or perhaps “NTLMv2 response only

1. Run [[Tools/Responder.md]] to poison LLMNR / SMB / ARP requests
2. Run [[Tools/smbrelayx.md]] to relay the ticket and drop tools / execute commands on the target server


## Tools
########
########


```meta
ttp: T1557.001
requirements: and(smbv1,smbsigningoff)
results: user, admin
description: Relay smb connections to gain access to another workstation
```