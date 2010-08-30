#!/usr/bin/env python

import psutil

class DelugeDriver():
    def is_running(self):
        processes = [process.cmdline for process in psutil.process_iter()]
        def is_deluge(cmdline): return "/usr/bin/deluge-gtk" in cmdline
        return filter(is_deluge, processes)
        #for process in psutil.process_iter():
            #if "/usr/bin/deluge-gtk" in process.cmdline:
                #return True

if __name__ == "__main__":
    if DelugeDriver().is_running(): print "Beware the deluge." 
