from itertools import product

def chess_knight(start, nb_moves):
    #Raise exeption if start not good or if nb_moves not good
    #Change start into coord : OK
    [x, y] = cell2coord(start)
    # Create the list of next positions
    # Reduce the list to valid position
    # retrun results

    return x

def cell2coord(start):
    lettre2num = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8}
    return[lettre2num[start[0].lower()], start[1]]
    
def nextpos(x, y):
    setOfPos = {}
    
    return setOfPos