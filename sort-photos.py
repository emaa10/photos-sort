# Sorts files (also photos and videos) by time changed.
# Use by airdropping photos from iCloud from iPhone to mac
# If want to sort by month, remove %d in last if sequence


import os
import shutil
from datetime import datetime

# Pfad zum Ordner mit den Dateien
ordner_pfad = "/Users/emanuelberger/Desktop/test"

# Gehe durch jede Datei im Ordner
for datei_name in os.listdir(ordner_pfad):
    datei_pfad = os.path.join(ordner_pfad, datei_name)

    # Überprüfe, ob es sich um eine Datei handelt
    if os.path.isfile(datei_pfad):
        # Erhalte das Änderungsdatum der Datei
        datei_datum = datetime.fromtimestamp(os.path.getmtime(datei_pfad))
        
        # Erstelle den Unterordnerpfad mit dem Format "yyyy-mm-dd"
        unterordner_name = datei_datum.strftime("%Y-%m-%d")
        unterordner_pfad = os.path.join(ordner_pfad, unterordner_name)
        
        # Erstelle den Unterordner, falls er noch nicht existiert
        if not os.path.exists(unterordner_pfad):
            os.makedirs(unterordner_pfad)
        
        # Verschiebe die Datei in den entsprechenden Unterordner
        ziel_pfad = os.path.join(unterordner_pfad, datei_name)
        shutil.move(datei_pfad, ziel_pfad)
        print(f"Die Datei {datei_name} wurde nach {ziel_pfad} verschoben.")
