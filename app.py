#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
import matplotlib.pyplot as plt
from openpyxl import workbook, load_workbook
import os
import pandas as pd
class AppGui:
    def __init__(self, master=None):
        # build ui
        self.data_analysis = tk.Toplevel(master, container="false")
        self.main = tk.Frame(self.data_analysis)
        self.title_prog = tk.Label(self.main)
        self.title_prog.configure(
            background="#474747",
            font="{Arial} 20 {bold}",
            foreground="#ffffff",
            justify="center",
        )
        self.title_prog.configure(padx="5", pady="5", text="DATA ANALYSIS")
        self.title_prog.place(
            anchor="center",
            relwidth="0.57",
            relx="0.50",
            rely="0.08",
            width="300",
            x="0",
            y="0",
        )
        self.okno_plikow = tk.Frame(self.main)
        self.nazwa_pliku = tk.Entry(self.okno_plikow)
        self.file_name = tk.StringVar(value="")
        self.nazwa_pliku.configure(
            font="{aRIAL} 12 {}",
            justify="center",
            #state="readonly",
            textvariable=self.file_name,
        )
        self.nazwa_pliku.place(
            anchor="nw",
            relheight="0.51",
            relwidth="0.7",
            relx="0.03",
            rely="0.29",
            x="0",
            y="0",
        )
        self.file_btn = tk.Button(self.okno_plikow, command=open)
        self.file_btn.configure(
            background="#f34e49",
            font="{arial} 12 {bold}",
            foreground="#ffffff",
            text="FILE",
        )
        self.file_btn.place(
            anchor="nw",
            relheight="0.56",
            relwidth="0.25",
            relx="0.74",
            rely="0.26",
            x="0",
            y="0",
        )
        self.okno_plikow.configure(background="#474747", height="200", width="200")
        self.okno_plikow.place(
            anchor="nw",
            relheight="0.1",
            relwidth="0.48",
            relx="0.0",
            rely="0.18",
            x="0",
            y="0",
        )
        self.text = tk.Text(self.main)
        self.text.configure(
            background="#828282",
            blockcursor="false",
            font="{ARIAL} 12 {}",
            foreground="#ffffff",
        )
        self.text.configure(height="10", padx="15", pady="10", setgrid="false")
        self.text.configure(takefocus=False, width="50", wrap="word")
        _text_ = "Witaj w programie do analizy danych.\n Aby rozpocząć wybierz plik, a następnie zaznacz \ninteresujące cię opcję.\n " \
       "Po wciśnięciu przycisku start wyświetli się podgląd z wynikami \n a jeśli chcesz aby wyniki pojawiły się w pliku pdf,\n wystarczy że zaznaczysz opcję generuj pdf\n" \
       "i po wciśnięciu przycisku start zamiast podglądów\n wygeneruje ci się plik pdf z tymi wszystkimi wynikami."
        self.text.insert("0.0", _text_)
        self.text.place(
            anchor="nw",
            relheight="0.73",
            relwidth="0.39",
            relx="0.6",
            rely="0.17",
            x="0",
            y="0",
        )



        self.wybor_opcji_okno = tk.LabelFrame(self.main)

        self.button1 = tk.Button(self.wybor_opcji_okno)
        self.button1.configure(text="Odnow dane", command=self.aktualizuj)
        self.button1.place(anchor="nw", relx="0.1", rely="0.22", x="0", y="0")

        # CHART
        self.var1 = tk.IntVar()
        self.chart_btn = tk.Checkbutton(self.wybor_opcji_okno, variable=self.var1)

        self.chart_btn.configure(offvalue=0, onvalue=1, text="checkbutton1")

        self.chart_btn.configure(
            background="#474747",
            font="{arial} 10 {bold}",
            foreground="#ffffff",
            selectcolor="#00ff40",
        )
        self.chart_btn.configure(text="Chart")
        self.chart_btn.place(anchor="nw", relx="0.05", rely="0.05", x="0", y="0")

        self.opcje1 = []

        self.__tkvar = tk.StringVar(value="None")
        self.__tkvar2 = tk.StringVar(value="None")

        self.x_btn = tk.OptionMenu(
            self.wybor_opcji_okno, self.__tkvar, None, *self.opcje1, command=None
        )
        self.x_btn.place(
            anchor="nw", relwidth="0.17", relx="0.36", rely="0.05", x="0", y="0"
        )
        self.y_btn = tk.OptionMenu(
            self.wybor_opcji_okno, self.__tkvar2, None, *self.opcje1, command=None
        )
        self.y_btn.place(
            anchor="nw", relwidth="0.17", relx="0.56", rely="0.05", x="0", y="0"
        )
        # 2
        self.var2 = tk.IntVar()
        self.fpack_btn = tk.Checkbutton(self.wybor_opcji_okno, variable=self.var2)
        self.fpack_btn.configure(
            background="#474747",
            font="{arial} 10 {bold}",
            foreground="#ffffff",
            selectcolor="#00ff40",
        )

        self.fpack_btn.configure(text="1st pack of data analysis(median avg etc)")
        self.fpack_btn.place(anchor="nw", relx="0.05", rely="0.3", x="0", y="0")

        # 3
        self.var3 = tk.IntVar()
        self.spack_btn = tk.Checkbutton(self.wybor_opcji_okno, variable=self.var3)
        self.spack_btn.configure(
            background="#474747",
            font="{arial} 10 {bold}",
            foreground="#ffffff",
            selectcolor="#00ff40",
        )

        self.spack_btn.configure(text="2st pack of data analysis(median avg etc)")
        self.spack_btn.place(anchor="nw", relx="0.05", rely="0.45", x="0", y="0")

        # PDF
        self.var4 = tk.IntVar()
        self.pdf_btn = tk.Checkbutton(self.wybor_opcji_okno, variable=self.var4)
        self.pdf_btn.configure(
            background="#474747",
            font="{arial} 10 {}",
            foreground="#ffffff",
            justify="left",
        )

        self.pdf_btn.configure(
            relief="flat", selectcolor="#00ff40", text="Generate PDF file"
        )
        self.pdf_btn.place(anchor="nw", relx="0.05", rely="0.71", x="0", y="0")

        self.ok_btn = tk.Button(self.wybor_opcji_okno, command=self.zapisz)
        self.ok_btn.configure(
            font="{ARIAL} 12 {bold}", relief="flat", takefocus=False, text="Ok"
        )
        self.ok_btn.place(
            anchor="nw", relheight="0.12", relx="0.83", rely="0.05", x="0", y="0"
        )
        self.wybor_opcji_okno.configure(
            background="#474747",
            font="{arial} 12 {}",
            foreground="#ffffff",
            height="200",
        )
        self.wybor_opcji_okno.configure(
            text="Choose your analysis options:", width="200"
        )
        self.wybor_opcji_okno.place(
            anchor="nw",
            relheight="0.58",
            relwidth="0.56",
            relx="0.01",
            rely="0.31",
            x="0",
            y="0",
        )
        self.main.configure(background="#474747", height="450", width="750")
        self.main.pack(side="top")

        self.start_btn = tk.Button(self.data_analysis, command=funkcja_start)
        self.start_btn.configure(
            background="#00ff80",
            font="{ARIAL} 12 {bold}",
            foreground="#ffffff",
            justify="left",
        )
        self.start_btn.configure(text="START")
        self.start_btn.place(anchor="nw", relx="0.9", rely="0.92", x="0", y="0")
        self.data_analysis.configure(background="#474747", height="450", width="750")
        self.data_analysis.resizable(False, False)

        # Main widget
        self.mainwindow = self.data_analysis

    def run(self):
        self.mainwindow.mainloop()

    def callback(self, event=None):
        pass

    def aktualizuj(self):
        self.opcje1 = (new2.danenaglowki)
        print(self.opcje1)

        menu = self.x_btn["menu"]
        menu.delete(0, "end")
        menu2 = self.y_btn["menu"]
        menu2.delete(0, "end")
        for string in self.opcje1:
            menu.add_command(label=string, command=lambda value=string: self.__tkvar.set(value))
            menu2.add_command(label=string, command=lambda value=string: self.__tkvar2.set(value))

        self.__tkvar.set(self.opcje1[0])
        self.__tkvar2.set(self.opcje1[1])

    def zapisz(self):
        print(self.__tkvar.get())
        print(self.__tkvar2.get())
        new2.dowykresu = [self.__tkvar.get(), self.__tkvar2.get()]

class Dane:
    def __init__(self):
        self.plikdane = []
        self.danenaglowki = []
        self.dowykresu = []

# --- Otwarcie pliku, zapisanie danych do klasy
def open():
    # initialdir="/"
    app.data_analysis.filename = filedialog.askopenfilename(initialdir="/", title="select a file", filetypes=(
        ("xlsx files", "*.xlsx"), ("txt files", "*.txt"), ("all type", "*.*")))
    app.nazwa_pliku.delete(0, "end")
    app.nazwa_pliku.insert(0, app.data_analysis.filename)
    # zapisanie danych do zmiennej w klasie:
    new2.plikdane = pd.read_excel(app.nazwa_pliku.get())
    # zapisanie nazw naglowkow do zmiennej w klasie
    new2.danenaglowki = new2.plikdane.columns

    app.opcje = new2.danenaglowki

    print(new2.danenaglowki)
    print(len(new2.danenaglowki))
    #xdd2()
# ---
# ---
def funkcja_start():
    if app.var4.get() and (app.var1.get() or app.var2.get() or app.var3.get()):
        # generuj plik pdf z wynikami.
        print("Generuj PDF")
    elif (app.var1.get() or app.var2.get() or app.var3.get()) and app.nazwa_pliku.get():
        #podglad = Toplevel()
        if app.var1.get():
            #komunikat1 = Label(podglad, text="var1. wykres")
            #komunikat1.pack()
            #komunikat1a = Label(podglad, text=new2.dowykresu)
            #komunikat1a.pack()
            print("WYKRES\n " + str(new2.dowykresu))
            wykres()
        if app.var2.get():
            #komunikat2 = Label(podglad, text="var2. Mediana")
            #komunikat2.pack()
            print("Mediana")
        if app.var3.get():
            #komunikat3 = Label(podglad, text="var3. srednia")
            #komunikat3.pack()
            print("Srednia")
    else:
        print("Zaznacz jakies opcje ")
# ---
def wykres():
    x1 = new2.dowykresu[0]
    y1 = new2.dowykresu[1]
    # print(x1 + " " + y1)
    new2.plikdane.plot(x=x1, y=y1)
    plt.show()
# ---

# =======================MAIN=======================
if __name__ == "__main__":
    new2 = Dane()
    app = AppGui()
    app.run()



