notenliste = []
def rechner_notenpunkte(punkte_gesamt):
    if float(punkte_gesamt) >= 0:
        notenpunkte_gesamt = 0 
    if float(punkte_gesamt) > 18:
        notenpunkte_gesamt = 1
    if float(punkte_gesamt) > 19:
        notenpunkte_gesamt = 2
    if float(punkte_gesamt) > 32:
        notenpunkte_gesamt = 3
    if float(punkte_gesamt) > 39:
        notenpunkte_gesamt = 4
    if float(punkte_gesamt) > 44:
        notenpunkte_gesamt = 5
    if float(punkte_gesamt) > 49:
        notenpunkte_gesamt = 6
    if float(punkte_gesamt) > 54:
        notenpunkte_gesamt = 7
    if float(punkte_gesamt) > 59:
        notenpunkte_gesamt = 8
    if float(punkte_gesamt) > 64:
        notenpunkte_gesamt = 9
    if float(punkte_gesamt) > 69:
        notenpunkte_gesamt = 10
    if float(punkte_gesamt) > 74:
        notenpunkte_gesamt = 11
    if float(punkte_gesamt) > 79:
        notenpunkte_gesamt = 12
    if float(punkte_gesamt) > 84:
        notenpunkte_gesamt = 13
    if float(punkte_gesamt) > 89:
        notenpunkte_gesamt = 14
    if float(punkte_gesamt) > 94:
        notenpunkte_gesamt = 15
    return notenpunkte_gesamt


frage0=input("Sollen schriftliche Noten oder AT-Noten ermittelt werden? (schr/at) ")
if frage0=="schr" or frage0=="schriftliche Noten":

    print("Alle 3 Aufgaben haben zusammen 100 Punkte.")
    max_punkte_nr1 = input("Wie viel Punkte hat davon Aufgabe 1.? ")
    max_punkte_nr2 = input("Wie viel Punkte hat davon Aufgabe 2.? ")
    max_punkte_nr3 = input("Wie viel Punkte hat davon Aufgabe 3.? ")
    gesamt_punkte_inhalt = 0
    max_gesamt_punkte_inhalt = float(max_punkte_nr1) + float(max_punkte_nr2) + float(max_punkte_nr3)
    if max_gesamt_punkte_inhalt == 100:

        gewichtung_note_inhalt = input("Wie viele Prozent der Note enspricht der Inhalt? ")
        gewichtung_note_inhalt = float(gewichtung_note_inhalt) / 100
        gewichtung_note_form = input("Wie viele Prozent der Note enspricht die Form und Sprache? ")
        gewichtung_note_form = float(gewichtung_note_form) / 100
        max_gewichtung_note = float(gewichtung_note_inhalt) + float(gewichtung_note_form)
        if max_gewichtung_note == 1:
            
            frage1 = input("Möchten sie die schriftliche Note für eine Person ermitteln? (j/n) ")
            while frage1 == "j" or frage3=="j":
                name = input("Für wen sollen die schriftliche Note ermittelt werden? (Name) ")
                
                gesamt_punkte_nr1 = max_punkte_nr1      
                gesamt_punkte_nr1 = input("Wie viele Punkte bekommt " + name + " für Aufgabe 1. von " + gesamt_punkte_nr1 + " Punkten? ")
                gesamt_punkte_inhalt = float(gesamt_punkte_inhalt) + float(gesamt_punkte_nr1)
                gesamt_punkte_nr2 = max_punkte_nr2   
                gesamt_punkte_nr2 = input("Wie viele Punkte bekommt " + name + " für Aufgabe 2. von " + gesamt_punkte_nr2 + " Punkten? ")
                gesamt_punkte_inhalt = float(gesamt_punkte_inhalt) + float(gesamt_punkte_nr2)
                gesamt_punkte_nr3 = max_punkte_nr3 
                gesamt_punkte_nr3 = input("Wie viele Punkte bekommt " + name + " für Aufgabe 3. von " + gesamt_punkte_nr3 + " Punkten? ")
                gesamt_punkte_inhalt = float(gesamt_punkte_inhalt) + float(gesamt_punkte_nr3)
                notenpunkte_gesamt_inhalt = rechner_notenpunkte(float(gesamt_punkte_inhalt))
                gesamt_note_inhalt = (17 - int(notenpunkte_gesamt_inhalt)) / 3

                print("Es gibt für die Form und Sprache maximal 100 Punkte.")
                gesamt_punkte_form = input("Wie viele Punkte bekommt " + name + " für Form und Sprache? ")
                notenpunkte_gesamt_form = rechner_notenpunkte(float(gesamt_punkte_form))
                note_gesamt_form = (17 - int(notenpunkte_gesamt_form)) / 3

                note_gesamt = (float(gesamt_note_inhalt) * float(gewichtung_note_inhalt)) + (float(note_gesamt_form) * float(gewichtung_note_form))
                frage2 = input("Soll das Ergebnis in Notenpunkten oder Noten dargestellt werden? (NP/N) ")
                if frage2 == "NP" or frage2 == "Notenpunkte":
                    notenpunkte_gesamt = -(float(note_gesamt) * 3 - 17) 
                    notenliste.append([name, notenpunkte_gesamt, " NP"])
                    print(name,", ", notenpunkte_gesamt ," NP")
                elif frage2 == "N" or frage2 == "Noten":
                    notenliste.append([name, note_gesamt])
                    print(name, ", " ,note_gesamt)
                frage3 = input("Möchten sie die Note für noch eine Person ermitteln? (j/n) ")

            if frage3 == "n":
                frage4 = input("Möchten sie die Notenliste anzeigen? (j/n) ")
                if frage4 == "j":
                    print(notenliste)
                elif frage4 == "n":
                    print(" ")

        elif max_gewichtung_note != 1:
            print("Error, bitte beachten, dass die Gewichtung zusammen 100 Prozent ergeben muss!")

    elif max_gesamt_punkte_inhalt != 100:
      print("Error, bitte beachten, dass alle 3 Aufgaben zusammen 100 Punkte ergeben müssen!")
    


elif frage0=="at" or frage0=="AT-Noten":
    
    gewichtung_note_muendlich = input("Wie viele Prozent der Note enspricht die mündliche Note? ")
    gewichtung_note_muendlich = float(gewichtung_note_muendlich) / 100
    gewichtung_note_andere = input("Wie viele Prozent der Note ensprechen andere Arbeiten wie z.B. Tests? ")
    gewichtung_note_andere = float(gewichtung_note_andere) / 100
    max_gewichtung_note = float(gewichtung_note_andere) + float(gewichtung_note_muendlich)

    max_aktive = 10
    max_passive = 10
    max_qualitaet = 10
    max_team = 10
    max_fachsprache = 10
    max_gesamt_punkte=50
    gesamt_punkte_muendlich = 0

    if max_gewichtung_note == 1:
        frage01 = input("Möchten sie die AT-Note für eine Person ermitteln? (j/n) ")
        while frage01 == "j":
            name = input("Für wen sollen die AT-Note ermittelt werden? (Name) ")
            
            aktive=max_aktive 
            aktive=input("Wie viele Punkte bekommt " + name + " für aktive Mitarbeit von " + aktive + " Punkten? ")
            gesamt_punkte_muendlich=float(gesamt_punkte_muendlich) + float(aktive)
            passive=max_passive
            passive=input("Wie viele Punkte bekommt " + name + " für passive Mitarbeit von " + passive+ " Punkten? ")
            gesamt_punkte_muendlich=float(gesamt_punkte_muendlich) + float(passive)
            qualitaet=max_qualitaet
            qualitaet=input("Wie viele Punkte bekommt " + name + " für Qualität der Beiträge von " + qualitaet + " Punkten? ")
            gesamt_punkte_muendlich=float(gesamt_punkte_muendlich) + float(qualitaet)
            team=max_team 
            team=input("Wie viele Punkte bekommt " + name + " für Mitarbeit im Team von " + team + " Punkten? ")
            gesamt_punkte_muendlich=float(gesamt_punkte_muendlich) + float(team)
            fachsprache=max_fachsprache
            fachsprache=input("Wie viele Punkte bekommt " + name + " für Fachsprache von " + fachsprache + " Punkten? ")
            gesamt_punkte_muendlich=float(gesamt_punkte_muendlich) + float(fachsprache)
            gesamt_punkte_muendlich = float(gesamt_punkte_muendlich)*(100/gesamt_punkte_muendlich)
            
            notenpunkte_gesamt_muendlich = rechner_notenpunkte(float(gesamt_punkte_muendlich))
            gesamt_note_muendlich = (17 - int(notenpunkte_gesamt_muendlich)) / 3

            gesamt_punkte_andere=0
            frage02 = input("Möchten sie andere Noten wie z.B Tests hinzufügen? (j/n) ")
            if frage02 == "j":
                frage03 = input("Wie viele Noten möchten sie hinzufügen")
                anzahl_noten_andere = frage03
                for i in range(anzahl_noten_andere):
                    print("Jeder andere schriftliche Arbeit hat maximal 20 Punkte")
                    max_punkte_andere=20*anzahl_noten_andere
                    frage04 = input("Wie viele Punkte bekommt " + name + " ? " )
                    gesamt_punkte_andere=gesamt_punkte_andere+frage04

                gesamt_punkte_andere=(100/max_punkte_andere)*gesamt_punkte_andere
                notenpunkte_gesamt_andere = rechner_notenpunkte(float(gesamt_punkte_andere))
                gesamt_note_andere = (17 - int(notenpunkte_gesamt_andere)) / 3

                note_gesamt_at = (float(gesamt_note_muendlich) * float(gewichtung_note_muendlich)) + (float(gesamt_note_andere) * float(gewichtung_note_andere))
                frage2 = input("Soll das Ergebnis in Notenpunkten oder Noten dargestellt werden? (NP/N) ")
                if frage2 == "NP" or frage2 == "Notenpunkte":
                    notenpunkte_gesamt_at = -(float(note_gesamt_at) * 3 - 17) 
                    notenliste.append([name, notenpunkte_gesamt_at, " NP"])
                    print(name,", ", notenpunkte_gesamt_at ," NP")
                elif frage2 == "N" or frage2 == "Noten":
                    notenliste.append([name, note_gesamt_at])
                    print(name, ", " ,note_gesamt_at)
                frage3 = input("Möchten sie die Note für noch eine Person ermitteln? (j/n) ")

    elif max_gewichtung_note != 1:
            print("Error, bitte beachten, dass die Gewichtung zusammen 100 Prozent ergeben muss!")

    if frage3 == "n":
        frage4 = input("Möchten sie die Notenliste anzeigen? (j/n) ")
        if frage4 == "j":
            print(notenliste)
        elif frage4 == "n":
            print(" ")