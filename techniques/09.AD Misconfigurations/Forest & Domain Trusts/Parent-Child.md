# Parent - Child
When a child domain is added to a forest, it automatically creates a transitive, two-way trust with its parent. This be found in the lab where edu.evil.corp is a child domain of evil.corp.

```beacon
beacon> powershell Get-DomainTrust

SourceName      : edu.evil.corp			//current domain
TargetName      : evil.corp				//foreign domain
TrustType       : WINDOWS_ACTIVE_DIRECTORY
TrustAttributes : WITHIN_FOREST				//parent/child domain
TrustDirection  : Bidirectional				//bidirectional/two-way, One-way trust)
WhenCreated     : 2/19/2022 1:28:00 PM
WhenChanged     : 2/19/2022 1:28:00 PM
```

| Trust type | Transitivity                | Direction          | Description                                                                                                                                    |
| ---------- | --------------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| External   | Nontransitive               | One-way or two-way | Provide access to resources that are located on a domain that is located in a separate non joined forest.                                      |
| Realm      | Transitive or nontransitive | One-way or two-way | Form a trust relationship between a non-Windows Kerberos realm and a Windows Server 2008                                                       |
| Forest     | Transitive                  | One-way or two-way | Share resources between forests. Two-way trust: authentication requests can reach the other forest.                                            |
| Shortcut   | Transitive                  | One-way or two-way | Improve user logon times between two domains within a Windows Server forest. This is useful when two domains are separated by two domain trees |

If we have Domain Admin privileges in the child, we can also gain Domain Admin privileges in the parent using Golden Ticket with a special attribute called SID History.  So when creating a Golden Ticket, the SID of a privileged group (EAs, DAs, etc) in the parent domain can be added to the SID history which will grant access to all resources in the parent.

If edu.evil.corp also had a child (e.g. test.edu.evil.corp), then a DA in TEST would be able to use their krbtgt to hop to DA/EA in evil.corp instantly because the trusts are transitive.

There are also other means which do not require DA in the child, some of which we've already seen. You can also [[Kerberoasting]] and [[AS-REP Roasting]] across domain trusts, which may lead to privileged credential disclosure. Because principals in EDU can be granted access to resources in EDU, you may find instances where they are accessing machines we have compromised. If they interact with a machine with [[Unconstrained Delegation]], we can capture their TGTs. If they're on a machine interactively, e.g. over RDP, we can impersonate them just like any other user.

## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```