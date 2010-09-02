#!/usr/bin/env python

import delugedriver
import network
import notifier

class DelugeBreaker:

    def act(self):
        if network.is_dangerous():
            delugedriver.pause()
            notifier.deluge_paused()
