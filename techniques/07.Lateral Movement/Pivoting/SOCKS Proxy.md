# Socks Proxy

## Setup SOCKS via Cobalt Strike
``````beacon
beacon> socks 1080
[+] started SOCKS4a server on: 1080
``````

This will bind port 1080 on the Team Server.
``````bash
root@kali:~# ss -lpnt
State   Recv-Q  Send-Q  Local Address:Port Peer Address:Port    Process
LISTEN  0       128     .:1080             .:*                  users:(("java",pid=1222,fd=11))
``````

#opsec This binds 1080 on all interfaces and since there is no authentication available on SOCKS4, this port can technically be used by anyone.
Always ensure your Team Server is adequately protected and never exposed directly to the Internet.

## Tunnel Windows
We can tunnel GUI apps that run on Windows using a proxy client such as [[Proxifier]].

### RunAs
Some applications (such as the RSAT tools) don't provide a means of providing a username or password, because they're designed to use a user's domain context. You can still run these tools on your attacking machine. If you have the clear text credentials, use `runas /netonly`.

``````powershell
C:\>runas /netonly /user:EDU\patrick "C:\windows\system32\mmc.exe C:\windows\system32\dsa.msc"
Enter the password for EDU\patrick:
Attempting to start C:\windows\system32\mmc.exe C:\windows\system32\dsa.msc as user "EDU\patrick" ...
``````

### Mimikatz
You can use [[Mimikatz#Spawn process with injected credentials]] - [[Pass-the-Hash]]


## Tools
########
########


```meta
ttp: T1000
requirements: admin
results: 
description: 
```