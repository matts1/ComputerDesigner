# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('builder')

from builder_lib import Window
from builder.AboutBuilderDialog import AboutBuilderDialog
from builder.PreferencesBuilderDialog import PreferencesBuilderDialog

# See builder_lib.Window.py for more details about how this class works
class BuilderWindow(Window):
    __gtype_name__ = "BuilderWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(BuilderWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutBuilderDialog
        self.PreferencesDialog = PreferencesBuilderDialog

        # Code for other initialization actions should be added here.

