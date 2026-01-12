# Chapter 1 Mastering Security Basics
## Core Security Goals
<u>What is a Use Case?</u>
A **use case** describes a goal that an **organization** wants to **achieve**. A common naming strategy for a use case is a **verb-noun** example: “Place Order” 
Imagine Lisa wants to place an order via an online e-commerce system
- Place Order Use Case elements:
	- **Actors**
		- Lisa a buyer or Billing system or Fulfillment system
	- **Precondition**
		- A precondition must occur before the process can start. “Lisa needs to select item before an order can be placed.”
	- **Trigger**
		- Starting check out process
	- **Postcondition**
		- Occur after the actor triggers the process. In this case, Lisa’s order will be put into the system after she completes the purchase. SHe’ll receive an acknowledgment for her order
	- **Normal Flow**
		- A use case will typically list each of the steps in a specific order
	- **Alternate Flow**
		- All purchases won’t be the same. For example, instead of using existing billing and shipping information, Lisa might want to use different credit card or a different shipping address. It’s also possible for lisa to change her mind and abandon the process before completing or even cancel the purchase after she completes the process

## CIA Triad
- Confidentiality
- Integrity
- Availability

## Ensure Confidentiality
A common use case that any organization has is to support confidentiality. ***Confidentiality*** prevents unauthorized disclosure of data
<u>Confidentiality Methods</u>
- **Encryption**
	- Scrambling of data to make it unreadable by unauthorized personnel
		- Example: encrypting PII in emails before they are sent
- **Access Controls**
	- *Identification*
		- Users claim an identity with a unique username
	- *Authentication*
		- Users prove their identity with authentication such as with a password
	- *Authorization*
		- Next, you can grant or restrict access to resources using an authorization method, such as permissions
- **Steganography and Obfuscation**
	- Steganography
		- Hiding data within data
	- Obfuscation
		- Attempt to make something unclear or difficult to understand

Summary: Confidentiality ensures the data is only viewable by authorized users. The best way to protect the confidentiality of data is by encrypting it. This includes any type of data , such as PII, data in databases, and data on mobile devices. Access controls help protect confidentiality by restricting access. Steganography helps provide confidentiality by hiding data, such as hiding text files within an image file.

## Provide Integrity
Another common use case is to support integrity. ***Integrity*** provides assurances that data has not been changed (modified, tampered with, or corrupted)
<u>Verifying Integrity</u>
- **Hashing**
	- A hash is simply a number created by executing a hashing algorithm against data, such as a file or message
	- Hashing Algorithms
		- Message Digest 5 (MD5)
		- Secure Hash Algorithm (SHA)
		- Hash-based Message Authentication Code (HMAC)
	- Hashing doesn’t tell you what modified the message, only that the message has been modified and is not to be trusted
	- Use with email and any data file. Some email programs use message authentication code (MAC)
	- You can also use hashing techniques when downloading or transferring files.
	- Two key concepts to integrity:
		- Integrity provides assurances that data has not been modified, tampered with , or corrupted
		- Hashing verifies integrity
- **Digital Signatures, Certificates, and Non-Repudiation**
	- Digital signatures can verify the integrity of emails and files and they also provide authentication and non-repudiation (cannot deny). Digital signatures require certificates

## Increase Availability.
Availability ensures that systems are up and operational when needed and often addressed single points of failure. You can increase availability by adding the following:
- **Redundancy and Fault Tolerance**
	- Adds duplication to critical systems
	- Must remove each single point of failure (SPOF)
		- Disk Redundancies
			- RAID-1 (mirroring)
			- RAID-5 (striping with parity)
			- RAID-10 (striping with a mirror)
		- Server redundancies
			- Failover cluster
			- Virtualization
			- Load Balancing
			- Site redundancies
			- Backups
			- Alternate Power
			- Cooling Systems
- **Patching**
	- Software bugs cause a wine range of problems, including security issues and even random crashes
	- Organizations commonly implement patch management programs to ensure that systems stay up to date with current patches

## Resources Versus Security Constraints
- Organizations frequently need to balance resource availability with security constraints
- Security experts might say the cost for additional resources is worth it but executives looking to increase the value of the company don’t see that

## Introducing Basic Risk Concepts
One of the basic goals of implementing IT security is to reduce risk.
Keywords:
- **Risk**: the possibility or likelihood of a threat exploiting a vulnerability resulting in a loss
- **Threat**: any circumstance or event that has the potential to compromise confidentiality, integrity, or availability
- **Security Incident**: an adverse event or series of events that can negatively affect the confidentiality, integrity, or availability of an organization’s IT systems and data. This includes intentional attacks, malicious software infections, accidental data loss and much more
- **Risk Mitigation**: reduces the chances that a threat will exploit a vulnerability. Reducing vulnerabilities and reducing impact of threat
**Summary**: Risk is the likelihood that a threat will exploit a vulnerability. Risk mitigation reduces the chances that a threat will exploit a vulnerability, or reduces the impact of the risk, by implementing security controls

## Understanding Control Types
Security Control types are as follows:
- **Technical** = controls using technology
- **Administrative** = controls use administrative or management methods
- **Physical** = refers to controls you can physically touch
- **Preventive** = attempt to prevent an incident from occuring (**before**)
- **Detective** = attempt to detect incidents after they have occurred (**during**)
- **Corrective** = attempt to reserve the impact of an incident (**after**)
- **Deterrent** = attempt to discourage individuals from causing an incident
- **Compensating** = alternative controls used when a primary control is not feasible
Most security controls can be classified as technical, administrative, or physical

## Technical Controls
An administrator installs and configures a **technical control** and the technical control then provides the **protection automatically**. Here are several examples:
- **Encryption**
- **Antivirus software**
- **IDS / IPS**
- **Firewall**
- **Least Privilege**
Technical Controls use technology to reduce vulnerabilities

## Administrative Controls 
**Administrative controls** use methods mandated by organizational **policies** or other **guidelines**. Common administrative controls are:
- **Risk assessments**: quantify and qualify risks within an organization so that the organization can focus on the serious risks
- **Vulnerability assessments**: attempts to **discover** current vulnerabilities or weaknesses
- **Penetration Tests**: These go a step further than a vulnerability assessment by attempting to **exploit vulnerabilities.**
Some administrative controls focus on physical security and the environment. Example: an access list identifies individuals allowed into a secured area and Guards verify identification for area

Many administrative controls are also known as operational or management controls. These help ensure day to day operations of an org comply with the overall security place of the organization. These include:
- **Awareness and training**: Training helps users maintain password security, follow clean desk policy and understand threats such as phishing and malware, and much more
- **Configuration and change management**: uses baselines to ensure systems start in a secure hardened state. Change management helps ensure that changes don’t result in unintended configuration errors
- **Contingency planning**: reducing the overall impact on the organization if an outage occurs
- **Media protection**: Media includes physical media such as USB flash drives, external and internal drives, and back up tapes
- **Physical** and **environmental** protection: Cameras, door locks, HVAC

## Physical controls
Any controls you can physically touch. Examples: Lighting, signs, fences, security guards and more. Many physical controls are also technical controls

## Control Goals
These next controls are classified by their intended goal.
- **Preventive Controls**: preventing security incidents (prepare and take action)
	- **Hardening**: practice of making a system or application more secure than its default configuration
	- **Security awareness and training**: ensuring users are aware of security vulnerabilities and threats helps prevent incidents
	- **Security Guards**: Guards prevent and deter many attacks
	- **Change management**: ensures changes don’t result in unintended outages
	- **Account disablement policy**: ensures that user accounts are disabled when an employee leaves
- **Detective Controls**: attempting to detect when vulnerabilities have been exploited. Some examples are
	- **Log Monitoring**
	- **Trend Analysis**
	- **Security Audit**
	- **Video Surveillance**
	- **Motion Detection**

### **Comparing Detection and Prevention Controls**
- Detective controls can’t predict when an incident will occur
	- Video Surveillance: Recording capabilities make cameras detective
	- Guards are primarily prevention controls

### **Corrective Controls**
Corrective controls attempt to reverse the impact of an incident or problem after occurred. Some examples are:
- **IPS**
- **Back Ups and system recovery**

### **Deterrent Controls**
Deterrent Controls attempt to discourage a threat. They are often described as preventive controls. Some examples are:
- Cable Locks
- Hardware Locks

### **Compensating Controls**
Alternative controls used instead of a primary control. an example of this is using Time based one time password when a smart card is not ready for new employees

### Combining Control Types and Goals
Control types are not mutually exclusive. Will fit into multiple categories

### Implementing Virtualization
Allows you to host one or more virtual systems or virtual machines (VMs) on a single physical system. Remember the following terms:
- **Hypervisor**
- **Host**
- **Guest**
- **Host elasticity and scalability**

### Comparing Hypervisors
- Type I: run directly on the system hardware “Bare-metal”
- Type II: run as software within a host operating system

### Application Cell or Container Virtualization
Runs applications in isolated cells (or container)

## Secure Network Architecture
VMs can provide segregation, segmentation and isolation of individual systems

### Snapshots
provides you with a copy of the VM at a moment in time, which you can use a back up.

## VDI/VDE and Non-Persistence
User’s desktop operating system runs as a VM on a server.
- Persistence: User changes stay when logged out
- Non-Persistence: User changes revert back to a snapshot when logged out 

### VMs as Files
a VM is a group of files. easy to migrate to different physical servers when one fails

### Risk Associated with Virtualization
- **VM Escape**: an attack that allows an attacker to access the host system within the virtual system.
- **VM Sprawl**: occurs when an organization has many VMs that aren’t managed properly.

### Loss of Confidentiality
VMs make it easy to steal data, internally and externally

## Using Command-Line Tools
can be invaluable when troubleshooting or analyzing systems

## Windows Command Line
launch the Command Prompt

## Linux Terminal
launch the Terminal App

## Understanding Switches and Getting Help
Almost every command has options available that you can invoke with a switch.
- **Windows**: slash (/) or dash(-) after the command
- **Linux**: dash(-) after command
To get help, use:
- **Windows**: /?
- **Linux**: no switch

## Understanding Case
Most windows commands are not case sensitive. Linux commands are case sensitive.

## Ping
uses ICMP packets to test connectivity for remote systems. also used to test valid host names, test the NIC, and check security posture of a network. Examples:
- ping 192.168.1.1
- ping -t 192.168.1.1 = unlimited pings
- ping -c 4 192.168.1.1 = count 4 pings

### Using ping to check Name resolution 
- ping [www.google.com](http://www.google.com)

![[Pasted Graphic.jpg]]

### Beware of Firewalls
Firewalls can be configured to block ICMP traffic because of DoS attacks.

### Using Ping to Check Security Posture
check to see if firewall is properly configured

## Ipconfig, ifconfig, and ip
used to display TCP/IP information for a system and often used as first step of troubleshooting connectivity. linux/unix based systems use ifconfig. below are common commands:
- **ipconfig**: basic information for TCP/IP
- **ipconfig /all**: comprehensive listing of TCP/IP info for each NIC
	- MAC address, DNS servers, DHCP config
	- linux: ifconfig -a
- **ipconfig /displaydns**: shows contents of DNS cache and hostname to IP address mappings included in hosts file
- **ipconfig /flushdns**: erase contents of DNS cache
specific to linux:
- **ifconfig eth0**: shows config of first Ethernet interface, can also use eth1, eth2 etc
- **ifconfig eth0 promisc**: enables promiscuous mode on first ethernet interface
	- Promiscuous mode allows a NIC to process all traffic it receives.
- **ifconfig eth0 allmulti**: enables multicast mode on NIC: processes all multicast traffic

## Netstat
allows you to view statistics for TCP/IP protocols on a system, active connections. good to check for infected connections to remote computers. some commands you can use:
- **Netstat**: displays a listing of **all TCP connections**.
- **netstat -a**: displays a listing of all TCP and UDP ports that a system is **listening** on as well as **open connections**
- **netstat -r:** displays routing table
- **netstat -e**: displays details on network statistics, including how many bytes the system sent and received.
- **netstat -s**: displays statistics of packets sent or received for specific protocols
- **netstat -n**: displays addresses and port numbers in numerical order. this can be useful when looking for specific information
- **netstat -p** ***protocol*****:** shows statistics on a specific protocol
you can combine many switches together. example:
- **netstat -anp tcp**: show a listing of ports the system is listening on (-a), listed in numerical order (-n) for only tcp (-p tcp)
Netstat displays state of connection. common states are:
- **ESTABLISHED**: normal state for the data transfer phase of a connection
- **LISTEN**: system is waiting for a connection request
- **CLOSE_WAIT**: indicates the system is waiting for connection termination request
- **TIME_WAIT**: indicates system is waiting for enough time to pass to be sure remote system received a TCP-based acknowledgement of the connection
- **SYN_SENT**: indicates a TCP SYN packets ben sent.
- **SYN_RECEIVED**: indicates the system sent a SYN-ACK packet after receiving a SYN packet

## Tracert
lists the routers between two systems. typically used to identify faulty routers on the network. useful when troubleshooting WAN connections
- tracert -d: will not resolve host names (faster)

## Arp
Address Resolution Protocol: resolved IP addresses to MAC addresses and store result in the ARP cache. common commands:
- **arp -a**: shows arp cache
- **arp -a 192.168.1.1**: displays arp cache entry for specific IP address

## Practice Questions 
1. B
2. B
3. ~~A~~ D
4. D
5. C
6. B
7. D
8. A
9. A
10. C
11. A
12. C
13. ~~D~~ A
14. D
15. D

13/15 = 87%