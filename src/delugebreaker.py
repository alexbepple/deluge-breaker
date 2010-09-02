#!/usr/bin/env python

import delugedriver
import network
import notifier

class DelugeBreaker:

    def act(self):
        if not network.is_safe_for_p2p():
            delugedriver.pause()
            notifier.deluge_paused()
