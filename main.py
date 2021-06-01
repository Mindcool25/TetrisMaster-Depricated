from colorama import Fore
from random import randint
import os
import block
import time
import os


def createBoard() -> object:
    playfield = []
    for i in range(22):
        row = []
        for j in range(10):
            row.append(0)
        playfield.append(row)
    return playfield


def printBoard(playfield):
    board = ""
    for i in playfield:
        board += Fore.WHITE + "|"
        for j in i:
            if j == 0:
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
        board += Fore.WHITE + "|\n"
    board += (Fore.WHITE + "_" * 32) + "\n"
    print(board)


block = block.Block(1)
for i in range(20):
    block.drop()
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    printBoard(block.draw(createBoard()))
