# Hardening

### Hardening

Hardening - Act of configuring an operating system securely by updating it, creating rules and policies to govern it, and removing unnecessary applications and services

Mitigate **risk** by minimizing **vulnerabilities** to reduce exposure to **threats**

### Unnecessary Applications (OBJ 1.6)

Least Functionality - Process of configuring workstation or server to only provide essential applications and services

Personal computers often accumulate programs over time

Utilize a secure baseline image when adding new computers

SCCM - Microsoft’s configuration management

### Restricting Applications (OBJ 3.2 & 4.4)

Application Whitelist - Only applications that are on the list are allowed to be run by the operating system while all other applications are blocked 

Application Blacklist - Any application placed on the list will be prevented from running while all others will be permitted to run

Whitelisting and blacklisting can be centrally managed.

### Trusted Operating System (OBJ 3.2 & 3.3)

Trusted Operating System (TOS) - an operating system that meets the requirements set forth by government and has multilevel security

Windows 7 or Newer
Mac OS 10.6+
FreeBSD
Red Hat Enterprise server

You need to identify the current version and build prior to updating system

### Updates & Patches (OBJ 1.6 & 3.2)

Patches - a single problem-fixing piece of software for an operating system or application

Hotfix - a single problem-fixing piece of software for an operating system or application

Patches and Hotfizes are now used interchangeably by most manufactures

Updates

- &nbsp;
		1. Security Update - software code that is issued for a product-specific security-related vulnerability
		1. Critical Update - Software code for a specific problem addressing a critical non security bug in software
		2. Service pack - A tested cumulative grouping of patches, hotfixes, security updates, critical updates ,and possibly some feature or design changes
		3. Windows Update - Recommended update to fix a noncritical problem that users have found, as well as to provide additional features or capabilities
		4. Drive Update - Updated device driver to fix a security issue or add a feature to a supported piece of hardware

		Windows 10uses the Windows Update program (wuapp.exe) to manage updates

### Patch Management (OBJ 1.6 & 3.2)

		Patch management - Process of planning, testing, implementing and auditing of software patches

		1. Planning
			1. Verify it is compatible with your systems and plan for how you will test and deploy
		1. Always test a patch prior to automating it’s deployment
		2. Manually or automatically deploy the patch to all your clients to implement it
			1. Large organizations centrally manage updates through an update server
		1. Disable the wuauserv service to prevent Windows Update from running automatically
		2. It is important to audit the clients status after patch deployment

### Group Policies (OBJ 2.1)

		Group Policy - a set of rules or policies that can be applied to a set of users or computer accounts within an operating system.

		Group policy editor - access the GPR by opening the Run prompt and enter gpedit
			Password complexity
			Account lockout policy
			Software restrictions
			Application restrictions

		Active directory domain controllers have a more advanced Group Policy editor

		Security template - a group of policies that can be loaded through one procedure

		Baselining - Process of measuring changes in the network, hardware, and software environment
			A baseline establishes what is normal so you can find deviations

### File Systems and Hard Drives (OBJ 2.1 & 3.2)

		Level of security of a system is effected by it’s file system type
			NTFS - Windows (preferred)
			FAT32 - Windows
			ext4 - Linux
			HFS+ (older)
			APFS - macOS (newer)

		All hard drive will eventually fail
			1. Remove temporary files by Ising Disk Cleanup
			1. Periodic file system checks
			2. Defragment your disk drive
			3. Back up your data (local or cloud back up)
			4. Use and practice restoration techniques