#!/usr/bin/env python

import logging
from pythonwifi.iwlibs import Wireless

def at_home():
    ap_mac = Wireless('wlan0').getAPaddr()
    is_safe = '00:1F:3F:1A:11:21' == ap_mac
    logging.info("Is this the home wifi? {0}".format(is_safe))
    return is_safe
