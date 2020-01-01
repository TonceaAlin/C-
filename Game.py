from Human import Human
from Board import Board
class Game:
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        self.last_move = None

    def start(self):
        while True:
            try:
                while True:
                    if self._move(self.player1, 1):
                        break
                    if self._move(self.player2, 2):
                        break
            except:
                pass

    def _move(self, player, value):
        column = -1
        if type(player) is Human:
            self.draw_board()
            column = input("Please insert the column(from 1 to 7)")
            column = int(column)
        self.last_move = player.move(column, value)
        game_status, winner = self.is_Over()
        if game_status is True:
            self.game_over(value)

    def is_Over(self):
        line = self.last_move.get_line()
        column = self.last_move.get_column()
        value = self.last_move.get_value()
        if len(self.board.get_emptyCells()) == 0 or self.board.get_longestSequenceLine() == 4 or self.board.get_longestSequenceColumn() == 4:
            return True, value
        return False, value

    def draw_board(self):
        self.board.ShowBoard()

    def game_over(self, value):
        print("Game over!")
        if value == 1:
            print("You won!!")
        else:
            print("You lost!")
