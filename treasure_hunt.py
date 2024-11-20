# Game data
locations = {
    'start': {
        'description': "You are at the starting point. There are two paths: left and right.",
        'options': {'left': 'forest', 'right': 'cave'}
    },
    'forest': {
        'description': "You are in a dense forest. There are two paths: forward and backward.",
        'options': {'forward': 'river', 'backward': 'start'}
    },
    'cave': {
        'description': "You are inside a dark cave. There are two paths: forward and backward.",
        'options': {'forward': 'treasure', 'backward': 'start'}
    },
    'river': {
        'description': "You are at the edge of a roaring river. There is no way forward.",
        'options': {'backward': 'forest'}
    },
    'treasure': {
        'description': "You've found the treasure! Congratulations!",
        'options': {}
    }
}

is_on = True
position = "start"

while is_on:
    user_initial_response = input(locations[position]["description"])
    next_move = locations[position]["options"][user_initial_response]
    position = next_move
    if position == "treasure":
        print(locations[position]["description"])
        break