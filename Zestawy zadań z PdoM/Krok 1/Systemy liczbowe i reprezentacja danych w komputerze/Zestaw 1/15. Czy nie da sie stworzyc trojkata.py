def check_no_triangle(nums):
    n = len(nums)

    # Sprawdzenie wszystkich trójek liczb
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                x, y, z = nums[i], nums[j], nums[k]

                # Sprawdzamy, czy da się zbudować trójkąt
                if x + y <= z or x + z <= y or y + z <= x:
                    return True  # Znaleziono trójkę, która nie spełnia warunku

    return False  # Wszystkie trójki spełniają warunek


# Wczytanie liczb od użytkownika
n = int(input("Podaj liczbę elementów: "))
nums = []

for _ in range(n):
    num = int(input("Podaj liczbę: "))
    nums.append(num)

# Sprawdzenie, czy istnieje trójka, z której nie da się zbudować trójkąta
if check_no_triangle(nums):
    print("Istnieje trójka liczb, dla której nie można zbudować trójkąta.")
else:
    print("Nie ma takiej trójki liczb.")
