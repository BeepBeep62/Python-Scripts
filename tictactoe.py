board = {
    '9': " ",
    '8': " ",
    '7': " ",
    '6': " ",
    '5': " ",
    '4': " ",
    '3': " ",
    '2': " ",
    '1': " "
}
def print_board(board): #Print Board
    print(board['7']+'|'+board['8']+'|'+board['9']+'|')
    print("-------")
    print(board['4']+'|'+board['5']+'|'+board['6']+'|')
    print("-------")
    print(board['1']+'|'+board['2']+'|'+board['3']+'|')
count = 0
turn = "X"
for i in range(0,10):
    print_board(board)
    print("its ur turn, "+turn+", which place you want to move to? enter a number from 1 to 9")
    move = input("enter a number from 1 to 9: ")
    if board[move]==" ":
        board[move]=turn
        count = count+1
    else:
        print("Occupied")
        continue
    if count >= 5:
        if board['7'] == board['8'] == board['9'] != " ":
            print_board(board)
            print("game over yu won")
            break
        elif board['4'] == board['5'] == board['6'] != " ":
            print_board(board)
            print("game over yu won")
            break
        elif board['3'] == board['2'] == board['1'] != " ":
            print_board(board)
            print("game over yu won")
            break
        elif board['1'] == board['4'] == board['7'] != " ":
            print_board(board)
            print("game over yu won")
            break
        elif board['2'] == board['5'] == board['8'] != " ":
            print_board(board)
            print("game over yu won")
            break
        elif board['3'] == board['6'] == board['9'] != " ":
            print_board(board)
            print("game over yu won")
            break
        elif board['7'] == board['5'] == board['3'] != " ":
            print_board(board)
            print("game over yu won")
            break
        elif board['1'] == board['5'] == board['9'] != " ":
            print_board(board)
            print("game over yu won")
            break
    if count == 9:
        print("NOBODY OF U WON?!!?!?!?! plesmnds es")
    if turn=="X":
        turn = "O"
    else:
        turn = "X"