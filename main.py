from colorama import Fore
from random import randint
import os
import block
import time
import keyboard


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


# Movement function
def move():
	while True:
		if keyboard.is_pressed("a"):
			obj.left(board)
		elif keyboard.is_pressed("s"):
			obj.slam(board)
		elif keyboard.is_pressed("d"):
			obj.right(board)
		elif keyboard.is_pressed("w"):
			obj.rotate(board)


for j in range(10):
	board = createBoard()
	obj = block.Block(1)

	for i in range(200):
		# Clearing the screen, doesn't work in pycharm
		os.system('cls' if os.name == 'nt' else 'clear')
		# Dropping the block one unit
		obj.drop(board)
		if not obj.isAtBottom:
			obj.newRotate(board)
		else:
			obj.losing(board)
			board = obj.draw(board)
			del obj
			obj = block.Block(randint(1, 7))
		board = obj.draw(board)
		printBoard(board)
		input()
