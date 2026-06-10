from tkinter import *
from tkinter import messagebox

def esepteu():
    try:
        san = float(entry.get())
        kvadrat = san ** 2
        kub = san ** 3

        natizhe.config(text=f"Квадраты: {kvadrat}\nКубы: {kub}")

    except ValueError:
        natizhe.config(text="Қате: Сан енгізіңіз!")
        messagebox.showerror("Қате", "Сан енгізіңіз!")

window = Tk()
window.title("Санның квадраты мен кубын есептеу")
window.geometry("300x200")

Label(window, text="Санды енгізіңіз:").pack(pady=5)

entry = Entry(window)
entry.pack(pady=5)

Button(window, text="Есептеу", command=esepteu).pack(pady=10)

natizhe = Label(window, text="Нәтиже:")
natizhe.pack(pady=10)

window.mainloop() з