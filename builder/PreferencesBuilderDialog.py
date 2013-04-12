# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

# This is your preferences dialog.
#
# Define your preferences in
# data/glib-2.0/schemas/net.launchpad.builder.gschema.xml
# See http://developer.gnome.org/gio/stable/GSettings.html for more info.

from gi.repository import Gio # pylint: disable=E0611

from locale import gettext as _

import logging
logger = logging.getLogger('builder')

from builder_lib.PreferencesDialog import PreferencesDialog

class PreferencesBuilderDialog(PreferencesDialog):
    __gtype_name__ = "PreferencesBuilderDialog"

    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the preferences dialog"""
        super(PreferencesBuilderDialog, self).finish_initializing(builder)

        # Bind each preference widget to gsettings
        settings = Gio.Settings("net.launchpad.builder")
        widget = self.builder.get_object('example_entry')
        settings.bind("example", widget, "text", Gio.SettingsBindFlags.DEFAULT)

        # Code for other initialization actions should be added here.
