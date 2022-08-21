# Overpass-the-Hash
Authentication via Kerberos (AES key) rather than NTLM.

### Manually
[[Use Kerberos ticket (kirbi)]]

### Inject TGT automatically
- Use [[Rubeus#Request TGT and inject into sacrificial process]]


## Detection
When a TGT is requested, event `4768: A Kerberos authentication ticket (TGT) was requested` is generated.
* NTLM is often KeyType **RC4-HMAC** (0x17) and nowadays not often used.
* Nowadays used is  **AES256** (0x12).

This means we can find 4768's where the encryption type is RC4, which can be significant outliers.
>event.code: 4768 and winlog.event_data.TicketEncryptionType: 0x17


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description:
opsec: true
``` 