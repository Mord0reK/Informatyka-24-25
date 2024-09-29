masa = int(input("Podaj swoją masę ciała w kilogramach: "))
wysokość = int(input("Podaj swoją wysokość w centymetrach: "))

m = wysokość / 100

bmi = masa / (m * 2)

print("Twoje BMI wynosi: ", round(bmi, 2))