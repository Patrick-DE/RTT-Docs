# Examples

|  |  |
|---|---|
| ssh -L EXTIP:80 | Lokal |
| ssh -R EXTIP:80 | Remote |


## Ausgangslage:

*   Ziel: Direkt an die Datenbank
*   Notebook lauscht auf 3306
*   Firewall alle Ports blocked außer 22
*   Server lauscht NUR auf 127.0.0.3306
*   Tooling if more complex: reGeorg


```bash
ssh -L 3306:127.0.0.1:3306 ubuntu@172.17.0.4 -N

Ssh |-lokal | ClientPort | access auf dem Server nach folgende Addresse | ssh daten | -N
```


## Remote Tunnel

ReverseShell / Webshell

```java
ssh -R 3306:127.0.0.1:3306 ubuntu@172.17.0.4 -N
```

Lausche bei target auf 3306 und schicke es an mich zurück

Requirement:
*   OpenSSH on the local machine
    
Setup SSH connection to the server:
```java
ssh -R 6666:127.0.0.1:22 patrick@cloud.eisenschmidt.family -p 44022 -N
```

Make all traffic redirect to local OpenSSH client, thus make remote traffic accessible locally

```java
ssh -i cert.pem -D 0.0.0.0:1234 ubuntu@server
ssh -D 8080 -p 6666 Sh8do@127.0.0.1 -N
```
