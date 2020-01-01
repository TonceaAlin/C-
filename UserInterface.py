from Board import Board
from Human import Human
from Computer import Computer
from GUI import *



def menu():
        startMessage = int(input("Press '1' to start the game or '0' to exit"))
        if startMessage == 1:
            board = Board()
            player1 = Human("Human wannabe",1 )
            player2 = Computer(2, 1, 4)
            def checkColumnInteger(message):
                if message.isdigit():
                    column = int(message)
                    if column > 0 and column < 8:
                        return True
                return False

            while (board.isDraw() == False):
                humanColumn = input(player1.get_name() + ", choose your column: ")
                while (checkColumnInteger(humanColumn) == False):
                    humanColumn = input("Please choose a number between 1 and 7: ")
                humanColumn = int(humanColumn)
                humanColumn -= 1
                while board.move(player1.get_value(), humanColumn) == False:
                    humanColumn = input("Please choose a column which is not full: ")
                    while (checkColumnInteger(humanColumn) == False):
                        humanColumn = input("Please choose a number between 1 and 7: ")
                    humanColumn = int(humanColumn)
                    humanColumn -= 1
                print(board)
                if board.isGameWon() == True:
                    print(player1.get_name() + " wins.")
                    break
                computerColumn = int(player2.move(board))
                print("The computer chose column: " + str(computerColumn + 1))
                board.move(player2.get_value(), computerColumn)
                print(board)
                if board.isGameWon() == True:
                    print("The computer wins.")
                    break

            if board.isDraw() == True:
                print("Draw")

            print("\n")
            print("\n")


        elif startMessage == 0:
            return

        else:
            print("please, try again")
            menu()



interfaceType = input("Press '1' for Graphical user interface or '2' for a simple user interface")
if int(interfaceType) == 2:
    menu()
else:
    window = tk.Tk()
    window.wm_title("Connect4")
    gui_board = BoardFrame(window)
    window.mainloop()


