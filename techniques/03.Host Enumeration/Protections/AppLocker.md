## Identify 
1. Via registry `HKLM\Software\Policies\Microsoft\Windows\SrpV2`.
2. [[Group Policy (GPO)#Identify]]
    ```gpo
    KeyName     : Software\Policies\Microsoft\Windows\SrpV2\Exe\921cc481-6e17-4653-8f75-050b80acca20
    ValueName   : Value
    ValueType   : REG_SZ
    ValueLength : 736
    ValueData   : <FilePathRule Id="921cc481-6e17-4653-8f75-050b80acca20"
                    Name="(Default Rule) All files located in the Program Files folder"
                    Description="Allows members of the Everyone group to run applications that are located in the Program Files folder."
                    UserOrGroupSid="S-1-1-0"
                    Action="Allow">
    <Conditions>
    <FilePathCondition Path="%PROGRAMFILES%\*"/>
    </Conditions>
    </FilePathRule>
    ```


## Tools
########
########


```meta
ttp: M1038
requirements:
results: 
description: 
```