from datetime import datetime

san = 0

while True:
    print("\n===== Конвертер =====")
    print("1. Км -> М")
    print("2. М -> Км")
    print("3. Кг -> Г")
    print("4. Г -> Кг")
    print("5. C -> F")
    print("6. F -> C")
    print("0. Шығу")

    tandau = input("Таңдау: ")

    if tandau == "1":
        km = float(input("Км енгізіңіз: "))
        m = km * 1000
        print(f"{km} км = {m} м")
        san += 1

    elif tandau == "2":
        m = float(input("М енгізіңіз: "))
        km = m / 1000
        print(f"{m} м = {km} км")
        san += 1

    elif tandau == "3":
        kg = float(input("Кг енгізіңіз: "))
        g = kg * 1000
        print(f"{kg} кг = {g} г")
        san += 1

    elif tandau == "4":
        g = float(input("Г енгізіңіз: "))
        kg = g / 1000
        print(f"{g} г = {kg} кг")
        san += 1

    elif tandau == "5":
        c = float(input("°C енгізіңіз: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {f}°F")
        san += 1

    elif tandau == "6":
        f = float(input("°F енгізіңіз: "))
        c = (f - 32) * 5/9
        print(f"{f}°F = {c:.2f}°C")
        san += 1

    elif tandau == "0":
        print("\nБағдарлама аяқталды.")
        print("Жалпы орындалған конвертация саны:", san)
        break

    else:
        print("Қате таңдау!")
        continue

    print("Уақыты:")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))