#!/usr/bin/env python

class DelugeBreaker:

    def __init__(self, network, deluge, notifier):
        self.network = network
        self.deluge = deluge
        self.notifier = notifier

        self.policies = {}
        self.policies[True] = self.resume_deluge
        self.policies[False] = self.pause_deluge

    def act(self):
        self.policies[self.network.is_safe_for_p2p()]()

    def pause_deluge(self):
        self.deluge.pause()
        self.notifier.deluge_paused()

    def resume_deluge(self):
        self.deluge.resume()
        self.notifier.deluge_resumed()

