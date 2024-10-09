tekst = str(input("Podaj tekst: "))

wyrazy = tekst.split()

for i in range(len(wyrazy)):
    if len(wyrazy[i]) % 2 == 1 and wyrazy[i][0] == "p":
        print(wyrazy[i])