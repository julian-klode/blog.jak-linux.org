---
author: juliank
date: 2014-08-06 23:01:15+00:00
draft: false
title: Configuring an OpenWRT Router as a repeater for a FRITZ!Box with working Multicast
type: post
url: /2014/08/07/configuring-an-openwrt-router-as-a-repeater-for-a-fritzbox-with-working-multicast/
categories:
- OpenWRT
---

Since some time, those crappy Fritz!Box devices do not support WDS anymore, but rather a proprietary solution created by AVM. Now what happens if you have devices in another room that need/want wired access (like TVs, Playstations) or if you want to extend the range of your network? Buying another Fritz!Box is not very cost efficient - What I did was to buy a cheap TP-Link TL-WR841N (can be bought for 18 euros) and installed OpenWRT on it. Here's how I configured it to act as a WiFi bridge.

Basic overview: You configure OpenWRT into station mode (that is, as a WiFi client) and use relayd to relay between the WiFi network and your local network. You also need igmpproxy to proxy multicast packages between those networks, other UPnP stuff won't work.

I did this on the recent Barrier Braker RC2. It should work on older versions as well, but I cannot promise it (I did not get igmpproxy to work in Attitude Adjustment, but that was probably my fault).

Note: I don't know if it works with IPv6, I only use IPv4.

You might want to re-start (or start) services after the steps, or reboot the router afterwards.




## Configuring WiFi connection to the FRITZ!Box



**Add to: /etc/config/network**

    
    
    config interface 'wwan'
    	option proto 'dhcp'
    

  


(you can use any other name you want instead of wwan, and a static IP. This will be your uplink to the Fritz!Box)

**Replace wifi-iface in: /etc/config/wireless:**

    
    
    config wifi-iface
    	option device 'radio0'
    	option mode 'sta'
    	option ssid 'FRITZ!Box 7270'
    	option encryption 'psk2'
    	option key 'PASSWORD'
    	option network 'wwan'
    

  


(adjust values as needed for your network)





## Setting up the pseudo-bridge



First, add `wwan` to the list of networks in the `lan` zone in the firewall. Then add a forward rule for the lan network (not sure if needed). Afterwards, configure a new `stabridge` network and disable the built-in DHCP server.

**Diff for /etc/config/firewall**

    
    
    @@ -10,2 +10,3 @@ config zone
     	list network 'lan'
    +	list network 'wwan'
     	option input 'ACCEPT'
    @@ -28,2 +29,7 @@ config forwarding
     
    +# Not sure if actually needed
    +config forwarding
    +	option src 'lan'
    +	option dest 'lan'
    +
     config rule
    

  


**Add to /etc/config/network**

    
    
    config interface 'stabridge'
    	option proto 'relay'
    	option network 'lan wwan'
    	option ipaddr '192.168.178.26'
    

  


(Replace 192.168.178.26 with the IP address your OpenWRT router was given by the Fritz!Box on wlan0)


Also make sure to ignore dhcp on the lan interface, as the DHCP server of the FRITZ!Box will be used:

**Diff for /etc/config/dhcp**

    
    
    @@ -24,2 +24,3 @@ config dhcp 'lan'
            option ra 'server'
    +       option ignore '1'
    

  





## Proxying multicast packages



For proxying multicast packages, we need to install igmpproxy and configure it:

**Add to: /etc/config/firewall**

    
    
    # Configuration for igmpproxy
    config rule
    	option src      lan
    	option proto    igmp
    	option target   ACCEPT
    
    config rule
    	option src      lan
    	option proto    udp
    	option dest     lan
    	option target   ACCEPT
    

  


(OpenWRT wiki gives a different 2nd rule now, but this is the one I currently use)

**Replace /etc/config/igmpproxy with:**

    
    
    config igmpproxy
    	option quickleave 1
    
    config phyint
    	option network wwan
    	option direction upstream
    	list altnet 192.168.178.0/24
    
    config phyint
    	option network lan
    	option direction downstream
    	list altnet 192.168.178.0/24
    

  


(Assuming Fritz!Box uses the `192.168.178.0/24` network)

Don't forget to enable the igmpproxy script:

    
    # /etc/init.d/igmpproxy enable

  




## Optional: Repeat the WiFi signal



If you want to repeat your WiFi signal, all you need to do is add a second `wifi-iface` to your `/etc/config/wireless`.


    
    
    config wifi-iface
    	option device 'radio0'
    	option mode 'ap'
    	option network 'lan'
    	option encryption 'psk2+tkip+ccmp'
    	option key 'PASSWORD'
    	option ssid 'YourForwardingSSID'
    

  





## Known Issues


If I was connected via WiFi to the OpenWRT AP and switch to the FRITZ!Box AP, I cannot connect to the OpenWRT router for some time.

The igmpproxy tool writes to the log about changing routes.



## Future Work


I'll try to get the FRITZ!Box replaced by something that runs OpenWRT as well, and then use OpenWRT's WDS support for repeating; because the FRITZ!Box 7270v2 is largely crap - loading a page in its web frontend takes 5 (idle) - 20 seconds (1 download), and it's WiFi speed is limited to about 20 Mbit/s in WiFi-n mode (2.4 GHz (or 5 GHz, does not matter), 40 MHz channel). It seems the 7270 has a really slow CPU.
