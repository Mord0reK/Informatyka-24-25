# Ciągi liczbowe A i B oraz wartość x
A = [2, 3, 7, 8, 11, 12, 15, 18, 20]
B = [1, 4, 5, 6, 9, 10, 13, 17, 21]
x = 27

# Szukanie pary liczb, których suma wynosi x
i = 0  # Indeks dla A
j = len(B) - 1  # Indeks dla B

while i < len(A) and j >= 0:
    suma = A[i] + B[j]
    
    if suma == x:
        print(f"Znaleziono: {A[i]} + {B[j]} = {x}")
        break
    elif suma < x:
        i += 1  # Przesuwamy się w prawo w A
    else:
        j -= 1  # Przesuwamy się w lewo w B
