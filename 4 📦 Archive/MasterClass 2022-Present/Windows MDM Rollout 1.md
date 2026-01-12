# Windows MDM Rollout

Small Subset of Windows users
- ~26 users

Solve for Security and enrollment solutions

In line with JAMF for Macs

**Implementing True Single Sign-In with OneLogin with Hardware**

**Microsoft Intune**
- tied into Microsoft Office
- needs business premium
- all done through OL, when they are added to M365 > **add them to business** and it adds them to **Intune**

Where the Helpdesk is needed
- Enrolling existing users.
- we need to run the command line to enroll in Intune
	- Unlike JAMF, you can run the command and bring it into Intune
	- run as Admin
	- enroll > back up data > reset device back to fresh to be setup
		- 5 commands in powershell (Sahib to share doc)
		- right click start button
		- prompt for admin > enter password
		- Copy and paste all 5 commands
			- enter technicians OL credentials
		- Check Intune for enrollment
			- **could take from 1 hour to 5 days**
			- **Devices**
				- **Windows**
				- **search by serial number**
				- **check autopilot devices**

Implementation

Helpdesk driving it home with End Users



#MasterClass