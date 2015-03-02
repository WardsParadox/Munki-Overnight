# Munki-Overnight
Run Munki Overnight (so laptops can update with lid closed)

I have been working on a way to get laptops to install updates with the lid 
closed also but wirelessly. 

I came up with this: please note, this works pretty well in my environment 
and requires the NoSleep extension 
<https://github.com/integralpro/nosleep> along with pmset and a 
launchd and Munki <https://github.com/munki/munki/wiki>. with pmset the laptops will only turn on at the specified time if 
there is a power source or whenever a power source gets connected after 
that so it works with our carts just fine. I use Workgroup Manager to set the Shutdown and Poweron times but if youre not using that pmset commands should work.

at boot up it will enable nosleep extension both on battery and external power. 
next my launchd runs a script that checks the time and battery level. if 
the time is the same hour (2am) of the startup time i set with MCX, then 
run munki and shut down. if the time is not within the hour then its 
probably getting used at a normal time so disable nosleep extension and 
continue running. 

seems to work pretty well in my environment.


