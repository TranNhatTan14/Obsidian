---
tags:
  - Tool
  - Network
  - Apple
---
https://manual.nssurge.com/book/understanding-surge/en/
https://kb.nssurge.com/surge-knowledge-base/
https://manual.nssurge.com/

### Use Surge for data

Keyword: 4G, v2ray

Drawback: Chai pin

- Hack mạng, hack app 
- Làm VPN 
- DNS

- Networking tool for iOS and MaOS
- Takeover
- proxy service and virtual NIC takeover
- Proxy
- Take over network requests by starting a local proxy service and configuring the system proxy on 127.0.0.1
- Virtual Network Interface (VIF)
- TUN and TAP VIF
- provide VPN support
- Socket FIlter
- Processing
- Modify the network requests and responses that have been taken over
- Forwarding
- Forward the taken over network request to other proxy sever
- Intercept
- Intercept and save specific data of network requests and responses
- Decrypt HTTPS traffic with MITM
- customize DNS server, configure DNS-over-HTTPS globally
- Surge iOS registers itself as a proxy server, and a TUN virtual network card is established using the Network Extersion API
- Surge Mac, enabling the "Set as System Agent" - proxy (method 1)
- "Enhanced Mode" - virtual network card (method 2)
- Take over local program and take over a network request from another divice

Surge is a **network toolbox** for power users and a high-performance **HTTP/SOCKS5 proxy server**

- Outbound mode
- MitM
- Body viewer
- Remote Controller
- Ruleset & External Policy Group
- TLS
- Scripting: Use JavaScript to extend the ability of Surge as you wish
- Module
- Mock: Mock the API server and return static response. This feature may also be called as Map Local or API Mocking
- HTTP API: Control Surge with HTTP API with another app or from another device
- Proxy Chain: Connection to a remote host will be performed sequentially from one proxy server to another
- L3 Packet Capture: Capture the raw network layer TCP/UDP/ICMP packet and view. You may also export the .pcap file to other tools

[https://github.com/deezertidal](https://github.com/deezertidal)

[https://github.com/Maasea](https://github.com/Maasea)

[https://community.nssurge.com/](https://community.nssurge.com/)

[https://whatshub.top/script](https://whatshub.top/script)

[https://apps.apple.com/us/app/stay-for-safari/id1591620171?platform=iphone](https://apps.apple.com/us/app/stay-for-safari/id1591620171?platform=iphone)

###### Rule Analysis

A series of tools for analyzing rule configuration, including rule counters, performance test

###### Smart Group

A brand new type of policy group, driven by our meticulousu designed algorithm engine, which can automatically select the appropriate policy from the sub-policies of this policy group

###### Body Rewrite

Surge can rewrite the body of HTTP request or response, replacing the original content with regular expression. If you need to make more flexible modification, try scripting

###### Interactive widget

Interactive widgets that support iOS 17 system, can direct operate Surge on the desktop

###### Real-Time Speed View

Show live speed or request list floating window when using other application

###### Encrypted DNS

Use encrypted DNS protocol to perform DNS queries, including DNS-over-HTTPS (DoH, RFC 8484), DNS-over-QUIC and DNS-over-HTTP/3

###### MITM over HTTP/2

Decrypt HTTPS traffic with MITM over HTTP/2 protocol, which can improve the performance of concurrent requests

###### SSH Proxy

You can use SSH protocol as a proxy protocol. The feature is equivalent to the ssh -D command

###### Personal Hotspot Proxy Access

When using an iPhone/iPad as a hotspot, an HTTP or SOCKS5 proxy can be used on the client device to take over the traffic using Surge iOS

###### Hybrid Network

###### WireGuard

Uses Surge as a WireGuard client, converting L3 VPN as an outbound proxy policy

###### Surge Private DDNS

###### Web Dashboard

###### L3 Packet Capture

Capture the raw network layer TCP/UDP/ICMP packets and view. You may also export the .pcap file to other tools

###### Proxy Chain

Connection to a remote host will performed sequentially from one proxy server to another

###### HTTP API

Control Surge with HTTP API with another app or from another device

###### Mock API

You mey mock API server and return a static response. This feature may also be called as Map Local or API Mocking

###### Module

Override the current profile with a set of settings. Highly flexible for diverse purposes.

###### Script 

Use JavaScript to extend the ability of Surge as your wish

###### TLS v1.3

TLS v1.3 support for HTTPS/SOCKS5-TLS proxy

###### Ruleset & External Policy Group

Use a ruleset or proxies that defined in another file or URL

###### Body Viewer

Preview captured data with text viewer, JSON viewer and image viewer, or open it with another app

###### MitM

Decrypt HTTPS traffic with man-in-the-middle (MitM) attack

### Outbound Mode

Forward request to proxy servers with rule-based system or globally

- Local Balance Group
- VMess Protocol
- Trojan Protocol
- Snell v4 Protocol
- Firewall
- Egress Control
- Information Panel
- Response Header Rewrite
- DNS-over-HTTPS
- TUIC Protocol