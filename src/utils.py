def cmd_help():
    """Print a list of all game commands"""
    commands = [
        '"h, help" for Help',
        '"q, quit" for Quit',
        '"n, north" for North',
        '"e, east" for East',
        '"s, south" for South',
        '"w, west" for West',
        '"t, take, get" "item" for Take Item',
        '"d, drop" "item" for Drop Item',
        '"i, inventory" for Inventory',
        '"u, use" "item" for Use Item'
    ]
    print('\n' + '=' * 80)
    print('Commands:')
    commands_str = ''
    for i in range(len(commands)):
        if i and not i % 2:
            commands_str += '\n'
        spacer = ' ' * (40 - len(commands[i]))
        commands_str += f'{commands[i]}{spacer}'
    print(commands_str)

def message_factory(msg):
    """Returns a function that prints a given message"""
    def message():
        print(msg)
    return message

def rope_event_factory(room, room_2):
    """
    Returns a function that prints a message,
    updates a room, and connects it to another room
    """
    def callback():
        print('You used the "rope". You can now climb down the chasm.')
        room.description = """\
            A steep cliff appears before you, falling
            into the darkness. Ahead to the north, a light flickers in
            the distance. A climbing rope is fastened securely.
            """
        room.n_to = room_2
        room_2.s_to = room
    return callback