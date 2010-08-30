#!/usr/bin/env python

import psutil

def is_running():
    processes = [process.cmdline for process in psutil.process_iter()]
    def is_deluge(cmdline): return "/usr/bin/deluge-gtk" in cmdline
    return filter(is_deluge, processes)

if __name__ == "__main__":
    if is_running(): print "Beware the deluge." 
