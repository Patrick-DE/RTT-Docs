
## [[Reverse Port Forward]]
Machines:

| Nr | System | Task |
| -- | ------ | ---- |
| 1  | _dc1.edu.evil.corp_ | Proxy Server |
| 2  | _ad.evil2.corp_ | Target |
| 3  | _dc1.evil.corp_ | Start |

1. Create proxy on 1 to forward to 2 port 4444
`netsh interface portproxy` allows to view and configure a proxy for both IPv4 and IPv6 traffic between networks.
>netsh interface portproxy add v4tov4 listenaddress= listenport= connectaddress= connectport= protocol=tcp

Where:
-   **listenaddress** is the IP address to listen on (probably always 0.0.0.0).
-   **listenport** is the port to listen on.
-   **connectaddress** is the destination IP address.
-   **connectport** is the destination port.
-   **protocol** to use (always TCP).

>netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=4444 connectaddress=10.10.14.55 connectport=4444 protocol=tcp

2. Verify its there with `netsh interface portproxy show`. 
```cmd
C:\>netsh interface portproxy show v4tov4
Listen on ipv4:             Connect to ipv4:
Address         Port        Address         Port
--------------- ----------  --------------- ----------
0.0.0.0         4444        10.10.14.55    4444
```

3. Connect from 3 zu 1 and you will see the connection being made in the PowerShell script.

Test if the proxy works on 2:
``````powershell
$endpoint = New-Object System.Net.IPEndPoint ([System.Net.IPAddress]::Any, 4444)
$listener = New-Object System.Net.Sockets.TcpListener $endpoint
$listener.Start()
Write-Host "Listening on port 4444"
while ($true)
{
  $client = $listener.AcceptTcpClient()
  Write-Host "A client has connected"
  $client.Close()
}
``````

Initiate connection from 3.
``````powershell
PS C:\> Test-NetConnection -ComputerName 10.10.1.8 -Port 4444

ComputerName     : 10.10.1.8
RemoteAddress    : 10.10.1.8
RemotePort       : 4444
InterfaceAlias   : Ethernet
SourceAddress    : 10.10.2.78
TcpTestSucceeded : True
``````

4. To remove the portproxy:
>C:\>netsh interface portproxy delete v4tov4 listenaddress=0.0.0.0 listenport=4444

Aspects to note about netsh port forwards:
- You need to be a local administrator to add and remove them, regardless of the bind port.
- They're socket-to-socket connections, so they can't be made through network devices such as firewalls and web proxies.
- They're particularly good for creating relays between machines.

```meta
requirements: admin
results: 
stealthy: true
methods: 
oss: #win
source: 
description: 
```