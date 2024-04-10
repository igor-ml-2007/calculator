import tkinter

import math


def click(val):
    e = entry.get()
    ans = " "

    try:
        if val == 'C':
            e = e[0:len(e) - 1]
            entry.delete(0, 'end')
            entry.insert(0, e)
            return ''
        elif val == "CE":
            entry.delete(0, "end")
        elif val == "V":
            ans = math.sqrt(eval(e))
        elif val == "n":
            ans = math.pi
        elif val == "cose":
            ans = math.cos(math.radians(eval(e)))
        elif val == "sine":
            ans = math.sin(math.radians(eval(e)))
        elif val == "tane":
            ans = math.tan(math.radians(eval(e)))
        elif val == "27":
            ans = 2 * math.pi
        elif val == "cosh":
            ans = math.cosh(eval(e))
        elif val == "sinh":
            ans = math.sinh(eval(e))
        elif val == "tanh":
            ans = math.tanh(eval(e))
        elif val == chr(8731):
            ans = eval(e) ** (1 / 3)
        elif val == "x\u02b8":
            entry.insert("end", "****")
            return ''
        elif val == "x\u00B2":
            ans = eval(e) ** 2
        elif val == "In":
            ans = math.log2(eval(e))
        elif val == "deg":
            ans = math.degrees(eval(e))
        elif val == "pad":
            ans = math.radians(eval(e))
        elif val == "e":
            ans = math.e
        elif val == "log10":
            ans = math.log10(eval(e))
        elif val == "x!":
            ans = math.factorial(eval(e))
        elif val == chr(247):
            entry.insert("end", "/")
            return
        elif val == "=":
            ans = eval(e)
        else:
            entry.insert("end", val)
            return ''
        entry.delete(0, 'end')
        entry.insert(0, ans)
    except SyntaxError:
        pass


root = tkinter.Tk()
root.title('calculator')
root.config(bg="black")

entry = tkinter.Entry(root, font=('arial', 20, 'bold'), bg='black', fg='white', bd=10, width=30)
entry.grid(row=0, column=0, columnspan=8)

button_list = ['C', 'CE', 'V', '+', 'n', 'cose', 'tane', 'sine', '1', '2', '3', '-', '2n',
               'cosh', 'tanh', 'sinh', '4', '5', '6', '*', chr(8731), "x\u02b8", "x\u00B2",
               '7', '8', '9', chr(247), 'In', 'deg', 'pad', 'e', '0', '.', '%', '=', 'log10',
               '(', ')', 'x!']

r = 1
c = 0

for i in button_list:
    button = tkinter.Button(root, width=5, height=2, bd=2, text=i, bg='black', fg='black',
                            font=('arial', 18, 'bold'), command=lambda button=i: click(button))
    button.grid(row=r, column=c, pady=1)
    c += 1
    if c > 7:
        r += 1
        c = 0

root.mainloop()
