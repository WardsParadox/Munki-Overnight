#!/bin/sh

# NOTE: This Requires NoSleep https://github.com/integralpro/nosleep be installed with the "Command-Line Interface"
# NoSleep is installed with as requires key in munki and using installer_choices_xml keys to install "Command-Line Interface"

#checks for the hour of the time only; cuts to format (HH:M)
SystemHour=$(date "+TIME:: %H" | cut -c 8-9)

#hour of time we have set computers to turn on (HH) done this way so it'll only run within that hour
TurnOnTime=02

if [ "$SystemHour" = "$TurnOnTime" ] ; then

		#set closing lid not to sleep laptop
		#/usr/local/bin/NoSleepCtrl -a -b -s 1,1
	
		#gives time for noSleep extension to load
		/usr/bin/caffeinate sleep 5

		#check system battery 
		battPercentage=$(pmset -g batt | grep "InternalBattery-0" | cut -c 21-23 | sed s/\%//)
		if [ "$battPercentage" -gt 50 ] ; then
		
			# Make sure we can talk to the server before running.
			until /sbin/ping -c 1 h-munki.riverdale.edu; do /bin/sleep 3; done

			/usr/local/munki/managedsoftwareupdate --auto

			#/usr/local/munki/managedsoftwareupdate --quiet --munkistatusoutput
			#/usr/local/munki/managedsoftwareupdate --installonly --munkistatusoutput
			
			#recommended by Walter
			#/usr/local/munki/supervisor --delayrandom 90 --timeout 43200 --/usr/local/munki/managedsoftwareupdate --auto
	
			sleep 5
			sudo shutdown -h now
		else
			echo "Battery too low to run updates."
			sudo shutdown -h now
		fi	
else

	echo "Its not time to run updates."
	
	#set closing lid back to sleep laptop
	/usr/local/bin/NoSleepCtrl -a -b -s 0,0
fi

exit 0
