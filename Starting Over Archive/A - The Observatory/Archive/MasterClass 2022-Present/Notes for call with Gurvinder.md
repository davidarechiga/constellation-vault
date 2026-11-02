Notes for call with Gurvinder

Things to note:
1. User is inputting the correct password and email address and gets to the point where a Yubikey MFA confirmation is required:
	1. I have just done the following: 
		1. This means that the CORRECT credentials allow the user to get to the next steps
		2. Gurvinder's Security Policy was set to Group Policy is MFA Exception - Yubikey so I have set it to MFA Exception Yubikey
		3. 15-20 Yubikeys - this means whatever Yubikey he's on now definitely won't work as one was already reset
			1. I have cleared that Yubikey and he should try again with the most RECENT one he has.
1. 15-20 Yubikeys - I would question if the user is properly using the Yubikey. The buttons on the Yubikey can be highly sensitive and accidentally send multiple codes at once if a user isn't actioning the Yubikey properly.
	1. I would ask Elisha to have someone watch Gurvinder use the Yubikey
	2. Have Gurvinder open up a new tab > navigate to the URL portion of the window > and press the Yubikey to see if a correctly-generated code pops up
	3. I would confirm that Gurvinder has received the correct type of Yubikey that fits the access to OneLogin (there are different types of Yubikeys)