#!/usr/bin/env python

import os.path
def activate_virtualenv():
    src_dir = os.path.dirname(__file__)
    ve_activator=os.path.join(src_dir, '../bin/activate_this.py')
    execfile(ve_activator, dict(__file__=ve_activator))

activate_virtualenv()

import logging
logging.basicConfig(level=logging.DEBUG)

import delugedriver as deluge
from delugebreaker import DelugeBreaker
import networkobserver
import network
from networkchecker import NetworkChecker
import notifier

network_checker = NetworkChecker(network)
deluge_breaker = DelugeBreaker(network_checker, deluge, notifier.notifyosd)

def use_deluge_breaker():
    if deluge.is_running():
        deluge_breaker.act()

if __name__ == "__main__":
    networkobserver.when_network_becomes_available(use_deluge_breaker)
    networkobserver.start()

