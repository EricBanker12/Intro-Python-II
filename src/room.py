# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    """
    Class containing room name, description, current items,
    connected rooms, and methods to return or manipulate them.
    """
    def __init__(self, name, description):
        """Constructs a room with name and description"""
        self.name = name
        self.description = description
        self.items = []
        self.connections = {}

    def __getter__(cmd):
        """factory for property's fget"""
        return lambda self: self.connections[cmd]

    def __setter__(cmd):
        """factory for property's fset"""
        def setter(self, room):
            self.connections[cmd] = room
        return setter

    def move(self, cmd):
        """Returns connection or raises an exception"""
        return self.connections[cmd]

    def take(self, item_name):
        """Removes an item by name and returns it"""
        index = [item.name for item in self.items].index(item_name)
        return self.items.pop(index)

    def give(self, item):
        """Adds an item"""
        self.items.append(item)
        self.items.sort(key=lambda item: item.name)

    n_to = property(__getter__('n'), __setter__('n'), doc='northern connection')
    e_to = property(__getter__('e'), __setter__('e'), doc='eastern connection')
    s_to = property(__getter__('s'), __setter__('s'), doc='southern connection')
    w_to = property(__getter__('w'), __setter__('w'), doc='western connection')