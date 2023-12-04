#Python script som leser innholdet i en fil og hasher innholder ved hjelp av SHA256-algoritmen.
#Den vil opprette en ny tekstfil og lagre hash verdien i den nye filen.

#Importerer nødvendig bibliotek.
import hashlib

# Åpner filen for lesing. Filen ligger på samme sted som der skriptet kjører.
fil = open('SHA256-Generator-Reader\sha256lisens.txt', 'rb')
filinnhold = fil.read()
fil.close()

# Generer en hash av filinnholdet.
hash = hashlib.sha256(filinnhold).hexdigest()

# Oppretter en ny fil og skriver hashen til filen.
hashfil = open('SHA256-Generator-Reader\hashetsha256lisens.txt', 'w')
hashfil.write(hash)
hashfil.close()