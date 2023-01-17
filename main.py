import tkinter as tk
from tkinter import *
from tkinter import ttk
from array import *
import numpy as np
import numpy as np


baxodir = tk.Tk()
#Dasturning bacground rangi
baxodir.configure(background='#edf0ee')
baxodir.geometry("900x700")
baxodir.title("Transport muammosi")
heading = Label(text = "Vogel's approximation method", fg = "white", width = "500", height = "1", font=('Arial 24'))
heading.pack()

# scrollbar canvas birinchi sp
frame1 = ttk.Frame(baxodir, relief="raised")
frame1.pack(fill=BOTH, side=LEFT)
canvas1 = Canvas(frame1)
canvas1.pack(side=LEFT, fill=BOTH)
scrolbar1 = ttk.Scrollbar(frame1, orient=VERTICAL, command=canvas1.yview)
scrolbar1.pack(side=RIGHT, fill=Y)
birlashuvchi = Frame(canvas1)
canvas1.create_window((50,10), window=birlashuvchi, anchor="nw")
canvas1.configure(yscrollcommand=scrolbar1.set)
canvas1.bind('<Configure>', lambda e: canvas1.configure(scrollregion = canvas1.bbox("all")))


# scrollbar canvas 2 birlashuvchi 2 dm
frame2 = Frame(baxodir, bd=1, relief="raised")
frame2.pack(fill=BOTH, side=LEFT)
canvas2 = Canvas(frame2)
canvas2.pack(side=LEFT, fill=BOTH) 
scrolbar2 = ttk.Scrollbar(frame2, orient=VERTICAL, command=canvas2.yview)
scrolbar2.pack(side=RIGHT, fill=Y)
birlashuvchi2 = Frame(canvas2)
canvas2.create_window((50,10), window=birlashuvchi2, anchor="nw")
canvas2.configure(yscrollcommand=scrolbar2.set)
canvas2.bind('<Configure>', lambda e: canvas2.configure(scrollregion = canvas2.bbox("all")))


# scrollbar canvas 3 birlashuvchi 3 matx
frame3 = Frame(baxodir, bd=1, relief="raised")
frame3.pack(fill=BOTH, side=LEFT)
canvas3 = Canvas(frame3)
canvas3.pack(side=LEFT, fill=BOTH, expand=1) 
scrolbar3 = ttk.Scrollbar(frame3, orient=VERTICAL, command=canvas3.yview)
scrolbar3.pack(side=RIGHT, fill=Y)
birlashuvchi3 = Frame(canvas3)
canvas3.create_window((50,10), window=birlashuvchi3, anchor="nw")
canvas3.configure(yscrollcommand=scrolbar3.set)
canvas3.bind('<Configure>', lambda e: canvas3.configure(scrollregion = canvas3.bbox("all")))



def tekshir_s_d(s, d):
    for i in s:
        if i != 0:
            return 1
    for i in d:
        if i != 0:
            return 1
    return 0

def vam(r, c, s, d, cc, a, maxi):
    while tekshir_s_d(s, d):
        dc = []
        dr = []
        if r != 1:
            for i in range(c):
                l = []
                for j in range(r):
                    l.append(cc[j][i])
                m1 = min(l)
                l.remove(m1)
                m2 = min(l)
                dr.append(m2-m1)
        if c != 1:
            for i in range(r):
                l = []
                for j in range(c):
                    l.append(cc[i][j])
                m1 = min(l)
                l.remove(m1)
                m2 = min(l)
                dc.append(m2-m1)
        if r == 1:
            for i in range(c):
                dr = [0]
            for i in range(r):
                if cc[i] == cc[0]:
                    z = i
            for i in range(c):
                a[z][i] = d[i]
        if c == 1:
            for i in range(r):
                dc = [0]
            for i in range(c):
                if cc[0][i] != cc[i]:
                    break
                z = i
            for i in range(r):
                a[i][z] = s[i]
   
        if len(dc) == 0 or len(dr) == 0:
            break
        q1 = max(dc)
        q2 = max(dr)
        m = max(q1, q2)
        w = 0
        if m in dc:
            w = 1
        else:
            w = 2
        if w == 1:
            for i in range(r):
                if m == dc[i]:
                    index = i
            k = 0
            mi = cc[index][0]
            for i in range(c):
                if mi > cc[index][i]:
                    mi = cc[index][i]
                    k = i
            a[index][k] = min(s[index], d[k])
            s[index] -= a[index][k]
            d[k] -= a[index][k]
            if s[index] == 0:
                for i in range(c):
                    cc[index][i] = maxi
            elif d[k] == 0:
                for i in range(r):
                    cc[i][k] = maxi   
        if w == 2:
            for i in range(c):
                if m == dr[i]:
                    index = i
            k = 0
            mi = cc[0][index]
            for i in range(r):
                if mi > cc[i][index]:
                    mi = cc[i][index]
                    k = i
   
            a[k][index] = min(s[k], d[index])
            s[k] -= a[k][index]
            d[index] -= a[k][index]
   
            if s[k] == 0:
                for i in range(c):
                    cc[k][i] = maxi
            elif d[index] == 0:
                for i in range(r):
                    cc[i][index] = maxi
   
        r = len(cc)
        if r == 0:
            break
        c = len(cc[0])


#===========================================================#
l1 = 0
l2 = 0
def a_input_function1():
    global l1, a_label, a_input, a
    a_label = Label(birlashuvchi, text=f"Supply{l1+1}", fg = "white")
    a_label.pack(side=TOP)
    a_input = Entry(birlashuvchi, font = 20, fg = "white")
    a_input.pack()
    a.append(a_input)
    l1+=1

def a_input_function2():
    global l2, b_input, b
    b_label = Label(birlashuvchi2, text=f"Demand{l2+1}")
    b_label.pack()
    b_input = Entry(birlashuvchi2, font = 20, fg = "white")
    b_input.pack()
    b.append(b_input)
    l2+=1

def a_input_function3():
    global a_1, row, list3
    for i in range(len(a)):
        col = []
        for j in range(len(b)):
            l_1 = Label(birlashuvchi3, text=f"Matrix[{i}][{j}]", fg = "white")
            l_1.pack()
            a_1 = Entry(birlashuvchi3, width="6", fg = "white")
            a_1.pack()
            col.append(a_1)
        list3.append(col)
a = []
s = np.array([])
b = []
d = np.array([])
list3 = []
cc = []


def ekrangaLCM():
    global s, d, cc
    for i in range(len(a)):
        intt = int(a[i].get())
        s = np.append(s, intt)
    for i in range(len(b)):
        intt2 = int(b[i].get())
        d = np.append(d, intt2)
    for i in list3:
        col2 = []
        for j in i:
            intt3 = int(j.get())
            col2.append(intt3)
        cc.append(col2)
    main(cc,d,s)

def main(cc,d,s):
    global c_vam, a
    r = len(s)
    c = len(d)

    a = np.zeros((r, c))
    copyocopy = np.zeros((r, c))

    for i in range(r):
        for j in range(c):
            copyocopy[i][j] = cc[i][j]

    maxi = cc[0][0]
    for i in range(r):
        for j in range(c):
            if maxi < cc[i][j]:
                maxi = cc[i][j]
    maxi += 1

    vam(r, c, s, d, cc, a, maxi)
    c_vam = 0
    for i in range(r):
        for j in range(c):
            c_vam += a[i][j]*copyocopy[i][j]

    natija(a, c_vam)
def natija(a, c_vam):
    from tkinter import Tk, Text
    root = Tk()
    root.title("Natija:")
    text = Text(root, height=8)
    text.pack()
    text.insert("1.0",a)
    text2 = Text(root, height=8)
    text2.pack()
    text2.insert("1.0",c_vam)
    root.mainloop()


add_label1 = tk.Label(birlashuvchi, text = "Supply qo'shish", fg = "white", font=('Arial 20'))
add_label1.pack(side=tk.TOP)
add_input1 = tk.Button(birlashuvchi, text="+", activeforeground = "green", width=10, font=('Arial 20'), fg = "black", command=a_input_function1)
add_input1.pack(side=tk.TOP)


add_label2 = tk.Label(birlashuvchi2, text = "Demand qo'shish", fg = "white", font=('Arial 20'))
add_label2.pack()
add_input2 = tk.Button(birlashuvchi2, text="+", activeforeground = "green", width=10, font=('Arial 20'), fg = "black", command=a_input_function2)
add_input2.pack(side=tk.TOP)


add_label3 = tk.Label(birlashuvchi3, text = "Matrix qo'shish", fg = "white", font=('Arial 20'))
add_label3.pack()
add_input3 = tk.Button(birlashuvchi3, text="+", activeforeground = "green", width=10, font=('Arial 20'), fg = "black", command=a_input_function3)
add_input3.pack(side=tk.TOP)


enter2 = tk.Button(birlashuvchi3, text="Javob", activeforeground = "green", width=10, font=('Arial 20'), command=ekrangaLCM)
enter2.pack(side=tk.TOP)

baxodir.mainloop()

