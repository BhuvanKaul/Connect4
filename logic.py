import random


def validate_input(prompt, valid_inputs):
    user_attempt = input(prompt)

    while user_attempt not in valid_inputs:
        print("Invalid input, please try again.")
        user_attempt = input(prompt)
    return user_attempt


# Copy and paste create_board here
def create_board():
    """
    Returns a 2D list of 6 rows and 7 columns to represent
    the game board. Default cell value is 0.

    :return: A 2D list of 6x7 dimensions.
    """
    # Implement your solution below

    board = [[0 for y in range(7)] for x in range(6)]

    return board


# Copy and paste print_board here
def print_board(board):
    """
	Prints the game board to the console.

	:param board: The game board, 2D list of 6x7 dimensions.
	:return: None
	"""
    print("========== Connect4 =========")
    print("Player 1: X       Player 2: O\n")
    print("  1   2   3   4   5   6   7")
    print(" --- --- --- --- --- --- ---")

    for row in board:
        row_str = "|"
        for cell in row:
            if cell == 0:
                row_str += "   |"
            elif cell == 1:
                row_str += " X |"
            elif cell == 2:
                row_str += " O |"
        print(row_str)
        print(" --- --- --- --- --- --- ---")

    print("=============================")


# Define drop_piece function
def drop_piece(board, player, column):
    """
	Drops a piece into the game board in the given column.
	Please note that this function expects the column index
	to start at 1.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player dropping the piece, int.
	:param column: The index of column to drop the piece into, int.
	:return: True if piece was successfully dropped, False if not.
	"""

    # Check if the column is already full
    if board[0][column - 1] != 0:
        return False

    # Find the lowest empty cell in the selected column
    row = 5
    while row >= 0:
        if board[row][column - 1] == 0:
            break
        row -= 1
    # Place the player's token in the lowest empty cell
    board[row][column - 1] = player

    return True


def end_of_game(board):  # Question 6
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of 6 rows x 7 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
    """
    # if there is still a spot that = 0, and no one has won, end_of_game should = 0
    # which should allow the game to continue
    # if player 1 or 2 has 4 spots in a row (4 spots in a row = 1 or 4 spots in a row = 2),
    # end_of_game = 1 or 2 respectively which will result in a player winning and the game ending
    # if all the spots on the board are occupied, and no one has won the game (no 4 in a row),
    # then print 3 for a draw

    # Winning in straight
    # for some y, if there are any combination of x coordinates where there are 4 in a row eg. x1, x2, x3 and x4 = 2 then p2 wins
    for x in range(2, 4):
        for y in range(7):
            if (board[x][y] == board[x - 1][y] and board[x][y] == board[x + 1][y] and board[x][y] != 0):
                if (board[x][y] == board[x - 2][y] or board[x][y] == board[x + 2][y]):
                    return board[x][y]

    # Winning in line
    # similar to straight however for y coords changing instead of x
    for x in range(6):
        for y in range(2, 5):
            if (board[x][y] == board[x][y - 1] and board[x][y] == board[x][y + 1] and board[x][y] != 0):
                if (board[x][y] == board[x][y - 2] or board[x][y] == board[x][y + 2]):
                    return board[x][y]

    # Winning in diagonal
    # combination of winning in a line and winning in a straight, where (x1,y1), (x2,y2), (x3,y3) and (x4,y4) are all the same given value
    for x in range(1, 4):
        for y in range(1, 6):
            if (y < 6):  # Right diagonal
                if (board[x][y] == board[x - 1][y - 1] and board[x][y] == board[x + 1][y + 1] and board[x][y] != 0):
                    if (board[x][y] == board[x + 2][y + 2]):
                        return board[x][y]
            if (y >= 2):
                if (board[x][y] == board[x - 1][y + 1] and board[x][y] == board[x + 1][y - 1] and board[x][y] != 0):
                    if (board[x][y] == board[x + 2][y - 2]):
                        return board[x][y]

    # For continuing play
    # if there is no combination of spots where there are 4 in a row, the ga me is not over and therefore should be continued
    for x in range(6):
        for y in range(7):
            if (board[x][y] == 0):
                return 0

    # For draw
    # if there is no remaining spaces on the board, none of the above conditions will be met and therefore the board will return a draw
    return 3


# Don't forget to include any helper functions you may have created


def clear_screen():
    """
    Clears the terminal for Windows and Linux/MacOS.

    :return: None
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def local_2_player_game():
    """
    Runs a local 2 player game of Connect 4.

    :return: None
    """
    # Implement your solution below
    board = create_board()
    progress = end_of_game(board)
    player = 1
    count = 0
    prev_move = 0
    clear_screen()
    while (progress == 0):
        print_board(board)

        if (count == 1):
            print("Player", 1 if player == 2 else 2, "dropped a piece into column", prev_move)

        print("Player:", player)

        move = int(validate_input("please enter the column you would like to drop: ", "1, 2, 3, 4, 5, 6, 7"))

        while (drop_piece(board, player, move) is False):
            print("That column is full, please try again.")
            move = int(validate_input("please enter the column you would like to drop: ", "1, 2, 3, 4, 5, 6, 7"))

        prev_move = move
        if (player == 1):
            player = 2
        else:
            player = 1

        count = 1
        progress = end_of_game(board)
        clear_screen()

    print_board(board)
    if (progress == 1):
        print("Player 1 won\n")
    elif (progress == 2):
        print("Player 2 won\n")
    else:
        print("Draw\n")

    sth = input("Press Enter to go back to menu\n")

    return main()


# ==== End ====
def valid_column(board):
    return [col for col in range(7) if board[0][col] == 0]


def cpu_player_easy(board, player):
    """
    Executes a move for the CPU on easy difficulty. This function
    plays a randomly selected column.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below

    ran_move = random.choice(valid_column(board))
    drop_piece(board, player, ran_move + 1)

    return ran_move + 1


# cpu_player_medium
def cpu_player_medium(board, cpu_piece):
    player_piece = 1 if cpu_piece == 2 else 2

    # Check if there is any column left for computer to play
    valid_cols = valid_column(board)

    # Check if CPU can win
    for col in valid_cols:
        temporary_board = [row[:] for row in board]
        # drop every piece in ever column in the board
        drop_piece(board, cpu_piece, col + 1)
        # After drop piece to the board, check if the cpu can win
        if (end_of_game(board) != 0):
            board[:] = temporary_board
            drop_piece(board, cpu_piece, col + 1)
            return col + 1
        board[:] = temporary_board

    # Check if CPU needs to block human player
    for col in valid_cols:
        temporary_board = [row[:] for row in board]
        # drop in every column in the board
        drop_piece(board, player_piece, col + 1)
        # After drop piece to the board, check if the player win, to block
        if (end_of_game(board) != 0):
            board[:] = temporary_board
            drop_piece(board, cpu_piece, col + 1)
            return col + 1
        board[:] = temporary_board

    # Otherwise, make a random move
    left_column = random.choice(valid_cols)
    drop_piece(board, cpu_piece, left_column + 1)
    return left_column + 1


# Don't forget to include any helper functions you may have created

def print_rules():
    """
    Prints the rules of the game.

    :return: None
    """
    clear_screen()
    print("================= Rules =================")
    print("Connect 4 is a two-player game where the")
    print("objective is to get four of your pieces")
    print("in a row either horizontally, vertically")
    print("or diagonally. The game is played on a")
    print("6x7 grid. The first player to get four")
    print("pieces in a row wins the game. If the")
    print("grid is filled and no player has won,")
    print("the game is a draw.")
    print("=========================================")
    sth = input("Press enter to back menu\n")
    return main()


def game_against_cpu():
    option = input("Choose difficulty level 1 (easy), 2 (medium), 3 (hard): ")
    board = create_board()
    count = 0
    cpu_player = 1
    player = 2

    if option == "3":
        go_f_s = "2"

    else:
        # Choose to go first or second
        go_f_s = input("Press 1 to go first, 2 to go second: ")



    if (go_f_s == "2"):
        if (option == "1"):
            move = cpu_player_easy(board, cpu_player)
        elif (option == "2"):
            move = cpu_player_medium(board, cpu_player)
        elif option == "3":
            move = cpu_player_hard(board)

    clear_screen()

    progress = end_of_game(board)

    while (progress == 0):
        print_board(board)

        if (count == 0 and go_f_s == "2"):
            print("CPU dropped a piece into column: ", move)

        if (count == 1):
            print("CPU dropped a piece into column: ", prev_move)

        print("Your next move!")

        move = int(validate_input("please enter the column you would like to drop: ", "1, 2, 3, 4, 5, 6, 7"))

        while (drop_piece(board, player, move) is False):
            print("That column is full, please try again.")
            move = int(validate_input("please enter the column you would like to drop: ", "1, 2, 3, 4, 5, 6, 7"))

        if (option == "1"):
            move = cpu_player_easy(board, cpu_player)
        elif (option == "2"):
            move = cpu_player_medium(board, cpu_player)
        elif option == "3":
            move = cpu_player_hard(board)

        prev_move = move

        count = 1
        progress = end_of_game(board)
        clear_screen()

    print_board(board)

    if (progress == 1):
        print("CPU_Player won")
    elif (progress == 2):
        print("Player won")
    else:
        print("Draw")

    return None


def main_menu():
    clear_screen()
    print("=============== Main Menu ===============")
    print("Welcome to Connect 4!")
    print("1. View Rules")
    print("2. Play a local 2 player game")
    print("3. Play a game against the computer")
    print("4. Exit")
    print("=========================================")
    print()


def main():
    clear_screen()
    """
    Defines the main application loop.
    User chooses a type of game to play or to exit.

    :return: None
    """
    # Implement your solution below
    main_menu()
    option = int(input("Choose options: "))

    if (option == 1):
        print_rules()
        print("Press anything and hit enter to go back")
    elif (option == 2):
        local_2_player_game()
    elif (option == 3):
        game_against_cpu()
    elif (option == 4):
        quit()

    return None


def search_horizontal(board, row_index, element_index, user):
    longest_chain_right, longest_chain_left = 1, 1

    # checking towards right for the longest chain
    check_element_index = element_index + 1
    while check_element_index <= 6:
        if board[row_index][check_element_index] == user:
            longest_chain_right += 1
            check_element_index += 1
        else:
            break

    # checking towards left for the longest chain
    check_element_index = element_index - 1
    while check_element_index >= 0:
        if board[row_index][check_element_index] == user:
            longest_chain_left += 1
            check_element_index -= 1
        else:
            break

    if longest_chain_right > longest_chain_left:
        return [longest_chain_right, 'horizontal', 'right']
    else:
        return [longest_chain_left, 'horizontal', 'left']


def search_vertical(board, row_index, element_index, user):
    longest_chain = 1

    # checking downwards only for longest chain
    check_row_index = row_index + 1
    while check_row_index < 6:
        if board[check_row_index][element_index] == user:
            longest_chain += 1
            check_row_index += 1
        else:
            break

    return [longest_chain, 'vertical', 'down']


def search_diagonally(board, row_index, element_index, user):
    longest_chain_right, longest_chain_left = 1, 1

    # checking diagonally towards the lower right positions for the longest chain
    check_row_index = row_index + 1
    check_element_index = element_index + 1
    while check_row_index < 6 and check_element_index <= 6:
        if board[check_row_index][check_element_index] == user:
            longest_chain_right += 1
            check_row_index += 1
            check_element_index += 1
        else:
            break

    # checking diagonally towards the lower left positions for the longest chain
    check_row_index = row_index + 1
    check_element_index = element_index - 1
    while check_row_index < 6 and check_element_index >= 0:
        if board[check_row_index][check_element_index] == user:
            longest_chain_left += 1
            check_row_index += 1
            check_element_index -= 1
        else:
            break

    if longest_chain_right > longest_chain_left:
        return [longest_chain_right, 'diagonal', 'right']
    else:
        return [longest_chain_left, 'diagonal', 'left']


def search_row_index(board, column_index):
    for row_index in range(5, -1, -1):
        if board[row_index][column_index] == 0:
            return row_index


def compare_chain_lengths(board, row_index, element_index, user):
    horizontal = search_horizontal(board, row_index, element_index, user)
    vertical = search_vertical(board, row_index, element_index, user)
    diagonal = search_diagonally(board, row_index, element_index, user)

    if horizontal[0] >= vertical[0] and horizontal[0] >= diagonal[0]:
        longest_chain_orientation = horizontal
    elif vertical[0] > horizontal[0] and vertical[0] >= diagonal[0]:
        longest_chain_orientation = vertical
    else:
        longest_chain_orientation = diagonal

    return longest_chain_orientation


round_one = True


def cpu_player_hard(board):
    global round_one
    """
    Executes a move for the CPU on hard difficulty.
    This function creates a copy of the board to simulate moves.

    <Insert player strategy here>

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: None
    """

    # Making the cpu go first because it increases the chances of winning
    cpu_piece = 1
    player_piece = 2

    # Check if there is any column left for computer to play
    valid_cols_index = valid_column(board)

    if round_one:
        drop_piece(board, cpu_piece, 3)
        round_one = False
        return 3
    else:
        # Check if CPU can win
        for col in valid_cols_index:
            temporary_board = [row[:] for row in board]
            # drop every piece in ever column in the board
            drop_piece(board, cpu_piece, col + 1)
            # After drop piece to the board, check if the cpu can win
            if (end_of_game(board) == 1):
                board[:] = temporary_board
                drop_piece(board, cpu_piece, col + 1)
                return col + 1
            board[:] = temporary_board

        # Check if CPU needs to block human player
        for col in valid_cols_index:
            temporary_board = [row[:] for row in board]
            # drop in every column in the board
            drop_piece(board, player_piece, col + 1)
            # After drop piece to the board, check if the player win, then block
            if (end_of_game(board) == 2):
                board[:] = temporary_board
                drop_piece(board, cpu_piece, col + 1)
                return col + 1
            board[:] = temporary_board

        # If the cpu can't win nor block it will move strategically, to make the longest chain possible

        tries = []

        for cols in valid_cols_index:

            temporary_board = [row[:] for row in board]
            # drop in every column in the board
            drop_piece(temporary_board, cpu_piece, cols + 1)
            row_index = search_row_index(board, cols)
            longest_chain = compare_chain_lengths(temporary_board, row_index, cols, 1)
            tries.append([cols, longest_chain])

        longest_chain_length = 0
        longest_chain = None
        for each_try in tries:
            if each_try[1][0] > longest_chain_length:
                longest_chain = each_try
                longest_chain_length = each_try[1][0]
        drop_piece(board, cpu_piece, longest_chain[0] + 1)
        return longest_chain[0] + 1


main()
