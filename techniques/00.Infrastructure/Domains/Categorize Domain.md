## Setting up dummy site
Two steps: 
* point the domain to the dummy site you want it to be categorised to
* request a category from the different services 

## Request a category
Request a new finance category on the following sites: 

IMPORTANT: Immediately request a new category, do not check the category beforehand! Otherwise your site is categorised anyways with 'uncategorised' instead of immediately what you want it to be. There is a chance that reassigning categories are verified by analysts. This increases the chance of the domain being categorised as something like 'placeholder' (blocked category at some banks)     

Side note: Use fake details when asked for Name, Email, Company name. Create for example a protonmail account for email.

| | |
|---|---|
| Fortinet | https//fortiguard.com/faq/wfratingsubmit <br/>https://www.fortiguard.com/learnmore#wf |
| Bluecoat | https://sitereview.bluecoat.com/ <br/> - top domain is sufficient, no need for subdomains (if you submit subdomain, categories are not transferred to the domain, but categories for the domain are transferred to the subdomains as well) <br/> - it seems (this might be incorrect) that bluecoat manually verifies domains that have been requesting financial categories but automatically assigns other categories such as sport/recreation |
| palo alto | https://urlfiltering.paloaltonetworks.com/ |
| F5 | Not public |
| Check Point | https://www.checkpoint.com/urlcat/ <br/>(even with free account not much you can do) |
| McAfee | https://www.trustedsource.org/en/feedback/url?action=checksingle <br/>use an account |
| Cisco WFA | Check category of domain <br/> https://talosintelligence.com/reputation_center/lookup <br/> There is limit of 10 requests <br/>Request new category: <br/> WSA FAQ: How do I verify which category a URL belongs to and submit a change request? <br/>1. Create bogus Cisco account <br/>2. Go to  https://talosintelligence.com/tickets <br/> 3. Click Create New Ticket.<br/> 4. Click Submit a Web Categorization Ticket. <br/> 5. Enter the URL, IP address, or domain of the website in question (up to 50 entries can be entered at a time) and click Get Category Data.<br/>6. In order to suggest the same category for multiple entries, choose from the categories in the box next to "Bulk Select Download" (up to five categories can be chosen). Then, from the Bulk Select Download drop-down list, choose Web Security Appliance.<br/> 7. In order to suggest categories for individual entries, choose from the categories box next to each entry in the column "Suggested Content Categories". Then, from the Select Platform drop-down list, choose Web Security Appliance.<br/> 8. Add comments and site descriptions to the box below the entries. Provide as much detail as possible.<br/> 9. Click SUBMIT.<br/> 10. Later, verify the status on the Talos Intelligence Tickets portal page.

## Tools
########
########


```meta
ttp: T1583.001
internal: false
requirements: 
results: 
description: Categorizing / Regategorizing domains in order to bypass trust based network filtering
```