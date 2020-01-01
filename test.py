from Human import Human
from Computer import Computer
from Board import Board
import unittest


class testBoard(unittest.TestCase):

    def test_emptyboard_gameNotWon(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        self.assertFalse(board.isGameWon())

    def test_notEmptyBoard_gameNotWon(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.matrix[0][1] = value1
        board.matrix[0][1] = value1
        board.matrix[0][2] = value1
        board.matrix[0][3] = value2
        self.assertFalse(board.isGameWon())

    def test_notEmptyBoard_gameWon(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.matrix[0][0] = value1
        board.matrix[1][0] = value1
        board.matrix[2][0] = value1
        board.matrix[3][0] = value1
        self.assertTrue(board.isGameWon())

    def test_emptyBoard_notDraw(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        self.assertFalse(board.isDraw())

    def test_notEmptyBoard_notDraw(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.matrix[0][3] = value1
        board.matrix[1][4] = value2
        self.assertFalse(board.isDraw())

    def test_notEmptyBoard_draw(self):
        '''
        X O X O X O
        X O X O X O
        O X O X O X
        O X O X O X
        X O X O X O
        X O X O X O
        '''
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        for column in range(7):
            if column % 2 == 0:
                board.matrix[0][column] = value1
                board.matrix[1][column] = value1
                board.matrix[2][column] = value2
                board.matrix[3][column] = value2
                board.matrix[4][column] = value1
                board.matrix[5][column] = value1
            else:
                board.matrix[0][column] = value2
                board.matrix[1][column] = value2
                board.matrix[2][column] = value1
                board.matrix[3][column] = value1
                board.matrix[4][column] = value2
                board.matrix[5][column] = value2
        self.assertTrue(board.isDraw())

    def test_emptyBoard_movePossible(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.move(value1, 2)
        self.assertTrue(board.matrix[5][2] == value1)

    def test_notEmptyBoard_moveNotPossible(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.move(value1, 3)
        board.move(value1, 3)
        board.move(value1, 3)
        board.move(value1, 3)
        board.move(value1, 3)
        board.move(value1, 3)
        self.assertFalse(board.move(value2, 3))

class testHuman(unittest.TestCase):
    def test_getName(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        self.assertTrue(player1.get_name() == "juan")
    def test_getValue(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        self.assertTrue(player1.get_value() == 1)

class testComputer(unittest.TestCase):
    def test_getValue(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        self.assertTrue(player2.get_value() == 2)

        '''
    |~|~|O|~|~|~|~|
    ---------------
    |~|~|X|~|~|~|~|
    ---------------
    |~|~|O|~|~|~|~|
    ---------------
    |~|~|X|~|~|~|~|
    ---------------
    |~|X|O|~|~|~|~|
    ---------------
    |X|O|O|~|~|~|~|
        '''

    def test_isLegalMove_notLegal(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.move(value1, 3)
        board.move(value1, 3)
        board.move(value1, 3)
        board.move(value1, 3)
        board.move(value1, 3)
        board.move(value1, 3)
        self.assertFalse(player2.islegalmove(board, 3))

    def test_verticalConnections_length2(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.matrix[5][0] = value1
        board.matrix[4][1] = value1
        board.matrix[3][2] = value1
        board.matrix[5][1] = value2
        board.matrix[5][2] = value2
        board.matrix[4][2] = value2
        board.matrix[2][2] = value2
        board.matrix[1][2] = value1
        board.matrix[0][2] = value2
        self.assertTrue(player2.findVerticalConnection(4, 2, board, 2, value2) == 1)

    def test_verticalConnections_length3(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.matrix[5][0] = value1
        board.matrix[4][1] = value1
        board.matrix[3][2] = value1
        board.matrix[5][1] = value2
        board.matrix[5][2] = value2
        board.matrix[4][2] = value2
        board.matrix[2][2] = value2
        board.matrix[1][2] = value1
        board.matrix[0][2] = value2
        self.assertTrue(player2.findVerticalConnection(4, 2, board, 3, value2) == 0)

    def test_horizontalConnections_length2(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.matrix[5][0] = value1
        board.matrix[4][1] = value1
        board.matrix[3][2] = value1
        board.matrix[5][1] = value2
        board.matrix[5][2] = value2
        board.matrix[4][2] = value2
        board.matrix[2][2] = value2
        board.matrix[1][2] = value1
        board.matrix[0][2] = value2
        self.assertTrue(player2.findHorizontalConnection(5, 1, board, 2, value2) == 1)

    def test_horizontalConnections_length3(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.matrix[5][0] = value1
        board.matrix[5][3] = value2
        board.matrix[4][1] = value1
        board.matrix[3][2] = value1
        board.matrix[5][1] = value2
        board.matrix[5][2] = value2
        board.matrix[4][2] = value2
        board.matrix[2][2] = value2
        board.matrix[1][2] = value1
        board.matrix[0][2] = value2
        self.assertTrue(player2.findHorizontalConnection(5, 1, board, 3, value2) == 1)

    def test_digonalConnections_length2(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.matrix[5][0] = value1
        board.matrix[4][1] = value1
        board.matrix[3][2] = value1
        board.matrix[5][1] = value2
        board.matrix[5][2] = value2
        board.matrix[4][2] = value2
        board.matrix[2][2] = value2
        board.matrix[1][2] = value1
        board.matrix[0][2] = value2
        self.assertTrue(player2.findDiagonalConnection(5, 1, board, 2, value2) == 1)

    def test_digonalConnections_length3(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.matrix[5][0] = value1
        board.matrix[4][1] = value1
        board.matrix[3][2] = value1
        board.matrix[5][1] = value2
        board.matrix[5][2] = value2
        board.matrix[4][2] = value2
        board.matrix[2][2] = value2
        board.matrix[1][2] = value1
        board.matrix[0][2] = value2
        self.assertTrue(player2.findDiagonalConnection(5, 0, board, 3, value1) == 1)

    def test_checkConnections_player_length2(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.matrix[5][0] = value1
        board.matrix[4][1] = value1
        board.matrix[3][2] = value1
        board.matrix[5][1] = value2
        board.matrix[5][2] = value2
        board.matrix[4][2] = value2
        board.matrix[2][2] = value2
        board.matrix[1][2] = value1
        board.matrix[0][2] = value2
        self.assertTrue(player2.checkForConnection(board,value1,2) == 2)

    def test_checkConnections_player_length3(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.matrix[5][0] = value1
        board.matrix[4][1] = value1
        board.matrix[3][2] = value1
        board.matrix[5][1] = value2
        board.matrix[5][2] = value2
        board.matrix[4][2] = value2
        board.matrix[2][2] = value2
        board.matrix[1][2] = value1
        board.matrix[0][2] = value2
        self.assertTrue(player2.checkForConnection(board, value1, 3) == 1)

    def test_checkConnections_player_length4(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.matrix[5][0] = value1
        board.matrix[4][1] = value1
        board.matrix[3][2] = value1
        board.matrix[5][1] = value2
        board.matrix[5][2] = value2
        board.matrix[4][2] = value2
        board.matrix[2][2] = value2
        board.matrix[1][2] = value1
        board.matrix[0][2] = value2
        self.assertTrue(player2.checkForConnection(board, value1, 4) == 0)

    def test_checkConnections_computer_length2(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.matrix[5][0] = value1
        board.matrix[4][1] = value1
        board.matrix[3][2] = value1
        board.matrix[5][1] = value2
        board.matrix[5][2] = value2
        board.matrix[4][2] = value2
        board.matrix[2][2] = value2
        board.matrix[1][2] = value1
        board.matrix[0][2] = value2
        self.assertTrue(player2.checkForConnection(board, value2, 2) == 3)

    def test_checkConnections_computer_length3(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.matrix[5][0] = value1
        board.matrix[4][1] = value1
        board.matrix[3][2] = value1
        board.matrix[5][1] = value2
        board.matrix[5][2] = value2
        board.matrix[4][2] = value2
        board.matrix[2][2] = value2
        board.matrix[1][2] = value1
        board.matrix[0][2] = value2
        self.assertTrue(player2.checkForConnection(board, value2, 3) == 0)

    def test_checkConnections_computer_length4(self):
        player1 = Human("juan", 1)
        player2 = Computer(2, 1, 4)
        board = Board()
        value1 = 1
        value2 = 2
        board.matrix[5][0] = value1
        board.matrix[4][1] = value1
        board.matrix[3][2] = value1
        board.matrix[5][1] = value2
        board.matrix[5][2] = value2
        board.matrix[4][2] = value2
        board.matrix[2][2] = value2
        board.matrix[1][2] = value1
        board.matrix[0][2] = value2
        self.assertTrue(player2.checkForConnection(board, value2, 4) == 0)


if __name__ == '__main__':
    unittest.main()
