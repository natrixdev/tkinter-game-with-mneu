from tkinter import *   
from tkinter import ttk
import sys
from jogo import *    
import tkinter as tk
from tkinter import simpledialog


file = 'score.txt'     
class GameGUI(object):    

    def __init__(self, root):
        self.root = root

        self.GameButton = Button(root, text="Play", command=self.NewGame)  
        self.GameLabel = Label(root, text="Press to Play", fg="black", font=("Helvetica",10)) 

        self.SaveButton = Button(root, text="Save", command=self.Save)  
        self.SaveLabel = Label(root, text="Press to Save", fg="black", font=("Helvetica",10)) 

        self.ScoreButton = Button(root, text="See Score", command=self.Score) 
        self.ScoreLabel = Label(root, text="Press to see the Score", fg="black", font=("Helvetica",10)) 
        self.ExitButton = Button(root, text="Exit",command=self.Exit) 
        self.ExitLabel = Label(root, text="Press to Exit", fg="red", font=("Helvetica",10)) 

        self.ReturnMenu = Button(root, text="Return to Menu", command=self.MainMenu)  

        self.MainMenu()

    def MainMenu(self):   
        self.RemoveAll()
        self.GameButton.grid()
        self.GameLabel.grid()
        self.SaveButton.grid()
        self.SaveLabel.grid()
        self.ScoreButton.grid()
        self.ScoreLabel.grid()
        self.ExitButton.grid()
        self.ExitLabel.grid()

    def NewGame(self):    
        root = tk.Tk()    
        root.title('Jogo')
        game = Game(root) 
        game.mainloop()   
        self.GameButton.grid_remove()
        self.GameLabel.grid_remove()
        self.ExitButton.grid_remove()
        self.ExitLabel.grid_remove()

    def Score(self):   
        file = open('score.txt', 'r+')     
        with open('score.txt') as file: 
            data = file.read()
        textbox = Text(root)        
        textbox.insert("1.0",data)  
        textbox.grid()              
        self.ReturnMenu.grid()

    def RemoveAll(self):    
        self.GameButton.grid_remove()
        self.GameLabel.grid_remove()
        self.ScoreButton.grid_remove()
        self.ScoreLabel.grid_remove()
        self.ExitButton.grid_remove()
        self.ExitLabel.grid_remove()
        self.ReturnMenu.grid_remove()

    def Exit(self):   
        self.root.quit
        sys.exit(0)


    def Save(self):  
      global file   
      name = simpledialog.askstring(title="Save", prompt="Enter your Name: ")
      points = simpledialog.askstring(title="Save", prompt="Enter your Score: ")
      f = open(file, 'a+')
      f.write(name +'\t' + points+'\n')   
      f.close()   



if __name__ == '__main__':    

    root = Tk()
    GameGUI = GameGUI(root)
    root.mainloop()