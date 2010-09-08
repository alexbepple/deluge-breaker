from nose.tools import istest, assert_true, assert_false
from mockito import mock, when, verify

import networkchecker

class Network_Test:

    def setUp(self):
        self.network = mock()
        self.checker = networkchecker.NetworkChecker(self.network)

    @istest
    def is_safe_when_at_home(self):
        when(self.network).at_home().thenReturn(True)
        assert_true(self.checker.is_safe())
    
    @istest
    def is_not_safe_when_not_at_home(self):
        when(self.network).at_home().thenReturn(False)
        assert_false(self.checker.is_safe())
    
