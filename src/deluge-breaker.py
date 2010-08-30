#!/usr/bin/env python

from deluge_driver import DelugeDriver
from network import Network
from notifier import Notifier

def notify_if_deluge_needs_halting():
    if DelugeDriver().is_running() and not Network().is_ok_for_p2p():
        Notifier().notify()

if __name__ == "__main__":
    notify_if_deluge_needs_halting()

