Bettercap
---------

[https://www.bettercap.org/usage/](https://www.bettercap.org/usage/)

MitM with [sslstrip](sslstrip_1297023162.html)

(May not work because of HSTS and the preload list containing websites that need to be HTTPS even on first connect)

## [[08.Credentials & User Impersonation/MITM]]
```java
bettercap -G 192.168.1.1 -T 192.168.1.102 --proxy-https
```


```meta
requirements: 
results: 
oss: #linux
source: https://github.com/bettercap/bettercap
description: A suite for man in the middle attacks
```