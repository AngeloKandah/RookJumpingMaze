import numpy
import random
from part1 import makeBoard, printBoard
def traverseBoard(board):
    evalboard = numpy.zeros([board.shape[0],board.shape[0]], dtype = int)
    frontier = []
    frontier.append((0,0,0))
    while len(frontier) > 0:
        current = frontier.pop(0)
        if((current[1] + board[current[0],current[1]]) < board.shape[0]):
            if(evalboard[(current[0], current[1]+board[current[0],current[1]])] == 0):
                frontier.append((current[0], current[1]+board[current[0],current[1]], current[2]+1))
                evalboard[(current[0], current[1]+board[current[0],current[1]])] = current[2]+1

        if((current[1] - board[current[0],current[1]]) >= 0):
            if(evalboard[(current[0], current[1]-board[current[0],current[1]])] == 0):
                frontier.append((current[0], current[1]-board[current[0],current[1]], current[2]+1))
                evalboard[(current[0], current[1]-board[current[0],current[1]])] = current[2]+1

        if((current[0] + board[current[0],current[1]]) < board.shape[0]):
            if(evalboard[(current[0] + board[current[0],current[1]], current[1])] == 0):
                frontier.append((current[0] + board[current[0],current[1]], current[1], current[2]+1))
                evalboard[(current[0] + board[current[0],current[1]], current[1])] = current[2]+1

        if((current[0] - board[current[0],current[1]]) >= 0):
            if(evalboard[(current[0] - board[current[0],current[1]], current[1])] == 0):
                frontier.append((current[0] - board[current[0],current[1]], current[1],current[2]+1))
                evalboard[(current[0] - board[current[0],current[1]], current[1])] = current[2]+1
    return evalboard

def printevalBoard(evalboard):
    for row in range(evalboard.shape[0]):
        if(row > 0):
            print()
        for col in range(evalboard.shape[1]):
            if(row == 0 and col == 0):
                print("", 0, end= " ")
            elif(evalboard[row,col] == 0):
                print("--", end= " ")
            elif(evalboard[row,col] >= 10):
                print(evalboard[row,col], end = " ")
            else:
                print("", evalboard[row,col], end= " ")
    print()

def evalNumber(evalboard):
    if(evalboard[evalboard.shape[0]-1,evalboard.shape[1]-1] == 0):
        return 1000000
    else:
        return evalboard[evalboard.shape[0]-1,evalboard.shape[1]-1]*-1
                
if __name__ == "__main__":
    board = makeBoard(5)
    printBoard(board)
    print("Moves from start:")
    printevalBoard(traverseBoard(board))
    print(evalNumber(traverseBoard(board)))
    