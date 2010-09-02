#!/usr/bin/env python

from nose.tools import *
from nose.plugins.skip import SkipTest
from mockito import *

import delugebreaker
from delugebreaker import DelugeBreaker

class DelugeBreaker_Test:

    def setUp(self):
        delugebreaker.delugedriver = mock()
        delugebreaker.network = mock()
        delugebreaker.notifier = mock()

    @istest
    def pauses_the_deluge_when_network_is_not_safe(self):
        when(delugebreaker.network).is_safe_for_p2p().thenReturn(False)
        DelugeBreaker().act()
        verify(delugebreaker.delugedriver).pause()
        verify(delugebreaker.notifier).deluge_paused()

    @istest
    def does_not_halt_the_deluge_when_network_safe(self):
        when(delugebreaker.network).is_safe_for_p2p().thenReturn(True)
        DelugeBreaker().act()
        verifyNoMoreInteractions(delugebreaker.delugedriver)
        verifyNoMoreInteractions(delugebreaker.notifier)
