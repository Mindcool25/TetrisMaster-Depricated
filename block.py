class Block:
	"""Class for block object"""

	# Initializing block type when object is created and defining the shape
	def __init__(self, blockType):
		# Initial x and y values
		self.x = 6
		self.y = 0

		# setting block properties
		self.type = blockType
		self.blockShape = []
		self.Shape()
		self.isAtBottom = False
		self.rotation = 0

		# Setting the lost flag to false
		self.lost = False
		return

	# Setting the shape from block type to a matrix (OLD)
	def shapeOLD(self):
		if self.type == 1:
			self.blockShape = [[1, 1, 1, 1], [0, 0, 0, 0]]
		elif self.type == 2:
			self.blockShape = [[0, 2, 0, 0], [0, 2, 2, 2]]
		elif self.type == 3:
			self.blockShape = [[0, 0, 0, 3], [0, 3, 3, 3]]
		elif self.type == 4:
			self.blockShape = [[0, 4, 4, 0], [0, 4, 4, 0]]
		elif self.type == 5:
			self.blockShape = [[0, 0, 5, 5], [0, 5, 5, 0]]
		elif self.type == 6:
			self.blockShape = [[0, 6, 6, 0], [0, 0, 6, 6]]
		elif self.type == 7:
			self.blockShape = [[0, 0, 7, 0], [0, 7, 7, 7]]
		return

	# Newer version of setting the shape of the block. Gives all possible states of all blocks as they should be.
	def Shape(self):
		if self.type == 1:
			self.blockShape = [
				[
					[0, 0, 0, 0],
					[1, 1, 1, 1],
					[0, 0, 0, 0],
					[0, 0, 0, 0]
				],
				[
					[0, 0, 1, 0],
					[0, 0, 1, 0],
					[0, 0, 1, 0],
					[0, 0, 1, 0]
				],
				[
					[0, 0, 0, 0],
					[0, 0, 0, 0],
					[1, 1, 1, 1],
					[0, 0, 0, 0]
				],
				[
					[0, 1, 0, 0],
					[0, 1, 0, 0],
					[0, 1, 0, 0],
					[0, 1, 0, 0]
				],
			]
		elif self.type == 2:
			self.blockShape = [
				[
					[2, 0, 0, 0],
					[2, 2, 2, 0],
					[0, 0, 0, 0],
					[0, 0, 0, 0]
				],
				[
					[0, 2, 2, 0],
					[0, 2, 0, 0],
					[0, 2, 0, 0],
					[0, 0, 0, 0]
				],
				[
					[0, 0, 0, 0],
					[2, 2, 2, 0],
					[0, 0, 2, 0],
					[0, 0, 0, 0]
				],
				[
					[0, 2, 0, 0],
					[0, 2, 0, 0],
					[2, 2, 0, 0],
					[0, 0, 0, 0]
				]
			]
		elif self.type == 3:
			self.blockShape = [
				[
					[0, 0, 3, 0],
					[3, 3, 3, 0],
					[0, 0, 0, 0],
					[0, 0, 0, 0]
				],
				[
					[0, 3, 0, 0],
					[0, 3, 0, 0],
					[0, 3, 3, 0],
					[0, 0, 0, 0]
				],
				[
					[0, 0, 0, 0],
					[3, 3, 3, 0],
					[3, 0, 0, 0],
					[0, 0, 0, 0]
				],
				[
					[3, 3, 0, 0],
					[0, 3, 0, 0],
					[0, 3, 0, 0],
					[0, 0, 0, 0]
				]
			]
		elif self.type == 4:
			self.blockShape = [
				[
					[0, 0, 0, 0],
					[0, 4, 4, 0],
					[0, 4, 4, 0],
					[0, 0, 0, 0]
				],
				[
					[0, 0, 0, 0],
					[0, 4, 4, 0],
					[0, 4, 4, 0],
					[0, 0, 0, 0]
				],
				[
					[0, 0, 0, 0],
					[0, 4, 4, 0],
					[0, 4, 4, 0],
					[0, 0, 0, 0]
				],
				[
					[0, 0, 0, 0],
					[0, 4, 4, 0],
					[0, 4, 4, 0],
					[0, 0, 0, 0]
				]
			]
		elif self.type == 5:
			self.blockShape = [
				[
					[0, 5, 5, 0],
					[5, 5, 0, 0],
					[0, 0, 0, 0],
					[0, 0, 0, 0]
				],
				[
					[0, 5, 0, 0],
					[0, 5, 5, 0],
					[0, 0, 5, 0],
					[0, 0, 0, 0]
				],
				[
					[0, 0, 0, 0],
					[0, 5, 5, 0],
					[5, 5, 0, 0],
					[0, 0, 0, 0]
				],
				[
					[5, 0, 0, 0],
					[5, 5, 0, 0],
					[0, 5, 0, 0],
					[0, 0, 0, 0]
				]
			]
		elif self.type == 6:
			self.blockShape = [
				[
					[6, 6, 0, 0],
					[0, 6, 6, 0],
					[0, 0, 0, 0],
					[0, 0, 0, 0]
				],
				[
					[0, 0, 6, 0],
					[0, 6, 6, 0],
					[0, 6, 0, 0],
					[0, 0, 0, 0]
				],
				[
					[0, 0, 0, 0],
					[6, 6, 0, 0],
					[0, 6, 6, 0],
					[0, 0, 0, 0]
				],
				[
					[0, 6, 0, 0],
					[6, 6, 0, 0],
					[6, 0, 0, 0],
					[0, 0, 0, 0]
				]
			]
		elif self.type == 7:
			self.blockShape = [
				[
					[0, 7, 0, 0],
					[7, 7, 7, 0],
					[0, 0, 0, 0],
					[0, 0, 0, 0]
				],
				[
					[0, 7, 0, 0],
					[0, 7, 7, 0],
					[0, 7, 0, 0],
					[0, 0, 0, 0]
				],
				[
					[0, 0, 0, 0],
					[7, 7, 7, 0],
					[0, 7, 0, 0],
					[0, 0, 0, 0]
				],
				[
					[0, 7, 0, 0],
					[7, 7, 0, 0],
					[0, 7, 0, 0],
					[0, 0, 0, 0]
				]
			]
		return

	# Easy one liner to rotate the array of a block
	def rotateOLD(self, board):
		# For some reason it still allows rotation after the block lands on another block.
		# Not sure how to fix that at this moment.
		backup = self.blockShape[self.rotation]
		self.clear(board)
		self.blockShape[self.rotation] = list(zip(*self.blockShape[self.rotation][::-1]))
		for row in range(len(self.blockShape[self.rotation])):
			for column in range(len(self.blockShape[self.rotation][row - 2])):
				if self.blockShape[self.rotation][row - 2][column - 2] != 0:
					if row + self.y < len(board) and column + self.x < len(board[0]):
						if board[row + self.y][column + self.x] != 0:
							self.blockShape[self.rotation] = backup
							break
					else:
						self.blockShape[self.rotation] = backup
		return

	# Second attempt to rotation 
	def rotate(self, board):
		# Saving a backup of the original rotation value
		oldRotate = self.rotation

		# Make sure the rotation doesn't overflow
		if self.rotation == 3:
			newRotate = 0
		else:
			newRotate = self.rotation + 1

		# Checking for collisions
		# iterating through both rows and columns of the blockShape
		for row in range(len(self.blockShape[newRotate])):
			for column in range(len(self.blockShape[newRotate][row - 2])):
				# Making sure that the space in blockShape is occupied
				if self.blockShape[newRotate][row][column] > 0:
					# Making sure that the x and y values are withing the playing field
					if not row + self.y < len(board) and not column + self.x < len(board[0]):
						print("hit! (side)")
						break

					# Checking for collisions, rotate if collision isn't found
					# TODO Fix this part of the program, doesn't seem to be working
					elif not board[row + self.y][column + self.x] != 0:
						self.rotation = newRotate
						print("rotating...")
					else:
						self.rotation = oldRotate
						print("hit!")
		return

	# Drawing piece on board
	def draw(self, board):
		# Making sure that the newly drawn block won't collide with anything
		if not self.collide(board, 0, 0):
			# Iterating through the blockShape and setting the spaces in the board accordingly
			for i in range(len(self.blockShape[self.rotation])):
				for j in range(len(self.blockShape[self.rotation][i])):
					if self.blockShape[self.rotation][i][j] != 0:
						board[self.y + i][self.x - j] = self.blockShape[self.rotation][i][j]
		# If the block does collide, the player loses
		else:
			print()
			print("You Lose!")
			self.lost = True
			exit()
		# Returns the newly drawn board
		return board

	# Clearing piece that is moving
	def clear(self, board):
		for i in range(len(self.blockShape[self.rotation])):
			for j in range(len(self.blockShape[self.rotation][i])):
				if self.blockShape[self.rotation][i][j] != 0:
					board[self.y + i][self.x - j] = 0
		return board

	# Moving piece down
	def drop(self, board):
		if not self.collide(board, 0, 1):
			self.y += 1
		return

	# Moving piece to the right
	def right(self, board):
		if not self.collide(board, 1, 0):
			self.x += 1
		return

	# Moving piece to the lift
	def left(self, board):
		if not self.collide(board, -1, 0):
			self.x -= 1
		return

	# Slam piece down the farthest it can go
	def slam(self, board):
		for i in range(len(board) - self.y):
			if not self.collide(board, 0, 1):
				self.y += 1

	# Checking if a movement will be valid
	def collide(self, board, move_x, move_y):
		collision = False  # Setting collision to false to allow the block to fall if it doesn't collide with anything
		board = self.clear(board)  # Clearing board as to not detect itself
		# Looping through blockShape to check for collisions
		for i in range(len(self.blockShape[self.rotation])):
			for j in range(len(self.blockShape[self.rotation][i])):
				# Check if the block occupies a space and if so check for collision
				if self.blockShape[self.rotation][i][j] > 0 and board[self.y + i + move_y][self.x - j + move_x]:
					collision = True
					if move_y > 0:
						self.isAtBottom = True
		return collision

	# Losing condition
	def losing(self, board):
		for i in range(len(board[0]) - 2):
			if board[0][i + 1] != 0:
				print()
				print("You lose")
				exit()
		self.lost = True
