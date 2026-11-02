# Network+ Study

## New Study Material

IaaS

DS3 Connection

VLAN

<span style="font-family:.AppleSystemUIFont;">Evil Twin</span>

T1

DB-9

Business Continuity Plan

DLP - Data Loss Prevention

Discovery Protocol

Quarantine

Virtual PBX


## Infrastructure
vSAN

iSCSI
DS3/BNC
T1/T3
SIP
Port 5060, 5061

2/4 post racks
Virtual Switch


STP (Spanning Tree Protocol 802.1D)
Blocking
BPDUs are received but they are not forwarded
Used at beginning and on redundant links
Listening
Populating MAC address table
does not forward frames
Learning
Processes BPDUs
Switch determines it’s role in the spanning tree
Forwarding State
Forwards frames for operations

Link cost
associated with the speed of the link. the lower the link’s speed, the higher the cost




## Network Security 4.0
PAP - Password Authentication Protocol
least secure option when it comes to PPP authentication methods
credentials are passed in clear text between the client and the remote node, which makes it rather easy to eavesdrop.

ICA - Independent computing architecture
Citrix Systems proprietary protocol that allows applications running on one platform to be seen and controlled from a remote client

802.1X
Type of network admission control (NAC) which can permit or deny a wireless or wired LAN client access to a network. 
The device seeking admission to the network is called the **supplicant.** 
The device to which the supplicant connects (either wirelessly or through a wired connection) is called the **authenticator**. 
The credentials are checked on Authentication Server

FTP Bounce Attack
FTP supports a variety of commands for setting up a session and managing file transfers. One of these commands is the PORT command and can, in some cases, be used by an attacker to access a system that would otherwise deny the attacker. 

HIPS - Host-Based Intrusion Prevention System
A host that can protect itself by inspecting traffic flowing into its network interface

SSL - Secure Sockets Layer
Provides cryptography and reliability for upper layers (Layer 5-7) of the OSI model. Mostly used for Web Browsers

TLS - Transport Layer Security
Largely replaced SSL as the VPN protocol of choice for providing cryptography and reliability to upper layers of the OSI Model

TACACS+ - Terminal Access Controller Access-Control System Plus
TCP-Based protocol used to communicate with an AAA server. Unlike Remote Authentication Dial-In User Server (RADIUS), TACACS+ encrypts an entire authentication packet rather than just the password.

Authentication Header
one of two major protocols used in IPsec, with the other being Encapsulating Security Payload (ESP)
AH only provides authentication capabilities, whereas ESP can provide both authentication and encryption

PKI - Public Key Infrastructure
Uses digital certificates and a certificate authority to allow secure communication across a public network

Security Policies 
Governing Policy
Focused toward technicians and managers. It is a high-level document that focuses on the organization
**Technical Policies**
policies for passwords
emails
wireless devices
remote access
Bring Your Own Device
**End User Policies**
Acceptable Use (AUP)
Privileged User Agreement
On-boarding/Off-boarding
Consent to Monitoring
Non-Disclosure (NDA)
Cellular
etc
**Standards, Guidelines, & Procedures**
What things are done in an organization
STEP by STEP

Bring Your Own Device (BYOD)
BYOD brings new vulnerabilities
**Bluejacking**
sending of unauthorized messages over Bluetooth
**Bluesnarfing**
Provides unauthorized access to wireless through Bluetooth
**Bluebugging**
Unauthorized backdoor to connect Bluetooth back to attacker
Data Loss Prevention
Policy that seeks to minimize accidental or malicious data loss. It **should be over the entire network** and not just email or file storage

System Lifecycle
Conceptual Design
Preliminary Design
Detailed Design
Production and Installation
Operations and Support - 70% of life
Phase Out
Disposal

Licensing Restrictions and Export Controls
All software needs to have proper licensing, including any virtual machines. Some items are restricted from being exported to certain regions of the world; example is cryptography.
Make sure you are not breaking laws

Incident Response
How will you react to a security violation?

Cleaning up after a breach
Containing the incident

**Means**
Did suspect have technical skills to perform attack
**Motive**
Why would they perform the attack?
**Opportunity**
Do They have the time and access?

Multi-factor Authentication
 Proving your identity with more than 1 method

**Something you know (knowledge factor)**
usernames
passwords
not changing default credentials
using common passwords
weak and short password
PINs
answers to personal questions
**Something You Have (Possession Factor)**
Smartcards
store digital certificates on the card which are accessed once a valid PIN is provided
Key fobs
RFIP tags
**Something You Are (Inherence Factor)**
Fingerprints
Retina Scans
Voice prints
**Something You Do**
How you sign your name
how you draw a particular pattern
how you say a certain passphrase
**Somewhere You Are**
Geotagging
Geofencing

Firewalls
Use a set of rules defining the types of traffic permitted or denied through the device. They can either be a software or hardware

Can also perform NAT or PAT

If you add an access list to an interface and you do not have at least one permit statement, then you effectively shut down the interface because of implicit “deny any” at the end of every list.

Packet Filtering (All or nothing based on rules)
A device that filters traffic based on a set of rules specifying what traffic is allowed to enter and exit an interface **without inspecting the traffic. Based on Packet header**
Source IP address/Port Number
Destination IP address/port number
Stateful
a stateful firewall **inspects traffic** leaving an inside network as it goes out the same session. Then when returning traffic of the same session (as identified by source and destination IP addresses and port numbers) attempts to enter the inside network, the stateful firewall permits that traffic. the process of inspecting traffic to identify unique sessions is called stateful inspection

NextGen Firewalls (NGFW)
Third-Generation firewalls
conduct deep packet inspection and packet filtering
operates at the higher levels of OSI model than traditional firewall

Access Control List (ACL)
Set of rules typically applied to router interfaces that permit or deny certain traffic

Source IP, PORT or MAC

Destination IP, Port, or MAC

Firewall Zones
Inside
Connects to your corporate LAN
Outside
Typically connects to Internet
DMZ (semi trusted)
Connects to devices that should have restricted access from the outside zone (like web servers) 
UTM - Unified Threat Management Devices
Device that combines firewall, router, intrusion detection/prevention system, anti malware, and other security features into a single device

IDS / IPS
IDS - Passive monitor
IPS - Active, can block traffic

Detection Types
Signature-Based
Signature contains strings of bytes (a pattern) that triggers detection
Policy Based Detection
Relies on specific declaration of the security policy e.g. No Telnet allowed
Anomaly-Based
Statistical Anomaly
watches traffic patterns to build baseline
Non-statistical
Administrator defines the patterns/baseline (uploading huge amounts of data)
NIPS - network based
HIPS - host based


VPN - Virtual Private Networks
Enables word in remote offices or telecommuting and allows users to securely connect to the corporate network over an untrusted network

Site-to-Site
interconnect two sites and provides an inexpensive alternative to a leased line

Client to site
connects a remote user with a site and is commonly called remote access

SSL - Secure Sockets Layer
Provides cryptography and reliability for upper layers (Layer 5-7) of the OSI model. Mostly used for Web Browsers

TLS - Transport Layer Security
Largely replaced SSL as the VPN protocol of choice for providing cryptography and reliability to upper layers of the OSI Model

DTLS - Datagram Transport Layer Security
Used to secure UDP traffic. It is based on the TLS protocol and is designed to give security to UDP by preventing eavesdropping, tampering, and message forgery
L2TP - Layer 2 Tunneling Protocol
Lacks security features like encryption. It can be used for secure VPN if combined with additional protocols for encryption services

IPsec - IP Security
VPNs most commonly use IPSec to provide protection for their traffic over the internet
Offers following Protections by default:
**Confidentiality**: 
Data confidentiality is proved by encrypting data. A third party intercepts the encrypted data, they will not be able to interpret it.
**Integrity**:
Data integrity ensures that data is not modified in transit. For example, routers at each end of a tunnel can calculate a checksum value or a hash value for the data and if both routers calculate the same value, then the data has most likely not been modified in transit
 **Authentication**:
Data authentication allows parties involved in a conversation to verify the other party as the party they claim to be.
IKE - Internet Key Exchange
Uses encryption between authenticated peers to create a secure tunnel

Main
3 Separate exchanges occur
Aggressive
more quickly achieves results of main mode using only 3 packets
Quick
negotiates parameters of the IPSec session

Phase 1

- &nbsp;
				1. Encryption and authentication protocols are established between VPN endpoints to create the IKE Phase 1 Tunnel
				1. ISAKMP is established using main or aggressive mode to create a security Association
				2. Key exchange occurs in both directions
			Phase 2
				1. Within the secure IKE Phase 1 tunnel, encryption and authentication protocols are established between VPN endpoints to create the IPSec tunnel
				1. Each data flow uses a separate key exchange
			Transport Mode
				Uses packet’s original IP header and is used for client to site VPN. This approach works will if increasing the packet size could cause issues
			Tunnel Mode
				Encapsulates entire packet to provide new header which will have the source and destination of the VPN termination devices at the different sites. It is used for site to site VPNs

			For Exam:


Worm
Can infect a system or propagate to other systems without any intervention from the end user.

Trojan Horse
a program that appears to be for one purpose but secretly performs another task like collecting data from email

Virus
piece of code (program or script) that infects a system because an end user executed a program


## Wireless Security Encryption
Pre-Shared Key

- &nbsp;
		- both AP and client uses same encryption key
		- Scalability is difficult if key is compromised
		- all clients must know the same password
	WEP
		Wired Equivalent Privacy
			Original 802.11 wireless security stand and claimed to be as secure as wired networks
			NEVER USE WEP, it’s insecure
			**Initialization Vectors**
	WPA
		Wi-Fi Protected Access
			Replaced WEP and its weaknesses. It follows the Temporal Key Integrity Protocol (TKIP) and uses Message Integrity Check (MIC)
	WPA2
		Current Standard
		Created as part of IEEE 802.11i standard and requires stronger encryption and integrity checking through Counter Mode with Cipher Block Chaining Message Authentication Code Protocol (CCMP)

		AES - 128-bit key or above
			password attacks, guessing password with brute force or dictionary

			preshared key - personal mode
			enterprise with authentication server

	WEP and WPA/WPA2 Security Cracking
		utilizes can capture wireless packets and run mathematical algorithms to determine the pre-shared key
		Aircrack-ng

		Network Authentication 802.1x
			Each User authenticates with their own credentials. This is also used in wired networks

	Extensible Authentication Protocol (EAP)
		Authentication performed using 802.1x

	MAC Address Filtering
		Configuring an AP with a listing of permitted MAC addresses (like an ACL)
			Easy to spiff mac addresses

	Network Admission Control (NAC)
		Permits or denies access to the network based on characteristics of the device instead of checking user credentials

		Conducts a picture assessment of client (EG checking the OS and antivirus of client)

	Captive Portals
		Webpage accepts the credentials of the user and presents them to the authentication server

	Geofencing
		GPS or RFID defines real-world boundaries where barriers can be active or passive. Device can send alerts if it leaves area

	Disable SSID Broadcast
		Configures an AP to not broadcast the name of Wireless LAN
			Knowledgeable users can still easily find the SSID using wireless sniffing tools

	Rogue Access Point
		Malicious users setup an AP to lure legitimate users to connect to the AP. Such malicious users can then capture all the packets (data) going through the rogue access point

	Unsecure Wireless Network


![[Image.tiff]]

## Subnetting

## Cable Testing Tools
Multimeter
used with copper cabling to verify, resistant amperage or voltage, and used to test source power to a device or devices own power supply
Cable Tester
Verifies continuity for each wire in the cable to ensure there are no breaks
Cable Certifier
Used with Existing cable to determine it’s category or test data throughput
ca be used to determine length of cable and if cable is properly crimped
Butt Set
Test equipment tools used by telephone technicians to check for dial tone or verify that a call can be placed from the line
limit use for network technicians unless you are working on DSL line

Throughput Tester
Network appliance that typically has multiple network interfaces and can generate high clues of pseudo-random data for wired and wireless networks

Bit-Error Rate Tester (BERT)
Generates patterns at one end of a link and analyzes the received patterns for errors
BER - BIT ERROR RATE

BER = Bit Errors / Bit’s Transferredd


## Antenna Types
Depends on the coverage area
Different factors
Distance
Pattern of wireless coverage
Environment (indoor/Outdoor)
Avoiding Interference

**Omnidirectional** - Radiates power equals in all directions

**Unidirectional** - focuses power in one direction (Yagi Antenna)
Power over a longer distance / connect buildings to other buildings
Also used to keep wireless inside the building

Patch Antenna - 

Whip Antenna - Omnidirectional

Parabolic Antenna - Special Type of Unidirectional / Microwave Signals / Satellite

 


## SCADA/ICS

## Firewalls / ACL Configuration

## Network Attacks

## ARP Caching

## Wireless Modulation
Direct-Sequence Spread Spectrum (DSSS)
Modules data over an entire range of frequencies using a series of signals known as chips They are more susceptible to environmental interference and use entire frequency spectrum to transmit

Frequency-Hopping Spread Spectrum (FHSS)
Devices hop between predetermined frequencies. This increases security as hops occur based on a common timer

Orthogonal Frequency Division Multiplexing (OFDM)
Uses slow modulation rate with simultaneous transmission of data over 52 data streams. This allows for higher data rates while resisting interference between data streams

Frequencies and Channels
IEEE 802.11 standards are differentiated by their characteristics, such as frequency range used:
2.4 GHz band
2.4 GHz to 2.5 GHz range
5 GHz band
5.75 GHz to 5.875 GHz range

Each band has specific frequencies to avoid overlapping other signals
Channels 1, 6, 11

Radio Frequency Interference (RFI)
caused by using similar frequencies to WLAN
Other Wi-Fi Devices (overlapping channels)
Cordless phones and baby monitors
Microwave ovens
Wireless security systems
Physical Obstacles (Walls, appliances, cabinets)
Signal Strength (configurable on some devices)
 **(error reading attachment)**
## Encryption

## Spanning Tree Protocol

## Security Policies

## Troubleshooting

## Point to Point Connection