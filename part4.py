from part1 import makeBoard, printBoard
from part2 import traverseBoard, printevalBoard, evalNumber
from part3 import hillDescent

def randomRestarts(x, y, board):
    board = makeBoard(5)
    bestboard = board.copy()
    bestval = evalNumber(traverseBoard(bestboard))
    for i in range(y):
        hillboard = hillDescent(x, board)
        hillval = evalNumber(traverseBoard(hillboard))
        if(hillval <= bestval):
            bestboard = hillboard
            bestval = hillval
        board = makeBoard(5)
    return bestboard


if __name__ == "__main__":
    x = int(input("Iterations? "))
    y = int(input("Hill descents? "))
    board = makeBoard(5)
    randomboard = randomRestarts(x, y, board)
    printBoard(randomboard)
    print("Moves from start:")
    printevalBoard(traverseBoard(randomboard))
    print(evalNumber(traverseBoard(randomboard)))