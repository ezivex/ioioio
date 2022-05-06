# importowanie:
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
from openpyxl import workbook, load_workbook
import os
import pandas as pd
# ==========================================
# ==========================================
# Funckje/klasy:
class Dane:
    def __init__(self):
        self.plikdane = []
        self.danenaglowki = []
        self.dowykresu = []

# --- Otwarcie pliku, zapisanie danych do klasy
def open():
    # initialdir="/"
    root.filename = filedialog.askopenfilename(initialdir="/", title="select a file", filetypes=(
        ("xlsx files", "*.xlsx"), ("txt files", "*.txt"), ("all type", "*.*")))
    wpisywanieplikow.delete(0, "end")
    wpisywanieplikow.insert(0, root.filename)
    # zapisanie danych do zmiennej w klasie:
    new2.plikdane = pd.read_excel(wpisywanieplikow.get())
    # zapisanie nazw naglowkow do zmiennej w klasie
    new2.danenaglowki = new2.plikdane.columns
    # wyswietlenie tych danych
    niewiem = Label(root, text=new2.plikdane)
    niewiem.pack()
    print(new2.danenaglowki)
    print(len(new2.danenaglowki))
    xdd2()
# ---
def funkcja_start():

    if varpdf.get() and (var1.get() or var2.get() or var3.get()):
        # generuj plik pdf z wynikami.
        print("Generuj PDF")
    elif (var1.get() or var2.get() or var3.get()) and wpisywanieplikow.get():
        podglad = Toplevel()
        if var1.get():
            wykres()
        if var2.get():
            komunikat2 = Label(podglad, text="var2. Mediana")
            komunikat2.pack()
        if var3.get():
            komunikat3 = Label(podglad, text="var3. srednia")
            komunikat3.pack()
    else:
        print("Zaznacz jakies opcje ")
# ---
def xdd2():
    clicked1 = StringVar()
    clicked2 = StringVar()

    clicked1.set(new2.danenaglowki[0])
    clicked2.set(new2.danenaglowki[1])

    drop1 = OptionMenu(root, clicked1, *new2.danenaglowki)
    drop2 = OptionMenu(root, clicked2, *new2.danenaglowki)
    drop1.pack()
    drop2.pack()
    a1 = clicked1.get()
    a2 = clicked2.get()
    print("Naglowek_1 " + clicked1.get())
    print("Naglowek_2 " + clicked2.get())
    drop_przycisk = Button(root, text="zapisz", command=lambda: test(clicked1.get(), clicked2.get()))
    drop_przycisk.pack()
# ---
def test(a, b):
    print("zapisano")
    new2.dowykresu = [a, b]
    for i in range(0, len(new2.dowykresu)):
        print("co zostalo klikniete: " + str(new2.dowykresu[i]))

def wykres():
    x1 = new2.dowykresu[0]
    y1 = new2.dowykresu[1]
    # print(x1 + " " + y1)
    new2.plikdane.plot(x=x1, y=y1)
    plt.show()


# df = pd.read_csv(r'https://analityk.edu.pl/wp-content/uploads/2020/12/data.csv')
# df['date'] = pd.to_datetime(df.date, format='%d/%m/%Y')
# x=df['date']
# y=df['Close']
# plt.plot(x,y)

# df.plot(x='date',y='Close', legend=False)

# ==========================================
# ==========================================
# MAIN:
root = Tk()
root.title("DATA ANALISYS")
# ---
new2 = Dane()

wpisywanieplikow  = Entry(root, width=35, borderwidth=5)
wpisywanieplikow.pack()
przycisk_pliki = Button(root, text="Open file", command=open)
przycisk_pliki.pack()
var1 = IntVar()
opcja1 = Checkbutton(root, text="Wykres", variable=var1)
opcja1.pack()
var2 = IntVar()
opcja2 = Checkbutton(root, text="Mediana", variable=var2)
opcja2.pack()
var3 = IntVar()
opcja3 = Checkbutton(root, text="Srednia", variable=var3)
opcja3.pack()
varpdf = IntVar()
opcjapdf = Checkbutton(root, text="generujj pdf", variable=varpdf)
opcjapdf.pack()

przycisk_start = Button(root, text="Start", command=funkcja_start)
przycisk_start.pack()

root.mainloop()
# ==========================================
# ==========================================
