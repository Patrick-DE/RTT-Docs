# Exlcusions
Pretty much every antivirus solution allows you to define exclusions to on-demand and real-time scanning.  Windows Defender allows admins to add exclusions via GPO, or locally on a single machine.

The three flavours are:

-   Extension - exclude all files by their file extension.
-   Path - exclude all files in the given directory.
-   Process - exclude any file opened by the specified processes.

```beacon
beacon> remote-exec winrm dc-2 Get-MpPreference | select Exclusion*

ExclusionExtension : 
ExclusionIpAddress : 
ExclusionPath : {C:\Shares\software}
ExclusionProcess :
```

If the exclusions are configured via GPO and you can [[Dump GPOs]] the corresponding Registry.pol file, you can read them with [[GPRegistryPolicyParser]].

## Define Defender Exclusions
```powershell
Set-MpPreference -ExclusionPath "<path>"
```

## Tools
########
########


```meta
ttp: T1562.001
requirements:
results: 
description: 
```