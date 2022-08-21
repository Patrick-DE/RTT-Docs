# NMAP

Scan phases
===========

1.  Script pre-scanning
    1.  only when NSE scans
    2.  executed once per run
2.  Target enumeration
    1.  executed once per run
3.  Host discovery
    1.  also known as "Ping Scanning"
    2.  skipped with -Pn
    3.  assume all hosts are online
4.  Reverse-DNS resolution
    1.  provides DNS name for ip address 
    2.  skipped with -n
    3.  force with -r
5.  Port scanning
    1.  executed once per host
    2.  skipped with -sn
6.  Version detection
    1.  enabled with -sV
7.  OS detection
    1.  enable with -O
8.  Traceroute
    1.  enable with --traceroute
9.  Script scanning
    1.  most NSE is run here
10.  Output
    1.  write to screen or files
11.  Script post-scanning
    1.  possible to use but currently not used

Commands
========

1.  Version:  
    nmap -V
2.  Help  
    nmap, nmap -h, man nmap
3.  Input  
    \-iL hostList
4.  Output  
    \-oN textfile  
    \-oX xml  
    \-oS scriptkiddy  
    \-oG greppable format  
    \-oA normal + xml + greppable  
    \-v, -vv, -vvv increase level of details
5.  TCP Flags  
    \-sS: TCP SYN scan  
    \-sA: TCP ACK scan  
    \-sT: TCP connect scan
6.  ICMP scan  
    Ping Scan != ICMP  
    _nmap -sn -PE <target>_
7.  NSE scripts
    _nmap <option> -sC <target> (_launch all 'default' NSE  
    nmap --script vuln --script-args=unsafe=1 -iL hostname.txt  
    nmap --script-help=</script>
    _nmap <option> --script=</script name or category , seperated> <target>_ (launch specific NSE script)  
    _nmap --script ssl-enum-ciphers -p 443 www.example.com_
8.  Scan-Technique  
    \-sS (TCP Syn Scan, default NMAP)  
    \-sT (TCP Connect Scan, default if no admin)  
    \-sU (UDP Scan)  
    \-sO (IP protocol Scan)
9.  Discovery Options  
    \-sL (List Scan)  
    \-sn (No Port Scan, called Ping Scan or Ping Sweep, GET MAC+IP+Name), ICMP echo request + TCP SYN to 443 + ACK to 80 + ICMP timestamp  
    \-Pn (No ping, 1000Ports for every IP), Skip discovery step  
    \-F (Most common 100 Ports)  
    \-n (No DNS resolution)  
    \-R (Resolve all using DNS)  
    \--traceroute (Trace path to host)  
    \--dns-server <server1>,<server2> (Use custom DNS server for PTR lookup)
10.  TCP Flags  
    \-PS (SYN Ping)  
    \-PA (ACK Ping)  
    \-PU (UDP Ping)  
    \-PY (SCTP INIT Ping), Stream Control Transmission Protocol  
    \-PO (IP Protocol Ping)  
    \-PE, -PP, -PM (ICMP Ping)  
    \-PR (ARP Ping), Get-MAC address in a local network -sn is BETTER
11.  States  
    Open: Accept packets  
    Closed: Is reachable but nothing excepts the packets  
    Filtered: Packet filtering is blocking  
    Unfiltered: Accessible but cannot detect
12.  Timing templates  
    \-T0 (Paranoid, IDS evasion)  
    \-T1 (Sneaky, IDS evasion)  
    \-T2 (Polite, Slows down)  
    \-T3 (Normal (Default)  
    \-T4 (Aggressive, fast reliable network)  
    \-T5 (Insane, Very fast network)
13.  Version detection  
    \-sS (Version detection)  
    \--version-light (--version-intensity 2)  
    \--version-all (--version-intensity 9)
14.  OS discovery  
    _nmap -T4 -O -v --script=smb-os-discovery_ (OS discovery)  
    \--osscan-limit (If not 1xOpen  & 1xClosed port exist, nmap will NOT guess, reduce bullshit)  
    \--osscan-guess or --fuzzy (NMAP will best guess the OS)  
    \--max-os-tries <value> (increase speed)
15.  ALL IN ONE  
    \-A (advanced and aggressive), detailed port scanning, version detection, os detection, and NSE 'default' scripts)

######

## [[OT Devices]]
> .\nmap.exe -p- --script=s7-info,modbus-discover,bacnet-info,enip-info,Siemens-CommunicationsProcessor.nse,Siemens-HMI-miniweb.nse,Siemens-Scalance-module.nse,Siemens-SIMATIC-PLC-S7.nse,Siemens-WINCC.nse 172.29.137.100

## [[SMB Signing]]
> nmap -Pn -sS -T4 --open --script smb-security-mode -p445 ADDRESS/MASK

## [[User enum]]
> nmap -n -sV --script "ldap* an not brute" -p 389 <dc-ip>

## [[Exposed Machines]] [[Domain Computers]]
* Ping Scan  
> nmap -sP -p <ip>
* Search smb vuln  
> nmap -PN --script smb-vuln* -p139,445 <ip>
* Classic Scan  
> nmap -PN -sC -sV <ip>
* Full Scan  
>nmap -PN -sC -sV -p- <ip>
* UDP Scan  
>nmap -sU -sC -sV <ip>

## [[SOCKS Proxy]]
Nmap example via proxychains:
``````sh
proxychains nmap -n -Pn -sT -p445,3389,5985 10.10.1.20
``````
⚠️ICMP and SYN scans cannot be tunnelled, so we must disable ping discovery (`-Pn`) and specify TCP scans (`-sT`) for this to work

```meta
requirements: 
results: 
category:
opsec: 
oss: #linux, #win
source: https://nmap.org/
description: Nmap Free Security Scanner, Port Scanner, & Network Exploration Tool 
```