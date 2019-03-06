from __future__ import print_function
import random

class _game():
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    positions = {"left_diagonal" : (0, 4, 8), "right_diagonal" : (2, 4, 6), "top_row" : (0, 1, 2), "middle_row" : (3, 4, 5), "bottom_row" : (6, 7, 8), "left_column" : (0, 3, 6),"middle_column" : (1, 4, 7),"right_column" : (2, 5, 8)}
    sums = {"left_diagonal" : 0, "right_diagonal" : 0, "top_row" : 0, "middle_row" : 0, "bottom_row" : 0, "left_column" : 0,"middle_column" : 0,"right_column" : 0}
    number_of_players = 1
    current_player = 1
    difficulty = 1
    
    def __init__(self):
        self.prompt_number_of_players()
        if self.number_of_players == 1:
            self.prompt_difficulty()
        while not self.check_winner():
            self.print_board()
            self.prompt_move()
            self.calculate_sums()
            self.print_board()
            if self.number_of_players == 2:
                self.prompt_move()
            elif self.number_of_players == 1:
                if self.difficulty == 1:
                    self.board[self.random_move()] = 10
                elif self.difficulty == 2:
                    self.board[self.two_in_a_row_or_block_opponent()] = 10
            self.calculate_sums() 
        else:
            self.print_board()
            print(self.check_winner())

    def empty_spot(self, key):
        for position in self.positions[key]:
            if self.board[position] == 0:
                return position

    def two_in_a_row_or_block_opponent(self):
        two_in_a_row = False
        block = False
        for value in self.sums.itervalues():
            if value == 20:
                two_in_a_row = True
            elif value == 2:
                block = True
        for key in self.sums:
            if self.sums[key] == 20 or ((self.sums[key] == 2 and not two_in_a_row) or (self.sums[key] == 10 and not two_in_a_row and not block)):
                return self.empty_spot(key)
        else:
            return self.random_move()

    def prompt_number_of_players(self):
        print("Do you want to play against a computer or another user?")
        print("1 computer" + '\t' + "2 user")
        answer = int(raw_input())
        if answer == 1 or answer == 2:
            self.number_of_players = answer

    def prompt_difficulty(self):
        print("How difficult do you want the computer to play?")
        print("1 Beginner (Random)" + '\t' + "2 Expert (two-in-a-row + block oppenent")
        answer = int(raw_input())
        if answer == 1 or answer == 2:
            self.difficulty = answer

    def random_move(self):
        move = random.randrange(0, len(self.board))
        while not self.board[move] == 0:
            move = random.randrange(0, len(self.board))
        else:
            return move


    def check_winner(self):
        for key in self.sums:
            if self.sums[key] == 3:
                return "Player 1 has won"
            elif self.sums[key] == 30:
                if self.number_of_players == 1:
                    return "Player 2 has won"
                elif self.number_of_players == 1:
                    "Computer has won"
        else:
            return False

    def prompt_move(self):
        print("Where do want to move?")
        print("0 top left" + '\t' + "1 top middle" + '\t' + "2 top right")
        print("3 middle left" + '\t' + "4 middle" + '\t' + "5 middle right")
        print("6 bottom left" + '\t' + "7 bottom middle" + '\t' + "8 bottom right")
        move = int(raw_input())
        if self.board[move] == 0:
            if self.number_of_players == 2:
                if self.current_player == 1:
                    self.board[move] = 1
                    self.current_player = 2
                elif self.current_player == 2:
                    self.board[move] = 10
                    self.current_player = 1
            else:
                self.board[move] = 1

    def sum_board(self, key):
        sum = 0
        for position in self.positions[key]:
            sum += self.board[position]
        return sum

    def calculate_sums(self):
        for key in self.sums:
            self.sums[key] = self.sum_board(key)
            
    def print_board(self):
        line = '|'
        for index, position in enumerate(self.board):
            if position == 0:
                print(' ', end='')
            elif position == 1:
                print('X', end='')
            elif position == 10:
                print('O', end='')
            if index == 2 or index == 5 or index == 8:
                print('')                
            else:
                print('|', end='')

    






game = _game()




