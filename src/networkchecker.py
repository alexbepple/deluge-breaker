class NetworkChecker():
    def __init__(self, network):
        self.network = network

    def is_safe(self):
        return self.network.at_home()
