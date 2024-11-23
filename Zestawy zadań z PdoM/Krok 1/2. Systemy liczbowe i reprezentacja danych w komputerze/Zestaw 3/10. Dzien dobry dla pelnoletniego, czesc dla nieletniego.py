# Napisz program, który wczyta imię i wiek wyrażony w latach, a następnie wypisze powitanie. Dla osoby
# pełnoletniej wypisze napis „Dzien dobry” i jej imię, a dla niepełnoletniej napis „Cześć” i jej imię

name = input("Podaj imię: ")
wiek = int(input("Podaj wiek (w latach): "))

if wiek > 18:
    print("Dzień dobry,", name)
else:
    print("Cześć,", name)
