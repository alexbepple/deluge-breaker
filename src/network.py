#!/usr/bin/env python

from pythonwifi.iwlibs import Wireless

class Network():
    def is_ok_for_p2p(self):
        return '00:1F:3F:1A:11:21' == Wireless('wlan0').getAPaddr()

if __name__ == "__main__":
    if not Network().is_ok_for_p2p(): print "Beware the deluge."
