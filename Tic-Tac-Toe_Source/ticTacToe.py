import sys
import minimaxTicTacToe as AI
import tkinter as tk
from tkinter import Frame, Label, Menu, messagebox as msg
from tkinter.constants import ACTIVE, DISABLED, LEFT, RIGHT
from PIL import Image,ImageTk
xIsAI=False
oImg=Image.open("O.png").resize((100,100),Image.ANTIALIAS)
xImg=Image.open("X.png").resize((100,100),Image.ANTIALIAS)
emptyImg=Image.open("empty.png").resize((100,100),Image.ANTIALIAS)
xSmallImg=Image.open("x.png").resize((30,30),Image.ANTIALIAS)
oSmallImg=Image.open("o.png").resize((30,30),Image.ANTIALIAS)
player,ai="o","x"
count=0
isAITurn=True
board=[
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"]
]
def checkStatus(status):
    global board,count
    isGameEnd=False
    if(status==0 and not AI.isMoveLeft(board)):
        print("Tie")
        msg.showinfo("Tie","Game is Tie (:")
        isGameEnd=True
    if(status==10):
        print("AI Won")
        msg.showinfo("AI Won","AI won the game! Better luck next time (:")
        isGameEnd=True
    if(status==-10):
        print("Player won")
        msg.showinfo("Won","Congratulations! You won the game (:")
        isGameEnd=True
    if(isGameEnd):
        ans=msg.askquestion("","Want to play again")
        if(ans=="yes"):
            count+=1
            reset()
            board=[
                ["_","_","_"],
                ["_","_","_"],
                ["_","_","_"]
            ]
            n=count%2
            AI.changePlayer(n)
            if(n==0):
                game()
                return True
        else:
            quit()
    return False
def quit():
    sys.exit()
def setMove(n):
    global player,ai
    global isAITurn
    if(count%2==0):
        player,ai="o","x"
    else:
        player,ai="x","o"
    if(board[n[0]][n[1]]=="_"):
        if(isAITurn):
            board[n[0]][n[1]]=ai
            setImage(n,ai)
            isAITurn=False
        else:
            isAITurn=True
            board[n[0]][n[1]]=player
            setImage(n,player)
            game()
    else:
        print("Error","Already occupied")
    status=AI.evaluate(board)
    s=checkStatus(status)
    if(s):
        isAITurn=True

root=tk.Tk()
root.title("Tic Tac Toe")
root.maxsize(310,360)
root.minsize(310,360)
menuBar=Menu(root)
menuBar.add_command(label="Game")
# menuBar.add_command(label="About")
menuBar.add_command(label="Exit",command=quit)
root.config(menu=menuBar)
xSmall=ImageTk.PhotoImage(xSmallImg)
oSmall=ImageTk.PhotoImage(oSmallImg)
aiSymbol=Label(text="AI    ",image=xSmall,compound=RIGHT)
playerSymbol=Label(text="Player    ",image=oSmall,compound=RIGHT)
aiSymbol.grid(row=3,column=0)
playerSymbol.grid(row=3,column=2)
o=ImageTk.PhotoImage(oImg)
x=ImageTk.PhotoImage(xImg)
empty=ImageTk.PhotoImage(emptyImg)
bt1=tk.Button(image=empty,command=lambda:setMove((0,0)))
bt2=tk.Button(image=empty,command=lambda:setMove((0,1)))
bt3=tk.Button(image=empty,command=lambda:setMove((0,2)))

bt4=tk.Button(image=empty,command=lambda:setMove((1,0)))
bt5=tk.Button(image=empty,command=lambda:setMove((1,1)))
bt6=tk.Button(image=empty,command=lambda:setMove((1,2)))

bt7=tk.Button(image=empty,command=lambda:setMove((2,0)))
bt8=tk.Button(image=empty,command=lambda:setMove((2,1)))
bt9=tk.Button(image=empty,command=lambda:setMove((2,2)))
bt1.grid(row=0,column=0)
bt2.grid(row=0,column=1)
bt3.grid(row=0,column=2)

bt4.grid(row=1,column=0)
bt5.grid(row=1,column=1)
bt6.grid(row=1,column=2)

bt7.grid(row=2,column=0)
bt8.grid(row=2,column=1)
bt9.grid(row=2,column=2)
def setImage(n,img):
    position=(n[0]*3)+n[1]+1
    if(img=="o"):
        if(position==1):
            bt1.config(image=o)
        elif (position==2):
            bt2.config(image=o)
        elif (position==3):
            bt3.config(image=o)
        elif (position==4):
            bt4.config(image=o)
        elif (position==5):
            bt5.config(image=o)
        elif (position==6):
            bt6.config(image=o)
        elif (position==7):
            bt7.config(image=o)
        elif (position==8):
            bt8.config(image=o)
        elif (position==9):
            bt9.config(image=o)
    else:
        if(position==1):
            bt1.config(image=x)
        elif (position==2):
            bt2.config(image=x)
        elif (position==3):
            bt3.config(image=x)
        elif (position==4):
            bt4.config(image=x)
        elif (position==5):
            bt5.config(image=x)
        elif (position==6):
            bt6.config(image=x)
        elif (position==7):
            bt7.config(image=x)
        elif (position==8):
            bt8.config(image=x)
        elif (position==9):
            bt9.config(image=x)
def game():
    move=AI.start(board)
    print(move)
    setMove((move[0],move[1]))
def reset():
    if(count%2==0):
        aiSymbol.config(image=xSmall)
        playerSymbol.config(image=oSmall)
    else:
        aiSymbol.config(image=oSmall)
        playerSymbol.config(image=xSmall)
    bt1.config(image=empty)
    bt2.config(image=empty)
    bt3.config(image=empty)
    bt4.config(image=empty)
    bt5.config(image=empty)
    bt6.config(image=empty)
    bt7.config(image=empty)
    bt8.config(image=empty)
    bt9.config(image=empty)
if(isAITurn):
    game()
root.mainloop()