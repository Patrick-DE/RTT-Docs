# SharpUp


## Identify modifiable services
``````beacon
beacon> execute-assembly C:\Tools\SharpUp\SharpUp\bin\Debug\SharpUp.exe

=== Modifiable Services ===

  Name             : Vuln-Service-2
  DisplayName      : Vuln-Service-2
  Description      : 
  State            : Running
  StartMode        : Auto
  PathName         : "C:\Program Files\Vuln Services\Service 2.exe"
``````

## Identify AlwaysInstallElevated
``````beacon
beacon> execute-assembly C:\Tools\SharpUp\SharpUp\bin\Debug\SharpUp.exe

=== AlwaysInstallElevated Registry Keys ===

  HKLM:    1
  HKCU:    1
``````
