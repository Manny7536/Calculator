import tkinter
from tkinter import*

root=Tk()
root.title("Manny Simple Calculator : )")
root.geometry("286x315+50+50")
root.resizable(False,False)
root.configure(bg="#17161b")

equation =""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def backspace():
    global equation
    equation = equation[:-1]
    label_result.config(text=equation)


def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calc():
    global equation
    result =""
    if equation !="":
        try:
            result= eval(equation)
        except:
            result="Error"
            equation =""
    label_result.config(text=result)


label_result = Label(root, width=25, height=2, text="", font=("arial",30))
label_result.pack()

Button(root, text="AC", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#3697f5", command=lambda: clear()).place(x=5,y=100)
Button(root, text="Back", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: backspace()).place(x=75,y=100)
Button(root, text="󠀥󠀥󠀥%", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("%")).place(x=145,y=100)
Button(root, text="➗", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("/")).place(x=215,y=100)

Button(root, text="7", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("7")).place(x=5,y=143)
Button(root, text="󠀥󠀥󠀥8", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("8")).place(x=75,y=143)
Button(root, text="9", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("9")).place(x=145,y=143)
Button(root, text="✖️", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("*")).place(x=215,y=143)

Button(root, text="4", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("4")).place(x=5,y=186)
Button(root, text="󠀥󠀥󠀥5", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("5")).place(x=75,y=186)
Button(root, text="6", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("6")).place(x=145,y=186)
Button(root, text="➖", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("-")).place(x=215,y=186)

Button(root, text="1", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("1")).place(x=5,y=229)
Button(root, text="󠀥󠀥󠀥2", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("2")).place(x=75,y=229)
Button(root, text="3", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("3")).place(x=145,y=229)
Button(root, text="➕", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("+")).place(x=215,y=229)

Button(root, text="0", width=11, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("0")).place(x=5,y=272)
Button(root, text="󠀥󠀥󠀥.", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show(".")).place(x=145,y=272)
Button(root, text="=", width=5, height=1, font=("arial",15,"bold"), bd=1, fg="#fff", bg="#fe9037",command=lambda: calc()).place(x=215,y=272)


root.mainloop()