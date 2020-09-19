from random import seed
from random import randint
def ismoveleft(b):
    for i in range(3):
        for j in range(3):
            if b[i][j]==' ':
                return True

    return False
def findscore(board):
    if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        if board[0][0]=='O':
            return 10
        elif board[0][0]=='X':
            return -10
    if board[0][2]==board[1][1] and board[1][1]==board[2][0]:
        if board[0][2]=='O':
            return 10
        elif board[0][2]=='X':
            return -10
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2]:
            if board[i][0]=='O':
                return 10
            elif board[i][0]=='X':
                return -10
    for i in range(3):
        if board[0][i]==board[1][i] and board[1][i]==board[2][i]:
            if board[0][i]=='O':
                return 10
            elif board[0][i]=='X':
                return -10
    return 0
def minmax(b1,ismax):
    score=findscore(b1)
    

    if score==10:
        return score
    if score==-10:
        return score
    
    if ismoveleft(b1)==False:
        
        
        return 0
    if ismax==True:
        
        best=-9999
        for i in range(3):
            
            for j in range(3):
                if b1[i][j]==' ':
                    b1[i][j]='O'
                    best=max(best,minmax(b1,not ismax))
                    b1[i][j]=' '
        return best
    else:
        
        best=9999
        for i in range(3):
            for j in range(3):
                if b1[i][j]==' ':
                    b1[i][j]='X'
                    k=minmax(b1,not ismax)
                    
                    best=min(best,k)
                    
                    b1[i][j]=' '
        return best
def findbestmove(b):
    bestval=-9999
    row=-1
    clm=-1
    for i in range(3):
        for j in range(3):
            if b[i][j]==' ':
                board[i][j]='O'
                
                moveval=minmax(b,False)
                
                b[i][j]=' '
                if moveval>bestval:
                    row=i
                    clm=j
                    bestval=moveval
    
    Move=[row,clm]
    return Move

def printboard(board):
    
    for i in range(R): 
        print("---------------------")
        
        for j in range(C): 
            print("  "+ board[i][j], end = "   |") 
        print()
    print("---------------------")

def createemptyboard(board):
    for i in range(R):          
        a =[] 
        for j in range(C):      
            a.append(' ') 
        board.append(a)
    return board
def maketoss():
    selection=input("THE ONE WHO WINS THE TOSS GOES FIRST \nHeads OR Tails\n")
    value=randint(0,1)

    if value==0:
        toss="Heads"
    else:
        toss="Tails"
    print("TOSS:"+toss)
    if selection==toss:
        print("\nYOU GO FIRST")
        turn="Human"
        return turn

    else:
        print("\nCOMPUTER GOES FIRST")
        turn="Computer"
        return turn
def setpos(pos):
    if pos==1:
        row=0
        clm=0
    if pos==2:
        row=0
        clm=1
    if pos==3:
        row=0
        clm=2
    if pos==4:
        row=1
        clm=0
    if pos==5:
        row=1
        clm=1
    if pos==6:
        row=1
        clm=2
    if pos==7:
        row=2
        clm=0
    if pos==8:
        row=2
        clm=1
    if pos==9:
        row=2
        clm=2
    arr=[row,clm]
    return arr
def playgame(board,turn):
    while(ismoveleft(board)):
        if(findscore(board)==10):
            print("\n****YOU LOST****\n")
            return
        if(findscore(board)==-10):
            print("\n***YOU WON****\n")
            return
        if turn=="Human":
            
            
            
            pos=int(input("Enter the position you want to put"))
            arr=setpos(pos)
            row=arr[0]
            clm=arr[1]
            if board[row][clm]==' ':
                board[row][clm]='X'
                printboard(board)
                turn="Computer"
            else:
                print("!!!Already filled!!!")

            
        elif turn=="Computer":
            Move=findbestmove(board)
            row=Move[0]
            clm=Move[1]
            board[row][clm]='O'
            print("Computer:")
            printboard(board)
            turn="Human"
    print("\n*****ITS A TIE****\n")   
R = 3
C = 3
board = []
turn="" 
row=-1
clm=-1
board=createemptyboard(board)


turn=maketoss()
printboard(board)
playgame(board,turn)







