# Active Directory Certificate Service
Active Directory Certificate Services (AD CS) is a server role that allows you to build a public key infrastructure (PKI). This includes public keys, digital certificates and signatures like (S/MIME), 802.1x, smart card logon, and SSL/TLS.

To find AD CS Certificate Authorities (CA's) in a domain or forest, run [[Certify]] with the cas parameter. [[Certify#Get certificat details]]

Vulnerabilities:
- [[Misconfigured Certificate Templates]]
- [[NTLM Relaying to ADCS]]

## Detection
* AD CS logging is not enabled by default. Logging for the following event can be enabled:
![](/Images/adcs.png)
* `Audit Certification Services` must be enabled via GPO.
* Event `4886`, "Certificate Services received a certificate request".
```kibana
event.code: 4886

Request ID:	7
Requester:	DEV\patrick
Attributes:	
  ccm:wkstn-3.evil.corp
```
* Event `4887` if the request was successful, and a certificate issued.  
Find requester: Lookup the certificate by `Request ID` and look at the "Subject Alternative Name".
* Event `4768` on the DC if a TGT is requested and will contain the certificate if used.
``````kibana
Certificate Information:
 Certificate Issuer Name:   ca1
 Certificate Serial Number:	65000022376D7D5EBB98E12D17600000000067
 Certificate Thumbprint:	3EB5532F3B986D7591EAB07D0C9EB1BFA3577C5F
``````

Read more [here](https://www.specterops.corp/assets/resources/Certified_Pre-Owned.pdf) a blogpost published by [Will Schroeder](https://twitter.com/harmj0y) & [Lee Christensen](https://twitter.com/tifkin_).

## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```