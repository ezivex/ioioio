#!/usr/bin/python3
import tkinter as tk
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
            state="readonly",
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
        self.file_btn = tk.Button(self.okno_plikow)
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
        _text_ = """some text"""
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
        self.chart_btn = tk.Checkbutton(self.wybor_opcji_okno)
        self.chart_btn.configure(
            background="#474747",
            font="{arial} 10 {bold}",
            foreground="#ffffff",
            selectcolor="#00ff40",
        )
        self.chart_btn.configure(text="Chart")
        self.chart_btn.place(anchor="nw", relx="0.05", rely="0.05", x="0", y="0")
        self.chart_btn.bind("<Button>", self.callback, add="")
        self.__tkvar = tk.StringVar(value="")
        __values = []
        self.x_btn = tk.OptionMenu(
            self.wybor_opcji_okno, self.__tkvar, None, *__values, command=None
        )
        self.x_btn.place(
            anchor="nw", relwidth="0.17", relx="0.36", rely="0.05", x="0", y="0"
        )
        __values = []
        self.y_btn = tk.OptionMenu(
            self.wybor_opcji_okno, self.__tkvar, None, *__values, command=None
        )
        self.y_btn.place(
            anchor="nw", relwidth="0.17", relx="0.56", rely="0.05", x="0", y="0"
        )
        self.fpack_btn = tk.Checkbutton(self.wybor_opcji_okno)
        self.fpack_btn.configure(
            background="#474747",
            font="{arial} 10 {bold}",
            foreground="#ffffff",
            selectcolor="#00ff40",
        )
        self.fpack_btn.configure(text="1st pack of data analysis(median avg etc)")
        self.fpack_btn.place(anchor="nw", relx="0.05", rely="0.3", x="0", y="0")
        self.spack_btn = tk.Checkbutton(self.wybor_opcji_okno)
        self.spack_btn.configure(
            background="#474747",
            font="{arial} 10 {bold}",
            foreground="#ffffff",
            selectcolor="#00ff40",
        )
        self.spack_btn.configure(text="2st pack of data analysis(median avg etc)")
        self.spack_btn.place(anchor="nw", relx="0.05", rely="0.45", x="0", y="0")
        self.pdf_btn = tk.Radiobutton(self.wybor_opcji_okno)
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
        self.ok_btn = tk.Button(self.wybor_opcji_okno)
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
        self.start_btn = tk.Button(self.data_analysis)
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


if __name__ == "__main__":
    app = AppGui()
    app.run()

