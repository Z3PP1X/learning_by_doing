import random

# 7. 

def compare_friends():

    list_of_friends = ['Denis', 'Thomas', 'Miguel', 'Calvin', 'Peter']

    a = list_of_friends
    b = list_of_friends

    # Überprüfe ob die Listen identisch sind

    return a == b
    
    

def compare_friends_2():
    # Überprüfe, ob die Reihenfolge eine Rolle spielt:

    list_of_friends = ['Denis', 'Thomas', 'Miguel', 'Calvin', 'Peter']

    # [:] Legt eine Kopie von list_of_friends an

    a = list_of_friends[:]
    b = list_of_friends[:]

    # Die Listen werden zufällig gemischt und im Anschluss verglichen, so können wir feststellen, ob die Reihenfolge eine Rolle spielt.

    random.shuffle(a)
    random.shuffle(b)

    return a == b



