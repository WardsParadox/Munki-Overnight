# Munki-Overnight
Run Munki Overnight (so laptops can update with lid closed)
I don't use Luggage to build my packages (removed the MakeFile and postflight, checkout a previous commit to get those back), as I run this via Munki. I have attached a munki .plist file I used to push the files out. Build a DMG with the com.example.overnightMunki.plist and the overnightMunki.py. Adjust as needed.

No warranties provided. Test in your environment.

Forked from https://github.com/jmartinez0837/Munki-Overnight

Moving over to pmset+caffeinate only. Eliminating Nosleep Extension.
Thanks to ldooks on IRC.freenode.net##osx-server for the amazing help and advice!
http://pastebin.com/W8ayMT7F for their original code.
