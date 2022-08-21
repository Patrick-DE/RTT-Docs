# SSH

## Pivoting

### Portforwarding
Connect to root@remote with the certificate foo.pem
Redirect local port 80 on the target to attacker machine 81
-f: will background the SSH connection
-N do not execute a command
```
ssh -i foo.pem root@<REMOTE> -R 81:localhost:80 -f -N
```

```meta
phases: 00
requirements: 
results: 
opsec: 
oss: #linux, #win
source: 
description: 
```