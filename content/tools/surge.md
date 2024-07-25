---
title: Surge 5
draft: false
tags:
  - network
  - tool
---

Hack mạng, hack app 
Làm VPN 
DNS

https://manual.nssurge.com/book/understanding-surge/en/
https://kb.nssurge.com/surge-knowledge-base/
https://manual.nssurge.com/

Networking tool for iOS and MaOS
Takeover
proxy service and virtual NIC takeover

Proxy
Take over network requests by starting a local proxy service and configuring the system proxy on 127.0.0.1

Virtual Network Interface (VIF)
TUN and TAP VIF
provide VPN support

Socket FIlter

Processing
Modify the network requests and responses that have been taken over

Forwarding
Forward the taken over network request to other proxy sever

Intercept
Intercept and save specific data of network requests and responses
Decrypt HTTPS traffic with MITM

customize DNS server, configure DNS-over-HTTPS globally

Surge iOS registers itself as a proxy server, and a TUN virtual network card is established using the Network Extersion API

Surge Mac, enabling the "Set as System Agent" - proxy (method 1)
"Enhanced Mode" - virtual network card (method 2)

Take over local program and take over a network request from another divice
