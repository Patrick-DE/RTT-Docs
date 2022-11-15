# Ettercap

Ettercap is an open-source program that combines a packet sniffer for different protocols (POP/HTPPS/HTTPS/SFTP), but it also offers password cracking features. It can sniff and gather data while using MITM attacks. We will be covering the Linux version for the most part and will use the graphical interface.

## [[08.Credentials & User Impersonation/MITM]]
Run ettercap with UI

```bash
sudo ettercap -G
```

1.  Select mode  
    **Unified**: sniff  
    **Bridged:** sniff and forward
2.  Select interface
3.  Host list → add target 1 (gateway) + add target 2 (host)
4.  Select attack (ARP poisoning, ICMP redirect, Port Stealing. DHCP spoofing)
5.  Check the MAC  
    Windows: arp -a  
    Linux: arp
6.  View → Connections

**SSL/TLS decryption**

*   change /etc/etthercap/etter.conf  
    +- ec\_uid = 0  
    +- ec\_gid = 0  
    \+ redir\_command\_on  
    \+ redir\_command\_off


```meta
requirements: 
results: 
oss: #linux
source: https://github.com/Ettercap/ettercap
description: A suite for man in the middle attacks
```