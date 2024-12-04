def szyfrowanie(tekst):
    print(tekst[::-1])

def odszyfrowanie(tekst):
    print(tekst[::-1])

tekst = str(input("Podaj tekst: "))
wybor = int(input("Co chcesz zrobić z tym tekstem, Zaszyfrować (1) czy odszyfrować (2): "))

if wybor == 1:
    print("Tekst zaszyfrowany: ")
    szyfrowanie(tekst)
else:
    print("Tekst odszyfrowany: ")
    odszyfrowanie(tekst)