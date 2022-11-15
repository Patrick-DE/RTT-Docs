# snmpwalk

## [[Vulnerable Machines]]

Uses snmp-getnext requests to enumerate a network device for their tree information. An object identified (OID) can be provided and from there all information below will be queried. If no OID is being provided, snmpwalk will start at the subtree rooted at SNMPv2-SMI::mib-2.

![](/Images/Tools/d2e354a3-b1dc-40fa-bb6f-323dea9713de.png)

If the OID is being displayed as follows

![](/Images/Tools/549ed8bc-0f8d-4d5a-89b0-df8cbff60ca3.png)

ensure to install the _snmp-mibs-downloader_ and commend the 4th line in /etc/snmp/snmp.conf.

Example to query installed programs:

![](/Images/Tools/0de1da34-6198-4529-90d3-40d89d6bccbd.png)

snmpset - modify
----------------

SNMPset is using the _set_ request to set or change information on the network entity. It allows managing the device.

The minimum requirement for this tool is a valid _OID_, a _type_ (integer, string), and a _value_. The following command changed the _sysContact_ key.

![](/Images/Tools/31682251-2c70-48eb-9587-abadd7f63da0.png)
![](/Images/Tools/8af26abc-4c3d-4ee2-9349-0895906829d6.png)

All available types are listed below:

![](/Images/Tools/a9790eba-1da7-4a28-b942-3083cc4e36d7.png)

You can find NMAP scripts for SNMP as follows:

```bash
ls /usr/share/nmap/scripts | grep -i snmp
```

The above-mentioned process enumeration can also be done with the following NMAP script

```java
sudo nmap -sU -p 161 --scripts=snmp-win32-services 192.168.1.1
```

Community string bruteforce

```bash
sudo apt install seclists
sudo nmap -sU -p 161 --scripts=snmp-brute --script-args=snmp.brute.communitiesdb=/usr/share/seclists/Misc/wordlist-common-snmp-community-strings.txt 192.168.1.1
```


```meta
requirements: 
results: 
oss: #linux, #win
source: https://linux.die.net/man/1/snmpwalk
description: snmpwalk is an SNMP application that uses SNMP GETNEXT requests to query a network entity for a tree of information.
```