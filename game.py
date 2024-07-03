from random import randint
from time import sleep
board = [[str(i+j) for i in range(1,4)] for j in range(0,9,3)] 
#print(board)
def get_index(i,j):
    row = (i - 2) // 4
    col = (j - 5) // 10
    return row,col

def print_board():
    print()
    for i in range(13):
        for j in range(31):
            if i % 4 == 0 and j % 10 == 0:
                print("+",end="")
            elif i % 4 == 0 and j % 10 != 0:
                print("-",end="")
            elif i % 4 != 0 and j % 10 == 0:
                print("|",end="")
            elif i % 2 == 0 and i % 4 != 0 and j % 5 == 0 and j % 10 != 0:
                row,col = get_index(i,j)
                print(board[row][col],end="")

            else:
                print(" ",end="")
        print()
    return

def check_row():
    for i in range(3):
        if board[i][0] == board[i][1] and  board[i][2] == board[i][1] and board[i][2] == "x":
            return -1
        elif board[i][0] == board[i][1] and  board[i][2] == board[i][1] and board[i][2] == "o":
            return 1
    else:
        return 0

def check_col():
    for i in range(3):
        if board[0][i] == board[1][i] and  board[2][i] == board[1][i] and board[2][i] == "x":
            return -1
        elif board[0][i] == board[1][i] and  board[2][i] == board[1][i] and board[2][i] == "o":
            return 1
    else:
        return 0

def check_diag():
    check =""
    for i in range(3):
        check+=board[i][i]
    if check == "xxx":
        return -1
    elif check == "ooo":
        return 1
    else:
        check =""
        for i in range(-3,0,1):
            check+=board[i][i]
        if check == "xxx":
            return -1
        elif check == "ooo":
            return 1
        else:
            return 0

def winner():
    return check_diag()+check_row()+check_col() 
def draw(win):
    

    for i in range(3):
        for j in board[i]:
            if j.isnumeric():
                return False
        else:
            return True
    else:
        return False

def valid_inp(inp):
    if not inp.isnumeric():
        return False
    if int(inp) < 10 and int(inp) > 0:
        for i in range(3):
            if inp in board[i]:
                return True
        else:
            return False
    else:
         return False

def take_inp(inp,str1):
    r= (int(inp)-1)//3
    c= (int(inp)-1)%3
    board[r][c]=str1
    print_board()

if __name__== "__main__":
    print_board()
    sleep(1)
    print("my turn: ")
    print("I choose 5")
    board[1][1] = "x"
    itsWin = winner() 
    itsDraw = draw(itsWin)
    print_board()
    while not itsWin and not itsDraw:
        sleep(1)
        print("\n")
        print("==================================")
        inp = input("your turn: ")
        while not valid_inp(inp):
            inp = input("not valid, try something else :")

        take_inp(inp,"o")

        itsWin = winner() 
        itsDraw = draw(itsWin)
        if itsWin:
            break
        print("==================================")
        sleep(1)
        print("now it's my turn!")
        while not valid_inp(inp):
            inp = str(randint(1,9))

        take_inp(inp,"x")
        itsWin = winner() 
        itsDraw = draw(itsWin)
    
    if itsDraw:
        print("Draw (\"_\";)")
    else:
        if itsWin == 1:
            print("it's your win ('>')")
        else:
            print("it's my win :)")


        
        
