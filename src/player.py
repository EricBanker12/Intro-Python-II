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
            self.move(cmd)
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