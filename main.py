from colorama import Fore
from random import randint
import os
import block
import time


# Creating the board with borders
def createBoard() -> object:
    playfield = []
    for i in range(22):
        row = []
        row.append(-1)
        for j in range(10):
            row.append(0)
        row.append(-1)
        playfield.append(row)
    row = []
    row.append(-1)
    for j in range(10):
        row.append(-2)
    row.append(-1)
    playfield.append(row)
    return playfield


# Function to print the board with correct coloration
def printBoard(playfield):
    board = ""
    # All the color fun stuff
    for i in playfield:
        for j in i:
            if j == -2:
                board += Fore.WHITE + "---"
            elif j == -1:
                board += Fore.WHITE + "|"
            elif j == 0:
                board += Fore.WHITE + " . "
            elif j == 1:
                board += Fore.LIGHTBLUE_EX + "[ ]"
            elif j == 2:
                board += Fore.BLUE + "[ ]"
            elif j == 3:
                board += Fore.LIGHTRED_EX + "[ ]"
            elif j == 4:
                board += Fore.YELLOW + "[ ]"
            elif j == 5:
                board += Fore.GREEN + "[ ]"
            elif j == 6:
                board += Fore.RED + "[ ]"
            elif j == 7:
                board += Fore.MAGENTA + "[ ]"
        board += Fore.WHITE + "\n"
    print(board)


obj = block.Block(1)
board = createBoard()
for i in range(150):
    os.system('cls' if os.name == 'nt' else 'clear')  # For some reason this only works not in pycharm
    obj.drop(board)
    board = obj.draw(board)
    printBoard(board)
    if obj.isAtBottom:
        del obj
        obj = block.Block(randint(1, 7))
