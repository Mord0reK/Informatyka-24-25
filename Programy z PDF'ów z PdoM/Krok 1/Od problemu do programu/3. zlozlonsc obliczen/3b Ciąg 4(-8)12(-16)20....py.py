#Ciąg: 4⋅(−8)⋅12⋅(−16)⋅20⋅... w nazwie sie nie dalo dobrze tego zapisac
def ciag_b(n):
    iloczyn = 1
    for i in range(1, n + 1):
        wyraz = (-1) ** (i + 1) * 4 * i
        iloczyn *= wyraz
    return iloczyn

# Przykładowe użycie
n = int(input("Podaj n: "))
print("Iloczyn pierwszych", n, "wyrazów ciągu: ", ciag_b(n))
