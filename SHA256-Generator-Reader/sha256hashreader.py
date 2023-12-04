#Python script som leser innholdet i en fil og verifiserer filintegriteten.
#Den vil opprette en ny tekstfil og lagre hash verdien i den nye filen.

#import hashlib

# Åpner filen for lesing. Filen ligger på samme sted som der skriptet kjører.
fil = open('sha256lisens.txt', 'rb')
filinnhold = fil.read()
fil.close()

# Generer en hash av filinnholdet.
nyhash = hashlib.sha256(filinnhold).hexdigest()

# Leser av hash filen.
hashfil = open('hashetsha256lisens.txt', 'r')
gammelhash = hashfil.read()
hashfil.close()

# Printer ut informasjon til terminalen basert på om det er en endring eller ikke.
if nyhash == gammelhash:
    print("Ingen endring.")
else:
    print("Filen har endringer.")