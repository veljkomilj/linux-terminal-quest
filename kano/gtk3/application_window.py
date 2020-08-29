#
# Custom window base class
#
# Copyright (C) 2014 - 2018 Kano Computing Ltd.
# License: http://www.gnu.org/licenses/gpl-2.0.txt GNU GPLv2
#
# You can use this as a base for you application's window in case
# you'd like to blur it.
#

from gi import require_version
require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk

from kano.gtk3.apply_styles import apply_common_to_screen


class ApplicationWindow(Gtk.Window):
    def __init__(self, title="Application", width=None, height=None):
        Gtk.Window.__init__(self, title=title)

        self.set_decorated(False)
        self.set_resizable(False)

        screen = Gdk.Screen.get_default()
        self._win_width = width
        if width <= 1:
            self._win_width = int(screen.get_width() * width)

        self._win_height = height
        if height <= 1:
            self._win_height = int(screen.get_height() * height)
        self.set_size_request(self._win_width, self._win_height)

        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect('delete-event', Gtk.main_quit)

        apply_common_to_screen()

        self._overlay = Gtk.Overlay()
        self.add(self._overlay)

        self._blur = Gtk.EventBox()
        self._blur.get_style_context().add_class('blur')

        self._blurred = False

        # TODO: Maybe handle the taskbar here to avoid even more code duplication?

    def blur(self):
        if not self._blurred:
            self._overlay.add_overlay(self._blur)
            self._blur.show()
            self._blurred = True

    def unblur(self):
        if self._blurred:
            self._overlay.remove(self._blur)
            self._blurred = False

    def set_main_widget(self, widget):
        self._overlay.add(widget)

    def remove_main_widget(self):
        for w in self._overlay.get_children():
            self._overlay.remove(w)
