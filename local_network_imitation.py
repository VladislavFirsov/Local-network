from random import randint


class Data:
    """Forms packages to send between servers
    """

    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


class Router:
    """Manager of packages
    """

    def __init__(self):
        self.servers = {}
        self.buffer = []

    def link(self, server):
        """Sets two-way communication between server and router
        """
        if server not in self.servers:
            self.servers[server.ip] = server
        server.link_to_router = self

    def unlink(self, server):
        if server in self.servers:
            self.servers.pop(server, False)
            server.link_to_router = None

    def send_data(self):
        """Sends the data and clears the buffer
        """
        for package in self.buffer:
            if package.ip in self.servers:
                self.servers[package.ip].buffer.append(package)
        self.buffer.clear()


class Server:
    def __init__(self):
        self.buffer = []
        self.ip = f'{255}.{255}.{randint(1, 255)}.{randint(1,255)}'
        self.link_to_router = None

    def send_data(self, data):
        if self.link_to_router:
            self.link_to_router.buffer.append(data)

    def get_data(self):
        packeges = self.buffer[:]
        self.buffer.clear()
        return packeges

    def get_ip(self):
        return self.ip
