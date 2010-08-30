#!/usr/bin/env python

import pygtk
import gtk

class Notifier:

    def notify(self):
        dialog = gtk.MessageDialog(buttons=gtk.BUTTONS_OK)
        dialog.set_title("Deluge Breaker")
        dialog.set_markup("Beware the deluge!")

        theme = gtk.icon_theme_get_default()
        icon = theme.load_icon("deluge", 16, 0)
        dialog.set_icon(icon)

        dialog.run()
        dialog.destroy()

if __name__ == "__main__":
    Notifier().notify()

