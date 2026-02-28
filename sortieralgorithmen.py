# MERGESORT
# definieren Funktion merge_sort, Zerteilung der Liste (erste Teil des Mechanismus)
def merge_sort(a):
 # kontrolieren ob die Liste ein oder weniger Elemente hat, in dem Fall sortieren nicht möglich
    if len(a) <= 1:
        print("übrige Elemente: ", a)
        return a
    
    elif len(a) >= 1:
        # mitte einer Liste definieren als variable, Anzahl der Elemente geteilt durch zwei
        mid = len(a) // 2
        right = merge_sort(a[mid:]) #rechte Seite der Liste wird mit merge_sort funktion sortiert
        left = merge_sort(a[:mid]) #linke Seite der Liste wird mit merge_sort funktion sortiert
        print("geteilte rechte Seite: ", right, " geteilte linke Seite: ", left)
    #züruckgeben der liste rechts und links, wobei dafür die Funktion merge zur verschmelzen aufgerufen wird
    return merge(right, left) 
# definieren Funktion merge, Verschmelzung der Liste (zweite Teil des Mechanismus)
def merge(right, left):
    # Erstellung Liste für Sortierung
    sorted =  []
    # Index startet für Sortierung bei 0
    right_index = 0
    left_index = 0
    # überprüfen, bis alle Elemente der jewiligen Liste überprüft wurden(vgl. von Index und Anzahl der Elemente)
    while right_index < len(right) and left_index < len(left):
        # wenn das Element auf der Rechten Seite größer ist als das auf der Linke wird es zu linken Seite hinzugefügt
        if right[right_index] < left[left_index]:
            sorted.append(right[right_index])
            right_index += 1 # nächste Index für linke für nächste Überprüfung verwendet
        # wenn das Element auf der Linken Seite größer ist als das auf der Rechte wird es zu rechten Seite hinzugefügt
        elif right[right_index] > left[left_index]:
            sorted.append(left[left_index])
            left_index += 1 # nächste Index für rechts für nächste Übeerprüfung verwendet
        print("Rechte Index: ",right_index," Linke Index: ",left_index)
    # anfügen der restlichen Elemente der Liste zur zu sortierenden Liste
    sorted += left[left_index:]
    sorted += right[right_index:]
    print("sortierte rechte Seite: ", right, " sortierte linke Seite: ", left)
    return(sorted)

# BUBBLESORT
# definieren einer Funktion um den Bubblesort Algorithmus aufzurufen, wobei der Parameter a die zu sortierende Liste beschreibt 
def bubble_sort(a):
    # kontrolieren ob die Liste ein oder weniger Elemente hat, in dem Fall sortieren nicht möglich
    if len(a) <= 1:
        print("Die Liste muss mindestens zwei Elemente haben um sortiert zu werden.")
    elif len(a) >= 1:
        # um die zuvergleichenden Elemente aufzurufen, Definition einer Variable die nach jeder Schleife 
        # denn aufzurufenden Index verändert, sodass die Elemente nacheinader verglichen werden
        index_value1 = len(a) - (len(a)+1)
        index_value2 = len(a) - len(a) 
        lenght=len(a)-1
        # For-Schleife, wird benötigt um Index-Variablen nach jedem Durchlauf durch die ganze Liste zurückzusetzen
        for i in range(len(a)-1):
            # For-Schleife, durchläuft jeweils zwei Elemente aus der Liste, verleicht Sie und ändert bei Bedarf die Reihenfolge
            for i in range(lenght):
                # verändert jede Schleife jeweils die Index-Varaiblen, um jede Schleife auf das nächste Elemente zu zugreifen 
                index_value1 += 1
                index_value2 += 1
                # Ausgabe der Werte, zur Kontrolle des Algorithmus
                print("Index:", index_value1,"und", index_value2) 
                print("Elemente:", a[index_value1],"und", a[index_value2] )
                # Vergleich der zwei Elemente
                if a[index_value1]>a[index_value2] :  
                    temp_value = a[index_value1]  # temporäre Speicherung vom 1. Element
                    a[index_value1] = a[index_value2]  # überschreiben von dem Index von 1. Element durch 2. Element
                    a[index_value2] = temp_value  # überschreiben von dem Index von 2. Element durch temporäre Speicherung vom 1. Element
                print(a)
            #Index-Variablen werden nach jedem Durchlauf durch die Liste "zurückgesetzt" 
            index_value1 = len(a) - (len(a)+1)
            index_value2 = len(a) - len(a)
            # reduziert die Anzahl der zweiten For-Schleife jeden Durchlauf um eins
            lenght -=1
    return a  # die sortierte Liste wird zurückgegeben

input_list = input("Liste: ")
data = input_list.split()
input_question = input("Bubblesort oder Mergesort(B/M): ")
if input_question == "B":
    print("sortierte Liste:", bubble_sort(data))
elif input_question =="M":
     print("sortierte Liste:", merge_sort(data))


