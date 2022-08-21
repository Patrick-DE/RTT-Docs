# Attack Surface Reduction Rules
## Checking for ASR
Can be easily done with [Situational Awareness BOF](https://github.com/trustedsec/CS-Situational-Awareness-BOF) `reg_query_recursive` in Cobalt Strike:
* reg_query_recursive HKLM Software\Policies\Microsoft\Windows Defender\Windows Defender Exploit Guard
* reg_query_recursive HKLM Software\Policies\Microsoft\Windows Defender\Policy Manager

ℹ️ The second query should give you some GUIDs if ASR is enabled, under the registry key ASRRules. The format will be ‘<GUID1>=1|<GUID2>=0'… This means that GUID1 is enabled (=1), GUID2 is disabled (=0). If the value is 2 (=2), it means the ASR rule is in audit mode, so not blocking. See the GUID reference table below to see the GUID mapping to ASR rules.

## ASR Rule to GUID Mapping
You can use this table as a reference for different GUIDs after you found which ASR rules are enabled on a host system, if it is enabled. Source of this table: [Source](https://github.com/microsoft/Microsoft-365-Defender-Hunting-Queries/blob/0d921e78b57dbc786587f750db9c0a2e73371a10/Protection%20events/ExploitGuardAsrDescriptions.txt#L13)

| Rule | GUID |
| ---- | ---- |
|Block executable content from email client and webmail|be9ba2d9-53ea-4cdc-84e5-9b1eeee46550|
|Block Office applications from creating child processes|d4f940ab-401b-4efc-aadc-ad5f3c50688a|
|Block Office applications from creating executable content|3b576869-a4ec-4529-8536-b80a7769e899|
|Block Office applications from injecting code into other processes|75668c1f-73b5-4cf0-bb93-3ecf5cb7cc84|
|Block JavaScript or VBScript from launching downloaded executable content|d3e037e1-3eb8-44c8-a917-57927947596d|
|Block execution of potentially obfuscated scripts|5beb7efe-fd9a-4556-801d-275e5ffc04cc|
|Block Win32 API calls from Office macro|92e97fa1-2edf-4476-bdd6-9dd0b4dddc7b|
|Block executable files from running unless they meet a prevalence, age, or trusted list criteria|01443614-cd74-433a-b99e-2ecdc07bfc25|
|Use advanced protection against ransomware|c1db55ab-c21a-4637-bb3f-a12568109d35|
|Block credential stealing from the Windows local security authority subsystem (lsass.exe)|9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2|
|Block process creations originating from PSExec and WMI commands|d1e49aac-8f56-4280-b9ba-993a6d77406c|
|Block untrusted and unsigned processes that run from USB|b2b3f03d-6a65-4f7b-a9c7-1c7ef74a9ba4|
|Block Office communication applications from creating child processes (available for beta testing)|26190899-1602-49e8-8b27-eb1d0a1ce869|
|Block Adobe Reader from creating child processes|7674ba52-37eb-4a4f-a9a1-f0f9a1619a2c|
|Block persistence through WMI event subscription|e6db77e5-3df2-4cf1-b95a-636979351e5b|


## Tools
########
########

```meta
ttp: T1000
requirements:
results: 
description: 
```