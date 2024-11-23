import math

def generuj_liczby_pierwsze(limit):
    sito = [True] * (limit + 1)
    sito[0] = sito[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sito[i]:
            for j in range(i * i, limit + 1, i):
                sito[j] = False
    return [x for x in range(2, limit + 1) if sito[x]]


def znajdz_maksymalny_iloczyn(maks_wartosc):
    limit = int(math.sqrt(maks_wartosc)) + 1
    liczby_pierwsze = generuj_liczby_pierwsze(limit)
    maks_iloczyn = 0
    para_liczb = (0, 0)

    # Szukamy największego możliwego iloczynu
    for i in range(len(liczby_pierwsze)):
        for j in range(i, len(liczby_pierwsze)):
            iloczyn = liczby_pierwsze[i] * liczby_pierwsze[j]
            if iloczyn < maks_wartosc and iloczyn > maks_iloczyn:
                maks_iloczyn = iloczyn
                para_liczb = (liczby_pierwsze[i], liczby_pierwsze[j])

    return maks_iloczyn, para_liczb


# Maksymalna wartość
maks_wartosc = 2_000_000_000
wynik, para = znajdz_maksymalny_iloczyn(maks_wartosc)

print(f"Największa liczba mniejsza niż 2 000 000 000 będąca iloczynem dwóch liczb pierwszych to: {wynik}")
print(f"Jest to iloczyn liczb pierwszych: {para[0]} i {para[1]}")
