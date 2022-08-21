# Seatbelt

## [[Misconfigurations/WSUS]] [[Protections/AppLocker]] [[AV-EDR]] [[Credential Guard]] [[Windows Audit Policies]] [[PowerShell Logging]] [[Event Forwarding]] [[Misconfigurations/WSUS]]
## Get systems environment
>execute-assembly C:\Tools\Seatbelt\Seatbelt\bin\Debug\Seatbelt.exe -group=system -outputfile="file.txt"

## [[User Access Control (UAC)]]
Query the configuration applied to a machine
``````beacon
beacon> execute-assembly C:\Tools\Seatbelt\Seatbelt\bin\Debug\Seatbelt.exe uac

====== UAC ======

ConsentPromptBehaviorAdmin     : 5 - PromptForNonWindowsBinaries
EnableLUA (Is UAC enabled?)    : 1
``````

## [[Web Proxies]]
Internet Settings
``````beacon
beacon> execute-assembly C:\Tools\Seatbelt\Seatbelt\bin\Debug\Seatbelt.exe InternetSettings

  HKCU                       ProxyEnable : 1
  HKCU                     ProxyOverride : ;local
  HKCU                       ProxyServer : squid.edu.evil.corp:3128
``````

## [[SQL Privilege Escalation]]
## Get TokenPrivileges
```beacon
beacon> getuid
[*] You are NT Service\MSSQL$SQLEXPRESS

beacon> execute-assembly C:\Tools\Seatbelt\Seatbelt\bin\Debug\Seatbelt.exe TokenPrivileges

====== TokenPrivileges ======

Current Token's Privileges

 SeAssignPrimaryTokenPrivilege:  DISABLED
 SeIncreaseQuotaPrivilege:  DISABLED
 SeChangeNotifyPrivilege:  SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED
 SeManageVolumePrivilege:  SE_PRIVILEGE_ENABLED
 SeImpersonatePrivilege:  SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED
 SeCreateGlobalPrivilege:  SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED
 SeIncreaseWorkingSetPrivilege:  DISABLED

[*] Completed collection in 0.01 seconds
```


```meta
requirements: 
results: 
opsec: 
oss: #win 
source: https://github.com/GhostPack/Seatbelt
description: Seatbelt is a .NET application written in C# that has various "host safety-checks". The information it gathers includes general OS info, installed antivirus, AppLocker, audit policies, local users and groups, logon sessions, UAC, Windows Firewall and more.
```