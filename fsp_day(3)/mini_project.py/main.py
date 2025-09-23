try:
    a= str(input("What's your name?"))
    print(a)

    if a.isnumeric():
        raise ValueError(f" Your name can't contain any digits!!!!")
    print(f" Welcome to this game {a}. Let's start!!!!")

except ValueError as v:
    print(v)

game_board= {'top-M': " " , 'top-L': " " , 'top-R': " " ,
             'mid-M': " " , 'mid-L': " " , 'mid-R': " " , 
             'down-M': " " , 'down-L': " " , 'down-R': " "}

def print_board(board):

    print(board['top-M'] + '|' + board['top-L'] + '|' + board['top-R'])
    print("******")

    print(board['mid-M'] + '|' + board['mid-L'] + '|' + board['mid-R'])
    print("******")

    print(board['down-M'] + '|' + board['down-L'] + '|' + board['down-R'])
    print("******")


# try:
def check_condition(board):
    condition=[
        ['top-M', 'top-L', 'top-R'],
        ['mid-M', 'mid-L', 'mid-R'],
        ['down-M', 'down-L', 'down-R'],
        ['top-M', 'mid-M', 'down-M'],
        ['top-L', 'mid-L', 'down-L'],
        ['top-R', 'top-R', 'down-R'],
        ['top-M', 'mid-L', 'down-R'],
        ['down-M', 'mid-L', 'top-R'],
            
    ]

    for i in condition:
        if(board[i[0]]== board[i[1]]== board[i[2]]!= " "):
            return True

        else:
            return False
            
turn= 'X'

for i in range(9):
    print_board(game_board)
    print('Turn for' + turn + '.Move on which space?')
    move= input()
    if(move in game_board and game_board[move]== " "): 
        game_board[move]= turn

    else:
        continue

    if(i>= 5):
        if(check_condition(game_board)):
            print_board(game_board)
        print("Player" + turn + "won!!!")
        exit

    if turn== 'X':
        turn= '0'

    else:
        turn= 'X'

else:
    print_board(game_board)
    print("Game tied!!!!")


# except KeyError as k:





    

