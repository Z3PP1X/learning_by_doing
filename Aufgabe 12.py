def berechne_note(punktzahl, max_punktzahl):
    
    if punktzahl < 0 or punktzahl > max_punktzahl:
        return -1   
    
    if punktzahl < 0.5 * max_punktzahl:
        return 5.0 
    
    note_schritte = (max_punktzahl * 0.5) / 9
    punktabstand = punktzahl - (max_punktzahl * 0.5)
    notenstufen = punktabstand / note_schritte

    note = 4.0 - notenstufen * 0.3

    if note <= 1.0:
        note = 1.0

    notenstufen_1 = [1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0]

    note = min(notenstufen_1, key=lambda x:abs(x-note))

    return note


    


test = berechne_note(150, 150)
print(test)

