a = int(input("Podaj pierwszy wiek: "))
b = int(input("Podaj drugi wiek: "))

if a > b:
    x = a // b
    print("Drugi wiek mieści się ", x , "raz-y w pierwszym wieku")
else:
    x = b // a
    print("Drugi wiek mieści się ", x , "raz-y w pierwszym wieku")