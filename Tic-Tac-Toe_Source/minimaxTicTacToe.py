import math
player,opponent='x','o'

def changePlayer(n):
    global player,opponent
    if(n==0):
        player,opponent="x","o"
    else:
        player,opponent="o","x"
def isMoveLeft(board):
    for i in board:
        if("_" in i):
            return True
    return False

def evaluate(b):
    for row in range(3) :    
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :       
            if (b[row][0] == player) :
                return 10
            elif (b[row][0] == opponent) :
                return -10
    for col in range(3) :
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
            if (b[0][col] == player) :
                return 10
            elif (b[0][col] == opponent) :
                return -10
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
        if (b[0][0] == player) :
            return 10
        elif (b[0][0] == opponent) :
            return -10
 
    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
        if (b[0][2] == player):
            return 10
        elif (b[0][2] == opponent) :
            return -10
    return 0
def minimax(board,depth,isMax):
    score=evaluate(board)
    if(score==10 or score==-10):
        return (score,depth)
    if(not isMoveLeft(board)):
        return (0,depth)
    if(isMax):
        best=(-math.inf,-1)
        for i in range(3):
            for j in range(3):
                if(board[i][j]=='_'):
                    board[i][j]=player
                    bestVal=minimax(board,depth+1,not isMax)
                    if(best[0]<bestVal[0]):
                        best=bestVal
                    board[i][j]="_"
        return best
    else:
        best=(math.inf,-1)
        for i in range(3):
            for j in range(3):
                if(board[i][j]=="_"):
                    board[i][j]=opponent
                    bestVal=minimax(board,depth+1,not isMax)
                    if(bestVal[0]<best[0]):
                        best=bestVal
                    board[i][j]="_"
        return best
def findBestMove(board):
    bestVal=(-math.inf,-1)
    bestMove=(-1,-1,-1)
    for i in range(3):
        for j in range(3):
            if(board[i][j]=="_"):
                board[i][j]=player
                moveVal=minimax(board,0,False)
                board[i][j]="_"
                if(moveVal[0]>bestVal[0] or (moveVal[1]<bestVal[1] and moveVal[0]==bestVal[0])):
                    bestVal=moveVal
                    bestMove=(i,j,bestVal)
    return bestMove
def displayBoard(board):
    for i in board:
        for j in i:
            print(j,end=" ")
        print()
    print("\n\n")
def start(board):
    return findBestMove(board)

