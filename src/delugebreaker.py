#!/usr/bin/env python

import deluge
import network
import notifier

class DelugeBreaker:

    def act(self):
        if network.is_dangerous():
            deluge.halt()
            notifier.warn_about_deluge()
