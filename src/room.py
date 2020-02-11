# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        """Constructs a room with name and description"""
        self.name = name
        self.description = description
        self.items = []
        self.connections = {}
    def __getter__(cmd):
        """factory for property's fget"""
        return lambda self : self.connections[cmd]
    def __setter__(cmd):
        """factory for property's fset"""
        def setter(self, room):
            self.connections[cmd] = room
        return setter
    def move(self, cmd):
        """Returns connection or raises an exception"""
        return self.connections[cmd]
    n_to = property(__getter__("n"), __setter__("n"), doc='northern connection')
    e_to = property(__getter__("e"), __setter__("e"), doc='eastern connection')
    s_to = property(__getter__("s"), __setter__("s"), doc='southern connection')
    w_to = property(__getter__("w"), __setter__("w"), doc='western connection')