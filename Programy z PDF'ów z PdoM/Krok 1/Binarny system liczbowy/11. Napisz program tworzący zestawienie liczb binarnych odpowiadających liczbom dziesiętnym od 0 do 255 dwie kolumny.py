#Napisz program tworzący zestawienie liczb binarnych odpowiadających liczbom dziesiętnym od 0 do 255.
#Efektem działania programu powinny być dwie kolumny: po lewej – liczby dziesiętne, a po prawej – liczby
#binarne

print("Liczba dziesiętna | Liczba binarna")
print("-------------------|---------------")
for i in range(256):
    print(f"{i:<17} | {bin(i)[2:]}")
