## Generieren Sie für Ihre Cousine in der Grundschule die untenstehende Tabelle mit
## dem kleinen Einmaleins.

def tabelle():

    zahl = [i for i in range(11)]
    multiplikator = [i for i in range(11)]

    kleines_1x1 = {a:{b: a*b for b in multiplikator}for a in zahl}

    return(kleines_1x1[i] for i in kleines_1x1)

i = 0
for zeile in tabelle():
    print(f'{i}: {zeile}')
    i += 1

    

## Alternativ:

def tabelle2():
    zahl = [i for i in range(11)]
    multiplikator = [i for i in range(11)]

    # Drucke die Kopfzeile der Tabelle
    kopfzeile = '    ' + ' '.join(f'{m:2}' for m in multiplikator)
    print(kopfzeile)
    print('    ' + '-' * len(kopfzeile))

    # Iteriere durch jede Zahl, um die Zeilen der Tabelle zu erstellen
    for a in zahl:
        # Erstelle eine Zeile mit der Nummer und den Produkten
        zeile = f'{a:2} |' + ' '.join(f'{a*b:2}' for b in multiplikator)
        print(zeile)


tabelle2()