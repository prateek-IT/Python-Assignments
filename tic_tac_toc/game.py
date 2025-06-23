# tic tak tok game in python

board = ["1", "2", "3","4", "5", "6", "7", "8", "9"]

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    #jeetne ki condiation
    win = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in win:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
        return False
    
    # game start
def play_game():
        turn = "X"
        for i in range (9):
            print_board()
            move = int(input(f"player {turn}, enter position (1-9):"))

            if board[move] == "X" or board[move] == "O":
                print("position already taken. try again.")
                continue

            board[move] = turn

            if check_winner(turn):
                print_board()
                print(f"player {turn} wins!")
                return
            
            #player change kro
            turn = "O" if turn == "X" else "X"

            print_board()
            print("match draw!")
if __name__ == "__main__":
    play_game()






