# Forged Certificates
The AD CS roles can either be installed on separate servers or on domain controllers. 
Forging certs can be used as
* Privilege Escalation if accessible by non-domain admins
* domain persistence method by creating (with priv key) certificates which can be used to request TGTs

The default validity period for a CA private key is 5 years, but can be set to any value during the setup.

Once on a CA, [[SharpDPAPI]] can extract the private keys.

1. [[SharpDPAPI#Dump private keys]]
2. Save the output to a `.pem` file and convert it to a `.pfx` with openssl on Kali, then move it back to the attacker machine.
3. Build the forged certificate with [[ForgeCert#Generate certificate with stolen pk]].
4. Use [[Rubeus#Ask TGT via certificate]] to request a legitimate TGT with this forged certificate and use it to access the domain controller.
5. [[Use Kerberos ticket (kirbi)]]

We're not limited to forging user certificates, we can do the same for machines. Combine this with the [[S4U2self Abuse]] trick to gain access to any machine or service in the domain.

## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```