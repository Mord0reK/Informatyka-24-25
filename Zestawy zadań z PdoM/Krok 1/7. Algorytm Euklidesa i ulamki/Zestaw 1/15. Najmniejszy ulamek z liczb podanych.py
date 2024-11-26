# Wersja 1

podane = []

for i in range(5):
    podane.append(int(input("Podaj liczbę: ")))

print("Najmniejszy możliwy ulamek z podanych liczb: ", min(podane), "/", max(podane))

# Wersja 2

a = int(input("Podaj liczbę: "))
b = int(input("Podaj liczbę: "))
c = int(input("Podaj liczbę: "))
d = int(input("Podaj liczbę: "))
e = int(input("Podaj liczbę: "))

licznik = min(a,b,c,d,e)
mianownik = max(a,b,c,d,e)

print("Najmniejszy możliwy ulamek z podanych liczb: ", licznik, "/", mianownik)