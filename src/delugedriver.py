#!/usr/bin/env python

import psutil

def is_running():
    processes = [process.cmdline for process in psutil.process_iter()]
    def is_deluge(cmdline): return "/usr/bin/deluge-gtk" in cmdline
    return filter(is_deluge, processes)

def pause():
    from deluge.ui.client import client
    from twisted.internet import reactor

    from deluge.log import setupLogger


    def disconnect(result):
        client.disconnect()
        reactor.stop()

    def on_connect_success(result):
        client.core.pause_all_torrents().addCallback(disconnect)

    def on_connect_fail(result):
        print "Connection failed!"

    setupLogger()
    d = client.connect()
    d.addCallback(on_connect_success)
    d.addErrback(on_connect_fail)
    reactor.run()

if __name__ == "__main__":
    if is_running(): print "Beware the deluge." 
