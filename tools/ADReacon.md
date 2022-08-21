# ADReacon

## Commands
ADReaper performs enumeration with various commands that performs LDAP queries with respective to it
```
PS C:\Users\redteamer\Desktop\shared>.\ADReaper.exe

      -command string

            Command to run
                  dc              - to list domain controllers
                  domain-trust    - to list domain trust
                  users           - to list all users
                  computers       - to list all computers
                  groups          - to list all groups with members
                  spn             - to list service principal objects
                  never-loggedon  - to list users never logged on
                  gpo             - to list group policy objects
                  ou              - to list organizational units
                  ms-sql          - to list MS-SQL servers
                  asreproast      - to list AS-REP roastable accounts
                  unconstrained   - to list Unconstrained Delegated accounts
                  admin-priv      - to list AD objects with admin privilege

      -dc string

            Enter the DC

      -filter string

            Filters to use for users/groups/computers

            list - lists all objects only
            fulldata - list all objects with properties
            membership - lists all members from an object

            (default "list")
      -name string

            Pass object name of user/group/computer

      -password string

            Enter the Password

      -user string

            Enter the Username
```

To list OUs from the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command ou
```

To list AD objects with higher privileges,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command admin-priv
```

## [[Domain Controller]]
To query the properties of Domain Controller of the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command dc
```

## [[Domain Trust]]
To query the Trust Attributes of the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command domain-trust
```

## [[Domain Users]]
To list all Users from the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command users
```

To list all Users with attributes from the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command users -filter full-data
```

To list attributes of Specific Users from the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command users -name <user>
```

To list the membership of the Specific User,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command users -name <user> -filter membership
```

## [[Domain Computers]]
To list all available Computers from the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command computers
```

To list all Computers with attributes from the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command computers -filter full-data
```

To list attributes of Specific Computer from the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command computers -name <computer name>
```

## [[Domain Groups]]
To list all available Groups from the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command groups
```

To list all Groups with attributes from the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command groups -filter full-data
```

To list attributes of Specific Group from the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command groups -name <group name>
```

To list members of Specific Group from the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command groups -name <group name> -filter membership
```

To list users Never Logged On from the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command never-loggedon
```

## [[Domain GPOs]]
To list GPOs from the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command gpo
```

## [[Database Server]]
To list MS-SQL Servers from the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command ms-sql
```

To list all attributes of MS-SQL Servers from the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command ms-sql -filter full-data.
```

To list all attributes of specific MS-SQL Server from the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command ms-sql -name <computer name> 
```

## [[Domain SPN]]
To list SPNs available in the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command spn
```

To list all attributes of Specific SPN from the domain,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command spn -name <sam of spn>
```

## [[Unconstrained Delegation]]
To list AD objects with Unconstrained Delegation enabled,
```
.\ADReaper.exe -dc <dc.domain> -user <username> -password <password> -command unconstrained 
```


```meta

requirements: domainuser,domainadmin
results:
opsec: true
oss: #win, #linux
source: https://github.com/AidenPearce369/ADReaper
description: ADReaper is a tool written in Golang which enumerates an Active Directory environment with LDAP queries within few seconds
```