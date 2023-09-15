import random
import tkinter as tk
from tkinter import StringVar, Button, Entry

mainwindow = tk.Tk()
mainwindow.title("Calculator")

ans_enty = Entry(mainwindow, relief="raised", bd=5, width=25, font=("Arial", 15), bg="black", fg="orange")
ans_enty.grid(row=0, column=0, columnspan=5)

# ... Rest of your button and widget definitions ...

equation = {}
btn_1=Button(mainwindow,text="1",padx=20,pady=10)
btn_1.grid(row=1,column=0)
btn_2=Button(mainwindow,text="2",padx=20,pady=10)
btn_2.grid(row=1,column=1)
btn_3=Button(mainwindow,text="3",padx=20,pady=10)
btn_3.grid(row=1,column=2)
btn_4=Button(mainwindow,text="4",padx=20,pady=10)
btn_4.grid(row=1,column=3)
btn_5=Button(mainwindow,text="/",padx=20,pady=10)
btn_5.grid(row=1,column=4)

btn_6=Button(mainwindow,text="5",padx=20,pady=10)
btn_6.grid(row=2,column=0)
btn_7=Button(mainwindow,text="6",padx=20,pady=10)
btn_7.grid(row=2,column=1)
btn_8=Button(mainwindow,text="7",padx=20,pady=10)
btn_8.grid(row=2,column=2)
btn_9=Button(mainwindow,text="8",padx=20,pady=10)
btn_9.grid(row=2,column=3)
btn_10=Button(mainwindow,text="*",padx=20,pady=10)
btn_10.grid(row=2,column=4)

btn_11=Button(mainwindow,text="9",padx=20,pady=10)
btn_11.grid(row=3,column=0)
btn_12=Button(mainwindow,text="0",padx=20,pady=10)
btn_12.grid(row=3,column=1)
btn_13=Button(mainwindow,text="O",padx=20,pady=10)
btn_13.grid(row=3,column=2)
btn_14=Button(mainwindow,text="C",padx=20,pady=10)
btn_14.grid(row=3,column=3)
btn_15=Button(mainwindow,text="+",padx=20,pady=10)
btn_15.grid(row=3,column=4)

btn_16=Button(mainwindow,text="=",padx=20,pady=10)
btn_16.grid(row=4,column=0)
btn_17=Button(mainwindow,text="H",padx=20,pady=10)
btn_17.grid(row=4,column=1)
btn_18=Button(mainwindow,text="R",padx=20,pady=10)
btn_18.grid(row=4,column=2)
btn_19=Button(mainwindow,text=".",padx=20,pady=10)
btn_19.grid(row=4,column=3)
btn_20=Button(mainwindow,text="-",padx=20,pady=10)
btn_20.grid(row=4,column=4)

def mouse_button_release(event):
    wid = event.widget
    tex = wid.cget("text")
    if tex in "0123456789.":
        ans_enty.insert(len(ans_enty.get()), tex)

    if tex == "O" and len(ans_enty.get()):
        oct_num = oct(int(float(ans_enty.get())))
        oct_num = oct_num[2:]
        ans_enty.delete(0, "end")
        ans_enty.insert(0, str(oct_num))

    if tex == "H" and len(ans_enty.get()):
        hex_num = hex(int(ans_enty.get()))   
        ans_enty.delete(0, "end")
        ans_enty.insert(0, str(hex_num))

    if tex == "R" and len(ans_enty.get()):
        r = random.randrange(0, int(float(ans_enty.get())) + 1)
        ans_enty.delete(0, "end")
        ans_enty.insert(0, str(r))
    
    if tex == "R" :
        r = random.randrange(0,100)
        ans_enty.delete(0, "end")
        ans_enty.insert(0, str(r))   


    if tex == "C":
        ans_enty.delete(0, "end")   
        equation.clear()

    if tex in "+-*/%":
        if ans_enty.get():
            equation['num_1'] = float(ans_enty.get())
            ans_enty.delete(0, "end")
            equation['operation'] = tex
    if tex == "=":
        if 'operation' in equation.keys() and len(ans_enty.get()):
            equation['num_2'] = float(ans_enty.get())
            ans_enty.delete(0, "end")

            num_1 = equation['num_1']
            op = equation['operation']
            num_2 = equation['num_2']

            if op == "+":
                ans = num_1 + num_2
            elif op == "-":
                ans = num_1 - num_2
            elif op == "*":
                ans = num_1 * num_2
            elif op == "/":
                ans = num_1 / num_2
            elif op == "%":
                ans = (num_1 / num_2) * 100

            ans_enty.insert(0, ans)  
            equation.clear()


mainwindow.geometry("300x230")  # Corrected geometry string
mainwindow.resizable(False, False)
mainwindow.bind("<ButtonRelease-1>", mouse_button_release)

mainwindow.mainloop()
