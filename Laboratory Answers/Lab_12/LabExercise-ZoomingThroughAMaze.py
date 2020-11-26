from os import system, name 
from board import Board
from commands import DashUpCommand,DashLeftCommand,DashDownCommand,DashRightCommand
import getch

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

class Controller:
    def __init__(self,board:Board):
        self.__board = board
        self.__commandHistory = []

    def pressUp(self):
        command = DashUpCommand(self.__board)
        self.__commandHistory.append(command)
        command.execute()

    def pressDown(self):
        command = DashDownCommand(self.__board)
        self.__commandHistory.append(command)
        command.execute()

    def pressLeft(self):
        command = DashLeftCommand(self.__board)
        self.__commandHistory.append(command)
        command.execute()

    def pressRight(self):
        command = DashRightCommand(self.__board)
        self.__commandHistory.append(command)
        command.execute()

    def undo(self):
        if self.__commandHistory: #checks if empty
            undoneCommand = self.__commandHistory.pop()
            undoneCommand.undo()


def main():
    level1 = Board("boardFile.in")
    level2 = Board("boardFile2.in")
    level3 = Board("boardFile3.in")
    levels = [level3, level2, level1]

    b = levels.pop()
    c = Controller(b)

    '''
    Controls:
          w
        a s d 
    '''
    
    while True:
        clear()
        print(b)
        key = ord(getch.getch())
        if key == 27: #ESC
            break
        elif key == 122: #Z key
            c.undo()
        elif key == 115: #letter s              
            c.pressDown()
        elif key == 119: #letter w
            c.pressUp()
        elif key == 97: #letter a
            c.pressLeft()
        elif key == 100: #letter d
            c.pressRight()
        if b.characterLocation() == b.endPoint():
            clear()
            print("You Won!")
            print(b)
            
            playAgain: str = input("Proceeding to Next Level? Yes/No: ")
            if(playAgain.lower() == "yes"):
                if levels:
                    b = levels.pop()
                    c = Controller(b)
                else:
                    print("You've reached the max Level. Thank you for Playing.")
                    break
            else:
                break
        
if __name__ == "__main__":
    main()