# BloodHound

BloodHound is an application that uses graph theory to display the relationships between different Active Directory components, specifically for the use case of finding attack paths. BloodHound requires the use of two additional components: a [neo4j](https://neo4j.com/) database and the [[SharpHound]] data collector.

#OPSEC Running collection methods such as **LocalAdmin**, **RDP**, **DCOM**, **PSRemote** and **LoggedOn** will allow SharpHound to enumerate every single computer in the domain. Collecting this information is useful to BloodHound and without it you may see fewer paths, at the obvious expensive of being loud on the wire.

## Custom Queries
### [[Kerberoasting]]
- Kerberoastable users
>MATCH (u:User {hasspn:true}) RETURN u
- With paths to computers
>MATCH (u:User {hasspn:true}), (c:Computer), p=shortestPath((u)-[*1..]->(c)) RETURN p
- List of kerberoastable users with groups
> MATCH (m:User {hasspn:true}), (n:Group), p=(m)-[:MemberOf]->(n) RETURN m.name as Account, n.name as Group, m.hasspn as Kerberoastable
### [[AS-REP Roasting]]
- AS-REP roastable users
>MATCH (u:User {dontreqpreauth:true}) RETURN u

### [[Unconstrained Delegation]]
>MATCH (c:Computer {unconstraineddelegation:true}) RETURN c

## [[Constrained Delegation]]
ℹ️ Constrained delegation can be configured on user accounts as well as computer accounts.  Make sure you search for both.
>MATCH (c:Computer), (t:Computer), p=((c)-[:AllowedToDelegate]->(t)) RETURN p

### [[Group Policy (GPO)]]
Generic Write on GPOs
>MATCH (gr:Group), (gp:GPO), p=((gr)-[:GenericWrite]->(gp)) RETURN p

### WriteProperty, WriteDacl, WriteOwner affecting OU
1st Line Support has **GenericAll** on multiple users and groups
>MATCH (g1:Group {name:"1ST LINE SUPPORT@edu.evil.corp"}), (g2:Group), p=((g1)-[:GenericAll]->(g2)) RETURN p

## [[Database Server]]
Finding potential MS SQL Admins, based on the assumption that the account running the SQL Service is also a sysadmin (which is very common);
>MATCH p=(u:User)-[:SQLAdmin]->(c:Computer) RETURN p

## [[Local Administrator Password Solution (LAPS)]]
Find computers that have LAPS applied to them:
>MATCH (c:Computer {haslaps: true}) RETURN c

Any groups that have an edge to machines via LAPS:
>MATCH p=(g:Group)-[:ReadLAPSPassword]->(c:Computer) RETURN p

```meta
requirements: 
results: 
opsec: 
oss: #win
source: https://github.com/BloodHoundAD/BloodHound
description: 
```