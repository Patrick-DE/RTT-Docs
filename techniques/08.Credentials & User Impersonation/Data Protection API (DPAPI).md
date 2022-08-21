# DPAPI

The Data Protection API (DPAPI) is a component built into Windows that provides a means for encrypting and decrypting data "blobs". It uses crypto keys that are bound to either a specific user or computer account and allows Windows and external applications to protect or unprotect data.

DPAPI is used by the Windows Credential Manager to store saved secrets such as RDP credentials, and others like Google Chrome.

The credential manager blobs are stored in the user's `AppData` directory.
>ls C:\Users\$env:username\AppData\Local\Microsoft\Credentials

The native `vaultcmd` tool can also be used to list them.
>beacon> run vaultcmd /listcreds:"Windows Credentials" /all

If size not null some creds are saved
>ls C:\Users\$env:username\AppData\Local\Google\Chrome\User Data\Default

## Tools
########
########


```meta
ttp: T1000
requirements: admin
results: 
description: 
```