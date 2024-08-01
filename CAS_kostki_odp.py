# -*- coding: utf-8 -*-
"""
@author: stme
"""

import random

number_of_ones = 0
number_of_pairs = 0
number_of_following_pairs = 0
sum_numbers = 0

# In der folgenden Variable wird abgelegt, ob in der letzten Runde
# ein Paar gewürfelt wurde
last_roll_was_pair = False

# Würfelausgabe: Die Werte werden als Liste gespeichert und können
# über den Index gelesen werden (siehe Aufgabe "Wochentagsberechnung").
dices = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]

for i in range(1000):  # 1000 Runden

    d1 = int(random.uniform(1, 7))
    d2 = int(random.uniform(1, 7))

    print("Runde", str(i + 1) + ":", dices[d1 - 1], dices[d2 - 1])
    if d1 == 1:
        number_of_ones += 1
    if d2 == 1:
        number_of_ones += 1

    if d1 == d2:
        number_of_pairs += 1

        if last_roll_was_pair == True:
            number_of_following_pairs += 1
        # am Schluss Variable zurücksetzen damit es für die
        # nächste Runde stimmt
        last_roll_was_pair = True
    else:
        last_roll_was_pair = False  # Falls kein Paar -> zurücksetzen

    sum_numbers += d1 + d2

print("number of ones:", number_of_ones)
print("number of pairs:", number_of_pairs)
print("number of following pairs:", number_of_following_pairs)
# Average Number kann aus der Gesamtsumme (sum_numbers) durch
# 2000 (1000 Runden mit 2 Würfeln) berechnet werden
print("average number:", sum_numbers / (1000 * 2))