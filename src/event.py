class GameEvent:
    def __init__(self, room, on_inventory = None, on_use = None):
        self.room = room
        self.on_inventory = on_inventory
        self.on_use = on_use
    def inventory(self, player):
        if player.room == self.room and self.on_inventory:
            self.on_inventory()
    def use(self, player):
        if player.room == self.room and self.on_use:
            self.on_use()
