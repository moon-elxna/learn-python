
class Smartphone():
    def __init__(self, marke, baujahr, farbe_gehaeuse, farbe_handyhuelle , display_groesse_px, display_groesse_zoll , display , akku, akku_kapazitaet , betriebssytem, sperrbildschirm_hintergrund, startbildschirm_hintergrund):
        self.marke = marke
        self.baujahr = baujahr 
        self.farbe_gehaeuse = farbe_gehaeuse
        self.farbe_handyhuelle = farbe_handyhuelle 
        self.display_groesse_px = display_groesse_px
        self.display_groesse_zoll = display_groesse_zoll
        self.display = display
        self.akku = akku
        self.akku_kapazitaet = akku_kapazitaet 
        self.betriebssytem = betriebssytem
        self.sperrbildschirm_hintergrund = sperrbildschirm_hintergrund
        self.startbildschirm_hintergrund = startbildschirm_hintergrund
    
    def aendern_farbe_gehaeuse(self, neue_farbe_gehaeuse):
        print("Die Farbe des Gehaeuses war " + self.farbe_gehaeuse + " und wird zu " + neue_farbe_gehaeuse + " geaendert.")
        self.farbe_gehaeuse = neue_farbe_gehaeuse
    def aendern_farbe_handyhuelle(self, neue_farbe_handyhuelle):
        print("Die Handyhuelle war " + self.farbe_handyhuelle + " und wird jetzt zu " + neue_farbe_handyhuelle + " geaendert." )
        self.farbe_handyhuelle = neue_farbe_handyhuelle
    def aufladen_akku(self, akku_stand, akku_zustand ):
        print("Der Akku wird von " + akku_stand + " auf " + akku_zustand + " aufgeladen.")
        #akku kan bisher nur auf 100% = 5000mAh aufgeladen werden; ??? Schleife einfügen um akku auf addieren zu können
    def aendern_akku(self, akku_zustand):
        print("Der Akku wurde ausgewechselt und hat jetzt wieder eine Kapazität von " + self.akku_kapazitaet + " anstatt " + akku_zustand + " beim alten Akku.") 
    def aendern_display(self):
        print("Das Display wurde wurde zu einem gleich grossen Display von " + self.display_groesse_px + " ausgewechselt.")
    def aendern_betriebssytem(self, betriebssytem):
        pass
    def aendern_sperrbildschirm_hintergrund(self, neue_sperrbildschirm_hintergrund):
        print("Der Sperrbildschirm Hintergrund wird von " + self.sperrbildschirm_hintergrund + " zu " + neue_sperrbildschirm_hintergrund + " gewechselt.")
        self.sperrbildschirm_hintergrund = neue_sperrbildschirm_hintergrund
    def aendern_startbildschirm_hintergrund(self, neue_startbildschirm_hintergrund ):
        print("Der Startbildschirm Hintergrund wird von " + self.startbildschirm_hintergrund + " zu " + neue_startbildschirm_hintergrund + " gewechselt.")
        self.startbildschirm_hintergrund = neue_startbildschirm_hintergrund
    def aendern_sperrbildschirm_hintergrund_und_starbildschirm_hintergrund(self, neue_sperrbildschirm_hintergrund_und_starbildschirm_hintergrund ):
        print("Der Sperr- und Startbildschirm Hintergrund wird von " + self.sperrbildschirm_hintergrund + " und " + self.startbildschirm_hintergrund+ " zu " + neue_sperrbildschirm_hintergrund_und_starbildschirm_hintergrund + " gewechselt.")
        self.sperrbildschirm_hintergrund_und_starbildschirm_hintergrund = neue_sperrbildschirm_hintergrund_und_starbildschirm_hintergrund

meinSmartphone = Smartphone("Xiaomi", "2023", "hellblau", "transparent", "2400 x 1080px", "6,67in","" ,"AMOLED", "5000 mAh", "Android", "Bild x", "Bild y")

altesSmartphone = Smartphone("Samsung", "2018", "grau", "lila", "1440 x 2960 px", "5,8in", "AMOLED","" ,"3000 mAh", "Android", "Bild z", "Bild a")




print(" ")
meinSmartphone.aendern_farbe_gehaeuse(altesSmartphone.farbe_gehaeuse)
print(" ")
meinSmartphone.aendern_farbe_handyhuelle("blau")
print(" ")
meinSmartphone.aufladen_akku("2000 mAh", "4650 mAh")
print(" ")
meinSmartphone.aendern_akku ("4650 mAh")
print(" ")
meinSmartphone.aendern_display()
print(" ")
meinSmartphone.aendern_sperrbildschirm_hintergrund(altesSmartphone.sperrbildschirm_hintergrund)
print(" ")
meinSmartphone.aendern_sperrbildschirm_hintergrund_und_starbildschirm_hintergrund("Bild xyz")
print(" ")
