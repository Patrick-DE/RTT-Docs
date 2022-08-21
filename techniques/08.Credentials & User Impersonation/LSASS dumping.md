# LogonPasswords
This feature retrieves NTLM hashes which can be used with [[Pass-the-Hash]] or cracking to recover the plain-text.

#OPSEC A lot of tradecraft that leverages NTLM are undesirable.
-   [[Pass-the-Hash]] requires patching LSASS.
-   [[Overpass-the-Hash]] with NTLM uses a weaker encryption compared to what Windows uses by default.

-> Better use [[eKeys]] to get the AES and [[Overpass-the-Hash]]

## Tools
########
########

```meta
ttp: T1000
requirements: admin
results: 
description: 
```