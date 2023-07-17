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
    if from_member in social_graph[to_member]['following']:
        if to_member in social_graph[from_member]['following']:
            return("friends")
        else:
            return("followed by")
    elif to_member in social_graph[from_member]['following']:
        return("follower")
    else:
        return("no relationship")
            
from_member = str(input("Enter base username here, including the @:"))
to_member = str(input("Enter comparison username here, including the @:"))
relationship_status(from_member, to_member, social_graph)


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
    rows = len(board)
    columns = len(board[0])
    counter1 = 0
    diagonal_set1 = []
    counter2 = 0
    counter3 = len(board[0])
    diagonal_set2 = []

    for row in board:
        if len(set(row)) == 1 and row[0] != '':
            return row[0]
    for col in range(columns):
        column = [board[row][col] for row in range(rows)]
        if len(set(column)) == 1 and column[0] != '':
            return column[0]
    while counter1 < (len(board)):
        diagonal_set1.append(board[counter1][counter1])
        counter1 += 1
    if counter1 == (len(board)) and len(set(diagonal_set1)) == 1:
        return diagonal_set1[0]
    while counter2 < len(board):
        counter3 = len(board) - counter2 - 1
        diagonal_set2.append(board[counter2][counter3])
        counter2 += 1
    if counter2 == len(board) and counter3 == 0 and len(set(diagonal_set2)) == 1:
        return diagonal_set2[0]
    return "NO WINNER"

print(tic_tac_toe(board1))
print(tic_tac_toe(board2))
print(tic_tac_toe(board3))
print(tic_tac_toe(board4))
print(tic_tac_toe(board5))
print(tic_tac_toe(board6))
print(tic_tac_toe(board7))

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
    a = []
    b = []
    total_travel_time = 0
    for key in route_map:
        if first_stop in key[0]:
            a = key
            break
    for key2 in route_map:
        if second_stop in key2[1]:
            b = key2
            break
    if a[0] == b[0]:
        print(int(route_map[a]["travel_time_mins"]))
    elif a[1] == b[0]:
        print(int(route_map[a]["travel_time_mins"]+route_map[b]["travel_time_mins"]))
    else:
        current_stop = first_stop
        total_travel_time = 0
        while current_stop != second_stop:
            for (start, end), details in route_map.items():
                if start == current_stop:
                    travel_time = details['travel_time_mins']
                    total_travel_time += travel_time
                    current_stop = end
                    break
        return total_travel_time
first_stop = str(input("Enter the first stop here:"))
second_stop = str(input("Enter the second stop here:"))
eta(first_stop, second_stop, legs_2)