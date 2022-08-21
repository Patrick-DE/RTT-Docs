# sslstrip

Although most of the users will confirm the certificate exception, enhancements in SSL attack tools have found ways to exploit SSL without the need to inject a self-signed cert. The default port is 10000 and MITM needs to be done before starting the tool.  
BlackHat 2009 Moxie Marlinspike introduced a new method for extracting information from a secure session by attacking HTTP. In order to demonstrate how this works, Marlinspike released a tool named sslstrip.

## [[08.Credentials & User Impersonation/MITM]]
![](/Images/Tools/4618cef1-9c6f-41a2-b7ba-bd5e41ff22ad.png)

There are some issues that present themselves in this type of attack for example:

*   Some content-encoding, such as gzip, is difficult to parse.
*   Cookies that are sent over HTTPS will not be sent over HTTP that has striped the SSL.
*   Any cached pages which did not have the links swapped out

In order to counter these shortcomings, sslstrip actually Strips parts of the requests for this information:

*   Stopping the secure bit on the _Set-Cookie_ statements on the pages
*   Strip the difficult encodings from the client requests
*   Strip the _if-modified-since_ headers to eliminate the cached pages being requested

How to proceed:

1.  Enable IP forwarding
2.  Setup port redirection using iptables
3.  Start sslstrip on port 8080, -w save logs into file, -f replace favicon
4.  Start ARP MitM between victim and gateway
    ```java
    echo 1 > /proc/sys/net/ipv4/ip_forward
    iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-ports 8080
    sslstrip -a -f -l 8080 -w els-sslt
    ```


```meta
requirements: 
results: 
opsec: 
oss: #linux
source: https://github.com/moxie0/sslstrip
description: sslstrip is a MITM tool that implements Moxie Marlinspike's SSL stripping attacks.
```