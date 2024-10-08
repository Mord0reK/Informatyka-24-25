#tego nowaka to chyba kule bija tyle tego jest 
def ciag_e(n):
    iloczyn = 1
    for i in range(1, n + 1):
        wyraz = (-1) ** (i + 1) * (4 * i - 1)
        iloczyn *= wyraz
    return iloczyn

# Przykładowe użycie
n = int(input("Podaj n: "))
print("Iloczyn pierwszych", n, "wyrazów ciągu e):", ciag_e(n))
