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
        self.notifier = mock()
        self.breaker = DelugeBreaker(self.network, self.driver, self.notifier)

    @istest
    def pauses_the_deluge_when_network_is_not_safe(self):
        when(self.network).is_safe_for_p2p().thenReturn(False)
        self.breaker.act()
        verify(self.driver).pause()
        verify(self.notifier).deluge_paused()

    @istest
    def pauses_the_deluge_only_once(self):
        when(self.network).is_safe_for_p2p().thenReturn(False)
        [self.breaker.act() for i in range(2)]
        verify(self.driver, times=1).pause()

    @istest
    def pauses_again_after_the_deluge_resumes(self):
        (when(self.network).is_safe_for_p2p()
            .thenReturn(False).thenReturn(True).thenReturn(False))
        [self.breaker.act() for i in range(3)]
        verify(self.driver, times=2).pause()
        
    @istest
    def resumes_the_deluge_when_network_safe(self):
        when(self.network).is_safe_for_p2p().thenReturn(True)
        self.breaker.act()
        verify(self.driver).resume()
        verify(self.notifier).deluge_resumed()

    @istest
    def resumes_the_deluge_only_once(self):
        when(self.network).is_safe_for_p2p().thenReturn(True)
        [self.breaker.act() for i in range(2)]
        verify(self.driver, times=1).resume()

    @istest
    def resumes_again_after_the_deluge_was_paused(self):
        (when(self.network).is_safe_for_p2p()
            .thenReturn(True).thenReturn(False).thenReturn(True))
        [self.breaker.act() for i in range(3)]
        verify(self.driver, times=2).resume()
