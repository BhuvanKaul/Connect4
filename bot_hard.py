import numpy as np
import sys
import math
import random
import pygame

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


def hard_bot_move(board):
    # Check if the bot can win in the next move
    for col in range(COLUMN_COUNT):
        temp_board = board.copy()
        if is_valid_location(temp_board, col):
            row = get_next_open_row(temp_board, col)
            drop_piece(temp_board, row, col, 2)
            if winning_move(temp_board, 2):
                return col

    # Check if the human can win in the next move and block
    for col in range(COLUMN_COUNT):
        temp_board = board.copy()
        if is_valid_location(temp_board, col):
            row = get_next_open_row(temp_board, col)
            drop_piece(temp_board, row, col, 1)
            if winning_move(temp_board, 1):
                return col

    # If neither winning nor blocking move is available, choose the column with the largest chain
    max_chain = -1
    best_col = random.choice(range(COLUMN_COUNT))

    for col in range(COLUMN_COUNT):
        temp_board = board.copy()
        if is_valid_location(temp_board, col):
            row = get_next_open_row(temp_board, col)
            drop_piece(temp_board, row, col, 2)
            current_chain = count_chain(temp_board, row, col, 2)
            if current_chain > max_chain:
                max_chain = current_chain
                best_col = col

    return best_col


def count_chain(board, row, col, piece):
    # Count the length of the chain in all possible directions
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    max_chain = 0

    for dir in directions:
        dx, dy = dir
        chain = 1

        for i in range(1, 4):
            x, y = col + i * dx, row + i * dy
            if 0 <= x < COLUMN_COUNT and 0 <= y < ROW_COUNT and board[y][x] == piece:
                chain += 1
            else:
                break

        for i in range(1, 4):
            x, y = col - i * dx, row - i * dy
            if 0 <= x < COLUMN_COUNT and 0 <= y < ROW_COUNT and board[y][x] == piece:
                chain += 1
            else:
                break

        max_chain = max(max_chain, chain)

    return max_chain


def full(board):
    top_row = board[5]
    for top_piece in top_row:
        if top_piece == 0:
            return False
    return True


def hard_bot():
    global SQUARESIZE, screen, height, RADIUS

    board = create_board()
    #print_board(board)
    game_over = False
    turn = 0

    pygame.init()

    SQUARESIZE = 100

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT + 1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE / 2 - 5)

    screen = pygame.display.set_mode(size)
    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN and turn == 0:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = myfont.render("Human wins!!", 1, RED)
                        screen.blit(label, (width // 2 - label.get_width() // 2, 10))
                        pygame.display.update()
                        game_over = True

                    turn += 1
                    turn = turn % 2

                    #print_board(board)
                    draw_board(board)


        # Bot's turn
        if turn == 1 and not game_over:
            col = hard_bot_move(board)
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_move(board, 2):
                label = myfont.render("Bot wins!!", 1, YELLOW)
                screen.blit(label, (width // 2 - label.get_width() // 2, 10))
                pygame.display.update()
                game_over = True

            #print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

        if full(board) and not game_over:
            print("OK")
            label = myfont.render("Draw!!", 1, WHITE)
            screen.blit(label, (230, 10))
            game_over = True

        pygame.display.update()

        if not game_over:
            pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)

        if game_over:
            pygame.time.wait(3000)


