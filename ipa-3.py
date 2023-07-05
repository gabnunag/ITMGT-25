'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}

def relationship_status(from_member, to_member, social_graph):

    fm_following = social_graph.get(from_member,{}).get("following", [])
    tm_following = social_graph.get(to_member,{}).get("following", [])

    if to_member in fm_following and from_member in tm_following: #if to_member is both in the following and follows from_member; they are friends
        return "friends" 
    
    elif from_member in tm_following: #if from_member is only in tm_following, then return only followed by 
        return "followed by"
        
    elif to_member in fm_following: #if to_member only in fm_following, then return only follower
        return "follower"
    
    elif to_member not in fm_following and from_member not in tm_following: #if to_member not in both from_member nor in tm_following, return no relationship
        return "no relationship" 
    
    else:
        return "error"
        
relationship_status("@eeebeee", "@chums", social_graph)


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

def tic_tac_toe(board):


    for row in board: 
        if all(cell == row[0] and cell for cell in row):
            return row[0]
        
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[row][col] for row in range(len(board))):
            return board[0][col]

    if all(board[i][i] == board[0][0] and board[i][i] for i in range(len(board))):
        return board[0][0]

    if all(board[i][len(board)-1-i] == board[0][len(board)-1] and board[i][len(board)-1-i] for i in range(len(board))):
        return board[0][len(board)-1]

    return "NO WINNER"

tic_tac_toe(board1)

#second for loop checks the columns of the tic tac toe game
#first if statement checks the diagonal correctness of the game, from the top-left corner to the bottom-right corner
#second if statement checks the diagonal correctness of the game, from the top-right corner to the bottom-left corner

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
legs1 = {
     ("upd","admu"): {
         "travel_time_mins": 10
     },
     ("admu","dlsu"): {
         "travel_time_mins": 35
     },
     ("dlsu","upd"): {
         "travel_time_mins": 55
     }
}

legs2 = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}

def eta(first_stop, second_stop, route_map): 
    stopover = first_stop
    total_traveltime = 0
    
    while stopover != second_stop:
        route = (stopover, second_stop)
        if route in route_map:
            total_traveltime += route_map[route]['travel_time_mins']
            stopover = second_stop
        else:
            next_stopover = None
            for route in route_map:
                if route[0] == stopover:
                    next_stopover = route[1]
                    break
            if next_stopover is not None:
                total_traveltime += route_map[route]['travel_time_mins']
                stopover = next_stopover
            else:
                return None
    
    return total_traveltime

eta("upd","dlsu", legs1)