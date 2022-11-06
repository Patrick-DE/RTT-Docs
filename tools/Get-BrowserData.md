## [[Bookmarks-History]]
```ps
.PARAMETER Browser
    The type of browser to enumerate, 'Chrome', 'IE', 'Firefox' or 'All'
.PARAMETER Datatype
    Type of data to enumerate, 'History' or 'Bookmarks'
.PARAMETER UserName
    Specific username to search browser information for.
.PARAMETER Search
    Term to search for

Example:
Enumerates bookmarks for Internet Explorer for the user 'user1' and only returns results matching the search term 'github'.

Get-BrowserData -Browser All -Datatype History -UserName user1 -Search 'github'


```

```meta
requirements: 
results: 
oss: #ps1
source: https://github.com/rvrsh3ll/Misc-Powershell-Scripts/blob/master/Get-BrowserData.ps1
description: Enumerates browser history or bookmarks for a Chrome, Internet Explorer, and/or Firefox browsers on Windows machines.
undetected: 
```
