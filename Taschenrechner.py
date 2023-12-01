## Wie viel ist 1000 ∙ 1,02510? (Kapital, das man nach 10 Jahren hätte, wenn man ein Anfangskapital von 1000€ zu 2,5% anlegen würde.

a = 1000 * 1.02510
print(a)

## 2. Wiederholen Sie die Aufgabe, aber weisen Sie nun entsprechende Werten den Variablen Anfangskapital, 
##Jahre und Zinssatz (in %) zu und führen Sie dann die Berechnung unter der Verwendung der Variablen durch.

def zinsrechner(anfangskapital: float, jahre: int, zinssatz:float):

    endkapital = anfangskapital * jahre ** ((1 + zinssatz)/100)
    return print(f'Ihr Endkapital beträgt nach {jahre} Jahren mit einem Zinssatz von {zinssatz}: {endkapital}€')

zinsrechner(10000, 3, 3.5)

## 3. Verwenden Sie die Funktion type(…), um herauszufinden, welchen Datentype Ihre Variable Jahre und Zinssatz haben.

def zinsrechner(anfangskapital: float, jahre: int, zinssatz:float):

    endkapital = anfangskapital * jahre ** zinssatz
    return type(anfangskapital, jahre, zinssatz)


## 4. Die Bank hat leider Ihren Zinssatz von 2,5% auf 2% gesenkt. Weisen Sie der Variable diesen Wert zu, 
## und schauen Sie sich erneut den Typ an. Was ist anders, als Sie das vielleicht von anderen Programmiersprachen her kennen.

# => Nachdem der Zinssatz nun bei 2% liegt ist ändert sich der Datentyp von float auf int. 
# Unterschied: In Python müssen Datentypen nicht deklariert werden. Der Datentyp der Variable ist also variabel.

