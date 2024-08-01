def zapisz_do_pliku(imie, nazwisko):
    with open('imiona.txt', 'a') as plik:
        plik.write(f"{imie} {nazwisko}\n")

def zapisz_imiona():
    while True:
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        zapisz_do_pliku(imie, nazwisko)
        print(f"Dodano {imie} {nazwisko} do pliku.")

        kontynuuj = input("Czy chcesz dodać kolejne imię i nazwisko? (t/n): ")
        if kontynuuj.lower() != 't':
            break

def numeruj_imiona():
    with open('imiona.txt', 'r') as plik:
        imiona = plik.readlines()

    with open('imiona.txt', 'w') as plik:
        for i, imie in enumerate(imiona, 1):
            plik.write(f"{i}. {imie}")

if __name__ == "__main__":
    zapisz_imiona()
    numeruj_imiona()
