from tkinter import *
# Set the screen
screen = Tk()
screen.geometry("1920x1080")
screen.title("Master Calculator")
screen.configure(bg = "Powder Blue")
#Top = Frame(screen, bg = "Cadet Blue", pady = 2, width = 500, height = 300, relief = RIDGE)
#Top.grid(row = 0, column = 0)
lblscrn = Label(screen, font = ("Times", 50, "bold"), text = "Master Calculator").pack(side = TOP)

# Set Value
def DTHCN():
	screenDTHCN = Toplevel(screen)
	screenDTHCN.title("Nhập Số Liệu Và Kết Quả Tính")
	screenDTHCN.geometry("450x400")
	#screenDTHCN.configure(bg = "Powder Blue")

	chieuDai = StringVar()
	chieuRong = StringVar()
	def PRINT():
		screenPRINT = Toplevel(screen)
		screenPRINT.title("PRINT")
		cd = int(str(chieuDai.get()))
		cr = int(str(chieuRong.get()))
		dt = cd*cr
		cv = (cd + cr)*2
		Label(screenDTHCN, text = "Chu Vi HCN" + str(cv)).pack(side = RIGHT)
		Label(screenDTHCN, text = "Diện Tích HCN" + str(dt)).pack(side = RIGHT)

	Label(screenDTHCN, text = "Vui Lòng Nhập Những Số Liệu Sau Đây:").pack(side = TOP, anchor = W, expand = NO)
	Label(screenDTHCN, text = "").pack(side = LEFT)
	Label(screenDTHCN, text = "Vui Lòng Nhập Chiều Dài:").pack(side = TOP, anchor = W, expand = NO)
	Entry(screenDTHCN, textvariable = chieuDai).pack(side = TOP, anchor = W)
	Label(screenDTHCN, text = "Vui Lòng Nhập Chiều Rộng:").pack(side = TOP, anchor = W)
	Entry(screenDTHCN, textvariable = chieuRong).pack(side = TOP, anchor = W)
	Button(screenDTHCN, text = "Calculator", height = 2, width = 18, command = PRINT).pack(side = TOP, anchor = W)
	#print(chieuDai, chieuRong)
	#Label(screenDTHCN, text = TDTHCN)

# Text and Buttons
button_tinh_hinh_chu_nhat = Button(screen, text = "Tính Hình Chữ Nhật", font = ("Times, 14"), fg = "black", height = 4, width = 25, command = DTHCN).pack(side = TOP, anchor = W, expand = NO)
button_tinh_hinh_tron = Button(screen, text = "Tính Hình Tròn", font = ("Times, 14"), fg = "black", height = 4, width = 25).pack(side = RIGHT, anchor = E)

screen.mainloop()

#def clear():
	#chieuDai = ""
	#chieuRong = ""