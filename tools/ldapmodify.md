# ldapadd

## [[Create Account]]
Add a new user to the AD via ldap
1. Create the file called user.ldif.txt
    ```bash
    # jdoe, Users, maxcrc.com
    dn: uid=jdoe,ou=People,dc=maxcrc,dc=com 
    ObjectCIass: posixAccount 
    objectC1ass: top 
    objectC1ass: inetOrgPerson 
    givenName: John 
    sn: Doe 
    uid: jdoe 
    homeDirectory: /home/jdoe 
    cn: jdoe 
    uidNumber: 18735 
    gidNumber: 500
    ```
2. Apply the file and add an element to the LDAP:
    `.\ldapmodify.exe -a -x -h 127.0.0.1 -D cn=Manager,dc=maxcrc,dc=com -W -f .\user.ldif.txt`


```meta
phases: 05,07
requirements: 
results: 
oss: #win, #linux
source: https://www.thegeekstuff.com/2015/02/openldap-add-users-groups/
description: Add user to OU
```