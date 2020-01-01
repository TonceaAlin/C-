class Board:
    def __init__(self):
        self.matrix = [[0]*7 for line in range(6)]

    def __str__(self):
        string = '------------------\n'
        for line in range(6):
            for column in range(7):
                string += '|'
                if self.matrix[line][column] == 0:
                    string += "~"
                elif self.matrix[line][column] == 1:
                    string += "X"
                else:
                    string += "O"

            string += '|\n'
            string += '---------------\n'
        return string

    def move(self, value, column):
        #makes a move on the table
        #input - the value to be put in the matrix and the chosen column for the move
        #output - true if the move is possible, false otherwise
        line = 5
        while line > -1:
            if self.matrix[line][column] == 0:
                self.matrix[line][column] = value
                return True
            line -= 1
        return False

    def isGameWon(self):
        # checks if the game was won (each possible way in the matrix)
        # returns true if it was, false otherwise
        for line in range(6):
            for column in range(4):
                if self.matrix[line][column] != 0:
                    if self.matrix[line][column] == self.matrix[line][column + 1] and self.matrix[line][column] == self.matrix[line][column + 2] and self.matrix[line][column] == self.matrix[line][column + 3]:
                        return True

        for line in range(7):
            for column in range(3):
                if self.matrix[column][line] != 0:
                    if self.matrix[column][line] == self.matrix[column + 1][line] and self.matrix[column][line] == self.matrix[column + 2][line] and self.matrix[column][line] == self.matrix[column + 3][line]:
                        return True

        for line in range(3):
            for column in range(4):
                if self.matrix[line][column] != 0:
                    if self.matrix[line][column] == self.matrix[line + 1][column + 1] and self.matrix[line][column] == self.matrix[line + 2][column + 2] and self.matrix[line][column] == self.matrix[line + 3][column + 3]:
                        return True

        for line in range(3):
            column = 6
            while column > 2:
                if self.matrix[line][column] != 0:
                    if self.matrix[line][column] == self.matrix[line + 1][column - 1] and self.matrix[line][column] == self.matrix[line + 2][column - 2] and self.matrix[line][column] == self.matrix[line + 3][column - 3]:
                        return True
                column -= 1

        return False

    def isDraw(self):
        #checks if the game is a draw
        #return true if the game is a draw, false otherwise
        for line in range(6):
            for column in range(7):
                if self.matrix[line][column] == 0:
                    return False
        return True

