#!/usr/bin/env python

import deluge
import network
from notifier import Notifier

def notify_if_deluge_needs_halting():
    if deluge.is_running() and network.is_dangerous():
        Notifier().notify()

if __name__ == "__main__":
    notify_if_deluge_needs_halting()

