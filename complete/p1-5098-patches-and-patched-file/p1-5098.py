from __future__ import print_function
import random

class _board():
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    positions = {"left_diagonal" : (0, 4, 8), "right_diagonal" : (2, 4, 6), "top_row" : (0, 1, 2), "middle_row" : (3, 4, 5), "bottom_row" : (6, 7, 8), "left_column" : (0, 3, 6),"middle_column" : (1, 4, 7),"right_column" : (2, 5, 8)}
    sums = {"left_diagonal" : 0, "right_diagonal" : 0, "top_row" : 0, "middle_row" : 0, "bottom_row" : 0, "left_column" : 0,"middle_column" : 0,"right_column" : 0}
    
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.current_player = 1
        pass
        
    def __str__(self):
        output = ""
        line = "|"
        for index, position in enumerate(self.board):
            if position == 0:
                output += " "
            elif position == 1:
                output += "X"
            elif position == 10:
                output += "O"
            if index == 2 or index == 5 or index == 8:
                output += "\n"             
            else:
                output += line
        return output

    def sum_board(self, key):
        sum = 0
        for position in self.positions[key]:
            sum += self.board[position]
        return sum

    def calculate_sums(self):
        for key in self.sums:
            self.sums[key] = self.sum_board(key)

    def empty_spot(self, key):
        for position in self.positions[key]:
            if self.board[position] == 0:
                return position            
                
    def move(self, position):
        if self.board[position] == 0:
            if self.number_of_players == 2:
                if self.current_player == 1:
                    self.board[move] = 1
                    self.current_player = 2
                elif self.current_player == 2:
                    self.board[move] = 10
                    self.current_player = 1
            else:
                self.board[move] = 1
        self.calculate_sums()
                
    def check_winner(self):
        for key in self.sums:
            if self.sums[key] == 3:
                return "Player 1 has won"
            elif self.sums[key] == 30:
                if self.number_of_players == 2:
                    return "Player 2 has won"
                elif self.number_of_players == 1:
                    "Computer has won"
        else:
            return False
            
    def available_moves(self):
        positions = []
        for position in self.board:
            if self.board[position] == 0:
                positions.append(position)
        return positions

    def available_winning_moves(self):
        positions = self.available_moves()
        winning_positions = []
        for key in self.sums:
            if self.sums[key] == 20:
                for position in self.positions[key]:
                    if position in positions:
                        winning_positions.append(position)
        return winning_positions
        
    def available_blocking_moves(self):
        positions = self.available_moves()
        blocking_positions = []
        for key in self.sums:
            if self.sums[key] == 2:
                for position in self.positions[key]:
                    if position in positions:
                        blocking_positions.append(position)
        return blocking_positions
        
    def available_improving_moves(self):
        positions = self.available_moves()
        improving_positions = []
        for key in self.sums:
            if self.sums[key] == 10:
                for position in self.positions[key]:
                    if position in positions:
                        improving_positions.append(position)
        return improving_positions
        
class _game():
    difficulty = 1
    
    def __init__(self):
        self.board = _board(self.prompt_number_of_players())

        if self.board.number_of_players == 1:
            self.prompt_difficulty()
            
        while not self.board.check_winner():
            print(self.board)
            self.board.move(self.prompt_move())
            print(self.board)
            if self.number_of_players == 2:
                self.board.move(self.prompt_move())
            elif self.number_of_players == 1:
                if self.difficulty == 1:
                    self.board.move(self.random_move())
                elif self.difficulty == 2:
                    self.board.move(self.two_in_a_row_or_block_opponent())
        else:
            print(self.board)
            print(self.check_winner())

    def two_in_a_row_or_block_opponent(self):
        two_in_a_row = False
        block = False
        winning_positions = self.board.available_winning_moves()
        if len(winning_positions) > 0:
            return winning_positions[0]
        blocking_positions = self.board.available_blocking_moves()
        if len(blocking_positions) > 0:
            return blocking_positions[0]
        improving_positions = self.board.available_improving_moves()
        if len(improving_positions) > 0:
            return improving_positions
        return self.random_move()

    def prompt_number_of_players(self):
        print("Do you want to play against a computer or another user?")
        print("1 computer" + '    ' + "2 user")
        answer = int(input())
        if answer == 1 or answer == 2:
            return answer

    def prompt_difficulty(self):
        print("How difficult do you want the computer to play?")
        print("1 Beginner (Random)" + '    ' + "2 Expert (two-in-a-row + block oppenent")
        answer = int(input())
        if answer == 1 or answer == 2:
            self.difficulty = answer

    def random_move(self):
        available_moves = self.board.available_moves()
        if len(available_moves) > 0:
            return available_moves[random.randrange(0, len(available_moves))]

    def prompt_move(self):
        print("Where do want to move?")
        print("0 top left" + '    ' + "1 top middle" + '    ' + "2 top right")
        print("3 middle left" + '    ' + "4 middle" + '    ' + "5 middle right")
        print("6 bottom left" + '    ' + "7 bottom middle" + '    ' + "8 bottom right")
        return int(input())

game = _game()
