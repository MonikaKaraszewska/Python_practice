
# bill = float(input("Wysokosc rachunku: "))
# procentTip = float(input("Ile procent napiwku: "))
#
# tip = float(bill * procentTip) /100
#
# calyRachunek = round(bill +tip,2)
# print("Do zapłaty właczajac napiwek: ", calyRachunek)

bill = float(input("Wysokosc rachunku: "))
procentTip = float(input("Ile procent napiwku: "))
def percentage(bill, procentTip):
    tip = bill * procentTip / 100
    return bill + tip


print(percentage(bill, procentTip))



