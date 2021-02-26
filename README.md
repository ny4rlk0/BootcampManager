# BootcampManager
Fixing broken funtionality of Apple's Bootcamp Driver on Windows 8-10 for older devices. (Tested on Macbook 2006 Late should have work any apple devices with Windows.) This broken functionality causes back light to not shine at all while Bootcamp is installed with Windows 7 compatibility since apple never released driver for it. This program is aimed to fix that. All brands belongs to their respective owners. I do not have any connection with apple. This is a custom fix use at your own risk. 

Currently known bugs: It wont launch if you are on battery not connected to AC charger. Thats because windows task scheduler cmd interface doesnt support it.

1)You have to manually open Windows Task Scheduler
2)Find BOOTCAMP_MANAGER
3)Right click settings
4)Conditions
5)Disable Run task while connected to AC only.
6)Press OK
