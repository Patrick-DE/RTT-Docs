# ldapsearch

## [[Validate Credentials]]
1. Get [[Domain Controller]]
2. Login
    `.\\ldapsearch.exe -x -h 127.0.0.1 -b dc=maxcrc,dc=com -w PW -D "cn=admin"`

3. Flags
    * x: anonymous connect
    * h: server
    * b: root (domain component)
    * w: password
    * W: interactive password
    * D: binddn - user

## [[User enum]]
> ldapsearch -x -h <ip> -s base

```meta
requirements: 
results:
description: Allows you to specify custom LDAP queries
category: Enumeration
stealthy: true
oss: #linux
source: https://linux.die.net/man/1/ldapsearch
```