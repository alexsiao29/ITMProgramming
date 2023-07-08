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
    
    if  from_member in social_graph[to_member]["following"] and to_member in social_graph[from_member]["following"]:
        statement="friends"
    elif to_member in social_graph[from_member]["following"]:
        statement="follower"
    elif from_member in social_graph[to_member]["following"]:
        statement="followed by"
    else: 
        statement="no relationship"
    
    return str(statement)

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
    
    check=[board[diag][diag] for diag in range(len(board))]
    if len(set(check))==1 and check[0]!="":
        result=check[0]
    else:
        checker=[board[diag][(diag+(len(board)))-(diag+1)]for diag in range(len(board))]
        if len(set(checker))==1 and checker[0]!="":
            result=checker[0]
        else:
            signal=""
            for line in board:
                if len(set(line))==1:
                    result=line[0]
                    signal="stop na"
                    break
            if signal!="stop na":
                for i_column in range(len(board)):
                    check = [board[count][i_column] for count in range(len(board))]
                    if len(set(check))==1 and check[0]!="":
                            result=check[0]
                            break
                    else:
                        result="NO WINNER"
    return result

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
    

    travel_time=0
    current=0
    keys_madali=list(route_map.keys())
    now=first_stop
    while now!=second_stop:
        for key in keys_madali:
            if key == (first_stop,second_stop):
                current=route_map[key]['travel_time_mins']
                break
            elif key[0]==now:
                travel_time=route_map[key]['travel_time_mins']
                break
            else:
                pass
        current=current+travel_time
        now=key[1]
    return current
