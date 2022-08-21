# Printer Bug
Forcing any machine in a forest to authenticate to another machine via the MS-RPRN Print System Remote Protocol. It interfaces between a print client and a print server via the print job processing and print system management.
Moreover, this RPC service is accessible by all domain users, and enabled by default.

The process:  
1. Use **RpcRemoteFindFirstPrinterChangeNotificationEx()**, to set up a change notification between a print server (dc-2) and a print client (wkstn1). This caused dc-2 to authenticate to wkstn1.
2. If wkstn1 is configured with [[Unconstrained Delegation]], this would allow the capture of the dc-2 TGT.
3. With the dc-2 TGT, a service ticket (TGS) can be created to access any service on dc-2 with local admin privs (-> domain admin).

The execution:
1. On the server with [[Unconstrained Delegation]] use [[Rubeus#Unconstrained Delegation]] to monitor
2. On your workstation execute the PoC
Where:
-   `dc-2` is the "target" server    
-   `wkstn1` is the "capture" server
3. Get the TGT on the server from 1
``````beacon
[*] 3/9/2022 12:00:07 PM UTC - Found new TGT:

  User                  :  DC-2$@edu.evil.corp
  StartTime             :  18/4/2022 12:12:15 AM
  EndTime               :  18/4/2022 12:12:13 PM
  RenewTill             :  1/1/1970 12:00:00 AM
  Flags                 :  name_canonicalize, pre_authent, forwarded, forwardable
  Base64EncodedTicket   :

 doERz [...snip...] M=

[*] Ticket cache size: 1
``````
4. Use [[Overpass-the-Hash#Manually]] to create a new logon session and [[DCSync]]


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
``` 