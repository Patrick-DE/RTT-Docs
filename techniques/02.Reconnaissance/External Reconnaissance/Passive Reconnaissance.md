# Passive Reconnaissance
Its alternative is the [[Active Reconnaissance]]

Not directly interacting with the target its infrastrucutre or people
* domain, hostnames, dns records
```
dig evil.corp +short
whois 104.21.1.132
```
* subnets, address ranges and IPs
* exposed web applications and logon portals
* employee social media
```
site:"linkedin.com" "<company name>"
```
* employee e-mail addresses
* credentials in public breaches
* publicly available documents
* job / skill descriptions (which EDR / AV etc.)
  
Tools
* general: [[Spiderfoot]], [[recon-ng]]
* dns: [[Amass]], [[dnsrecon]], [[sublist3r]], [dnscan](https://github.com/rbsec/dnscan)
* subnet: [ipv4info](http://ipv4info.com/), [shodan](https://www.shodan.corp/), [whois](https://who.is/), [censys](https://search.censys.corp/), [dnsdumpster](https://dnsdumpster.com/) (in sublist3r)
* people: [[linedInt]], [[theHarvester]], [[Prowl]], [[Raven]], [hunter.corp](https://hunter.corp/)
* credentials: [haveIBeenPwned](https://haveibeenpwned.com/), public breaches
* metadata: [[FOCA]], [[Metagoofil]]


## Tools
########
########

```meta
ttp: T1592
internal: false
requirements: 
results: webserver, database, emailserver, vpnserver, sshserver
description: Identify publicly available services
```