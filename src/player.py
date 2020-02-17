# Write a class to hold player information, e.g. what room they are in
# currently.
import re
from textwrap import dedent, wrap

class Player:
    """
    Class containing player name, current room, current items,
    and methods to print and manipulate them.
    """
    def __init__(self, name, room):
        """Construct a player with name and starting room."""
        self.name = name
        self.room = room
        self.items = []

    def status(self):
        """Print the current player status"""
        print('\n' + '=' * 80)
        name_location_spacing = ' ' * (70 - len(self.name) - len(self.room.name)) + 'Location: '
        print(f'{self.name}{name_location_spacing}{self.room.name}')
        for line in wrap(dedent(self.room.description), 50):
            print(line)
        for item in self.items:
            item.inventory(self)
        if self.room.items:
            print(
                '\nSearching around, you find:',
                *[f'\n{item.name}: {item.description}' for item in self.room.items]
            )

    def do(self, cmd):
        """Try to do an action."""
        print('\n' + '=' * 80)
        if re.compile('[nesw]|north|east|south|west').fullmatch(cmd):
            # cmd matches "n", "e", "s", "w", "north", "east", "south", or "west"
            self.move(cmd)
        elif re.compile('t \w+|take \w+|get \w+').fullmatch(cmd):
            # cmd matches "t [item_name]", "take [item_name]", or "get [item_name]"
            self.take(cmd)
        elif re.compile('d \w+|drop \w+').fullmatch(cmd):
            # cmd matches "d [item_name]" or "drop [item_name]"
            self.drop(cmd)
        elif re.compile('i|inventory').fullmatch(cmd):
            # cmd matches "i" or "inventory"
            self.inventory()
        elif re.compile('u \w+|use \w+').fullmatch(cmd):
            # cmd matches "u [item_name]" or "use [item_name]"
            self.use(cmd)
        else:
            print(f'Command "{cmd}" not recognized.\nEnter "h" for Help.')

    def move(self, cmd):
        """Move location to a connected room."""
        try:
            self.room = self.room.move(cmd[0])
            print(f'You have moved to {self.room.name}.')
        except:
            print('There is nothing in that direction.')

    def take(self, cmd):
        """Pick up an item from the current room"""
        try:
            item_name = cmd.split(' ')[1]
            item = self.room.take(item_name)
            item.on_take()
            self.items.append(item)
            self.items.sort(key=lambda item: item.name)
        except:
            print(f'The item "{item_name}" was not found.')

    def drop(self, cmd):
        """Drop an item into the current room"""
        try:
            item_name = cmd.split(' ')[1]
            index = [item.name for item in self.items].index(item_name)
            item = self.items.pop(index)
            item.on_drop()
            self.room.give(item)
        except:
            print(f'The item "{item_name}" was not found.')

    def inventory(self):
        """Print inventory contents"""
        if self.items:
            print(
                'In your inventory, you find:',
                *[f'\n{item.name}: {item.description}' for item in self.items]
            )
        else:
            print('Your inventory is empty.')

    def use(self, cmd):
        """Use an item in the current room"""
        try:
            item_name = cmd.split(' ')[1]
            index = [item.name for item in self.items].index(item_name)
            item = self.items[index]
            item.use(self)
            self.items.pop(index)
        except ValueError:
            print(f'The item "{item_name}" was not found.')
        except AttributeError:
            print(f'The item "{item_name}" has no use here.')
