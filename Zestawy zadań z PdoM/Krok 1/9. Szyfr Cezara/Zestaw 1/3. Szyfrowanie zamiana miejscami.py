def szyfrowanie(tekst):
    for i in range(0, len(tekst), 2):
        print(tekst[i + 1], end="")
        print(tekst[i], end="")

def odszyfrowanie(tekst):
    for i in range(1, len(tekst), 2):
        print(tekst[i], end="")
        print(tekst[i - 1], end="")

tekst = str(input("Podaj tekst: "))
wybor = int(input("Co chcesz zrobić z tym tekstem, Zaszyfrować (1) czy odszyfrować (2): "))

if wybor == 1:
    print("Tekst zaszyfrowany: ")
    szyfrowanie(tekst)
else:
    print("Tekst odszyfrowany: ")
    odszyfrowanie(tekst)