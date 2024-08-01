q=0
question1  = input("What's your name? ")

if question1 != "Monika" or question1 != "Asia":
    print("incorrect")

else:
    print("correct")
    q+=1

question2 = input("czy chcesz sie uczyc pythona? ")
if question2 == 'Tak' or question2 == 'tak':
    print("correct")
    q+=1
else:
    print("worng annswer")


question3 = input("How many bits are there in one byte? ")
if question3 != '8':
    print("incorrect")

else:
    print("correct")
    q+=1
print(f"opdowiedziałes poprawnie na {q} pytan")
x=1
print("---------------------")
print ("przygotuj się teraz na niemożliwy quiz z niepotrzebnej wiedzy")
print("---------------------")
pyt1= input ("co zostało przez przypadek przygrzane przy wymyślaniu mikrofalówki?")
if pyt1 == "czekolada" or "Czekolada":
    print ("siadaj, pała.")
else:
    print ("brawo!")
    x+=1
pyt2= input ("co oznacza skrót STL?")
if pyt2 != "Standard Triangle Language" or "standard triangle language":
    print ("siadaj, pała.")
else:
    print ("brawo!")
    x+=1
pyt3= input ("jakie zwierzę zabija najwięcej ludzi rocznie?")
if pyt3 != "komar" or "Komar":
    print ("siadaj, pała.")
else:
    print ("brawo!")
    x+=1
pyt4= input ("ile palców mają koty?")
if pyt4 != "18":
    print ("siadaj, pała.")
else:
    print ("brawo!")
    x+=1
pyt5= input ("ile z mamy rolek po papierze toaletowym?")
if pyt5 != "75":
    print ("siadaj, pała. P.S. przegracie")
else:
    print ("brawo! P.S. przegracie")
    x+=1
print("---------------------")
print("twoja ocena:", x)