def szyfrowanie(tekst):
    zaszyfrowany = ""
    for i in range(len(tekst)):
        zaszyfrowany = zaszyfrowany + chr(ord(tekst[i]) + 13)
    return zaszyfrowany

def odszyfrowanie(tekst):
    odszyfrowany = ("")
    for i in range(len(tekst)):
        odszyfrowany = odszyfrowany + chr(ord(tekst[i]) - 13)
    return odszyfrowany

tekst = str(input("Podaj tekst: "))
wybor = int(input("Co chcesz zrobić z tym tekstem, Zaszyfrować (1) czy odszyfrować (2): "))

if wybor == 1:
    print("Tekst zaszyfrowany: ", szyfrowanie(tekst))
else:
    print("Tekst odszyfrowany: ", odszyfrowanie(tekst))