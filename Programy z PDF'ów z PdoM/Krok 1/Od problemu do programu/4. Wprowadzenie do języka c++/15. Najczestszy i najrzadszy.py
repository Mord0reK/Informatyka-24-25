def f(lista):
    frequency = {}

    for num in lista:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_frequency = max(frequency.values())
    min_frequency = min(frequency.values())

    most_frequent = [key for key in frequency if frequency[key] == max_frequency]
    least_frequent = [key for key in frequency if frequency[key] == min_frequency]

    if len(most_frequent) == 1:
        print(f"Najczęściej występujący element: {most_frequent[0]}")
    else:
        print("Brak jednoznacznego najczęściej występującego elementu.")

    if len(least_frequent) == 1:
        print(f"Najrzadziej występujący element: {least_frequent[0]}")
    else:
        print("Brak jednoznacznego najrzadziej występującego elementu.")

lista = []

print("Podaj 15 liczb całkowitych:")
for i in range(15):
    number = int(input(f"Podaj liczbę {i+1}: "))
    lista.append(number)

f(lista)
