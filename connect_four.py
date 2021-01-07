import numpy as np
import pygame
import sys
pygame.init()
COLUMNS = 12
ROWS = 8

ITEM_SIZE = 100
width = COLUMNS * ITEM_SIZE
height = (ROWS + 1) * ITEM_SIZE  # +1 cause we need extra space at the top for the coin


# make array with zeros
def make_board():
    our_board = np.zeros((ROWS, COLUMNS))
    return our_board


board = make_board()
print(board)


# get index of last element in a column
def index_to_add(our_board, place_index):
    for row in range(ROWS):
        if our_board[row][place_index] == 0:
            return row
    return ROWS


# add element == drop one element at the end of column
def add_element(our_board, place_index, element_to_add):
    row = index_to_add(our_board, place_index)
    our_board[row][place_index] = element_to_add
    return our_board


# function that checks if the game was won by either of the players
def check_if_win(our_board):
    for rows in range(ROWS):
        for column in range(COLUMNS):
            if our_board[rows][column] == 0:
                continue
            else:
                player = our_board[rows][column]
                #print(rows, column)
                if column >= 3:  # check left side horizontally 3,4,5,6
                    if our_board[rows][column - 1] == player and  our_board[rows][column - 2] == player and our_board[rows][column - 3] == player:
                        print("1 opcja")
                        return player
                if column < COLUMNS - 3:  # check right side horizontally 0,1,2,3
                    if our_board[rows][column + 1] == player and  our_board[rows][column + 2] == player and our_board[rows][column + 3] == player:
                        print("2 opcja")
                        #print(our_board[rows][column], our_board[rows][column + 1], our_board[rows][column + 2], our_board[rows][column + 3])
                        return player
                if rows >= 3:  # check upper vertically 3,4,5
                    if our_board[rows - 1][column] == player and our_board[rows - 2][column] == player and our_board[rows - 3][column] == player:
                        print("3 opcja")
                        return player
                if rows < ROWS - 3:  # check lower vertically 0,1,2
                    if our_board[rows + 1][column] == player and our_board[rows + 2][column] == player and our_board[rows + 3][column] == player:
                        #print(our_board[rows][column], rows, column)
                        #print(our_board[rows + 1][column], rows + 1, column, "  ", our_board[rows + 2][column], our_board[rows + 2][column])
                        print("4 opcja")
                        return player
                if column < COLUMNS - 3 and rows < ROWS - 3: # check right diagonally "na ukos"
                    if our_board[rows + 1][column + 1] == player and our_board[rows + 2][column + 2] == player and our_board[rows + 3][column + 3] == player:
                        print("5 opcja")
                        #print(our_board[rows][column], our_board[rows + 1][column + 1], our_board[rows + 2][column + 2], our_board[rows + 3][column + 3])
                        return player

                if column >= 3 and rows < ROWS - 3:  # check left diagonally
                    if our_board[rows + 1][column - 1] == player and our_board[rows + 2][column - 2] == player and our_board[rows + 3][column - 3] == player:
                        print("6 opcja")
                        return player
    return 0  # there is no win


# check if element we want to add could fit inside the map.  error when = (too away to left, right, or at the top)
def is_valid(our_board, place_index):
    if place_index >= COLUMNS or place_index < 0 or index_to_add(our_board, place_index) == ROWS:
        return False
    else:
        return True


# print whole board
def show_board(our_board):
    our_board = np.flip(our_board, 0)  # odwrocic pionowo
    print(our_board)


# Draw board
def draw_board():
    pygame.draw.rect(screen, "blue", (0, ITEM_SIZE, width, height))


# Draw black circles
def draw_circles():
    for rows in range(ROWS):
        for columns in range(COLUMNS):
            pygame.draw.circle(screen, "black", (ITEM_SIZE / 2 + columns * ITEM_SIZE, ITEM_SIZE*1.5 + rows * ITEM_SIZE), ITEM_SIZE / 2 - 5)


def draw_black_rect_at_the_top():
    pygame.draw.rect(screen, "black", (0, 0, width, ITEM_SIZE))


screen_size = (width, height)
#screen = pygame.display.set_mode(screen_size)
#draw_board()
#draw_circles()
#draw_black_rect_at_the_top()
#pygame.display.update()

who_turn = 1
game_over = False
while not game_over:

    """for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_coordinate = event.pos[0]
            print(event.pos, x_coordinate)
            place = x_coordinate // ITEM_SIZE
            print(place)
            pygame.draw.circle(screen, "red",(event.pos[0], ITEM_SIZE / 2), ITEM_SIZE /2)
            pygame.display.update()
        if event.type == pygame.MOUSEMOTION:
            x_coordinate = event.pos[0]
            print(event.pos, x_coordinate)
            place = x_coordinate // ITEM_SIZE
            print(place)
            draw_board()
            draw_circles()
            draw_black_rect_at_the_top()
            pygame.draw.circle(screen, "red", (event.pos[0], ITEM_SIZE / 2), ITEM_SIZE / 2)
            pygame.display.update()"""

    if who_turn == 1:
        who_turn = 2
        place = int(input("Graczu nr1: gdzie chcesz odlozyc swoj element?"))
        type_again = True
        while type_again:
            if not is_valid(board, place):
                print("Element jest poza tablica, wczytaj ponownie")
                place = int(input("Graczu nr1: gdzie chcesz odlozyc swoj element?"))
            else:
                type_again = False
        add_element(board, place, 1)
    else:
        who_turn = 1
        piece = 2
        place = int(input("Graczu nr2: gdzie chcesz odlozyc swoj element?"))
        if not is_valid(board, place):
            print("Element jest poza tablica, wczytaj ponownie")
            place = int(input("Graczu nr2: gdzie chcesz odlozyc swoj element?"))
        else:
            type_again = False
        add_element(board, place, 2)
    show_board(board)
    if check_if_win(board) == 1:
        print("brawp wygral gracz nr 1")
        game_over = True
    elif check_if_win(board) == 2:
        print("brawp wygral gracz nr 2")
        game_over = True
    else:
        print("gra jeszcze trwa Lecimy Duuuuuur!")
print("end of game")
show_board(board)
