# File Properties

### Store Payload

* Powershell command resides in the "Author" property
  * Every time you edit the file, the "Authors" property will be deleted
* Hide payload on custom Excel forms or even inside the working spreadsheet, in an encoded form

### Store Arguments

* PowerShell command's arguments via invocation with StdIn.WriteLine

### Detection

* AutoOpen is picked up by some AVs
* Document_Open() is picked up by some AVs
* AMSI (on Win10) will most likely block the payload
* Variable is not used anywhere in the macro. Including some unused code is a simple obfuscation tactic though.

### Execution

1. Accessing the file's properties
2. Leveraging Windows Script Host to run a program locally, manipulate the contents of the registry, create a shortcut, or access a system folder.
3. Using WshShell object for executing PowerShell
4. Append arguments via StdIn.WriteLine

## Tools
########
########


```meta
ttp: TA0005
requirements: 
results: 
description: Macro leveraging file properties to hide its paylods and StdIn to avoid logging
```