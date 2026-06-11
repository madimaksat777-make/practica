from datetime import datetime

LOG_FILE = "log.txt"

# Атын тексеру
while True:
    name = input("Атыңыз: ").strip()
    if name:
        break
    print("Қате! Аты бос болмауы керек.")

# Жасты тексеру
while True:
    age = input("Жасыңыз: ").strip()

    if not age.isdigit():
        print("Қате! Жас тек сан болуы керек.")
        continue

    age = int(age)

    if age < 0:
        print("Қате! Жас теріс болмауы керек.")
        continue

    break

# Қаланы енгізу
city = input("Қалаңыз: ").strip()

# Экранға шығару
print("\n===== Пайдаланушы мәліметтері =====")
print(f"Аты: {name}")
print(f"Жасы: {age}")
print(f"Қаласы: {city}")

# Логқа жазу
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(LOG_FILE, "a", encoding="utf-8") as file:
    file.write(f"[{current_time}]\n")
    file.write("Пайдаланушы тіркелді\n")
    file.write(f"Аты: {name}\n")
    file.write(f"Жасы: {age}\n")
    file.write(f"Қаласы: {city}\n")
    file.write("-" * 30 + "\n")

# Статистика
with open(LOG_FILE, "r", encoding="utf-8") as file:
    lines = file.readlines()

user_count = 0
last_name = ""
last_time = ""

for i, line in enumerate(lines):
    if line.startswith("["):
        last_time = line.strip("[]\n")

    if line.startswith("Аты:"):
        user_count += 1
        last_name = line.replace("Аты:", "").strip()

print("\n===== Статистика =====")
print(f"Тіркелген пайдаланушылар саны: {user_count}")
print("Соңғы пайдаланушы:")
print(f"Аты: {last_name}")
print("Соңғы әрекет:")
print(last_time)