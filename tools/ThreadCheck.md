
## [[AMSI]]
### Example
> C:\Users\Rasta>ThreatCheck.exe -f Downloads\Grunt.bin -e AMSI

### Commands
```cmd
C:\>ThreatCheck.exe --help
  -e, --engine    (Default: Defender) Scanning engine. Options: Defender, AMSI
  -f, --file      Analyze a file on disk
  -u, --url       Analyze a file from a URL
  --help          Display this help screen.
  --version       Display version information.
```


```meta
requirements: 
results: 
oss: #win
source: https://github.com/rasta-mouse/ThreatCheck
description: Identifies the bytes that Microsoft Defender / AMSI Consumer flags on.
undetected: 
```