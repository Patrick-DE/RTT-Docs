
## [[S4U2self Abuse]]
To modify a ticket, open it with the ASN Editor.  Find the two instances where the **GENERAL STRING** "WKSTN2$" appears. ![](/Images/Pasted%20image%2020220316222605.png)
Double-click them to open the **Node Content Editor** and replace these strings with "cifs".  We also need to add an additional string node with the FQDN of the machine. Right-click on the parent **SEQUENCE** and select **New**.  Enter **1b** in the **Tag** field and click **OK**.  Double-click on the new node to edit the text.
 ![](/Images/Pasted%20image%2020220316222614.png)

```meta
requirements: 
results: 
opsec: 
oss: #win
source: https://github.com/PKISolutions/Asn1Editor.WPF
description: Change a bit in the ticket in order to change the service
```