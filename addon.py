import xbmcaddon
import xbmcgui
import subprocess
import os
import sys
import urllib2
 
_addon       = xbmcaddon.Addon()
_addonname   = addon.getAddonInfo('name')
_icon       = addon.getAddonInfo('icon')
time = 5000  # ms
 
line1 = "This is a VPN Script"
line2 = "It will allow you to turn on a vpn connection"
line3 = "And turn off a vpn connection"
### Customze to the vpn connection you want to open
### Edit the variable vpnclient below
vpnclient = "jimizwifi"
### End edit area
stat =""
try:
        subprocess.call(["sudo", "nmcli", "con", "up", "id", vpnclient])
except:
        e = sys.exc_info()[0]
        print e
        stat = e
finally:
        stat = stat +  "**** VPN Starting / On *****"
        ## print "**** VPN Starting ***"
 title= "VPN for Kodi"
 text= "VPN is now Running"
 xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(title, text, time, __icon__))

### lookup ip
response = urllib2.urlopen('http://mobileipinfo.com/ip.php/')
html = response.read()
line4 =  "Your IP IS " + html

xbmcgui.Dialog().ok(addonname, "Start VPN", line4, stat)







