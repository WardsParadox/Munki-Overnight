#!/usr/bin/python
# Libraries
import datetime
import time
import subprocess
import re
import syslog
import urllib2
from sys import exit

version = "1.3.1"
# Move Open Log to Front of all
syslog.openlog("Overnight Munki Updater V %s" % version)
#Variables
current_time = datetime.datetime.now().time().hour
<<<<<<< HEAD


# Functions
def laptops():
    battery_query = re.findall(
      r'\d+%', subprocess.check_output(['/usr/bin/pmset', '-g', 'batt'])
    )
    percentage = ''.join(battery_query)[:-1]
=======
battery_query = re.findall(
  r'\d+%', subprocess.check_output('/usr/bin/pmset -g batt', shell=True)
)
percentage = ''.join(battery_query)[:-1]

# Functions
def main():
>>>>>>> 0608cc1d4f8d75e6cee96760ea8cd2c3d31b8b5d
    print "{0}% Battery".format(percentage)
    syslog.syslog(syslog.LOG_ALERT, "The battery is at %s%% " % percentage)
    if current_time != 01 and current_time != 05:
        print "Hour of Day:", current_time
        print 'It is not time to run updates.'
        syslog.syslog(syslog.LOG_ALERT,
        "Hour is %s and is not time to run updates " % current_time)
        exit(0);
    elif percentage >= 50 :
        # Use --auto in case laptop does go to sleep,
        # When opened there will be no visual indication to the user
        # and they can still log in
        syslog.syslog(syslog.LOG_ALERT, "Running ManagedSoftwareUpdate")
        subprocess.call(['/usr/local/munki/managedsoftwareupdate','--auto'])
        subprocess.call(['shutdown','-h','now'])
    elif percentage <= 50:
        print 'Battery too low to run updates.'
        syslog.syslog(syslog.LOG_ALERT,
        "The battery is too low to run updates!! Battery at %s %%. \
        Shutting Down" % percentage)
def desktops():
        if current_time == 05:
            # Use --auto in case laptop does go to sleep,
            # When opened there will be no visual indication to the user
            # and they can still log in
            syslog.syslog(syslog.LOG_ALERT, "Running ManagedSoftwareUpdate")
            subprocess.call(['/usr/local/munki/managedsoftwareupdate','--auto'])
            subprocess.call(['shutdown','-h','now'])
        else:
            print 'It is not time to run updates.'
            syslog.syslog(syslog.LOG_ALERT,
            "Hour is %s and is not time to run updates " % current_time)
            exit(0);
def internet_on():
    try:
        response=urllib2.urlopen('https://www.google.com/',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False
def main():


# Main Run
while True:
    internet_on()
    break
if __name__ == '__main__':
    main()
<<<<<<< HEAD
    subprocess.call(['/sbin/shutdown','-h','now'])
=======
subprocess.call(['/sbin/shutdown','-h','now'])
>>>>>>> 0608cc1d4f8d75e6cee96760ea8cd2c3d31b8b5d
