from dbus.mainloop.glib import DBusGMainLoop
import dbus
import gobject

DBusGMainLoop(set_as_default=True)

def when_network_becomes_available(callback):

    def is_connected(props):
        return props.get("State") == 3

    def on_new_props(props):
        if is_connected(props):
            callback()

    system_bus = dbus.SystemBus()
    system_bus.add_signal_receiver(on_new_props, signal_name="PropertiesChanged", dbus_interface="org.freedesktop.NetworkManager")

def start():
    gobject.MainLoop().run()

