#!/usr/bin/env python

class DelugeBreaker:

    def __init__(self, network, deluge, notifier):
        self.network = network
        self.deluge = deluge
        self.notifier = notifier

    def act(self):
        if not self.network.is_safe_for_p2p():
            self.deluge.pause()
            self.notifier.deluge_paused()
