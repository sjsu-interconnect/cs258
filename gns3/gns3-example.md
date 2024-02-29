# GNS3 Exercise

## Exercise 1
- Connect two VPCSes by a switch.
- Set up IP addresses of the PCs by ```ip <IP address>/<mask>``` [Documentation here](https://docs.gns3.com/docs/emulators/vpcs/)
  - PC1 ```10.0.1.2```
  - PC2 ```10.0.1.3```

## Review: ICMP
- Read [this document](https://www.cloudflare.com/learning/ddos/glossary/internet-control-message-protocol-icmp/)
  - Why do you need ICMP?
  - What does it mean that ICMP is a connectionless protocol?
  - How can you send ping messages to a host?

## Exercise 2
- Start Wireshark on both links
- Send ping from PC1 to PC2
- Check the ICML packets on Wireshark
  - What are source and destination IP addresses?
  - What are source and destination MAC addresses?

## Exercise 3
- Try to change ```10.0.1.3``` to ```10.0.1.2```
  - What happened?
  - Any packets observed?
  - Reference: [Gratuitous ARP](https://wiki.wireshark.org/Gratuitous_ARP)


## Exercise 4
- Change ```10.0.1.3``` to ```10.0.2.3```
- Send ping from PC1 to PC2 
  - What happened?
  - Why?

## Exercise 5
- Change the L2 switch to a router (MikroTik)
- Set appropriate IP addresses to the interfaces (ports) of the router
  - Reference [Mikrotik Router Commands](https://help.mikrotik.com/docs/display/ROS/Command+Line+Interface)
  - ```ip address add address=<a.b.c.d/n> interface=<ether1>```
- Send ping from PC1 to PC2
  - What happened?
  - Why?
- A default gateway
  - Check the options of the ```ip``` command with ```ip ?```
  - You can print the current settings with ```show```
