# netcat

Versions
--------

1.  nc
2.  ncat (nmap BETTER)

  
Run
------

*   Listen one connection:

```java
nc -lvp 8080
```

*   Listen all the time: (Windows)

```java
nc -Lvp 8080
```

*   Connect:

```java
netcat -u host port
```

Quelle: [https://www.sans.org/security-resources/sec560/netcat\_cheat\_sheet\_v1.pdf](https://www.sans.org/security-resources/sec560/netcat_cheat_sheet_v1.pdf)


```meta
phases: 02
requirements: 
results: 
opsec: true
methods: 
oss: #win
source: http://netcat.sourceforge.net/
description: Netcat is a featured networking utility which reads and writes data across network connections, using the TCP/IP protocol.
```