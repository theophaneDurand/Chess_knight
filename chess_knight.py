from itertools import product

def chess_knight(start, nb_moves):
    """
    Fonction principale du programme
    
    Parameters
    ----------
    start : string
        start doit être une cellule sous forme de string de deux caractères une lettre entre "a" et "h" et un chiffre entre 1 et 8.
        une verification est effectuée sur le format de start
    nb_moves : int
        représente le nombre de mouvement que peut faire le cavalier

    Returns
    -------
    reachableCells : tab de strings
        représentes toutes les cellules où le cavalier peut aller en partant de la position %start% et en effectuant au maximum %nb_moves% déplacements.

    """
    #Raise exeption if start not good or if nb_moves not good
    if len(start) != 2 or start[0] not in "abcdefgh" or int(start[1]) < 1 or int(start[1]) > 8 or nb_moves < 1:
        raise TypeError("données d'entrée incorrectes") 
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
    """
    
    Parameters
    ----------
    start : string
           start doit être une cellule sous forme de string de deux caractères une lettre entre "a" et "h" et un chiffre entre 1 et 8

    Returns
    -------
     un tuple de 2 chiffres entre 1 et 8. Correspondant au numéro de la lettre (1 pour "a"... 8 pour "h") ainsi que le chiffre de la cellule

    """
    lettre2num = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8}
    coord = (lettre2num[start[0].lower()], int(start[1]))
    return coord
    
def nextpos(x, y):
    """
    
    Parameters
    ----------
    x : int
        x est un int entre 1 et 8.
    y : int
         est un int entre 1 et 8.

    Returns
    -------
    reachablePos : tab de tuple de deux int
        renvoit une liste de coordonnées correspondant aux coordonnées atteignable par un cavalier au coordonnées données en entrée.

    """
    # On calcule les positions atteignables depuis la position actuelle :
    reachablePos = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
    # On restreint les positions trouvées au positions réelles :
    reachablePos = [(x,y) for x,y in reachablePos if x > 0 and y > 0 and x <= 8 and y <= 8]
    # On renvoit le résultat
    return reachablePos

def coord2cell(coord):
    """

    Parameters
    ----------
    coord : tuple de deux int
        Ils correspondent aux coordonnées (entre 1 et 8)

    Returns
    -------
    cell : string
        cell doit être une cellule sous forme de string de deux caractères une lettre entre "a" et "h" et un chiffre entre 1 et 8.

    """
    lettre = ["", "a", "b", "c", "d", "e", "f",  "g", "h"]
    cell = lettre[coord[0]]+str(coord[1])
    return cell