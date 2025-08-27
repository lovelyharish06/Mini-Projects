from tkinter import *
from random import choice

stages = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========''',  # 0 wrong guesses

    '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========''',  # 1 wrong

    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========''',  # 2 wrong

    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''',  # 3 wrong

    '''
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========''',  # 4 wrong

    '''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========''',  # 5 wrong

    '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========''',  # 6 wrong — final stage
]


root=Tk()
root.title("HANGMAN GAME!")  #title of the tkinter window
root.geometry("720x480")

disp=StringVar()
msg=StringVar()
inp=StringVar()

words=["Python","Computer","Samsung","Integration","Cricket","Rubeen","Digital"]
x=choice(words).lower()
crt=[]
t=6

def update():
    cr = ' '.join([ch if ch in crt else "_" for ch in x])
    disp.set(cr)

def guess():
    global t
    g=inp.get().lower()
    inp.set("")

    if not g or len(g)!=1 or not g.isalpha():
        msg.set(f"Enter Valid Letter\nYour Tree\n{stages[6-t]}")
        return
    if g in crt:
        msg.set(f"Already Guessed,Try Another\nYour Tree\n{stages[6-t]}")
    elif g in x:
        crt.append(g)
        update()
        msg.set(f"Correct,Make Next Guess\nYour Tree\n{stages[6-t]}")
    else:
        crt.append(g)
        msg.set(f"Wrong,Guess Correctly\nYour Tree\n{stages[6-t]}")
        t-=1
    if '_' not in disp.get():
        msg.set("You win")
        gb.config(state="disabled")
        rb.pack(pady=10)    #Shows after win
    elif t==0:
        msg.set("You lost The Game")
        gb.config(state="disabled")
        rb.pack(pady=10)    #Shows after loss
    return

def reset():
    global x,crt,t
    x=choice(words).lower()
    crt = []
    t = 6
    disp.set("")
    inp.set("")
    msg.set("")
    update()
    gb.config(state="normal")
    rb.pack_forget()

Label(root, text="HANGMAN GAME!", font=("Arial", 20),fg="red").pack() #Title of the game
Label(root, textvariable=disp, font=("Arial", 18)).pack(pady=10)
ip=Entry(root,textvariable=inp,width=50)  #text entering box
ip.pack(padx=15,pady=15)
ip.bind("<Return>",lambda o:guess())
gb=Button(root,text="Guess",padx=15,pady=10,command=guess)   #guess button
gb.pack(pady=10)
Label(root, textvariable=msg, font=("Arial", 12), fg="blue").pack()  #displaying message and hanging tree

rb=Button(root,text="Try Again",padx=15,pady=10,command=reset)  #Try Again button
rb.pack_forget()   #Hides Initially

update()
root.mainloop()