#!/usr/bin/env python

import socket
import fcntl
import struct
import logging

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
        wifi_available = get_ip_address('wlan0') and True
    except IOError:
        wifi_available = False
    logging.info("Is a wifi available? {0}".format(wifi_available))
    return wifi_available


from pythonwifi.iwlibs import Wireless

def is_wifi_safe_for_p2p():
    ap_mac = Wireless('wlan0').getAPaddr()
    is_safe = '00:1F:3F:1A:11:21' == ap_mac
    logging.info("Is current wifi is safe for P2P? {0}".format(is_safe))
    return is_safe

def is_safe_for_p2p():
    return is_wifi_available() and is_wifi_safe_for_p2p()

