# ADSearch

## Commands
Get all groups ending with "Admins"
``````beacon
beacon> execute-assembly C:\Tools\ADSearch\ADSearch\bin\Debug\ADSearch.exe --search "(&(objectCategory=group)(cn=*Admins))"

[*] No domain supplied. This PC's domain will be used instead
[*] LDAP://DC=edu,DC=evil,DC=corp
[*] CUSTOM SEARCH: 
[*] TOTAL NUMBER OF SEARCH RESULTS: 6
[+] cn : Domain Admins
[+] cn : Key Admins
[+] cn : DnsAdmins
[+] cn : Oracle Admins
[+] cn : Subsidiary Admins
[+] cn : MS SQL Admins
``````

## [[Kerberoasting]]
Identify Kerberoastable user
``````beacon
execute-assembly C:\Tools\ADSearch\ADSearch\bin\Debug\ADSearch.exe --search "(&(sAMAccountType=805306368)(servicePrincipalName=*))"
  
[*] No domain supplied. This PC's domain will be used instead
[*] LDAP://DC=edu,DC=evil,DC=corp
[*] CUSTOM SEARCH: 
[*] TOTAL NUMBER OF SEARCH RESULTS: 2
 [+] cn : krbtgt
 [+] cn : MS SQL Service
 [+] cn : Honey Service
``````

## [[AS-REP Roasting]]
Identify AS-Reproastable user
``````beacon
beacon> execute-assembly C:\Tools\ADSearch\ADSearch\bin\Debug\ADSearch.exe --search "(&(sAMAccountType=805306368)(userAccountControl:1.2.840.113556.1.4.803:=4194304))" --attributes cn,distinguishedname,samaccountname

[*] No domain supplied. This PC's domain will be used instead
[*] LDAP://DC=edu,DC=evil,DC=corp
[*] CUSTOM SEARCH: 
[*] TOTAL NUMBER OF SEARCH RESULTS: 1
 [+] cn                : Oracle Service
 [+] distinguishedname : CN=Oracle Service,CN=Users,DC=edu,DC=evil,DC=corp
 [+] samaccountname    : svc_oracle
``````

## [[Unconstrained Delegation]]
Identify unconstrained delegation
``````beacon
beacon> execute-assembly C:\Tools\ADSearch\ADSearch\bin\Debug\ADSearch.exe --search "(&(objectCategory=computer)(userAccountControl:1.2.840.113556.1.4.803:=524288))" --attributes samaccountname,dnshostname,operatingsystem

[*] No domain supplied. This PC's domain will be used instead
[*] LDAP://DC=edu,DC=evil,DC=corp
[*] CUSTOM SEARCH: 
[*] TOTAL NUMBER OF SEARCH RESULTS: 2
 [+] samaccountname     : DC-2$
 [+] dnshostname        : dc-2.edu.evil.corp
 [+] operatingsystem    : Windows Server 2016 Datacenter

 [+] samaccountname     : SRV1$
 [+] dnshostname        : srv1.edu.evil.corp
 [+] operatingsystem    : Windows Server 2016 Datacenter
``````

## [[Constrained Delegation]]
Identify constrained delegation
[[PowerView#Constrained Delegation]]
Find all computers configured for constrained delegation and what they're allowed to delegate to (we need the `--json` output to drill down into the `msds-allowedtodelegateto` attribute).
``````beacon
beacon> execute-assembly C:\Tools\ADSearch\ADSearch\bin\Debug\ADSearch.exe --search "(&(objectCategory=computer)(msds-allowedtodelegateto=*))" --attributes cn,dnshostname,samaccountname,msds-allowedtodelegateto --json

[*] No domain supplied. This PC's domain will be used instead
[*] LDAP://DC=edu,DC=evil,DC=corp
[*] CUSTOM SEARCH: 
[*] TOTAL NUMBER OF SEARCH RESULTS: 1
[
  {
 "cn": "SRV2",
 "dnshostname": "srv2.edu.evil.corp",
 "samaccountname": "SRV2$",
 "msds-allowedtodelegateto": [
 "eventlog/dc-2.edu.evil.corp/edu.evil.corp",
 "eventlog/dc-2.edu.evil.corp",
 "eventlog/DC-2",
 "eventlog/dc-2.edu.evil.corp/EDU",
 "eventlog/DC-2/EDU",
 "cifs/wkstn2.edu.evil.corp",
 "cifs/WKSTN2"
 ]
  }
]
``````


```meta
requirements: domainuser,domainadmin
results:
category: Enumeration
stealthy: true
oss: #win
source: https://github.com/tomcarver16/ADSearch
description: Has fewer built-in searches compared to PowerView and SharpView, but it does allow you to specify custom LDAP queries which can be powerful
```