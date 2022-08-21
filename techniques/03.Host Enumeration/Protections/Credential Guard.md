# Credential Guard
## Identify
Since Windows10 1703 the process `Lsalso.exe` is running.

`(Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard).SecurityServicesRunning
`
* 0: Windows Defender Credential Guard ist deaktiviert (wird nicht ausgeführt)
* 1: Windows Defender Credential Guard ist aktiviert (wird ausgeführt)

## Activate
[MS Docu](https://docs.microsoft.com/de-de/windows/security/identity-protection/credential-guard/credential-guard-manage)

## Deactivate
[MS Docu](https://docs.microsoft.com/de-de/windows/security/identity-protection/credential-guard/credential-guard-manage#deaktivieren-sie-windows-defender-credential-guard)


## Tools
########
########

```meta
ttp: T1000
requirements: 
results: 
description: 
```