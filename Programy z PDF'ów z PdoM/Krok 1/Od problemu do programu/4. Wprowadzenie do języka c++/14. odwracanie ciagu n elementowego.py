def odwracanie(lista):
    lewo = 0
    prawo = len(lista) - 1

    # Zamieniamy elementy z lewej i prawej strony tablicy aż do środka
    while lewo < prawo:
        lista[lewo], lista[prawo] = lista[prawo], lista[lewo]
        lewo += 1
        prawo -= 1

# Pobieramy n i ciąg liczb od użytkownika
n = int(input("Podaj liczbę elementów w ciągu (n > 0): "))
lista = []

for i in range(n):
    element = float(input(f"Podaj element {i + 1}: "))
    lista.append(element)

print("Ciąg przed odwróceniem:", lista)

# Odwracamy ciąg
odwracanie(lista)

print("Ciąg po odwróceniu:", lista)
