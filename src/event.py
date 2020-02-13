class GameEvent:
    """
    Class containing a game-event with a set room,
    optional event handlers, and methods to call set handlers
    """
    def __init__(self, room, on_inventory = None, on_use = None):
        """Constructs an event with a room assignment and handler callbacks"""
        self.room = room
        self.on_inventory = on_inventory
        self.on_use = on_use

    def inventory(self, player):
        """Call handler for inventory event"""
        if player.room == self.room and self.on_inventory:
            self.on_inventory()

    def use(self, player):
        """Call handler for use event"""
        if player.room == self.room and self.on_use:
            self.on_use()
