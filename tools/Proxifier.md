# Proxyfier

## [[SOCKS Proxy]]
#opsec You can enable DNS lookups through Proxifier, but that will cause DNS leaks from your computer into the target environment.

Open **Proxifier**, go to **Profile > Proxy Servers** and **Add** a new proxy entry, which will point at the IP address and Port of your Cobalt Strike SOCKS proxy.
![](https://rto-assets.s3.eu-west-2.amazonaws.com/socks/proxy-servers.png)

Next, go to **Profile > Proxification Rules**. This is where you can add rules that tell Proxifier when and where to proxy specific applications. Multiple applications can be added to the same rule, but in this example, I'm creating a single rule for **adexplorer64.exe** (part of the Sysinternals Suite). When this application tries to connect to a target host within the **10.10.17.0/24** subnet (**edu.evil.corp**), it will be automatically proxied through the Cobalt Strike proxy server defined above.

![](https://rto-assets.s3.eu-west-2.amazonaws.com/socks/proxy-rule.png)

Now launch ADExplorer and connect to **10.10.17.71** (DC-2).
![](https://rto-assets.s3.eu-west-2.amazonaws.com/socks/ad-connect.png)

You will then see the traffic being proxied in Proxifier, and ADExplorer connects successfully.
![](https://rto-assets.s3.eu-west-2.amazonaws.com/socks/adexplorer.png)


```meta
requirements: 
results: 
oss: #win
source: https://www.proxifier.com/
description: Tunnel (GUI) apps that run on Windows via SOCKS
```