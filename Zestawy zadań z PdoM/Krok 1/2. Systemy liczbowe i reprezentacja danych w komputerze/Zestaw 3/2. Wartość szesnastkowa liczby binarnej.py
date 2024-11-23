# Zapisz liczbę binarną 1000100111010000 w systemie szesnastkowym.

binarna = "1000100111010000"

hex = hex(int(binarna, 2))[2:]

print(hex.upper())