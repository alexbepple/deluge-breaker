#!/usr/bin/env python

import deluge
import network
import notifier

def notify_if_deluge_needs_halting():
    if deluge.is_running() and network.is_dangerous():
        notifier.warn_about_deluge()

def see_about_deluge_when_network_becomes_available(state):
    if state == 3:
        notify_if_deluge_needs_halting()

def set_up_daemon():
    from dbus.mainloop.glib import DBusGMainLoop
    import dbus
    import gobject

    DBusGMainLoop(set_as_default=True)
    system_bus = dbus.SystemBus()

    system_bus.add_signal_receiver(see_about_deluge_when_network_becomes_available, signal_name="StateChanged", dbus_interface="org.freedesktop.NetworkManager")

    gobject.MainLoop().run()

if __name__ == "__main__":
    set_up_daemon()
