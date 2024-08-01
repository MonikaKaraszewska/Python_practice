import string

text19 = "hallo world of python"
text_German = "Python unterstützt mehrere Programmierparadigmen, z. B. die objektorientierte, die aspektorientierte und die funktionale Programmierung."

def counting_letters(text):
    text = text.upper()
    text = text.replace(' ', '')
    lista = []
    alfabet = string.ascii_uppercase
    for i in alfabet:
        ilosc = text.count(i)
        # print(f"{i} : {ilosc}")
        lista.append(ilosc)
    return lista

# procent = (ilosc/ len_text) *100
# return procent, i

print(counting_letters(text_German))



def language(text):
    result = counting_letters(text)
    text = text.replace(' ', '')
    len_text = len(text)
    procent_E = (result[4] / len_text)  * 100
    procent_0 = (result[14] / len_text)  * 100
    procent_T = (result[19] / len_text) * 100

    if procent_E >= 12.702:
        print(f"german 'E' = {procent_E}")
    else:
        print(f"english 'E' = {procent_E}")
    if procent_0 <= 7.507:
        print(f"german 'O' = {procent_0}")
    else:
        print(f"english 'O' = {procent_0}")

    if procent_T <= 6.15:
        print(f"german 'T' = {procent_T}")
    else:
        print(f"english 'T' = {procent_T}")

language(text_German)
language("Nach viel Widerspruch gegen den vermeldeten Fund des Moleküls Phosphin (PH3) in der Atmosphäre der Venus kommt nun Unterstützung aus unerwarteter Richtung: Eine 1978 durch die Atmosphäre des Planeten geflogene NASA-Sonde hat damals Spuren des Moleküls gefunden, haben Forscher bei einer Analyse der längst archivierten Daten herausgefunden. Damit liefern sie eine erste unabhängige Bestätigung des Sensationsfunds und dürften die Kontroverse neu entfachen. Immerhin hatte es geheissen, dass das Molekül auf nicht-biologischem Weg dort nicht entstehen dürfte. Ausser Phosphin wurden nun auch Hinweise auf andere biologisch relevante Chemikalien gefunden.")
