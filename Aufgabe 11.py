def berechne_note(punktzahl):
    if punktzahl < 0 or punktzahl > 100:
        return -1 
    if punktzahl < 50:
        return 5.0 
    
    
    abstand_zu_50 = punktzahl - 50
    note_schritte = abstand_zu_50 // 5
    
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

    print(note)

    return max(1.0, round(note, 1))



