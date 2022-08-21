# Macros on PowerPoint
* Use "Custom Actions"
    0. Activate Dev Tab (File->Options->Customize Ribbon)
    1. Developer Tab
    2. Visual Basic
    3. Insert choose Model
    4. Insert
    5. Choose an item to associate the action with 
    6. "Mouse Click" or Mouse Over
    7. Run macro

* Office 2007 Custom UI
    * Insert the module and save PowerPoint as a macro-supporting PowerPoint file
    * Unzip the PowerPoint file
    * Edit the _rels/.rels file to add the following line right before the last ```</Relationships>. <Relationship  Type=http://schemas.microsoft.com/office/2006/relationships/ui/extensibility Target=“/customUI/customUI.xml” Id=”Rd6e72c29d34a427e” />```
    * Create a new directory on the same level as the _rels directory called "customUI"
    * Inside customUI directory create a customUI.xml containing ```<customUI xmlns=http://schemas.microsoft.com/office/2006/01/customui onLoad=”name of your VBA module” ></customUI>```
    * Zip the whole directory and rename it to the filename you used to save the original PowerPoint presentation

## Detection


## Tools
########
########

```meta
ttp: T1000
internal: false
requirements: 
results: 
description: 
```