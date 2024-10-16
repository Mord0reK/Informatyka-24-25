#Napisz program przechowujący w strukturze listy kwadraty 100 kolejnych liczb naturalnych. Elementem listy o
#indeksie 0 powinna być liczba 0, elementem o indeksie 1 – liczba 1, elementem o indeksie 2 – liczba 4,
#elementem o indeksie 3 – liczba 9 itd.

kwadraty = [i ** 2 for i in range(100)]
print("Kwadraty 100 kolejnych liczb naturalnych:", kwadraty)
