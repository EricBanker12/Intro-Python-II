class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.event = None
    def on_take(self):
        print(f'You picked up the {self.name}.')
    def on_drop(self):
        print(f'You dropped the {self.name}.')
    def set_event(self, game_event):
        self.event = game_event
    def inventory(self, player):
        if self.event:
            self.event.inventory(player)
    def use(self, player):
        self.event.use(player)