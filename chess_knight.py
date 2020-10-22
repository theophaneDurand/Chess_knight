from itertools import product

#taille de l'échéquier : 
N = 8
lettre = " abcdefgh"

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
    # On lève une exeption si les données d'entrée ne sont pas correcte.
    if len(start) != 2 or start[0] not in "abcdefgh" or int(start[1]) < 1 or int(start[1]) > N or nb_moves < 1:
        raise TypeError("données d'entrée incorrectes") 
    
    reachableCells = [start]
    #On boucle sur le nombre de mouvement que le cavalier peut faire
    for i in range(nb_moves):
        reachableCoord = []
        # si il y a plusieurs mouvements, on regarde les cellules accessibles depuis les cellules précédentes
        for cell in reachableCells:
            # On change le nom de la cellule en deux coordonnées
            [x, y] = cell2coord(cell)
            # On créé la liste des position accessible depuis la position actuelle
            reachableCoord += nextpos(x, y)
            # On passe les coordonnées sous format cellule
        reachableCells += [coord2cell(coord) for coord in reachableCoord]
    # On enlève la cellule de départ de la liste
    reachableCells.remove(start)
    # On enlève les doublons
    reachableCells = list(set(reachableCells))
    # On trie les éléments de la liste
    reachableCells.sort()
    # On retourne le resultat
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
    coord = (lettre.find(start[0].lower()), int(start[1]))
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
    reachablePos = [(x,y) for x,y in reachablePos if x > 0 and y > 0 and x <= N and y <= N]
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
    cell = lettre[coord[0]]+str(coord[1])
    return cell