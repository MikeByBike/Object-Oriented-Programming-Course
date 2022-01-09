"""
File:           minimine.py
Author:         Michalis Iona
Description:    
"""

import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk 
from abc import ABC, abstractmethod
from mine import Mine
import pickle



class IGames(ABC):
    @abstractmethod
    def move(self, place):
        pass
    @abstractmethod
    def isReady(self):
        pass
    @abstractmethod
    def newGame(self):
        pass




class MiniMine(IGames, tk.Tk) :
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs) #call Tk class initializer
        self.geometry('400x400')
        self.slots = 10
        self.__mine = Mine(slots=self.slots, mines=20)
        self.__createLayout()
        self.restore()
        self.__mine.sow() #create mines ja mineinfo, default 10 mines
        self.protocol("WM_DELETE_WINDOW", self.__showResult) #closing from cross
    
        
    
        
    def __createLayout(self):
        self.title('MiniMine')
        self.__tvar = ['']*self.slots * self.slots #content, empty, mine or how many mine button sees
        self.buttons = [] #attribute so that buttons can be enabled and disabled
        for i in range(self.slots * self.slots):
            self.__tvar[i] = tk.StringVar(value='') #initiate StringVar  as empty
            self.buttons.append(ttk.Button(self, textvariable=self.__tvar[i], command=lambda i=i: self.move(i)))
            self.buttons[i].grid(row = i // self.slots, column = i % self.slots, sticky = tk.E + tk.W+ tk.N + tk.S)
            self.rowconfigure(i // self.slots, weight = 1)
            self.columnconfigure(i % self.slots, weight = 1)
    



    def __show(self, nro):
        self.__tvar[nro].set(self.__mine.mineinfo[nro]) 
        if self.__mine.mineinfo[nro] == 0 and str(self.buttons[nro].cget('state')) != 'disabled':
            self.buttons[nro].config(state='disabled')
            self.__mine.points += 100




    def __showResult(self, win=False, ready=False):
        if not ready and messagebox.askyesno('Minimine is ready to be closed, but', 'Are you sure you want to quit?'):
            self.serialize() 
            self.destroy()
        elif ready:                             
            title = "Start a new game?"
            txt = 'Congratulations, you have won!' if win else 'Ouch. Better luck next time!'
            if messagebox.askyesno(title, txt):
                self.newGame()
            else:
                self.serialize() 
                self.destroy()

    

    
    def restore(self):
        file = None
        try :
            file = open('ttt.dat', 'br')
            g = pickle.load(file)
            if g and isinstance(g, Mine):
                self.__mine = g
                if self.__mine.points != 0:
                    self.title(f'MiniMine - points {self.__mine.points}')
                for i in range(self.slots * self.slots):
                    if self.__mine.buttonStates[i] == 0:
                        self.buttons[i].config(state='disabled')
                    self.__tvar[i].set(f'{self.__mine.buttonLabels[i]}')
        except IOError as error :
            print(error)
        finally:
            if file :
                file.close()  
                
      
                
      
      
      
    def serialize(self):
        file = None
        try:
            file = open('ttt.dat', 'bw')
            # source, destination
            pickle.dump(self.__mine, file)
        except IOError as error:
            print(error)
        finally :
            if file :
                file.close()
       
                
       
        
       
  
    def move(self, nro):       
        self.buttons[nro].config(state='disabled')
        if nro in self.__mine.minet:
            #näytä kaikki minet, peli loppuu
            for i in self.__mine.minet:
                self.__tvar[i].set('*')
            self.__showResult(win=False, ready=True)
        else:
            self.__mine.points += 100    
            #nslots around button
            if nro % self.slots > 0:
                self.__show(nro - 1)
            if nro % self.slots < self.slots - 1:
                self.__show(nro + 1)
            if nro // self.slots > 0:
                self.__show(nro - self.slots)
            if nro // self.slots < self.slots - 1:
                self.__show(nro + self.slots)
            if nro % self.slots > 0 and nro // self.slots > 0:
                self.__show(nro - self.slots - 1)
            if nro % self.slots > 0 and nro // self.slots < self.slots - 1:
                self.__show(nro + self.slots - 1)
            if nro % self.slots <  self.slots - 1 and nro // self.slots > 0:
                self.__show(nro - self.slots + 1)
            if nro % self.slots < self.slots - 1 and nro // self.slots < self.slots - 1:
                self.__show(nro + self.slots + 1)
                    
            self.title(f'MiniMine - points {self.__mine.points}')
            if self.isReady(): 
                self.__showResult(win=True, ready=True)
        self.updateButtonStates()
      



          

    def updateButtonStates(self):
        for i in range(self.slots * self.slots):
            if str(self.buttons[i].cget('state')) == 'disabled':
                self.__mine.buttonStates[i] = 0 #disables the button when restored
            self.__mine.buttonLabels[i] = self.buttons[i].cget('text')      






    def newGame(self):
        self.__mine.newGame()
        self.__createLayout()
        




    def isReady(self):
        return self.__mine.isReady()
   

if __name__ == '__main__' :
   MiniMine().mainloop()







