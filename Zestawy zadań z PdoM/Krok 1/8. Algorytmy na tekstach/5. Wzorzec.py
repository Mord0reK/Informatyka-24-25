wyrazy = []

wzorzec = str(input("Podaj wzorzec: "))

wyraz = str(input("Podaj wyraz: "))

while wyraz != "***":
    wyrazy.append(wzorzec)
    wyraz = str(input("Podaj wyraz: "))

print("Wzorzec powtórzył się", wyrazy.count(wzorzec), "razy.")