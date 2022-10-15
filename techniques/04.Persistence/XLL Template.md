# XLL Template
XLL is an extension for Excel add-ins. In reality, XLL is just a regular PE-DLL file. The XLL file extension is associated with an icon very similar to other Excel-supported extensions.
If the XLL file is planted into the TrustCenter defined location (by default `C:\Program Files\Microsoft Office\<Office1x>\Xlstart` or `C:\Documents and Settings\<User_name>\Application Data\Microsoft\Excel\XLSTART`) the Add-In will automatically run on starting Excel.
One disadvantage of XLL files is that they can only be loaded by Excel with the correct bitness. For example, a 64-bit XLL can only be loaded by the 64-bit version of Excel.

## Detection
Excel-DNA has another attribute that may hinder coverage with Yara, likely unknown even to the malware authors. For some reason, many Excel-DNA samples have slightly more than 10,000 exported functions, most of them without any meaningful functionality. The Yara PE module export function parsing limit is only 8,192. Therefore, a Yara rule that targets a certain export name located at an index higher than 8192 will not match against the sample.

## Tools
########
########


```meta
ttp: T1137.006
requirements: 
results: persistence
opsec: true
description: Dropping an XLL template to XLStart folder in order to gain persistence through launching Excel
```