import json
import os

FILENAME = "students.json"


# Файлдан оқу
def load_students():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


# Файлға сақтау
def save_students(students):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)


# Студент қосу
def add_student(students):
    while True:
        name = input("Аты-жөні: ").strip()
        if name:
            break
        print("Қате! Аты бос болмауы керек.")

    while True:
        try:
            age = int(input("Жасы: "))
            if age > 0:
                break
            print("Қате! Жас теріс немесе 0 болмауы керек.")
        except ValueError:
            print("Қате! Сан енгізіңіз.")

    while True:
        try:
            grade = float(input("Бағасы: "))
            if 0 <= grade <= 100:
                break
            print("Қате! Баға 0 мен 100 аралығында болуы керек.")
        except ValueError:
            print("Қате! Сан енгізіңіз.")

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)
    save_students(students)

    print("\nСтудент сәтті қосылды!\n")


# Студенттер тізімі
def show_students(students):
    if not students:
        print("\nСтуденттер тізімі бос.\n")
        return

    print("\n===== Студенттер тізімі =====")
    for i, student in enumerate(students, start=1):
        print(
            f"{i}. {student['name']} | Жасы: {student['age']} | Бағасы: {student['grade']}"
        )
    print()


# Статистика
def show_statistics(students):
    if not students:
        print("\nСтатистика үшін мәлімет жоқ.\n")
        return

    total_students = len(students)

    average_grade = sum(student["grade"] for student in students) / total_students

    best_student = max(students, key=lambda x: x["grade"])

    print("\n===== Статистика =====")
    print(f"Студенттер саны: {total_students}")
    print(f"Орташа баға: {average_grade:.2f}")
    print("\nЕң жоғары баға:")
    print(f"{best_student['name']} - {best_student['grade']}\n")


# Негізгі бағдарлама
def main():
    students = load_students()

    while True:
        print("===== Студенттер базасы =====")
        print("1. Студент қосу")
        print("2. Студенттер тізімін көру")
        print("3. Статистика")
        print("0. Шығу")

        choice = input("Таңдауыңыз: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            show_statistics(students)
        elif choice == "0":
            print("Бағдарлама аяқталды.")
            break
        else:
            print("Қате таңдау!\n")


if __name__ == "__main__":
    main()
з