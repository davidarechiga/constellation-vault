# Secure Software Development
### Software Development (OBJ 2.1 & 2.3)
SDLC - Software Development Lifecycle
An organized process of developing a secure application throughout the life of the project

![[Screen Shot 2020-11-20 at 10.01.33 AM.png]]

SDLC Phases

Water-fall

- &nbsp;
			1. Planning and Analysis
				1. Rough to formalize
			1. Software/Systems Design
			2. Implementation
				1. Coding begins
				2. Basic debugging and testing
			1. Testing
				1. Checking code with different testing methods
			1. Integration
				1. Applications is integrated into the network environment
			1. Deployment
				1. Moved into production environment
			1. Maintenance
				1. Bug fixes, patches, and updates
				2. Number scheme for updates and patches
				3. Developing retiring plan

		Agile
			Software development is performed in time-boxed or small increments to allow more adaptivity to change

		DevOps
			Software development and information technology operations

### SDLC Principles (OBJ 1.6 2.3, 3.2 & 5.3)
		Developers should always remember confidentiality, integrity and availability.

		Confidentiality
			Ensures that only authorized users can access the data

		Integrity
			Ensures that the data is not modified or altered without permission
				Hash algorithms
				Journaling - logging

		Availability
			Ensuring that data is available to authorized users when it is needed

		Threat modeling helps prioritize vulnerability identification and patching

		Good security should be programmed in from the beginning

		Coding Practices
			1. Least Privilege
				1. Users and processes should be runs using the least amount of access necessary to perform a given function
			1. Defense in Depth
				1. Layering of security controls is more effective and secure than replying on a single control
			1. Never Trust User Input
				1. Any input that is received from a suer should undergo input validation prior to allowing it to be utilized by an application
			1. Minimize Attack Surface
				1. Reduce the amount of code used by a program, eliminate unneeded functionality, and require authentication prior to running additional plugins
			1. Create Secure Defaults
				1. Default installations should include secure configurations instead of requiring an administrator or user to add in additional security
			1. Authenticity and Integrity
				1. Applications should be deployed using code signing to ensure the program is not changed inadvertently or maliciously prior to delivery to an end user
			1. Fail Securely
				1. Applications should be coded to properly conduct error handling for exceptions in order to fail securely instead of crashing
			1. Fix Security Issues
				1. If a vulnerability is identified, then it should be quickly and correctly patched to remove vulnerability
			1. Rely on Trusted SDKs
				1. SDKs must come from trusted sources to ensure no malicious code is being added

### Testing Methods (OBJ 2.3 & 3.2)
System Testing

- &nbsp;
		1. Black Box Testing
			1. Occurs when a tester is not provided with any information about the system or program prior to conducting the test
		1. White Box Testing
			1. Occurs when a tester is provided full details of a system including the source code, diagrams, and user credentials in order to conduct the test.
		1. Gray Box testing
			1. Mixture of Black and White Box testing
			2. Gray Box will have a mixture of details but tester will not have full details

**Structured Exception Handling (SEH)**
Provides control over what the application should do when faced with a runtime or syntax error

Programs should use input validation when taking data from users
Applications verify that information received from a user matches a specific format or range of values

Static Analysis
Source code of an application is received manually or with automatic tools without running the code

Dynamic Analyisis
Analysis and testing of a program occurs while it is being executed or run

Fuzzing
Injection of randomized data into a software program in an attempt to find systems failures, memory leaks, error handling issues and improper input validation

### Software Vulnerabilities and Exploits (OBJ 1.2, 1.3 & 1.6)
Backdoors
Code placed in computer programs to bypass normal authentication and other security mechanisms
Backdoors are a poor coding practice and should not be utilized

Directory Traversal
Methods of accessing unauthorized directories by moving through the directory structure on a remote server

Arbitrary Code Execution
Occurs when an attacker is able to execute or run commands on a victim computer

Remote Code Execution
Occurs when an attacker is able to execute or run commands on a remote computer

Zero Day
Attack against a vulnerability that is unknown to the original developer or manufacturer

### Buffer Overflow (OBJ 1.3)
Definition: Occurs when a process stores data outside the memory range allocated by the developer

Buffer
A temporary storage area that a program uses to store data

Over 85% of data breaches were caused by a buffer overflow

Smash the stack
occur when a attacker fills up the buffer address may hit a NOP and on until it finds the attacker’s code to run

Address Space Layout Randomization
Method used by programmers to randomly arrange the different address spaces used by a program or process to precent buffer overflow exploits

Buffer Overflows attempt to put more data into memory than it is designed to hold

### XSS & XSRF (OBJ 1.3)
Cross-Site Scripting
Occurs when an attacker embeds malicious scripting commands on a trusted website

Stored/Persistent
Attempts to get data provided by the attacker to be saved on the web server by the victim 

Reflected
Attempts to have a non-persistent effect activated by a victim clicking a link on the site

DOM-based
Attempt to exploit the victims web browser 

Prevent XSS with output encoding and proper input validation

Cross-site Request Forgery (XSRF/CSRF)
Occurs when an attacker forces a user to execute actions on a web server for which they are already authenticated

Precent XSRF with tokens, encryption, XML file scanning, and cookie verification

### SQL Injection
Structured Query Language

SQL Injection
Attack consisting of the insertion or injection of an SQL query via input data from the client to a web application

Injection Attack
insertion of addition information or code through data input from a client to an application

Most common injection

- &nbsp;
			1. SQL
			1. HTML
			2. XML
			3. LDAP
		SQL injection is prevented through input validation and using least privilege when accessing a database

### XML Vulnerabilities OBJ 1.3
		Extensible Markup Language
			Used by web apps for authentications and authorizations, data exchange and uploading

		XML Exploits, XML Vulnerabilities, XML Injections

		XML data submitted without encryption or input validations is vulnerable to spoofing, request forgery and injection of arbitrary code

		XML Bomb (Billion Laughs Attack
			XML encodes entities that expand to exponential sixes, consuming memory on the host and potentially crashing it

		XML External Entity (XXE)
			An attack that embeds a request fro a local resource

		To prevent XML vulnerabilities from being exploited, use proper input validation

		anything that references XML is XML vulnerabilities on the test

### Race Conditions
		Race Condition
			a software vulnerability when the resulting outcome from the execution processes is directly dependent on the order and timing of certain events, and those events fail to execute in the order and timing intended by the developer

		a race condition vulnerability is found where multiple threads are attempting to write a variable or object at the same memory location

		Dereferencing
			a software vulnerability that occurs when the code attempts to remove the relationship between a pointer and the thing it points to

		Race conditions are difficult to detect and mitigate

		Dirty Cox Exploit

		Race conditions can also be used against databases and file systems
			Time of Check to Time of Use (TOCTTOU)
				The potential vulnerability that occurs when there is a change between when an app checked a resource and when the app used the resource
			How to prevent TOCTTOU
			1. Develop applications to not process things sequentially of possible
			1. Implement a locking mechanism to provide app with exclusive access
### Design Vulnerabilities
Vulnerabilities often arise from the general design of the software code
3 main types

- &nbsp;
		1. Insecure Components
			1. any code that is used or invoked outside the main program process
				1. Code reuse
				2. Third Party Library
				3. SDK (software development tool kits
		1. Insufficient Logging and Monitoring
			1. Any program that does not properly record or log detailed enough information for an analyst to perform their job
			2. Logging and monitoring must support  your use case and answer who, what, when, where, and how
		1. Weak or Default configurations
			1. any program and uses ineffective credentials or configurations, or one in which the defaults have not been changed for security
			2. Many applications choose to simply run as root or as a local admin
			3. permissions may be too permissive on files or directories due to weak configurations
		Best Practice
			Utilize scripted installations and baseline configuration templates to secure applications during installation