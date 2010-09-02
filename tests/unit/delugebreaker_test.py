#!/usr/bin/env python

from nose.tools import *
from nose.plugins.skip import SkipTest
from mockito import *

import delugebreaker
from delugebreaker import DelugeBreaker

class DelugeBreaker_Test:

    def setUp(self):
        self.driver = mock()
        self.network = mock()
        delugebreaker.notifier = mock()
        self.notifier = delugebreaker.notifier
        self.breaker = DelugeBreaker(self.network, self.driver, self.notifier)

    @istest
    def pauses_the_deluge_when_network_is_not_safe(self):
        when(self.network).is_safe_for_p2p().thenReturn(False)
        self.breaker.act()
        verify(self.driver).pause()
        verify(self.notifier).deluge_paused()

    @istest
    def does_not_halt_the_deluge_when_network_safe(self):
        when(self.network).is_safe_for_p2p().thenReturn(True)
        self.breaker.act()
        verifyNoMoreInteractions(self.driver)
        verifyNoMoreInteractions(self.notifier)
