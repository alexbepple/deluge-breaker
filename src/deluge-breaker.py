#!/usr/bin/env python

import deluge
import network
import notifier

def notify_if_deluge_needs_halting():
    if deluge.is_running() and network.is_dangerous():
        notifier.warn_about_deluge()

if __name__ == "__main__":
    notify_if_deluge_needs_halting()

