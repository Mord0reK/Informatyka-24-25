def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def znajdz_liczby_bliźniacze(start, koniec):
    pary_blizniacze = []
    for liczba in range(start, koniec - 1):
        if czy_pierwsza(liczba) and czy_pierwsza(liczba + 2):
            pary_blizniacze.append((liczba, liczba + 2))
    return pary_blizniacze

pary_dwucyfrowe = znajdz_liczby_bliźniacze(10, 100)
pary_trzycyfrowe = znajdz_liczby_bliźniacze(100, 1000)

print("Pary liczb bliźniaczych dwucyfrowych:")
print(pary_dwucyfrowe)

print("Pary liczb bliźniaczych trzycyfrowych:")
print(pary_trzycyfrowe)
