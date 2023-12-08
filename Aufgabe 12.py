def berechne_note(punktzahl, max_punktzahl):
    
    if punktzahl < 0 or punktzahl > max_punktzahl:
        return -1
    
    
    if punktzahl < 0.5 * max_punktzahl:
        return 5.0 
    
    note_schritte = (max_punktzahl - max_punktzahl * 0.5) // 9  

    note = 4.0 - note_schritte * 0.3

    note = max(1.0, note)
    
    rest = note % 1
    if rest > 0:
        if rest <= 0.3:
            note = int(note) + 0.3
        elif rest <= 0.7:
            note = int(note) + 0.7
        else:
            note = int(note) + 1.0 

    print(note_schritte)    

    print(round(note, 1))


berechne_note(150, 200)

