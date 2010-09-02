#!/usr/bin/env python

import psutil

def is_running():
    processes = [process.cmdline for process in psutil.process_iter()]
    def is_deluge(cmdline): return "/usr/bin/deluge-gtk" in cmdline
    return filter(is_deluge, processes)


from deluge.log import setupLogger
setupLogger()

from deluge.ui.client import client
from twisted.internet import reactor

def pause():
    def pause_all_torrents():
        return client.core.pause_all_torrents()
    tell_deluge_to(pause_all_torrents)

def resume():
    def resume_all_torrents():
        return client.core.resume_all_torrents()
    tell_deluge_to(resume_all_torrents)


def tell_deluge_to(act):
    def on_connect_success(result):
        def disconnect(result):
            client.disconnect()
            reactor.crash()
        act().addCallback(disconnect)

    def on_connect_fail(result):
        print "Connection failed!"

    d = client.connect()
    d.addCallback(on_connect_success)
    d.addErrback(on_connect_fail)
    reactor.run()

