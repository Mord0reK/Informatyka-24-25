def upstring(s):
    return s.upper()

slowo = str(input("Podaj słowo: "))

if upstring(slowo) == upstring(slowo)[::-1]:
    print("Słowo jest palindromem")
else:
    print("Słowo nie jest palindromem")