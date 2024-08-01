
date = input("Bitte Geburtstag (dd.mm) eingeben: ")

day = int(date[0:2])
month = int(date[3:])

if day < 1 or day > 31 or month < 1 or month > 12:
    print("Fehler")

elif day >= 23 and month == 11  or  day <= 21 and month == 12:
    print("Sie sind Schütze")