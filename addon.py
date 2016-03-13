import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "This is a VPN Script"
line2 = "It will allow you to turn on a vpn connection"
line3 = "And turn off a vpn connection"
 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)
