## [[Domain Controller]]
Show Domain  
* `nslookup -type=SRV _ldap._tcp.dc._msdcs.//DOMAIN/`
* `nslookup -type=SRV _kerberos._tcp.dc._msdcs.<searchdomain>`
* `nslookup -type=A gc._msdcs.<DNSForestName>`
* `nslookup -type=SRV _ldap._tcp.pdc._msdcs.<searchdomain>`
* `nslookup -type=SRV _ldap._tcp.gc._msdcs.<searchdomain>`
* `nslookup -type=A <DC_FQDN>`

## [[Find Mail Server]]
Find exchange server via nslookup  
`nslookup -q=MX <domain>`
`nslookup _tcp._autodiscover.domain.com`  
`nslookup autodiscover.domain.com`  
`nslookup mail.domain.com`  
`nslookup email.domain.com`  
`nslookup owa.domain.com`  
`nslookup securemail.domain.com`  


```meta
requirements: 
results: 
opsec: 
oss: #win
source: 
description: Nameserver lookups on the network
undetected: 
```