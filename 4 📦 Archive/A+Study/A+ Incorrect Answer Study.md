# A+ Incorrect Answer Study
## 5 - Hardware Network Troubleshooting
### **5.1 - Th**H**e Troubleshooting Process**
Change Control

- &nbsp;
			- A formal process for managing change
			- avoid downtime confusion and mistakes
			- corporate policy and procedures
		Nothing changes without the process
			- plans for a change
			- estimate the risk associated with the change
			- have a recovery place if the change doesn't work
			- test before making the change (duplicate server)
			- document all of this and get approval
			- make the change
	1. Identify the problem
		- Information gathering
			- get as many details as possible
			- duplicate the issue, if possible
		- Identify symptoms
			- may be more than a single symptom
		- question users
			- your best source of details
		- Determine if anything has changed
			- who's in the wiring cloest?
		- Approach multiple problems individually
			- break problems into smaller pieces
		- Back up everything
			- you'regoing to make some cahnges
			- you should always have a roolback plan
		- What else has changed?
			- the user may not be aware
			- environment changes
			- infastrusture changes
		- there may be some clues
			- check OS log files
			- Applications may have log information
	1. Establish a Theory
		2. Start with the obvious
			1. Occam's Razor applies
		1. consier everything
			1. even the not so obvious
		1. Make a list of all possible causes
			1. start with the easy theories
			2. and the least difficult to test
		1. Research the symptoms
			1. inteal knowledgebase
			2. Google searches
	1. Test the Theory
		1. Confirm the theory
			1. determine next steps to resolve problem
		1. Theory didn't work
			1. Re-stablish new theory or escalate
			2. call an expert
		1. The theory worked!
			1. Make a plan...
	1. Create a plan of action
		1. Build the plan
			1. correct the issue with minimum impact
			2. some iddues can't be resolved during production hours
		1. Identify potenial effects
			1. Every plan can go bad
			2. have a plan B
			3. and a plan C
	1. Implement the solution
		1. Fix the issue
			1. Implement during the change window
		1. escalate as necessary
			1. you may need help from a third party
	1. Very full system functionality
		1. it's not fixed until it's really fixed
			1. the test should be part of your plan
			2. have your customer confirm the fix
		1. implement preventaitve measures
			1. let's avoid this issue in the future
	1. Document findings
		1. it's not over until you build the knowledge base
			1. don't lose valuable knowledge!
		1. what action did you take?
			1. what outcome did it have?
		1. Consider a formal database
			1. help desk case notes
			2. searchable database
### **5.2 - Troubleshooting Common Hardware Problems**

- &nbsp;
	1. Unexpected Shutdowns
		1. No warning, black screen
			1. may have some details in your event viewer
		1. Heat-related issue
			1. High CPU or graphics, gaming (check thermal paste)
			2. check all fans and heat sinks
			3. BIOS may show fan status and temperatures 
		1. Failing hardware
			1. has anything cahnges?
			2. check device manager, run diagnostics
		1. could be anything
			1. Elimitnate whats working
	1. Lock Ups
		1. system completely stops
			1. Completely, usually not much in the event log
			2. Similar to unexpected shutdowns
		1. Check for any activity
			1. hard drive, status lights, try CTRL-ALT-DELTE
		1. Update drivers and software patches
			1. has this been done recently?
		1. Low Resources
			1. RAM, storage
		1. Hardware diagnstocs may be helpful
	1. POST (POWER ON SELF TEST)
		1. Test major system components before the operating system
			1. Main systems (CPU, CMOS, etc.)
			2. Video
			3. Memory
		1. Failures are usually noted with beeps and/or codes
			1. BIOS versions can differ, check your documentation
	1. POST and boot
		1. Blank Screen on boot
			1. listen for beeps
			2. bad video
			3. BIOS configuration issue
		1. BIOS time and setting
			1. Maintained with the motherboard battery
			2. Replace the battery
		1. Attempts to boot to incorrect device
			1. Set boot order in the BIOS configuration
			2. confirm that the startup device has a valid opeating system
			3. check for media in a startup device
	1. Continuous Reboots
		1. How far does the boot go before rebooting?
		2. BIOS only? OS Splash Screen?
		3. Bad Driver or configuration
			1. F8, "boot from last known configuration"
		1. Try F8, Safe Mode
			1. If system starts, disable automatic restarts in SYstem Properties
		1. Bad Hardware
			1. Try removing or replacing devcices
			2. check connections and reseat
	1. No Power
		1. No power
			1. No power at the source?
			2. no power from the power supply
			3. get our your multimeter
		1. Fans Spin - no power to other devices
			1. where is your face power connected?
			2. No POST? - bad motherboard?
			3. Case fans have lower voltage requirements
			4. Check the power supply output
	1. Overheating
		1. Heat generation
			1. CPU, video adapter, memory
		1. Cooling Systems
			1. Fans and airflow
			2. Heat sinks
			3. clean and clear
		1. Verify with monitoring software
			1. Built into the BIOS
			2. Try HWMonitor
				1. http://www.cpuid.com
	1. Loud Noises
		1. Computers should hum
			1. no grind
		1. Rattling
			1. Loose components
		1. Scraping
			1. Hard drive issues
		1. Clicking
			1. Fan problems
		1. Pop
			1. Blown capacitor
	1. Intermittent Device Failure
		1. Sometimes it works
			1. sometimes it doesn't
		1. Bad install
			1. Check and reseat
			2. Use all the screws
		1. Bad hardware
			1. Poor connection
			2. Heat and vibration
			3. might ahve to replace to solve
	1. Indicator Lights
		1. POST codes on the motherboard
		2. POWER
		3. Link Light
			1. Speed
			2. Activity
	1. Smoke and Burning Smell
		1. Electrical problems
			1. The smoke makes everything work
		1. Always disconnect power
			1. there should never be a burned odor
		1. Locate bad components
			1. even after the system has cooled down
			2. Replace all damaged parts
	1. Crash Screens
		1. Windows Stop Error
		2. Blue Screen of Death
			1. you don't want this
		1. Contains important information
			1. also written to event log
		1. Useful when tracking down problems
			1. Sometimes more userful for manufacturer support
	1. Spinning Ball of death
		1. macOS Spinning wait cursor
			1. feedback that something is happening
		1. the spin starts but it never stops
			1. You never get back control of your computer
		1. Many possible reasons
			1. application bug
			2. bad hardware
			3. slow paging to disk
		1. Restart the computer
			1. there may be details in the console logs
	1. Log Entries
		1. Windows
			1. Event Viewer
			2. Boot Logs
				1. System Configuration
				2. C:\Windows\nbtlog.txt
		1. Linux
			1. Individual application logs
			2. /var/log
		1. macOS
			1. Utilities / Console.app
	1. Error Messages
		1. The details of an error message can make or break a troubleshooting session
			1. write down everything
				1. take a picture
				2. make a video
				3. train your users
		1. The error might not make sense
			1. write it down anyway
			2. the internet will tell you what it means
			3. speed your time troubleshooting the right things
### **5.3 - Troubleshooting Hard Drives**

- &nbsp;
	1. Disk Failure symptoms
		1. Read/Write failure
			1. Cannot read from the source disk.
		1. Slow Performance
			1. Constant LED Activity
			2. Retry... Retry... Retry...
		1. Loud CLicking Noise
			1. The click of death
	1. Troubleshooting Disk Failures
		1. Get a Back up
			1. First thing -  a bad drive is bad
		1. Check Loose or damaged Cables
		2. Check for overheating
			1. Especially if problems occurs after startup
		1. Check power supply
			1. especially if new devices were added
		1. Run Hard drive diagnostics
			1. from the drive or computer manufacturer
			2. perferably on a known good computer
	1. Boot failure symptoms
		1. Drive not reecognized
			1. lights or no lights
			2. beeps
			3. error messages
		1. Operating System not found
			1. The drive is there
			2. Windows is not
	1. Troublehsooting boot failures
		1. Check your cables
		2. Physical problem
	1. Check boot sequence in BIOS 
		1. Check for removable disks (esepcailly USB)
		2. CHeck for disbaled storage interfaces
	1. For new isntallation, check hardware configuration
		1. Data and power cables
		2. try different SATA Interfaces
		3. Try Drive in different computer
	1. RAID not found
		1. Missing or faulty RAID controller
	1. RAID stops working
		1. Each RAID is different
		2. Don't start pulling drives util you check the console
	1. RAID Recovery
		1. Each RAID is different
		2. Don't start pulling drives util you check the console
	1. Crash Screen
		1. WIndows Stop Error, Apple Spinning Cursor
			1. a very serious issue
		1. May indicate a storage device issue
			1. Diagnostics needed for motherboard
	1. S.M.A.R.T. errors
		1. Self-monitoring, Analysis, and Reporting Technology
			1. Use third-party utilities
		1. Avoid Hardware failure
			1. look for warning signs
		1. Scheule disk checks
			1. built in to most drive arrays
		1. Warning Signs
			1. replace a drive
5.4 - Troubleshooting Video and Display Issues
	1. No video image
		1. Is it connected?
			1. We wouldnt ask if it wasn't a real solution
			2. Check both power and signal cable
		1. Input selection on monitor
			1. HDMI, DVI, VGA, etc.
		1. Image is dim
			1. check brightness controls
		1. Swap the monitor
			1. Try the monitor on another computer
		1. No video after windows Loads
			1. Use VGA mode (F8)
	1. Image Quality Problems
		1. Flickering, color patterns incorrect
			1. you can almost work with this
		1. check the cable pins
			1. especially if missing a color
		1. Distorted image and geometry
			1. Check the OS refresh rate and resolution settings
				1. need to match the display specifications
			1. Native resolution is important on LCD displays
			2. Check or replace cable
		1. Disable hardware acceleration
			1. troubleshoot with software drivers
		1. Oversized images and icons
			1. resolution set too low
				1. Lower = Larger
		1. Burn-in
			1. a problem across all monitor
			2. some displays will pixel-shift
				1. but you won't notice it
			1. LCDs have "image sticking"
				1. Remove by displaying a white screen for an extended period
	1. Other Video Issues
		1. Oixel Problems
			1. stuck pixels
			2. dead pixels
		1. Artifacts
			1. unusual graphics - check adapter
			2. image persistence - turn off display
			3. motion trails
				1. disabled advanced video features
		1. BSOD and overheating
			1. Video Drivers
			2. Monitor the internal temperature
### <span style="font-family:SFUIText-Bold;"><b>5.5 - Troubleshooting Laptops</b></span>

- &nbsp;
	1. LCD Display troubleshooting
		1. No DIsplayor DIM video
			1. verify the backlight
			2. look closely, it may be barely visible
			3. no backlight, replace the inverters
		1. Confirm video with an external display
			1. video good but LCD bad
			2. replace the LCD display
		1. Flickering video
			1. Connector problem
			2. bad video cable
			3. bad video hardware
	1. Input Issues
		1. Sticking keys
			1. difficult to clean
			2. keycaps are very very delicate!
		1. Ghost cursor / Pointer drift
			1. moudpad causes cursor to bounce around
			2. modify the configuration to check for palm press
			3. update your drivers
		1. Num lock indicator lights
			1. the letters are numbers
	1. Wireless Troubleshooting
		1. Multiple antennas
			1. Wifi main and aux, bluetooth
			2. antenna wires wrap around the laptop screen
		1. Easy to accidentally disconnect during maintenace
			1. No 802.11 wireless
			2. no bluetooth
		1. Check the connectors
			1. loose cables can cause intermittent wireless access
	1. Power issues
		1. Battery not charging
			1. Batteries lose capacity over time
			2. Laptop charging hardware may be faulty
		1. No power
			1. check the external power adapter "brick" with multimeter
			2. Master maptop reset
				1. hold power for 10 seconds
				2. each laptop is different
	1. External Monitor Issues
		1. Toggle Fn keys
			1. Secondary functions
			2. Toggle Between LCD / External Monitor / Both
		1. Use external monitor
			1. Bypass the external display (but not the video hardware)