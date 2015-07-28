#!/usr/bin/python
# Libraries
import datetime
import time
import os
import subprocess
import re
import syslog
import urllib2
from sys import exit

version = "1.3.0"
# Move Open Log to Front of all
syslog.openlog("Overnight Munki Updater V %s" % version)
#Variables
current_time = datetime.datetime.now().time().hour
battery_query = re.findall(
  r'\d+%', subprocess.check_output('pmset -g batt', shell=True)
)
percentage = ''.join(battery_query)[:-1]
# Functions
def runMunki():
    print percentage, "%s Battery"
    syslog.syslog(syslog.LOG_ALERT, "The battery is at %s %% " % percentage)
    if current_time != 01 and current_time != 05:
        print "Hour of Day:", current_time
        print 'It is not time to run updates.'
        syslog.syslog(syslog.LOG_ALERT, "It is %s and is not time to run updates " % current_time)
        exit(0);
    elif percentage >= 50 :
        # Use --auto in case laptop does go to sleep,
        # When opened there will be no visual to the user and they can still log in
        syslog.syslog(syslog.LOG_ALERT, "Running ManagedSoftwareUpdate")
        subprocess.call('/usr/local/munki/managedsoftwareupdate -v --auto',shell=True,stdout=subprocess.PIPE)
        time.sleep(5)
        os.system('shutdown -h now')
    elif percentage <= 50:
        print 'Battery too low to run updates.'
        syslog.syslog(syslog.LOG_ALERT, "The battery is too low to run updates!! Battery at %s %%. Shutting Down" % percentage)
def internet_on():
    try:
        response=urllib2.urlopen('http://www.google.com',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

# Main Run
while True:
 if internet_on():
    break
runMunki()
os.system('shutdown -h now')
