from tkinter import *
import random
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock,Paper,Scissors')
root.config(bg ='lightskyblue')
Label(root, text = 'Rock, Paper ,Scissors' , font='arial 20 bold', bg = 'azure').pack()
you = StringVar()
Label(root, text = 'choose any one: rock, paper ,scissors' , font='arial 15 bold', bg = 'azure').place(x = 20,y=70)
Entry(root, font = 'arial 15', textvariable = you , bg = 'azure').place(x=90 , y = 130)


#computer tern
comp= random.randint(1, 3) 
if comp == 1:
    comp = 'rock'
elif comp == 2:
    comp = 'paper'
elif comp == 3:
    comp = 'scissors'


#your tern
Result = StringVar()
def game():
    you1 = you.get()
# If two values are equal, declare a tie!
    if comp == you1:
        Result.set("         The game is a tie! You Both choose same.")
        
    

# Check for all possibilities when computer chose Rock
    elif comp == 'rock':
        if you1=='scissors':
            Result.set("            You Lose! Computer choose Rock.")
        elif you1=='paper':
            Result.set("            You Win! Computer choose Rock.")
    
# Check for all possibilities when computer chose Scissors
    elif comp == 'scissors':
        if you1=='paper':
            Result.set("            You Lose! Computer choose Scissors.")
        elif you1=='rock':
            Result.set("            You Win! Computer choose Scissors.")
    
# Check for all possibilities when computer chose Paper
    elif comp == 'paper':
        if you1=='rock':
            Result.set("            You Lose! Computer choose Paper.")
        elif you1=='scissors':
            Result.set("            You Win! Computer choose Paper.")

def Reset():
    you.set("")
    Result.set("") 
   
def Exit():
    root.destroy()

# Bottons Setting  
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='azure',width = 50,).place(x=25, y = 250)
Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='lavender' ,command = game).place(x=150,y=190)
Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='lavender' ,command = Reset).place(x=70,y=310)
Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='lavender' ,command = Exit).place(x=230,y=310)
root.mainloop()