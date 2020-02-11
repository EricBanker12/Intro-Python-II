# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room):
        """constructs a player with starting location"""
        self.room = room
    def move(self, cmd):
        """Moves location to a connected room"""
        try:
            self.room = self.room.move(cmd)
        except:
            print('\nThere is nothing in that direction.')