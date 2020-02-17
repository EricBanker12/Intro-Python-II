class Item:
    """
    Class containing item name, description, set event,
    and methods invoked through gameplay events
    """
    def __init__(self, name, description):
        """Constructs an item with name and description"""
        self.name = name
        self.description = description
        self.event = None

    def on_take(self):
        """Prints a message on item pickup"""
        print(f'You picked up the {self.name}.')

    def on_drop(self):
        """Prints a message on item drop"""
        print(f'You dropped the {self.name}.')

    def inventory(self, player):
        """Invoke inventory-event handler if set"""
        if self.event:
            self.event.inventory(player)

    def use(self, player):
        """Try to invoke use-event handler"""
        self.event.use(player)
