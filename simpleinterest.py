from tkinter import *
window=Tk()

# add widgets here


window.title('Interest Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')


app_label=Label(window, text="INTEREST CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

money_label=Label(window, text="Money", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
money_label.place(x=20, y=90)

money=Entry(window, text="", bd=2, width=22)
money.place(x=150, y=92)

timeLabel=Label(window, text='Time',fg = 'black', bg ='lightcyan', font=('Calibri', 12), bd=5 )
timeLabel.place(x=20, y= 152)

time=Entry(window, text='' ,bd = 2, width=22)
time.place(x=150, y = 150)

rateLabel=Label(window, text='Rate',fg = 'black', bg ='lightcyan', font=('Calibri', 12), bd=5 )
rateLabel.place(x=20, y= 212)

rate=Entry(window, text='' ,bd = 2, width=22)
rate.place(x=150, y = 210)

def calculateBmi():
    m = float(money.get())
    t = float(time.get()) 
    r = float(rate.get())
    tot = (m*t*r)/100
    tot = round(tot, 2)

    outputMsg = Label(result_frame, text =str(tot), bg = 'lightcyan', font=('Calibri', 12), width=42)
    outputMsg.place(x=20, y=40)
    outputMsg.pack()

button = Button(window, text='Calculate', fg = 'black', bg = 'blue', font=('Calibri', 12), bd=4, command=calculateBmi)
button.place(x=150, y=250)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12), width = 100, height=100)
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()



window.mainloop()