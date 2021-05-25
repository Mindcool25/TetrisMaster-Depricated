class Block:
    # Initalizing block type when object is created and defining the shape
    def __init__(self, blockType):
        self.type = blockType
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