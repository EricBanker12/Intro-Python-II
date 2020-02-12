# Write a class to hold player information, e.g. what room they are in
# currently.
import re

class Player:
    def __init__(self, name, room):
        """Construct a player with name and starting location."""
        self.name = name
        self.room = room
        self.items = []
    def do(self, cmd):
        """Try to do an action."""
        if re.compile('[nesw]|north|east|south|west').fullmatch(cmd):
            # cmd matches "n", "e", "s", "w", "north", "east", "south", or "west"
            self.move(cmd)
        elif re.compile('[t] \w+|take \w+|get \w+').fullmatch(cmd):
            # cmd matches "t [item_name]", "take [item_name]", or "get [item_name]"
            self.take(cmd)
        else:
            print('\n' + '=' * 80)
            print(f'Command "{cmd}" not recognized.\nEnter "h" for Help.')
    def move(self, cmd):
        """Move location to a connected room."""
        try:
            self.room = self.room.move(cmd[0])
        except:
            print('\n' + '=' * 80)
            print('There is nothing in that direction.')
    def take(self, cmd):
        """Pick up an item from the current room"""
        try:
            item_name = cmd.split(' ')[1]
            item = self.room.take(item_name)
            print('\n' + '=' * 80)
            item.on_take()
            self.items.append(item)
            self.items.sort(key=lambda item: item.name)
        except:
            print('\n' + '=' * 80)
            print(f'The item "{item_name}" was not found.')