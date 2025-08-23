import math
from tkinter import *
root = Tk()

ip=Entry(root,width=50)
ip.grid(row=0,column=0,columnspan=5,padx=15,pady=15)
root.title("CALCULATOR!")
#root.geometry("640x360")

a,s,op=None,None,None

def click(n):
    cr=ip.get()
    ip.delete(0,END)
    ip.insert(0,str(cr)+str(n))
    return
def add():
    global a,op
    cr=ip.get()
    a=float(cr)
    ip.delete(0,END)
    op='add'
    return

def sub():
    global a,op
    cr=ip.get()
    a=float(cr)
    ip.delete(0,END)
    op='sub'
    return

def multiply():
    global a,op
    cr=ip.get()
    a=float(cr)
    ip.delete(0,END)
    op='multiply'
    return

def divide():
    global a,op
    cr=ip.get()
    a=float(cr)
    ip.delete(0,END)
    op='div'
    return

def clear():
    ip.delete(0,END)
    global a,s,op
    a,s,op=None,None,None
    return

def pct():
    cr=ip.get()
    ip.delete(0,END)
    ip.insert(0,str(float(cr)/100))
    return

def equal():
    global a,s,op
    cr=ip.get()
    s=float(cr)
    ip.delete(0,END)
    if op=='add':
        ip.insert(0,str(a+s))
    if op=='sub':
        ip.insert(0,str(a-s))
    if op=='multiply':
        ip.insert(0,str(a*s))
    if op=='div':
        if s!=0:
            ip.insert(0,str(a/s))
        else:
            ip.insert(0,'Error')
    a,s,op=None,None,None
    return

def sqroot():
    cr=ip.get()
    r=math.sqrt(float(cr))
    ip.delete(0,END)
    ip.insert(0,str(r))
    return

def power():
    cr=ip.get()
    if cr=='^2':
        r=math.pow(float(cr),2)
    if cr=='^3':
        r=math.pow(float(cr),3)
    ip.delete(0,END)
    ip.insert(0,str(r))
    return

def sine():
    cr=ip.get()
    r=math.sin(math.radians(int(cr)))
    ip.delete(0,END)
    ip.insert(0,str(r))
    return

def cosine():
    cr=ip.get()
    r=math.cos(math.radians(int(cr)))
    ip.delete(0,END)
    ip.insert(0,str(r))
    return



b1=Button(root,text="1",padx=50,pady=25,command=lambda: click(1))
b2=Button(root,text="2",padx=50,pady=25,command=lambda: click(2))
b3=Button(root,text="3",padx=50,pady=25,command=lambda: click(3))
b4=Button(root,text="4",padx=50,pady=25,command=lambda: click(4))
b5=Button(root,text="5",padx=50,pady=25,command=lambda: click(5))
b6=Button(root,text="6",padx=50,pady=25,command=lambda: click(6))
b7=Button(root,text="7",padx=50,pady=25,command=lambda: click(7))
b8=Button(root,text="8",padx=50,pady=25,command=lambda: click(8))
b9=Button(root,text="9",padx=50,pady=25,command=lambda: click(9))
b0=Button(root,text="0",padx=50,pady=25,command=lambda: click(0))
bdot=Button(root,text=".",padx=51,pady=25,command=lambda: click("."))

bac=Button(root,text="AC",padx=47,pady=25,command=clear)
bpct=Button(root,text="%",padx=48.5,pady=25,command=pct)
beq=Button(root,text="=",padx=50,pady=60,command=equal)
broot=Button(root,text="√",padx=50,pady=25,command=sqroot)

badd=Button(root,text="+",padx=49,pady=25,command=add)
bsub=Button(root,text="-",padx=51,pady=25,command=sub)
bpdt=Button(root,text="*",padx=50,pady=25,command=multiply)
bdiv=Button(root,text="/",padx=51,pady=25,command=divide)

bsin=Button(root,text='sin',padx=46,pady=25,command=sine)
bcos=Button(root,text='cos',padx=46,pady=25,command=cosine)
bp2=Button(root,text='^2',padx=46,pady=25,command=power)
bp3=Button(root,text='^3',padx=46,pady=25,command=power)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
badd.grid(row=1,column=3)
bac.grid(row=1,column=4)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
bsub.grid(row=2,column=3)
bpct.grid(row=2,column=4)

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
bpdt.grid(row=3,column=3)

broot.grid(row=4,column=0)
b0.grid(row=4,column=1)
beq.grid(row=3,column=4,rowspan=2)
bdiv.grid(row=4,column=3)
bdot.grid(row=4,column=2)

bsin.grid(row=5,column=0)
bcos.grid(row=5,column=1)
bp2.grid(row=5,column=2)
bp3.grid(row=5,column=3)

def keyhan(event):
    k=event.char
    if k in '0123456789.':
        click(k)
    match k:
        case '+':add()
        case '-':sub()
        case '*':multiply()
        case '/':divide()
        case '\r':equal()
    return

root.bind('<Key>',keyhan)

root.mainloop()