class Block:
	"""Class for block object"""

	# Initializing block type when object is created and defining the shape
	def __init__(self, blockType):
		self.x = 6
		self.y = 0
		self.type = blockType
		self.blockShape = []
		self.shape()
		self.isAtBottom = False
		return

	# Setting the shape from block type to a matrix
	def shape(self):
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

	# Easy one liner to rotate the array of a block
	def rotate(self, board):
		backup = self.blockShape
		self.clear(board)
		self.blockShape = list(zip(*self.blockShape[::-1]))
		if self.collide(board, 0, 0):
			self.blockShape = backup
		return

	# Drawing piece on board
	def draw(self, board):
		for i in range(len(self.blockShape)):
			for j in range(len(self.blockShape[i])):
				if self.blockShape[i][j] != 0:
					board[self.y + i][self.x - j] = self.blockShape[i][j]
		return board

	# Clearing piece that is moving
	def clear(self, board):
		for i in range(len(self.blockShape)):
			for j in range(len(self.blockShape[i])):
				if self.blockShape[i][j] != 0:
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
		for i in range(len(self.blockShape)):
			for j in range(len(self.blockShape[i])):
				# Check if the block occupies a space and if so check for collision
				if self.blockShape[i][j] != 0 and board[self.y + i + move_y][self.x - j + move_x]:
					collision = True
					if move_y > 0:
						self.isAtBottom = True
		return collision
