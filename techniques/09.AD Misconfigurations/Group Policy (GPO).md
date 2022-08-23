# Group Policy (GPO) 
Group Policy Objects are collections of controls bound to computers or users within a OU.

Any domain user can read the GPOs and its permissions
-   Create GPOs
-   Modify existing GPOs
-   Link GPOs to OUs

## Identify
If installed use the native GPO report commands `Get-GPOReport` and `gpresult` utility. It can be exported and viewed as HTML. If not availabel use [[Dump GPOs]]

## Abuse
We can abuse these by modifying existing GPOs or creating and linking new GPOs to gain code execution or otherwise manipulate computer configurations.
- [[PowerView#Create new GPOs]]
- [[PowerView#Link GPOs]]
- [[PowerView#WriteProperty, WriteDacl, WriteOwner]]


## Tools
########
########


```meta
ttp: T1000
requirements: admin
results: vulngpo
description: 
```