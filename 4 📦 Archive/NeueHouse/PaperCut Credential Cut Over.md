# <span style="font-family:.AppleSystemUIFont;font-size:18pt;">PaperCut Credential Cut Over</span>
<span style="font-size:13pt;"><b><u>Prepare Cut Over</u></b></span>

1. <span style="font-size:13pt;">Setup Nexudus Extender on Papercut Server.</span> 
	1. <a href="https://www.papercut.com/kb/Main/UsingPaperCutWithNexudus" rel="noopener" class="external-link" target="_blank" style="font-size:13pt;color:#e4afaff;">https://www.papercut.com/kb/Main/UsingPaperCutWithNexudus</a>
	2. <a href="https://support.nexudus.com/hc/en-us/articles/360007478198-Papercut#requirements-0-1" rel="noopener" class="external-link" target="_blank" style="font-size:13pt;color:#e4afaff;">https://support.nexudus.com/hc/en-us/articles/360007478198-Papercut#requirements-0-1</a>
1. <span style="font-size:13pt;">Verify Users are syncing.</span>
	1. <span style="font-size:13pt;"><b>Common reasons why users are not syncing</b></span><span style="font-size:13pt;">:</span>
		1. <span style="font-size:13pt;">Customer already has PaperCut account with the same email (syncing from different sync source like Active Directory)</span>
		2. <span style="font-size:13pt;">Customer does not have a valid price plan.</span>
			1. <span style="font-size:13pt;">Customers that have had a contract/price plan in the past will still be in PaperCut. I don’t believe the PaperCut Extender deletes users. If they are just contacts from the beginning, they do not sync.</span>
		1. <span style="font-size:13pt;">Customer does not have printing credits applied to account</span>
			1. <span style="font-size:13pt;">Printing credits should be added to the price plan the customer has been assigned.</span>
			2. <span style="font-size:13pt;">Printing credits can also be added manually to a customer via the profile > benefits > printing credits section of their profile</span>
1. <span style="font-size:13pt;">Verify PaperCut User Printing Credits Syncing to Nexudus Profiles.</span>
		1. <span style="font-size:13pt;">You can adjust the printing credits in PaperCut web GUI and it will sync to nexudus. This is how I was able to get without wasting print jobs. We created tests accounts to verify.</span>
1. <span style="font-size:13pt;">Add printing credits to MSQ Staff. This is done on the Nexudus Price Plan.</span>
2. <span style="font-size:13pt;">Verify Printing functionality with Papercut Credentials for MSQ Staff.</span> 
3. <span style="font-size:13pt;">Add printing credits to all NH Plans</span>
4. <span style="font-size:13pt;">Verify Printing credits have been added to all users. This part has been long because there are so many customer price plans.</span>
<span style="font-size:13pt;"><b><u>Cut Over</u></b></span> 
1. <span style="font-size:13pt;">Back Up PaperCut Users (optional roll back plan)</span>
2. <span style="font-size:13pt;">Stop AD Sync</span>
3. <span style="font-size:13pt;">Delete PaperCut Users</span>
4. <span style="font-size:13pt;">Sync Nexudus</span>
5. <span style="font-size:13pt;">Confirm Nexudus Users are in Papercut</span>
6. <span style="font-size:13pt;">Test Printing Functionality</span>
7. <span style="font-size:13pt;">Connect with Users for new credentials</span>
<span style="font-size:13pt;"><b><u>Post Cut Over</u></b></span>
1. <span style="font-size:13pt;">Verify Credits continue to sync for members</span>


<span style="font-size:9pt;">NH Staff Credential Cut Over</span>

- [ ] <span style="font-size:9pt;">Brian Zapka</span> 
- [ ] <span style="font-size:9pt;">Brendan Guiney (papercut account made)</span>
- [ ] <span style="font-size:9pt;">Kastriot (nexuses account hasn’t synced)</span>
- [x] <span style="font-size:9pt;">Jessica young (message Tuesday to change)</span>
- [x] <span style="font-size:9pt;">Andrew Thomas</span>
- [x] <span style="font-size:9pt;">Anthony Farina (changed password)</span>

- [x] <span style="font-size:9pt;">Robert Marchetti</span>
- [x] <span style="font-size:9pt;">Kavel Gounden</span>
- [x] <span style="font-size:9pt;">Yerum</span>
- [x] <span style="font-size:9pt;">Jordan Parvex</span> 
- [x] <span style="font-size:9pt;">Holly</span>
- [x] <span style="font-size:9pt;">Jess Hanley (loved the new scan to email feature)</span>
- [x] <span style="font-size:9pt;">Kaitlin</span>
- [x] <span style="font-size:9pt;">Nick Demarco</span>
- [x] <span style="font-size:9pt;">Adriana</span>
- [x] <span style="font-size:9pt;">Frontdesk</span>

1. <span style="font-size:9pt;"><b>Write process for Paper cut Integrations</b></span>
2. <span style="font-size:9pt;"><b>Are only active members coming over? Contacts?</b></span>
	1. <span style="font-size:9pt;">Contacts do not sync over. Users need to have a price plan, they need to have printing credits and Pay as you print is enabled in integrations</span>
1. <span style="font-size:9pt;"><b>Start syncing all houses</b></span>
	1. <span style="font-size:9pt;">Turned on All Location Sync at 9:30am 4/16</span>
	2. <span style="font-size:9pt;">Tested with Isabel Pakzard - now showing up in our paper cut server. Other members that have emails synced from Active Directory have not synced.</span>
	3. <span style="font-size:9pt;">Also once I changed locations, more staff came over(I.e. Brendan Guiney)</span>
1. <span style="font-size:9pt;"><b>Contact paper cut to add NH Staff subnet</b></span>



<span style="font-size:9pt;">FAQ:</span>
<span style="font-size:9pt;">Assuming you setup PaperCut per the instructions above and have installed the Extender:</span>

- <span style="font-size:9pt;">It’s possible your users don’t have printing credit in Nexudus</span>
- <span style="font-size:9pt;">Check if the user is attached to a price plan</span>
- <span style="font-size:9pt;">Ensure “Pay as you print” is enabled in the Integrations tab of Nexudus</span>