import tkinter as tk

class BoardCanvas(tk.Canvas):

    def __init__(self, master=None, heigth=0, width=0):

        tk.Canvas.__init__(self, master, heigth=heigth, width=width)
        self.draw_gameBoard()

    def draw_gameBoard(self):
        self.create_oval()


class BoardFrame(tk.Frame):
    """The Frame Widget is mainly used as a geometry master for other widgets, or to
    provide padding between other widgets.
    """

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        #self.create_widgets()

    #def create_widgets(self):
        #self.boardCanvas = BoardCanvas(height=550, width=480)
        #self.boardCanvas.bind('<Button-1>', self.boardCanvas.gameLoop)
        #self.boardCanvas.pack()
