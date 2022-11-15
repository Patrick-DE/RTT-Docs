## [[Obfuscation]]
```sh
Usage:
  nimcrypt -f file_to_load -t csharp/raw/pe [-o <output>] [-p <process>] [-n] [-u] [-s] [-e] [-g] [-l] [-v] [--no-ppid-spoof]
  nimcrypt (-h | --help)

Options:
  -h --help     Show this screen.
  --version     Show version.
  -f --file filename     File to load
  -t --type filetype     Type of file (csharp, raw, or pe)
  -p --process process   Name of process for shellcode injection
  -o --output filename   Filename for compiled exe
  -u --unhook            Unhook ntdll.dll
  -v --verbose           Enable verbose messages during execution
  -e --encrypt-strings   Encrypt strings using the strenc module
  -g --get-syscallstub   Use GetSyscallStub instead of NimlineWhispers2
  -l --llvm-obfuscator   Use Obfuscator-LLVM to compile binary
  -n --no-randomization  Disable syscall name randomization
  -s --no-sandbox        Disable sandbox checks
  --no-ppid-spoof        Disable PPID Spoofing
```

```meta
requirements: 
results: 
category:
oss: #win
source: https://github.com/icyguider/Nimcrypt2
description: .NET, PE, & Raw Shellcode Packer/Loader written in Nim
```