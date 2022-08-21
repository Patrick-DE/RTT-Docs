# MSG
MSG file is a file format for storing Microsoft Outlook and Exchange message files. There have been attacks that leveraged this extension combined with embedded OLE objects to bypass corporate email defenses.
[source 1](https://medium.com/@networksecurity/oleoutlook-bypass-almost-every-corporate-security-control-with-a-point-n-click-gui-37f4cbc107d0)
[source 2](https://www.trustwave.com/Resources/SpiderLabs-Blog/Down-the-Rabbit-Hole--Extracting-Maliciousness-from-MSG-Files-Without-Outlook/)


## Tools
########
########

```meta
ttp: T1000
internal: false
requirements:
results: user, admin
description: MSG (email) file containing emails with embedded attachements
```