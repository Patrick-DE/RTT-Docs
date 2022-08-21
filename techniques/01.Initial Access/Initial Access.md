# Initial Access

There are mutliple ways to get initial entry here are a summary of often used techniques:
* Scripting functionality ([[01.Initial Access/Macros/Macros]])
* Exploitation of OS of third party; memory corruption, command injection
* Droppers
* In-memory or remote process shellcode injection
* Execution cradles
![cradles](/Images/ExecutionCradles.png "cradles".png)
  
clickonce
* applications act as a wrapper around .NET
* Deploy through Internet Explorer
* .msapp-ref, can be used
* Smart Screen Filter will block, use EV code signing certificate
  
WindowsScriptHost
* jscript / encoded .js .jse
* .vbs, .vbe
* .wsf
* execute via wscript.exe / cscript.exe
* sharpshooter generates all those
  
HTML applications
* .hta can rub#n vbscripts and jscript
* access to com and .net through DotNetToJScript
* executed under mshta.exe
  
shortcut files
* .lnk in zip or file formats
* wrap into an .ISO or 7zip to bypass length
  
creds phishing
* cloning pages
* evilginx2 for relaying session cookies, two factor tokens
* OAuth phishing, office-365-attack-toolkit

Get-Pipes
```csharp
using System.IO;
using System;

namespace GetNamedPipes
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("[*] Found the following pipes:");

            foreach(var pipe in Directory.GetFiles("\\\\.\\\\pipe"))
            {
                Console.WriteLine("- {0}", pipe);
            }
        }
    }
}
```


