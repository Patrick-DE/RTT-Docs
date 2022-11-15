
## [[Services]]
* Start service  
`sc [<ServerName>] start <ServiceName>`
* Stop dervice
`sc [<ServerName>] stop <ServiceName>` 
* List all services
`sc queryex type=service state=all`
* List service names only
`sc queryex type=service state=all | find /i "SERVICE_NAME:"`
* Search for specific service
`sc queryex type=service state=all | find /i "SERVICE_NAME: myService"`
* Get security identifier, [read more](https://www.winhelponline.com/blog/view-edit-service-permissions-windows/)  
`sc.exe sdshow [service_short_name]`


```meta
requirements: 
results: 
stealthy: true
oss: #win 
source: 
description: 
```