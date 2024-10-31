def najdluzszy_palindrom(s):
    najdluzszy = ""

    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if substring == substring[::-1]:
                if len(substring) > len(najdluzszy):
                    najdluzszy = substring

    return najdluzszy

# Wczytanie słowa od użytkownika
slowo = input("Wprowadź słowo z wielkimi literami: ")
wynik = najdluzszy_palindrom(slowo.upper())

# Wyświetlenie wyniku
print("Najdłuższy palindrom w słowie:", wynik)
