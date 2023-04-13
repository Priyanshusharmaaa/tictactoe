def check(board):
    for i in board:
        for j in i:
            if(j == ' '):
                return False

    return True

board = [[' ' for i in range(0,3)] for j in range(0,3)]
print(board[0])
print(board[1])
print(board[2])

gameover = False
n= 0
player1 = input("enter preferred char")
player2 = input("enter prefferred char")

while(gameover == False and player1 != player2):
    if(n%2==0):
        row = int(input("enter row"))
        cols = int(input("enter cols"))
        board[row][cols] = player1
        n+=1
    
    else:
        row = int(input("enter row"))
        cols = int(input("enter cols"))
        board[row][cols] = player2
        n+=1
    
    gameover = check(board)
f = 0
for i in board:
    ch = player1
    for j in i:
        if(ch != j):
            f= 1
            break
    if(f == 0):
        print("player1 is winner")
        break
    else:
        ch1 = player2
        for j in i:
            if(ch1 != j):
                f = 0
                break
    if(f==1):
        print("player2 is winner")
        break
for i in range(0,3):
    ch = player1
    for j in range(0,3):
        if(board[j][i] != ch):
            ch = player2
            break
    if(ch == player1):
        print("player1 is winner")
        break
    else:
        for j in range(0,3):
            if(board[j][i] != ch):
                ch = player1
                break
        if(ch == player2):
            print("player2 is winner")
            break
ch  = player1
if(board[0][0] == ch and board[1][1] == ch and board[2][2] == ch):
    print("player1 is winner")
else:
    print("player2 is winner")
print(board[0])
print(board[1])
print(board[2])







