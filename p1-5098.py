
board = [0 for x in range(9)]
winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],[0, 3, 6], [1, 4, 7], [2, 5, 8],[0, 4, 8], [2, 4, 6]]
sums = [0 for x in range(len(winning_combinations))]
computer_has_won = False
player_1_has_won = False
player_2_has_won = False
difficulty = 0


def calculate_move():
	pass

def move(player):
	if player == 0:
		print "Player 1: Where do you want to move?"
		move = int(raw_input())
		board[move] = 1
	elif player == 1:
		print "Player 2: Where do you want to move?"
		move = int(raw_input())
		board[move] = 10		
		pass
	elif player == 2:
		calculate_move()
	else:
		pass

def compute_sums():
	for index,combo in enumerate(winning_combinations):
		sum = 0
		for position in combo:
			sum += board[position]
		if sum == 30:
			computer_has_won = True
		elif sum == 3:
			player_1_has_won = True
		sums[index] = sum
			
def game_over():
	compute_sums
	return computer_has_won or player_1_has_won or player_2_has_won

def start_game(a):
	while not game_over():
		print board
		move(0)
		
	if computer_has_won:
		print "Computer has won, player 1 has lost."
	elif player_1_has_won:
		print "Player 1 has won, computer has lost."
	elif player_2_has_won:
		print "Player 2 has won, player 1 has lost."
	else:
		print ""
		
print "Do you want to play against the computer? y/n"
answer = raw_input()
if answer == 'y':
	print "How difficult should the computer the AI be? (1)Beginner/(2)Expert"
	answer = raw_input()
	if answer == 1 or answer == "Beginner":
		difficulty = 1
	elif answer == 2 or answer == "Expert":
		difficulty = 2
	else:
		print "Error invalid selection"
		
	print "Do you want to be x or o? x/o"
	answer = raw_input()
	if answer == 'x' or answer == 'o':
		start_game(answer)
	else:
		print "invalid input"
elif answer == 'n':
	pass
else:
	pass