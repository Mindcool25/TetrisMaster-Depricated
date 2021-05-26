from colorama import Fore
from random import randint
import os
import block
import time


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
    for j in range(11):
        row.append(-2)
    playfield.append(row)
    return playfield


def printBoard(playfield):
    board = ""
    for i in playfield:
        for j in i:
            if j == -2:
                board += Fore.WHITE + "[|]"
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


block = block.Block(1)
board = createBoard()
for i in range(20):
    block.drop()
    time.sleep(0.5)
    board = block.draw(board)
    printBoard(board)
