from Board import Board
class Computer():

    def __init__(self, playerValue, enemyValue, difficulty):
        self.player = playerValue
        self.difficulty = difficulty
        self.enemy = enemyValue

    def get_value(self):
        #returns the value for our player(player2 in this case)
        return self.player


    def islegalmove(self, board, column):
        #checks if the actual move is a good one( with the given column)
        #the move is ok if we have 0 in that position
        #returns true if it is or false if it is not
        line = 5
        while line > -1:
            if board.matrix[line][column] == 0:
                return True
            line -= 1
        return False

    def simulatemove(self, board, column, playerValue):
        # simulates a move for the actual board
        # input - the board, the column for the move, and the value to be put in the column
        # returns a new board with the move done
        board2 = Board()
        for line in range(6):
            for eachColumn in range(7):
                board2.matrix[line][eachColumn] = board.matrix[line][eachColumn]
        board2.move(playerValue, column)
        return board2

    def move(self, board):
        #function that searches for the best move to made
        #input - a possible state of the game
        #output - the best move to be made based on the bestscore
        legalmoves = {}
        for column in range(7):
            if self.islegalmove(board, column):
                board2 = self.simulatemove(board, column, self.player)
                legalmoves[column] = -self.find(self.difficulty - 1, board2, self.enemy)

        bestscore = -99999999
        bestmove = None
        moves = legalmoves.items()
        for move,score in moves:
            if score > bestscore:
                bestscore = score
                bestmove = move

        return bestmove

    def find(self, depth, board, playerValue):
        #function that finds the score of a move
        #input - depth of the connection, the board and the value to look for
        #output - the score of the given state of the game
        legalmoves = []
        for column in range(7):
            if self.islegalmove(board, column):
                board2 = self.simulatemove(board, column, playerValue)
                legalmoves.append(board2)
        if depth == 0 or len(legalmoves) == 0 or board.isGameWon():
            return self.value(board, playerValue)

        if playerValue == self.player:
            enemyValue = self.enemy
        else:
            enemyValue = self.player
        score = -99999999
        for eachMatrix in legalmoves:
            score = max(score, -self.find(depth - 1, eachMatrix, enemyValue))
        return score

    def value(self, board, playerValue):
       #calculates the value for the actual table using minmax algorithm
       #input - the actual board, the value
       #output - a score for this configuration
        if playerValue == self.player:
            enemyValue = self.enemy
        else:
            enemyValue = self.player

        playerFours = self.checkForConnection(board, playerValue, 4)
        playerThrees = self.checkForConnection(board, playerValue, 3)
        playerTwos = self.checkForConnection(board, playerValue, 2)
        enemyFours = self.checkForConnection(board, enemyValue, 4)
        enemyThrees = self.checkForConnection(board, enemyValue, 3)
        enemyTwos = self.checkForConnection(board, enemyValue, 2)
        if enemyFours > 0:
            return -100000
        else:
            return playerFours*100000 + playerThrees*100 + playerTwos - enemyThrees*100 - enemyTwos

    def checkForConnection(self, board, playerValue, length):
       #function that calculates the number of connections for different lengths
       #input - the game board, the value to look for and the length
       #output - total connections ( horizontal , vertical and digonal)
        count = 0
        for line in range(6):
            for column in range(7):
                if board.matrix[line][column] == playerValue:
                    count += self.findVerticalConnection(line, column, board, length, board.matrix[line][column])
                    count += self.findHorizontalConnection(line, column, board, length, board.matrix[line][column])
                    count += self.findDiagonalConnection(line, column, board, length, board.matrix[line][column])
        return count

    def findVerticalConnection(self, line, column, board, length, playerValue):
       #function that looks for vertical connections in the board
       #input - line and column, the board, the length for the connection and the value to look for
       #output - 1 if we find a connection and 0 otherwise
        count = 0
        if line + length - 1 < 6:
            for iterator in range(length):
                if board.matrix[line + iterator][column] == playerValue:
                    count += 1
                else:
                    break

        if count == length:
            return 1
        else:
            return 0

    def findHorizontalConnection(self, line, column, board, length, playerValue):
        #function that checks how many connections we have on horizontal positions
        #input - line and column , the board, length of the connection and the value to look for
        #output - 1 if we find a connection of the wanted length, 0 otherwise
        count = 0
        if column + length - 1 < 7:
            for iterator in range(length):
                if playerValue == board.matrix[line][column + iterator]:
                    count += 1
                else:
                    iterator = length + 1
        if count == length:
            return 1
        else:
            return 0

    def findDiagonalConnection(self, line, column, board, length, playerValue):
      #function that checks how many connections on diagonal we have
      #input - a certain line and a certain column, the board, the length we are looking for and the value too look for on the board
      #output - total connections
        total = 0
        count = 0
        if column + length - 1 < 7 and line + length - 1 < 6:
            for iterator in range(length):
                if playerValue == board.matrix[line + iterator][column + iterator]:
                    count += 1
                else:
                    iterator = length + 1
        if count == length:
            total += 1

        count = 0
        if column + length - 1 < 7 and line - length + 1 > -1:
            for iterator in range(length):
                if playerValue == board.matrix[line - iterator][column + iterator]:
                    count += 1
                else:
                    iterator = length + 1
        if count == length:
            total += 1

        return total


