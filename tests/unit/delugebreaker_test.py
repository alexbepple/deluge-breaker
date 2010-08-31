#!/usr/bin/env python

from nose.tools import *
from nose.plugins.skip import SkipTest
from mockito import *

import delugebreaker
from delugebreaker import DelugeBreaker

class DelugeBreaker_Test:

    def setUp(self):
        delugebreaker.deluge = mock()
        delugebreaker.network = mock()
        delugebreaker.notifier = mock()

    @istest
    def halts_the_deluge_when_network_is_dangerous(self):
        when(delugebreaker.network).is_dangerous().thenReturn(True)
        DelugeBreaker().act()
        verify(delugebreaker.deluge).halt()
        verify(delugebreaker.notifier).warn_about_deluge()

    @istest
    def does_not_halt_the_deluge_when_network_safe(self):
        when(delugebreaker.network).is_dangerous().thenReturn(False)
        DelugeBreaker().act()
        verifyNoMoreInteractions(delugebreaker.deluge)
        verifyNoMoreInteractions(delugebreaker.notifier)
