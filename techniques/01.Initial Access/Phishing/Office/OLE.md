# OLE (Object Linking and Embedding Objects)
Object Linking and Embedding(OLE) is a proprietary technology developed by Microsoft that allows embedding and linking to documents and other objects.
For example, a user can embed a spreadsheet (which is data that belongs to the spreadsheet application) in a word-processing document.
When the word-processing application displays the document to the user, it can establish a connection and can interact with the spreadsheet application to display the spreadsheet data to the user

Embed for example:
* Malicious Office documents
* VBS files 
* JS files 
* EXE files 
* HTA files 
* CHM files

Customize both the extension and the icon

## Payload
Insert > Object > object type list choose package > choose file > customize filename + extension + icon

## Execution
Autotrigger via custom automation
Choose OLE object to embed > Animations > Add Navigation > OLE Action verbs > Activate Contents
Animation tab > Animation Pane > navigate to the Animation Pane > choose object > right side down arrow = dropdown of the Object > Start after previous


## Tools
########
########

```meta
ttp:
internal: false
requirements:
results: user, admin
description: Object Linking and Embedding Objects in case macros are restricted.
```
