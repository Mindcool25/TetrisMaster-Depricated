class Block:
    """Class for block object"""

    # Initializing block type when object is created and defining the shape
    def __init__(self, blockType):
        self.x = 4
        self.y = 0
        self.type = blockType
        self.blockShape = []
        self.shape()
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
    def rotate(self):
        self.blockShape = list(zip(*self.blockShape[::-1]))
        return

    # Drawing piece on board
    def draw(self, board):
        for i in range(len(self.blockShape)):
            for j in range(len(self.blockShape[i])):
                board[self.y + i][self.x - j] = self.blockShape[i][j]
        return board

    # Moving piece down
    def drop(self):
        self.y += 1
        return

    # Moving piece to the right
    def right(self):
        self.x += 1
        return

    # Moving piece to the lift
    def left(self):
        self.x -= 1
        return

    

    # Moving piece down
    def drop(self):
        self.y += 1
        return

    # Moving piece to the right
    def right(self):
        self.x += 1
        return

    # Moving piece to the lift
    def left(self):
        self.x -= 1
        return

    