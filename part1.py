import numpy
import random
def makeBoard(x):
    board = numpy.random.randint(1, x, size=(x,x))
    for row in range(board.shape[0]):
        for col in range(board.shape[1]):
            if(board.shape[0]%2 == 1):
                if(col > board.shape[0]/2):
                    if(col - board[row,col] < 0):
                        board[row,col] = random.randint(1, round(board.shape[0]/2)+1)
                else:
                    if(board[row,col] + col + 1 > 5):
                        board[row,col] = random.randint(1, round(board.shape[0]/2)+1)       
                if(col == round((x-1)/2) and row == round((x-1)/2)):
                    board[row,col] = random.randint(1, round(board.shape[0]/2))
            else:
                if(col > board.shape[0]/2):
                    if(col - board[row,col] < 0):
                        board[row,col] = random.randint(1, round(board.shape[0]/2)+1)
                else:
                    if(board[row,col] + col + 1 > 5):
                        board[row,col] = random.randint(1, round(board.shape[0]/2)+1)       
                if(col == round((x-1)/2) and row == round((x-1)/2)):
                    board[row,col] = random.randint(1, round(board.shape[0]/2))
                if(col == round(x/2) and row == round(x/2)):
                    board[row,col] = random.randint(1, round(board.shape[0]/2))
                if(col == round((x-1)/2) and row == round(x/2)):
                    board[row,col] = random.randint(1, round(board.shape[0]/2))
                if(col == round(x/2) and row == round((x-1)/2)):
                    board[row,col] = random.randint(1, round(board.shape[0]/2))
    
    board[x-1,x-1] = 0
    return board

def printBoard(board):
    for row in range(board.shape[0]):
        if row > 0: 
            print()
        for col in range(board.shape[1]): 
            print(board[row,col], end = " ")
    print()


if __name__ == "__main__":
    x = int(input("Rook Jumping Maze size (5-10)? "))   
    while(x < 5 or x > 10):
        print("Please choose between 5 and 10")
        x = int(input("Rook Jumping Maze size (5-10)? ")) 
    board = makeBoard(x)
    printBoard(board)