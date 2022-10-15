# Macros

Macros can be written in one of the following languages:
* visual basic macros (excel 5.0)
* excel 4.0

| File extension | File Type           | Macros Permitted                                            |
| -------------- | ------------------- | ----------------------------------------------------------- |
| DOCX           | compressed document | No, with remote template                                    |
| DOTX           | compressed template | No                                                          |
| DOCM           | compressed document | Yes, Can be renamed and keep macro capabilities (RTF files) |
| DOTM           | compressed template | Yes                                                         |

Remote template in DOCX: File->Options->Add-Ins->Manage:Templates->Go

Identify associated filetypes:
```
assoc | findstr /i “word”
assoc | findstr /i “excel”
assoc | findstr /i “powerp”
```

Information about macros
* cross-platform
* Sandboxed on macOS
* direct WinAPI access
* COM object access
* GPOs applied per application
* Access scripts (.accde), manfile, 
* It is possible to sign payloads
* protected view since 2016
	* does not work for .slk, .one, .pub, .accde
	* still enable content (maros) required
	* change macro alert via AutoOpen / Document_Open() (https://www.greyhathacker.net/?tag=activex)
	* go legacy dialog: add the visibility="hidden" attribute to the workbookView element in the xl/workbook.xml file
	* remote template injection, settings.xml.rels file inside the docx
	!(Images/RemoteTemplateInjection.png "macro")
	
	* winapi + com
	![winapi](/Images/macro-winapi-com-1.png "winapi1".png)
	![winapi1](/Images/macro-winapi-com-1.png "winapi".png)
* OLE objects: can be embedded inside Office documents
	* .exe, .bat, .lnk, .hta, .vba, .js
	* there is a blocklist since 2016


## Tools
########
########

```meta
ttp: T1204.002
internal: false
requirements: 
results: user, admin
description: Macros used for phishing attacks via office
```