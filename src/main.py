#!/usr/bin/env python

import os.path
def activate_virtualenv():
    src_dir = os.path.dirname(__file__)
    ve_activator=os.path.join(src_dir, '../bin/activate_this.py')
    execfile(ve_activator, dict(__file__=ve_activator))

activate_virtualenv()

import deluge
import network
import notifier
import networkobserver

def notify_if_deluge_needs_halting():
    if deluge.is_running() and network.is_dangerous():
        notifier.warn_about_deluge()

if __name__ == "__main__":
    networkobserver.when_network_becomes_available(notify_if_deluge_needs_halting)
    networkobserver.start()

