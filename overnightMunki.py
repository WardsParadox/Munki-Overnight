#!/usr/bin/python

import datetime
import time
import os
import subprocess
import re
import sys

current_time = datetime.datetime.now().time().hour
battery_query = re.findall(
  r'\d+%', subprocess.check_output('pmset -g batt', shell=True)
)
percentage = ''.join(battery_query)[:-1]

print percentage, "% Battery"
if current_time != 01:
    print "Hour of Day:", current_time
    print 'Its not time to run updates.'
    sys.exit(0);
elif percentage >= 50 and current_time == 01:
  # Use --auto in case laptop does go to sleep,
  # When opened there will be no visual to the user and they can still log in
  subprocess.call(
    '/usr/bin/caffeinate -i /usr/local/munki/managedsoftwareupdate --auto',
    shell=True
  )
  time.sleep(5)
  os.system('shutdown -h now')

elif percentage <= 50:
  print 'Battery too low to run updates.'
  os.system('shutdown -h now')
