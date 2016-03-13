import xbmcaddon
import xbmcgui
import subprocess
import os
import sys
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "This is a VPN Script"
line2 = "It will allow you to turn on a vpn connection"
line3 = "And turn off a vpn connection"
vpnclient = "jimizwifi"
try:
        subprocess.call(["sudo", "nmcli", "con", "up", "id", vpnclient])
except:
        e = sys.exc_info()[0]
        print e
finally:
        stat = "**** VPN Starting / On *****"
        ## print "**** VPN Starting ***"
 
 
xbmcgui.Dialog().ok(addonname, line1, line2, line3, stat)
