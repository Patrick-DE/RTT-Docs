# Misconfigured Certificate Template
1. Find any vulnerable templates.
 ![](/Images/Pasted%20image%2020220316231825.png)

Important fields:
| Field | Value | Desc |
| ----- | ----- | ---- |
| Certificate Authority | `dc-1.evil.corp\ca-1` | Cert authority |
| Template | `VulnerableUserTemplate` | Cert Template |
| msPKI-Certificate-Name-Flag | `ENROLLEE_SUPPLIES_SUBJECT` | allows to provide a SAN (subject alternative name) |
| pkiextendedkeyusage | `Client Authentication`| allows for Client authentication | 
| Enrollment Rights | `\Domain Users` | Domain Users can request the cert |
| Object Control Permissions | `WriteOwner`, `WriteDacl`, `WriteProperty` |
Change Templates |

2. Request a user certificate.
3. Copy the whole certificate (including the private key) and save it to `cert.pem`. 
4. Use the `openssl` to convert it into pfx format.
    ``````sh
    openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx
    Enter Export Password:
    Verifying - Enter Export Password:
    ``````
5. Convert `cert.pfx` into a base64 encoded string and use [[Rubeus#Ask TGT via certificate]]. 
    ```sh
    cat cert.pfx | base64 -w 0
    ```


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```