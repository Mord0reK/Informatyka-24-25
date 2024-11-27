def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input("Podaj liczbę bombek w pudełku z dużymi bombkami: "))
m = int(input("Podaj liczbę bombek w pudełku z małymi bombkami: "))

nww = (n * m) // nwd(n, m)

# Minimalna liczba pudełek z dużymi i małymi bombkami
duze = nww // n
male = nww // m


print(f"Minimalna liczba pudełek: dużych - {duze}, małych - {male}")
