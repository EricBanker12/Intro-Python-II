from room import Room
from item import Item
from player import Player
from event import GameEvent
from utils import cmd_help, message_factory, rope_event_factory

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mouth beckons"
                ),
    'foyer':    Room("Foyer", 
                    """\
                    Dim light filters in from the south. Dusty
                    passages run north and east.
                    """
                ),
    'overlook': Room("Grand Overlook", 
                    """\
                    A steep cliff appears before you, falling
                    into the darkness. Ahead to the north, a light flickers in
                    the distance, but there is no way down the chasm.
                    """
                ),
    'chasm':    Room("Great Chasm", 
                    """\
                    Surrounded by darkness with the cliff looming
                    behind you, a northern, guiding light draws you in.
                    """
                ),
    'end':      Room("The End", "This is the end. Enter \"q\" to quit."),
    'narrow':   Room("Narrow Passage", 
                    """\
                    The narrow passage bends here from west
                    to north. The smell of gold permeates the air.
                    """
                ),
    'treasure': Room("Treasure Chamber", 
                    """\
                    You've found the long-lost treasure
                    chamber! Sadly, it has already been completely emptied by
                    earlier adventurers. The only exit is to the south.
                    """
                ),
}

# Declare all the items

item = {
    'sword': Item('sword', 'An abandoned, rusty, old sword.'),
    'rope': Item('rope', 'A long rope. Useful for towing or climbing.'),
    'bell': Item('bell', 'A small, metallic bell that jingles with every movement.'),
}

# Add events to items

item['rope'].event = GameEvent(
    room['overlook'],
    message_factory('\nMaybe you can use the rope.'),
    rope_event_factory(room['overlook'], room['chasm'])
)

# Add items to rooms

room['outside'].give(item['sword'])
room['treasure'].give(item['rope'])
room['treasure'].give(item['bell'])

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['chasm'].s_to = room['overlook']
room['chasm'].n_to = room['end']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def main():
    """Adventure game loop"""
    print('\n' + '=' * 80)
    name = input('Welcome!\nWhat is your name?\n: ')
    player = Player(name, room['outside'])
    cmd_help()
    while True:
        player.status()
        cmd = input('\nEnter a command... ("h" for Help)\n: ')
        if cmd == 'q' or cmd == 'quit':
            exit()
        if cmd == 'h' or cmd == 'help':
            cmd_help()
        else:
            player.do(cmd)

main()
