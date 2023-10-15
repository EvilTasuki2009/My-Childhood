import tkinter
from tkinter import *
import random

answer = [
	"ALOK",
	"KLA",
	"MOCO",
	"ANDREW",
	"FORD",
	"NIKITA",
	"HAYATO",
	"MAXIM",
	"ADAM",
	"EVA",
	"CLUE",
	"CAROLINE",
	"OLIVIA",
	"MISHA",
	"PALOMA",
	"MIGUEL",
	"KELLY",
	"WUKONG",
	"ANTONIO",
	"STEFFIE",
	"JOTA",
	"WOLFRAHH",
]

words = [
	"OLKA",
	"KAL",
	"COMO",
	"NAERDW",
	"RFOD",
	"ITINKA",
	"AHATYO",
	"IMAXM",
	"DMAA",
	"AEV",
	"ULEC",
	"OLECIRNA",
	"OLVAIIa",
	"HAMIS",
	"PAMALO",
	"GEIMUL",
	"ELKLY",
	"NUOKGW",
	"AONOTIN",
	"TSIEEFF",
	"JATO",
	"FARHLHOW",
]

num = random.randrange(0, 25, 1)

root = Tk()
root.geometry("350x400+400+300")
root.title("Trò chơi Jumbdled Words!")
root.configure(bg = "black")

lbl = Label(
	root,
	text = "Hello Here",
	font = ("Times 18"),
	bg = "black",
	fg = "white",
)
lbl.pack(pady = 30, ipady = 10, ipadx = 10)

e1 = Entry(
	root,
	font = ("Times 16"),
)
e1.pack()

btncheck = Button(
	root,
	text = "Kiểm Tra Đáp Án",
	font = ("Times", 16, "bold"),
	width = 16, 
	bg = "grey",
	fg = "Lime",
	relief = GROOVE,
)
btncheck.pack(pady = 40)

btnreset = Button(
	root,
	text = "Reset",
	font = ("Times", 16, "bold"),
	width = 16, 
	bg = "grey",
	fg = "red",
	relief = GROOVE,
)
btnreset.pack()






root.mainloop()



















































































