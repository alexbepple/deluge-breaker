#!/usr/bin/env python

import socket
import fcntl
import struct

def get_ip_address(ifname):
    # Blindly taken from http://code.activestate.com/recipes/439094-get-the-ip-address-associated-with-a-network-inter/
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def is_wifi_available():
    try:
        return get_ip_address('wlan0')
    except IOError:
        return False


from pythonwifi.iwlibs import Wireless

def is_wifi_safe_for_p2p():
    return '00:1F:3F:1A:11:21' == Wireless('wlan0').getAPaddr()

def is_safe_for_p2p():
    return is_wifi_available() and is_wifi_safe_for_p2p()

if __name__ == "__main__":
    if is_dangerous(): print "Network is dangerous."
