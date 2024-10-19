liczba = input("Podaj liczbe w systemie dziewiątkowym: ")

dziewiatkowy = liczba

trojkowa = ""

liczba = int(liczba, 9)


while liczba > 0:
    trojkowa = str(liczba % 3) + trojkowa
    liczba = liczba // 3

print("Liczba", dziewiatkowy, "zapisana w systemie trójkowym to: ",trojkowa)