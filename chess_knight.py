from itertools import product

def chess_knight(start, nb_moves):
    #Raise exeption if start not good or if nb_moves not good
    #Change start into coord : OK
    [x, y] = cell2coord(start)
    # Create the list of next positions : OK
    # Reduce the list to valid position : OK
    reachableCoord = nextpos(x, y)
    # Change coord into cell
    reachableCells = [coord2cell(coord) for coord in reachableCoord]
    # Sorting of the list
    reachableCells.sort()
    # retrun results
    return reachableCells

def cell2coord(start):
    lettre2num = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8}
    return[lettre2num[start[0].lower()], int(start[1])]
    
def nextpos(x, y):
    # On calcule les positions atteignables depuis la position actuelle :
    reachablePos = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
    # On restreint les positions trouvées au positions réelles :
    reachablePos = [(x,y) for x,y in reachablePos if x > 0 and y > 0 and x <= 8 and y <= 8]
    # On renvoit le résultat
    return reachablePos

def coord2cell(coord):
    lettre = ["", "a", "b", "c", "d", "e", "f",  "g", "h"]
    cell = lettre[coord[0]]+str(coord[1])
    return cell