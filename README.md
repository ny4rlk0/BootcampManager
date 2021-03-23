# BootcampManager
Fixing broken funtionality of Apple's Bootcamp Driver on Windows 8-10 for older devices. (Tested on Macbook 2006 Late should have work any apple devices with Windows.) This broken functionality causes back light to not shine at all while Bootcamp is installed with Windows 7 compatibility since apple never released driver for it. This program is aimed to fix that. All brands belongs to their respective owners. I do not have any connection with apple. This is a custom fix use at your own risk. 

PS:Portable Release is more stable and once you run and click Add to Boot you can delete the program.
If portable version wont work try SimpleBootcampPatcher Version.
(If you install older macbook's ssd, bootcamp drivers and windows 8.1 it could do any office tasks web surfing without sweat.)

Usage:
Install Apple Boot Camp Driver with windows 7 compatibility mode.
If you cannot install make sure os type is same as driver use x32 driver for x32 os and vice versa. 
Open Command Prompt as Administrator
CD into Driver Directory where BootCamp.msi
Type  "msiexec /i BootCamp.msi"
After run as administrator click Add to Boot.

(If you cant see your screen (Pitch Black) you can direct your phones flashlight to the screen to see temp before run this software.)

Currently known bugs: It wont launch if you are on battery not connected to AC charger. Thats because windows task scheduler cmd interface doesnt support it.
 
1)You have to manually open Windows Task Scheduler

2)Find BOOTCAMP_MANAGER_BOOT and BOOTCAMP_MANAGER_LOGIN and repeat this steps for both of them.

3)Right click properties

4)Conditions

5)Disable Run task while connected to AC only.

6)Press OK

