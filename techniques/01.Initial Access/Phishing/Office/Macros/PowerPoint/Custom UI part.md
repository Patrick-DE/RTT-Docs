Run the VBA module automatically as soon as the user enables macros.

1. Insert the module you want and save the PowerPoint presentation as a macro supporting PowerPoint file type
2. Unzip the PowerPoint file you saved
3. Edit the _rels/.rels file to add the following line right before the last </ Relationships>.  
`<Relationship Type=http://schemas.microsoft.com/office/2006/relationships/ui/extensibility Target=“/customUI/customUI.xml” Id=”Rd6e72c29d34a427e” />`
4. Create a new directory on the same level as the _rels directory called “customUI”.
5. Inside customUI directory create a customUI.xml file containing the following.  
`<customUI xmlns=http://schemas.microsoft.com/office/2006/01/customui onLoad=”name of your VBA module” ></customUI>`
6. Zip the whole directory and rename it to the filename you used to save the original PowerPoint presentation



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