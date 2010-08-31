#!/usr/bin/env python

from dbus.mainloop.glib import DBusGMainLoop
import dbus
import gobject

DBusGMainLoop(set_as_default=True)

def when_network_becomes_available(callback):
    def on_new_state(state):
        if state == 3:
            callback()

    system_bus = dbus.SystemBus()
    system_bus.add_signal_receiver(on_new_state, signal_name="StateChanged", dbus_interface="org.freedesktop.NetworkManager")

def start():
    gobject.MainLoop().run()

