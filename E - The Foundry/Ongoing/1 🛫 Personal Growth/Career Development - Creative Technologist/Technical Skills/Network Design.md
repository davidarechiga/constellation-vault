# Network Design
### OSI Model
Used to explain network communications between a host and remote device over a LAN or WAN

Physical
Represents the actual network cables and radio waves used to carry data over a network

Bits - Electrical signal or radiowave

Data Link Layer
Describes how a connection is established, maintained and transferred over the physical layer and uses physical addressing (MAC Addressing)

Frames

Network Layer
Uses logical address to route or switch information between hosts, the network, and the internetworks

Packets, IP addresses, Routers & Layer3 switches

Transport Layer
Manages and ensures transmission of the packets occurs from a host to a destination using either TCP or UDP

Segments (TCP) or Datagrams (UDP)

Session Layer
Manages the establishment, termination, and synchronization of a session over the network

Presentation Layer
Translates the information into a format that the sender and receiver both understand

Application Layer

- &nbsp;
			- Layer from which the message is created, formed and originated
			- consists of high level protocols like HTTP, SMTP and FTP

### Switches
		Switches are the combined evolution of hubs and switches

		MAC flodding
			- Attempt to overwhelm the limited switch memory set aside to store the MAC addresses for each port
		Mac spoofing
			- occurs when an attacker masks their own MAC address to pretend they have the MAC address of another device
			- often combined with ARP spoofing attack
			- Limit static MAC addresses accepted
			- limit duration of time ARP entry on hosts
			- conduct ARP inspection
		Physical Tampering
			- Occurs when an attacker attempts to gain physical access to switch
			- should be looked behind a cage in a locked room

### Routers
		Used to connect two or more networks to form an internetwork
			- SOHO Router to other offices via internet
		Routers rely on a packets IP addresses to determine the proper destination
		Once on the network, it conducts an ARP request to find final destination
		ACLs can be configured on routers
			an ordered set of rules that a router uses to decide whether to permit or deny traffic based upon given characteristics
		IP spoofing is used to trick a router’s ACL
		Out of the box, routers are insecure
			changing default username and password, default routing tables, default IP addresses

### network zones
		WAN Wide Area Network
		LAN Local Area Network
		DMZ De-Militarized Zone

		Any traffic you wish to keep **confidential** crossing the internet should use a **vpn**

		**Sub-Zones can be created to provide additional protection for some servers**

		Extranet
			Specialized type of DMZ that is created for your partner organizations to access over a wide area network

		Intranet are used when only one company is involved
			uses VPN tunnels

### Jumpbox
		Internet facing host
			any host that accepts inbound connections from the internet
				example: web server, email server, communication servers, public services
		DMZ - a segment isolated from the rest of a private network by one or more firewalls that accepts connections from the internet over designated ports
		Everything behind the DMZ is invisible to the outside network

		Harden anything in DMZ best as you can

		Bastion Hosts
			Hosts or servers in the DMZ which are not configured with any services that run on the local network

		to configure devices in the DMZ, a **jumpbox** is utilized
			a jump box is a hardened server that provides access to other hosts within the DMZ
				has to be heavily hardened
			the jump box and management workstation should only have the minimum required software to perform their job and be well hardened

### Network Access Control
		NAC - Security technique in which devices  are scanned to determine it’s current state prior to being allowed access onto a given network
		If the device fails the inspection, it is placed into digital quarantine

		Persistent Agents
			a piece of software that is installed on the device requesting access to the network
		Non-persistent agents
			uses a piece of software that scans the device remotely or is installed and subsequently removed after the scan
		NAC can e used as a hardware or software solution
		IEEE 802.1x standard is used in port-based NAC

### VLANS
		Segment the network
		Reduce collisions
		organize the network
		boost performance
		increase security

		Switch spoofing
			attacker configures their device to pretend it is a switch and uses it to negotiate a trunk link to break out of a VLAN
		DOuble tagging
			attacker adds an additional VLAN tag to create an outer and inner tag
		Prevent double tagging by moving all ports out of the default clan

### subnetting
		act of creating subnetworks logically through the manipulation of IP addresses

		Compartmentalized
		Efficient use of IP addresses
		reduced broadcast traffic
		reduced collisions

		Subnet’s policies and monitoring can aid in the security of your network

### Network Address Translation
		Process of changing an IP address while it transits across a router
		Using NAT can help us hide our network IPs
		Port Address Translation
			Router keeps track of requests from internal hosts by assigning them random high number ports for each request

### Telephony 
		Term used to describe devices that provide voice communication to users
		Modem
			a device that could modulate digital information into an analog signal for transmission over a standard dial-up phone line
		War Dialing
			Random calling for 56k modem servers
			Protect dialup recourses by using the callback feature
		Public Branch Exchange
			internal phone system used in large organizations
		Voice Over Internet Protocol
			Digital phone service provided by software or hardware devices over a data network
		Quality of Service