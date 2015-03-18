#
#   Copyright 2009 Joe Block <jpb@ApesSeekingKnowledge.net>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# v1.1 Added sleep command to give time for the NoSleep extension to load and batter percentage lines
# v1.2 Added postflight to set wakeonpoweron
# v1.3 Added sed command to remove percent sign from battPercentage logic
# v1.4 Changed order of nosleep command and battpercentage logic
# v1.5 added sudo to pmset in postflight

include /usr/local/share/luggage/luggage.make

TITLE=overnightMunki
REVERSE_DOMAIN=org.bsd7.techserv
PAYLOAD=pack-overnightMunki.py \
	pack-Library-LaunchDaemons-org.bsd7.techserv.overnightMunki.plist \
	pack-script-postflight
PACKAGE_VERSION=1.0

pack-overnightMunki.sh: l_etc_hooks
	@sudo mkdir ${WORK_D}/etc
	@sudo mkdir ${WORK_D}/etc/hooks
	@sudo ${CP} overnightMunki.py ${WORK_D}/etc/hooks
	@sudo chown root:wheel ${WORK_D}/etc/hooks/overnightMunki.py
	@sudo chmod 755 ${WORK_D}/etc/hooks/overnightMunki.py
	@sudo chmod +x ${WORK_D}/etc/hooks/overnightMunki.py
