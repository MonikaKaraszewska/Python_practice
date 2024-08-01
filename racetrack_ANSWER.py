#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 18:57:22 2022

@author: stme
"""

import random

racetrack = []  # leeres Spielbrett

for i in range(30):  # Erstellt das Spielbrett mit 30 Feldern
    n = random.randint(0, 3)
    racetrack.append(n)
print("lista: ", racetrack)
print(len(racetrack))
user_pos = 0
computer_pos = 0

while user_pos < 30 and computer_pos < 30:
    # Ausgabe Spielbrett
    line = " " * user_pos * 2  # Ausgabe Spieler
    line += "U"

    print(line)

    line = " " * computer_pos * 2  # Ausgabe Computer
    line += "C"

    print(line)

    line = ""  # Ausgabe des Racetracks
    for e in racetrack:
        line += str(e) + "|"

    line = line[:-1]

    print(line)

    # Spiellogik
    answer = input("Münze(1) oder Feld(2): ")
    if answer == "1":  # Münzwurf Spieler
        points_user = random.randint(1, 2)
    else:  # Feld Spieler
        points_user = racetrack[user_pos]

    points_computer = random.randint(1, 2)  # Münzwurf Computer

    user_pos += points_user
    computer_pos += points_computer

if user_pos > computer_pos:  # Ausgabe Sieg/Niederlage
    print("User wins")
elif user_pos < computer_pos:
    print("Computer wins")
else:
    print("Tie")
