# Ncrack

[https://nmap.org/ncrack/man.html](https://nmap.org/ncrack/man.html)

Services

|  |  |  |  |
|---|---|---|---|
| FTP | SSH | TELNET | HTTP(s) |
| POP3(s) | SMB | RDP | VNC |


Scope

```java
ncrack 10.10.10.0/24
ncrack add.els.com
ncrack 10.10.1,2.1-200 //10.10.1.1-200 + 10.10.2.1-200
ncrack 10.10.10.56
```

Running

```java
<service_name>://target:<port_number>
ncrack ssh://10.10.10.130
//multiple
ncrack telnet://10.10.10.130:25 telnet://10.10.10.131:25
//global settings
ncrack 10.10.10.10,15 -p ssh:50,telnet
```

Options

```java
--passwords-first //to try all pws for each user
--resume <path> //continue a previously saved session
-U <username_wordlist>
-P <password_wordlist>
-u username1,username2
-p pwd1,pwd2
-o [N/X/L] //xml output
-i [N/X/L] // provide nmap results to ncrack
```


```meta
phases: 08
requirements: 
results: 
opsec: 
oss: #linux
source: https://github.com/nmap/ncrack
description: Password spray against a lot of services
```