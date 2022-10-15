It was discovered that there is an open redirect feature/vulnerability in Google.
The following steps will descript the usage of this so called feature:
1. Create an *_ah* directory on our domain and inside it another directory called *conflogin*
2. Place our phishing page inside the *conflogin* directory in index.html or index.php file
3. Send the following link to our target `https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fappengine.google.com%2F_ah%2Fconflogin%3Fcontinue%3Dhttps%3A%2F%2Fattacker.domain%2F&service=ah`


## Tools
########
########

```meta
ttp: 
internal: false
requirements:
results: user, admin
description: Use open redirects to phish victims
```