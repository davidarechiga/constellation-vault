# Chapter 2 Understanding Identity and Access Management
## Exploring Authentication Concepts
- Authentication **proves** **identity** with credentials such as **username** and **password**.
- at least two entities know credentials: **user** and **authenticator**
- authentication is not limited to users: **Services**, **processes**, **workstations**, **servers**, and **network** **devices**

## Comparing Identification and AAA
- Authentication, authorization and accounting (AAA) work together with identification to provide a comprehensive access management system.
- Users are granted **authorization** to access resources based on their proven identity.
- Accounting methods tracks user activity and records the activity in logs
	- audit train we allows security professionals to re-create the events that preceded a security incident
- if users can bypass authentication, authorization and accounting processes are ineffective

## Comparing Authentication Factors
- **Something you know**: PINs or passwords
- **Something you have**: smart card or USB token
- **Something you are**: biometrics
- **somewhere you are**: your location using geolocation tech
- **something you do**: gestures on a touch screen

### Something you know
typically a shared secret such as password or even PIN
- Password Complexity
	- A strong password is of sufficient length doesn’t include words found in a dictionary or any part of a user’s name and combines 3 of 4 following characters:
		- Uppercase character
		- Lowercase character
		- numbers
		- special characters
- Training users about password behavior
	- importance of strong password
	- importance of never giving out password
- Password Expiration
	- users should change password every 45 or 90s days
- Password Recovery
	- it’s important to verify identity when reseting passwords
	- also important to set passwords that expire on first use
- Password History and Password Reuse
	- remembers last 24 passwords so they won’t be reused again
- Group Policy
	- Configure Group Policy Object and apply settings to multiple users and computers within the domain
		- resetting 5000 admin passwords
- Using Password Policy
	- specifying how strong, how often it needs to be reset, password history
- Implementing Account Lockout Policies
	- prevents users from guessing password
		- Account lockout threshold: max times for wrong password
		- account lockout duration: min time before retrying password
- Changing default passwords
	- many systems start with defaults that need to change
		- don’t use admin, administrator for username
		- create a decoy “admin” account

### Something You Have
Smart Cards, USB key fob, “something you can forget at home”

- **Smart cards**: credit card sized, embedded microchip and certificate. Requirements:
	- Embedded certificate
	- Public Key Infrastructure (PKI)
	- Often used at Dual-factor authentication
- CACs and PIVs
	- Common Access Card: specialized smart card for Department of Defense
		- Photo iden. and smart card for computer access
	- Personal Identity Verification: used by Federal Agencies, also photo identification
- Tokens or Key Fobs
	- Electronic device the size of a remote key for a car
	- Small LCD that displays a ever-changing number
	- Often used to authentication for websites
- HOTP and TOTP
	- HOTP: algorithm combines a secret key and incrementing counter and uses HMAC to create a hash of the result. It then converts into an HOTP value of six to eight digits
	- TOTP: similar but has a 30 second expiration typically

### Something You Are
Uses Biometrics for authentication. **Strongest individual method of authentication because it is most difficult for an attacker to falsify.**
- Biometric Methods:
	- **Fingerprint Scanner**
	- **Retina Scanner**: Pattern of blood vessels at the back of the eye for recognition
	- **Iris Scanner**: camera tech to capture patterns of the Iris around pupil
	- **Voice recognition**: identify who is speaking
	- **Facial Recognition**: identify people based on facial features
- Biometric Errors:
	- **False Acceptance**: incorrectly identifies an unauthorized user as an authorized user (**FAR** = False acceptance rate)
	- **False rejection**: incorrectly rejects an authorized user (**FRR** = False rejection Rate)
	- **Crossover Error rate**: the point where the FAR crosses over with the FRR
		- The crossover error rate (CER) measures the accuracy of a system and lower CERs are better.

### Somewhere You Are
Identifies a user’s location with Geolocation. Many authentication systems use IP address for geolocation.

### Something You Do
Actions you can take such as gestures on a touch screen. Can also be keystroke dynamics

### Dual-Factor and Multi-factor Authentication
Uses two different factors of authentication, such as something you have and something you know. Multi-factor uses two or more factors of authentication.

## Troubleshooting Authentication Issues
- Weak passwords
- Forgotten passwords
- Biometric errors

## Comparing Authentication Services
Goal is to not send unencrypted credentials over the network.

### Kerberos
Network authentication mechanism used within Windows Active Directory domains and some Unix environments. Kerberos requirements:
- A method of issuing tickets used for authentication
- Time Synchronization
- A database of subjects or users
Uses AD and KDC (Key Distribution Center) to issue timestamped tickets that expire after a certain time period

### NTLM
**New Technology LAN Manager** is a suite of protocols that provide authentication, integrity and confidentiality within Windows systems. Uses Message Digest hashing to challenge users and check their credentials. There are 3 versions of NTLM:
- NTLM is a simple MD4 has of a user’s password. Not recommended on today’s networks
- NTLMv2 is a challenge-response authentication protocol.
- NTLM2 Session improves NTLMv2 by adding mutual authentication

### LDAP and LDAPS
Lightweight Directory Access Protocol specifies formats and methods to query directories. Active Directory domains and  Unix realms us LDAP to identify objects in query strings with codes such as CN=Users and DC=DomainControllerName. LDAPS encrypts transmissions with TLS

### Single Sign-On
Accessing multiple systems while only provides credentials once. Kerberos and LDAP both use SSO

**SSO and Transitive Trusts**
A Transitive trust creates an indirect trust relationship.
- Homer trusts Moe
- Moe trusts Fat Tony
- Because of transitive trust relationship, Homer trusts Fat Tony

**SSO and SAML**
Security Assertion Markup Language is an Extensible Markup Language —based data format used for SSO on web browsers.