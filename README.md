# Munki-Overnight
Run Munki Overnight (so laptops can update with lid closed)
I don't use Luggage to build my packages. The MakeFile is for the Luggage and
wasn't touched after a simple update. I have attached the munki .plist file I
used to push the package out. Build a DMG with the com.example.overnightMunki.plist
and the overnightMunki.py. Adjust as needed.

No warranties provided. Test in your environment.

Forked from https://github.com/jmartinez0837/Munki-Overnight

Moving over to pmset+caffeinate only. Eliminating Nosleep Extension.
Thanks to ldooks on IRC.freenode.net##osx-server for the amazing help and advice!
http://pastebin.com/W8ayMT7F for their original code.
