
## [[Categorize Domain]]

⚠️ When attempting to categorise a site in Bluecoat, do not check the category first otherwise it will end up uncategorised! Individual hosts can however be categorised differently.

```
usage: chameleon.py [-h] [--proxy <proxy>] [--check] [--submit]
                    [--domain <domain>]

optional arguments:
  -h, --help         show this help message and exit
  --proxy <proxy>    Proxy type: a = all, b = bluecoat, m = mcafee, i = IBM
                     Xforce
  --check            Perform check on current category
  --submit           Submit new category
  --domain <domain>  Domain to validate
```


```meta
requirements: 
results: 
oss: #py
source: https://github.com/mdsecactivebreach/Chameleon
description: A tool for domain categorisation
undetected: 
```