number = '''73167176531330624919225119674426574742355349194934969835203127745063262395783180169848018694788518438586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557668966489504452445231617318564030987111217223831136222989342338030813533627661428280644448664523874930358907296290491560440772390713810515859307960866701724271218839987979087922749219016997208880937766572733300105336788122023542180975125454059475224352584907711670556136048395864467063244157221553975369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474821663704844019989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'''


lista = []

for i in range(len(number)-3):
        suma = int(number[i]) * int(number[i+1]) * int(number[i+2])
        lista.append(suma)

print(max(lista))

print("......bez listy")
counter = 0

for i in range(0,len(number)-2):
    suma = int(number[i]) * int(number[i+1]) * int(number[i+2])
    if counter < suma:
        counter = suma

print(counter)