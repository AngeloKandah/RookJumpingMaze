import random
import numpy
from part1 import makeBoard, printBoard
from part2 import printevalBoard, traverseBoard, evalNumber

def hillDescent(iterations, board):
    bestboard = board.copy()
    besteval = evalNumber(traverseBoard(bestboard))
    for i in range(iterations):
        evalboard = bestboard.copy()
        move = (random.randint(0,board.shape[0]-1), random.randint(0,board.shape[0]-1))
        while move == (board.shape[0]-1,board.shape[0]-1):
            move = (random.randint(0,board.shape[0]-1), random.randint(0,board.shape[0]-1))

        prev = evalboard[move]
        evalboard[move] = random.randint(1,board.shape[0]-1)
        evalboard[move] = checkMove(move, evalboard)
        while evalboard[move] == prev:
            evalboard[move] = random.randint(1,board.shape[0]-1)
            evalboard[move] = checkMove(move, evalboard)
        new = evalNumber(traverseBoard(evalboard))
        if(new <= besteval):
            besteval = new
            bestboard = evalboard.copy()
    return bestboard

def checkMove(move, evalboard):
    row = move[0]
    col = move[1]
    num = evalboard[move]
    x = evalboard.shape[0]
    if(col > evalboard.shape[0]/2):
        if(col - evalboard[row,col] < 0):
             num = random.randint(1, round(evalboard.shape[0]/2)+1)
    else:
        if(evalboard[row,col] + col + 1 > evalboard.shape[0]):
             num = random.randint(1, round(evalboard.shape[0]/2)+1)       
    if(col == round((x-1)/2) and row == round((x-1)/2)):
        num = random.randint(1, round(evalboard.shape[0]/2))
    return num

if __name__ == "__main__":
    x = int(input("Iterations? "))
    board = makeBoard(5)
    hillboard = hillDescent(x, board)
    printBoard(hillboard)
    print("Moves from start:")
    printevalBoard(traverseBoard(hillboard))
    print(evalNumber(traverseBoard(hillboard)))
