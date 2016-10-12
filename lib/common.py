#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

"""
Stuff shared between the python files
"""

import os
import sys
import xbmc
import xbmcaddon
import xbmcplugin
import xbmcgui

# Add the /lib folder to sys
sys.path.append(xbmc.translatePath(os.path.join(xbmcaddon.Addon("plugin.video.auvio").getAddonInfo("path"), "lib")))

# SimplePlugin
from simpleplugin import Plugin
from simpleplugin import Addon

# Create plugin instance
plugin = Plugin()

rtbf_url = 'http://www.rtbf.be/'
rtbf_url_api = rtbf_url + "api/"
auvio_url = 'http://www.rtbf.be/auvio/'
auvio_url_api = auvio_url + "api/"

#in minutes
cachetime_categories = 60 * 12
cachetime_channels = 60 * 12
cachetime_shows = 60 * 12
cachetime_medias_recent = 15
cachetime_media_data = 5
cachetime_radio_config = 60
cachetime_live = 5
cachetime_category_medias = 15
cachetime_channel_medias = 2

def popup(text, time=5000, image=None):
    title = plugin.addon.getAddonInfo('name')
    icon = plugin.addon.getAddonInfo('icon')
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % (title, text,time, icon))
