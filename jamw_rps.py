
from random import choice


def rock_paper_scissors(move, Your_score, Computer_score):



		x = choice("rps")

   		print x

		if move == "r" and x == "r":
			print "I pick rock"
			print "It's a tie!"
			print Your_score, Computer_score
			return Your_score, Computer_score
		elif move == "r" and x == "p":
			print "I pick paper" 
			print "I win"
			print Your_score, Computer_score
			return Your_score, Computer_score + 1
		elif move == "r" and x == "s":
			print "I pick scissors"
			print "You win"
			print Your_score, Computer_score
			return Your_score + 1, Computer_score
		elif move == "p" and x == "r":
			print "I pick rock"
			print "You win"
			print Your_score, Computer_score
			return Your_score + 1, Computer_score
		elif move == "p" and x == "p":
			print "I choose paper"
			print "It's a tie!"
			print Your_score, Computer_score
			return Your_score, Computer_score
		elif move == "p" and x == "s":
			print "I pick scissors"
			print "I win"
			print Your_score, Computer_score
			return Your_score, Computer_score + 1
		elif move == "s" and x == "r":
			print "I pick rock"
			print "I win"
			print Your_score, Computer_score
			return Your_score, Computer_score + 1
		elif move == "s" and x == "p":
			print "I pick paper"
			print "You win"
			print Your_score, Computer_score
			return Your_score + 1, Computer_score
		elif move == "s" and x == "s":
			print "I pick scissors"
			print "It's a tie!"
			print Your_score, Computer_score
			return Your_score, Computer_score


Your_score = 0
Computer_score = 0

print "Hi, I'm Doug the computer. Let's play a game of rock-paper-scissors!"

move = raw_input("Move? or q to quit: ")
while move != "q":
	Your_score, Computer_score = rock_paper_scissors(move, Your_score, Computer_score)
	move = raw_input("Move? or q to quit: ")


print "Final Score is You: %d, Computer: %d" % (Your_score, Computer_score)








