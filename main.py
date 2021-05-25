from colorama import Fore
from random import randint
import block


def createBoard() -> object:
    """

    :rtype: object
    """
    playfield = []
    for i in range(21):
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


for i in range(20):
    printBoard(createBoard())
    block = block.Block(2)
    block.draw(createBoard())
