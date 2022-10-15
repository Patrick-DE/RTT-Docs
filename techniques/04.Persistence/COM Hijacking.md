# Com Hijacking
## Theory
Component Object Model (COM) is a technology that enables intercommunication between software components of different languages. COM offers a standard interfaces which allows information to flow between them if implemented.

Each COM component is identified via a class ID (CLSID, a unique 128-bit GUID) and each component exposes functionality which can be identified via interface IDs (IIDs). A COM class (coclass) is an implementation of one or more interfaces, represented by their CLSID or a programmatic identifier (ProgID).

In Windows, COM classes and interfaces are defined in the registry under `HKEY__CLASSES__ROOT\CLSID` and `HKEY__CLASSES__ROOT\Interface` respectively. There exists also a RegFree COM which allows a COM component to exist without using the registry. In this case, data such as CLSID is stored in an XML manifest file.

 ![](/Images/regedit-com.png)

An in-process server allows the specified DLL (this DLL is the actual coclass implementation for this CLSID) to be loaded into the process space of the calling application - **InProcServer32** registers a 32bit in-process server.
Different **ThreadingModel**s can be selected:
* Apartment (Single-Threaded)
* Free (Multi-Threaded)
* Both (Single or Multi)
* Neutral (Thread Neutral).

You may also find **LocalServer32**, which provides a path to an EXE rather than DLL.

[OleView .NET](https://github.com/tyranid/oleviewdotnet) also allows us to find and inspect COM components.

 ![](/Images/oleview-com.png)

COM hijacking: Modify entries to point to an attacker controlled DLL.
The danger: You **will** break functionality.

When an application attempts to locate an object, there is a search order that it goes through.
Machine-wide: `HKEY__LOCAL__MACHINE\Software\Classes` 
Per-user: `HKEY__CURRENT__USER\Software\Classes`
These locations are then merged to form `HKEY__CLASSES__ROOT`.

Any user can hijack or even register new COM objects within HKCU - these only apply to themselves but they do take precedence over those in HKLM.


## Tools
########
########


```meta
ttp: T1546.015
requirements: 
results: persistence
description: Buying ages domains in order to bypass trust based connections
```