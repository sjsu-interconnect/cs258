# GNS3 Preparation
- Wireshark 
  - Wireshark is a free and open-source packet analyzer. It is used for network troubleshooting, analysis, software and communications protocol development, and education.
  - Install Wireshark from [https://www.wireshark.org/](https://www.wireshark.org/)
- Router Image
  - GNS3 does not come with any (virtual) routers. We need to download the image of a real router. In this class, we use a router image of [MikroTik](https://en.wikipedia.org/wiki/MikroTik), since it is freely available (unlike ~~Cisco's~~ router images).
  1. Go to [the MikroTik Router OS page](https://mikrotik.com/download)
  2. Scroll down to the "Cloud Hosted Router" section
  3. Download the Raw Disk Image of the ```7.13.5 Stable``` version
  4. Open the GNS3 Preferences; Go to QEMU the section from the left bar
  5. Click "New" button
  6. Name it as ```MikroTik-7.13.5```; Set the console type to ```telnet```; and import the router disk image you downloaded (you need to unzip it)
  7. Select the created router template and Click "Edit" button
  8. Under "General Settings" tab, change "Category" from "End devices" to "Routers"
  9. Under "Network" tab, 
     1.  Change "Adapters" to 5
     2.  Click "Configure custom adapters" and change the port names so they start from 1 (e.g. ```ether1```, ```ether2 ```, ..., ```ether5```). Note: this is because the actual port names defined in a MikroTik router starts from ```ether1``` to ```etherN```. You can check it by ```/interface print```