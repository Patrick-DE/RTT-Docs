# Hashcat


## Commands
- `-a 0` specifies the wordlist attack mode.
- `-m 1000` specifies that the hash is NTLM.
- `C:\Temp\ntlm.txt` is a text file containing the NTLM hash to crack.
- `D:\Tools\rockyou.txt` is the wordlist.
- `-r rules\add-year.rule` is our custom rule file

## Bruteforce NTLM
- `-a 3` specifies the mask attack.
- `?u?l?l?l?l?l?l?l?d` is the mask.

| ?   | Charset                                |
| --- | -------------------------------------- |
| l   | abcdefghijklmnopqrstuvwxyz             |
| u   | ABCDEFGHIJKLMNOPQRSTUVWXYZ             |
| d   | 0123456789                             |
| h   | 0123456789abcdef                       |
| H   | 0123456789ABCDEF                       |
| s   | `!"#$%&'()*+,-./:;<=>?@[\]^_``{ \| }~` |
| a   | ?l?u?d?s                               |
| b   | 0x00 - 0xff                            |

## [[Crack Credentials]]
## Cracking NTLM
``````sh
hashcat.exe -w 3 -r /rules/oneruletorulethemall -a 0 -m 1000 ntlm.txt C:\Temp\ntlm.txt D:\Tools\rockyou.txt
``````

``````beacon
hashcat.exe -a 3 -m 1000 C:\Temp\ntlm.txt ?u?l?l?l?l?l?l?l?d
``````

## Cracking krb5tgs
``````sh
hashcat.exe -w 3 -r /rules/oneruletorulethemall -a 0 -m 13100 ntlm.txt C:\Temp\ntlm.txt D:\Tools\rockyou.txt
``````

## Cracking krb5asrep
``````sh
hashcat.exe -w 3 -r /rules/oneruletorulethemall -a 0 -m 18200 ntlm.txt C:\Temp\ntlm.txt D:\Tools\rockyou.txt
``````

## Cracking netntlmv2
```sh
hashcat.exe -w 3 -r /rules/oneruletorulethemall -a 0 -m 5600 ntlm.txt C:\Temp\ntlm.txt D:\Tools\rockyou.txt
```


```meta
requirements: 
results: 
oss: #linux
source: https://hashcat.net/hashcat/
description: 
```