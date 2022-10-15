# Pass-the-Hash
It allows you to authenticate to a Windows service using the NTLM hash of a user. It works by starting a new logon session with a wrong details and replacing all session information like the domain, username and NTLM hash.  
The tool of choice would be [[Mimikatz]].

⚠️ Warning
* This requires patching LSASS which can be easily detected or prevented by PPL and requires local admin privs.  
* Not providing `/run` will spawn the process with UI (expected running as SYSTEM).

#OPSEC No LSASS memory patch and no admin rights are required with [[Overpass-the-Hash]]

## Detection
* Sysmon will record the process creation event for `cmd.exe` including the command line arguments `echo 1cbe909fe8a > \\.\pipe\16ca6d.`  
In Kibana:
>event.module: sysmon and event.type: process_start and process.name: cmd.exe and process.command_line: *\\\\.\\pipe\\*
* Event `4624` with logon type 9 will be recorded. This event records the executing user's Logon ID, which we can cross reference from the process creation event above.
>event.code: 4624 and winlog.logon.id: 0xe6d64

## Troubleshoot
1. There is a problem if the account is not RID-500 (Admin) and only in the admin group

2. The two registry entries needed are:
    ```powershell
    Set-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name LocalAccountTokenFilterPolicy -Value 1 -Type DWord
    Set—ItemProperty -Path HKLM:\System\CurrentControlSet\Services\LanManServer\Parameters -Name RequireSecuritySignature -Value 0 -Type DWord
    ```
    OR
    ```powershell
    reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f
    reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters" /v RequireSecuritySignature /t REG_DWORD /d 0 /f
    ```

## Tools
########
########


```meta
ttp: T1550.002
requirements: admin
results: 
description: 
``` 