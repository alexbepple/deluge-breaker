#!/usr/bin/env python

class DelugeBreaker:

    def __init__(self, network, deluge, notifier):
        self.network = network
        self.deluge = deluge
        self.notifier = notifier

        self.policies = {}
        self.when_next_resumed(self.resume_deluge)
        self.when_next_paused(self.pause_deluge)

    def act(self):
        self.policies[self.network.is_safe_for_p2p()]()

    def do_nothing(self):
        pass

    def pause_deluge(self):
        self.deluge.pause()
        self.notifier.deluge_paused()
        self.when_next_resumed(self.resume_deluge)
        self.when_next_paused(self.do_nothing)

    def resume_deluge(self):
        self.deluge.resume()
        self.notifier.deluge_resumed()
        self.when_next_resumed(self.do_nothing)
        self.when_next_paused(self.pause_deluge)

    def when_next_resumed(self, action):
        self.policies[True] = action

    def when_next_paused(self, action):
        self.policies[False] = action
