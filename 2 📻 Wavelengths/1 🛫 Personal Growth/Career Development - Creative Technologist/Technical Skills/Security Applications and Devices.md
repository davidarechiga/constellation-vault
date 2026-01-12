# Security Applications and Devices

### Software Firewalls (OBJ 3.2)
Personal Firewalls - Software applications that protects a single computer from unwanted internet traffic
Host based firewalls

win: Windows Firewalls
macOS: PF and IPFW
Linux: iptables

WIndows Firewalls:
Basic version: useful more most home users
Advanced: type wf.msc into cmd prompt

OSX: Security and Privacy and pf (packet filter)

Linux: iptables

Many anti-malware suites also contain software firewalls
Make sure signatures are up to date

### IDS - Intrusion Detection System (OBJ 3.2 & 3.3)
HIDS - Host Based
Runs as software
NIDS - network hardware installed on network

Signature-based - a specific string of bytes triggers an alert

Policy-based - replies on specific declaration of the security poly

Anomaly-based - analyzes the current traffic against an established baseline and triggers an alert if outside the statistical average

<b><u>Alerts</u></b>
True Positive - Malicious activity is identified as an attack
True Negative - Legitimate activity is identified as legitimate traffic

False Positive - Legitimate activity is identified as an attack
False Negative - Malicious activity is identified as legitimate traffic

IDS can only alert and log suspicious activity…

IPD can also stop mallows activity from being executed

HIDS logs are used to recreate the events after an attack has occurred

### Pop-Up Blockers (OBJ 1.1, 3.3, 4.4)

- &nbsp;
		- Most web browsers have the ability to block javascript created pop-ups
		- Users may enable pop-ups because they are required for a website to function
		- Malicious attackers could purchase ads (pay per click) through various networks
		- Content Filters - blocking of external files containing javascript, images, or web pages from loading in a browser
		- Ensure your browser and it’s extensions are updated regularly 

### Data Loss Prevention (OBJ 2.1, 3.2, 4.4)
		Monitors data of a system while in use, in transit, or at rest to detect attempts to steal the data

		Endpoint DLP System - Software-based client that monitors the data in use on a computer and can stop a file transfer or alert an admin of the occurrence

		Network DLP System - Software or hardware-based solution that is installed on the perimeter of the network to detect data in transit

		Storage DLP System - Software installed on servers in the datacenter to inspect the data at rest

		Cloud DLP System - Cloud software as a service that protects data being stored in cloud services

### Securing the BIOS (OBJ 3.2)
		Basic Input Output System - Firmware that provides the computer instructions for how to accept input and send output
		Unified Extensible Firmware Interface (UEFI)

		1. Flash the BIOS
		1. Use a BIOS Password
		2. Configure the BIOS Boot Order
		3. Disable the external ports and devices
		4. Enable Secure Boot Option

### Securing Storage Devices (OBJ 2.1, 2.5, 3.3)
Removable Media

- &nbsp;
		- You should always encrypt files on removable media
		- Removable media controls - Technical limitations placed on a system in regards to the utilization of USB storage devices and other removable media
		Create administrative controls such as policies
		NAS - Network attached storage device
			NAS systems often implement RAID arrays to ensure high Availability

		SAN - Storage Area Network
			Network designed specifically to perform block storage functions that may consist of NAS devices 

		1. Use data encryption
		1. Use proper authentication
		2. Log NAS Access

### Disk Encryption (OBJ 2.1, 2.8, 3.2)
Encryption scrambles data into unreadable information

Self-Encrypting Drive
Storage device that performs whole disk encryption by using embedded hardware

Software
Mac: FileVault
Win: Bitlocker

Trusted Platform Module (TPM) - Chip residing on the motherboard that contains an encryption key
If your motherboard doesn’t have TPM, you can use an external USB Drive as a key

Advanced Encryption Standard - Symmetric key encryption that supports 128-bit and 256-bit keys

Encryption adds security but has lower performance

HSM - Hardware Security Module - Physical devices that act as a secure crypto processor during the encryption process

### End Point Analysis (OBJ 3.1 & 3.3)

- &nbsp;
			1. **Anti Virus**
				1. Software capable of detecting and removing virus infections and (in most cases) other types of malware such as trojans, rootlets, adware, spyware, password crackers, network mappers, DoS tools, and others
			1. **HIDS/HIPS**
				1. A type of IDS or IPD that monitors a computer system for unexpected behavior or drastic changes to the system’s state on an end point.
			1. **EPP - Endpoint Protection Platform**
				1. A software agent and monitoring system that performs multiple security tasks such as anti-virus, HIDS/HIPS, firewall, DLP and file encryption
			1. EDR - Endpoint Detection and Response 
				1. A software agent that collects system data and logs for analysis by monitoring system to provide early detection of threats
			1. UEBA - User and Entity Behavior Analytics
				1. A system that can provide automated identification of suspicious activity by user accounts and computer hosts.
				2. Heavily dependent on advanced computing techniques like artificial intelligence and machine learning