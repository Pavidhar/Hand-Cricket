
from random import randint
from random import choice

print("WELCOME TO HAND CRICKET")
t=int(input("Input 1 to show rules, Input anything else to continue "))
if t==1:
	print("OVERVIEW AND RULES\nThis is a Player vs Computer Game.\nA Side bats first and then the other tries to score more runs than them.\nBoth the sides; the batting and the bowling side takes out a number between 1 and 10, both included.\nIf the numbers match, the Batsman loses his/her wicket.\nIf the numbers don’t match than the number taken out by the batsman is added in their total score.\nThe game has 2 modes: Easy and Hard. Each has similar gameplay but as the name suggest, one is harder than the other. You need to input ‘1’ for Easy and ‘2’ for Hard mode.\nIf you win the randomly decided toss, then input ‘1’ for Batting and ‘2’ for bowling.\nNext you input a number between 1-10 and the computer also outputs a number between 1-10, and the game continues.\n\n ")

while True:
	runs_player=0
	runs_computer=0
	out=["Ball goes Straight into the fielder's hand!","Straight to the stumps!!","Ball hits the pad...The Umpire gives the finger!","Thrown Straight to the stumps...RUN OUT",]
	mode=int(input("Choose a mode:\nInput 1 for Easy Mode\nInput 2 for Hard Mode\nInput anything else to quit\n"))

	def playerfirst():
		while True:
			global runs_player
			global runs_computer
			Comp=randint(1,10)
			Player=int(input("Play a shot:"))
			
			if Comp!=Player:
				print("Computer:",Comp)
				runs_player += Player
				print("                                    Score:",runs_player)
			else:
				print("Computer:",Comp)
				print(choice(out))
				print("OUT! You scored:",runs_player,"runs.")
				break

		while runs_computer<=runs_player:
			#giving a 1/4+ probability of taking the wicket
			z=randint(1,4)
			if z==1:
				Player=int(input("Throw a ball:"))
				print("Computer:",Player)
				print(choice(out))
				print("OUT! Computer scored:",runs_computer)
				break
			else:
				Comp=randint(1,10)
				Player=int(input("Throw a ball:"))
				print("Computer:",Comp)
				if Comp!=Player:
					runs_computer+=Comp
					print("                                    Score:",runs_computer)
				else:
					print(choice(out))
					print("OUT! Computer scored:",runs_computer,"runs.")
					break
	def compfirst():
		
		global runs_player
		global runs_computer
		while True:
			#giving a 1/3+ probability of taking the wicket
			z=randint(1,3)
			if z==1:
				Player=int(input("Throw a ball:"))
				print("Computer:",Player)
				print(choice(out))
				print("OUT! Computer scored:",runs_computer)
				break
			else:
				Comp=randint(1,10)
				Player=int(input("Throw a ball:"))
				print("Computer:",Comp)
				if Comp!=Player:
					runs_computer+=Comp
					print("                                    Score:",runs_computer)
				else:
					print(choice(out))
					print("OUT! Computer scored:",runs_computer,"runs.")
					break

		while runs_computer>=runs_player:
			Comp=randint(1,10)
			Player=int(input("Play a shot:"))
			print("Computer: ",Comp)
			if Comp!=Player:
				runs_player+=Player
				print("                                    Score:",runs_player)
			else:
				print(choice(out))
				print("OUT! You scored:",runs_player,"runs.")
				break
	def easy():
		toss=randint(1,2)
		#50%-50% probability of a toss outcome
		if toss==1:
			x=input("You Won the toss. Choose :\nInput 1 to Bat\nInput 2 to Ball\nInput anything else to quit")
			if x==1:
				playerfirst()
			elif x==2:
				compfirst()
		else:
			#computer has equal probability of choosing batting or bowling.
			y=randint(1,2)
			if y==1:
				print("Computer has selected to ball first.")
				playerfirst()
			else:
				print("Computer has selected to bat first.")
				compfirst()
	def hard():
		global runs_player
		global runs_computer
		tosshard=randint(1,2)
		if tosshard==1:
			batball=int(input("You Won the toss. Choose :\nInput 1 for Bat\nInput 2 for Ball\nInput anything else to quit\n"))
			if batball==1:
				while True:
					Player=int(input("Play a shot:"))
					z=randint(1,4)
					#1/4+ probability the computer takes your wicket
					if z==1:
						Comp=Player
						print("Computer:",Comp)
						print(choice(out))
						print("OUT! You scored:",runs_player,"runs.")
						break
					else:
						Comp=randint(1,10)
						if Comp==Player:
							print("Computer:",Comp)
							print(choice(out))
							print("OUT! You scored:",runs_player,"runs.")
							break
						else:
							print("Computer:",Comp)
							runs_player+=Player
							print("                                    Score:",runs_player)
				while runs_player>=runs_computer:
					Player=int(input("Throw a ball:"))
					Comp=randint(1,10)
					if Comp==Player:
						print("Computer:",Comp)
						print(choice(out))
						print("OUT! Computer Scored:",runs_computer,"runs")
						break
					else:
						print("Computer:",Comp)
						runs_computer+=Comp
						print("                                    Score:",runs_computer)
			elif batball==2:
			
				while True:
					Player=int(input("Throw a ball:"))
					Comp=randint(1,10)
					print("Computer:",Comp)
					if Comp==Player:
						print(choice(out))
						print("OUT! Computer Scored:",runs_computer,"runs")
						break
					else:
						runs_computer+=Comp
						print("                                    Score:",runs_computer)
				while runs_computer>=runs_player:
						Player=int(input("Play a shot:"))
						z=randint(1,4)
						if z==1:
							Comp=Player
							print("Computer:",Comp)
							print(choice(out))
							print("OUT! You scored:",runs_player,"runs.")
							break
						else:
							Comp=randint(1,10)
							if Comp==Player:
								print("Computer:",Comp)
								print(choice(out))
								print("OUT! You scored:",runs_player,"runs.")
								break
							else:
								print("Computer:",Comp)
								runs_player+=Player
								print("                                    Score:",runs_player)
		else:
			print("Computer won the toss")
			#comp chooses bat or ball
			compchoose=randint(1,2)
			if compchoose==1:
				print("Computer has choosen to Ball first.")
				while True:
					Player=int(input("Play a shot:"))
					z=randint(1,4)
					if z==1:
						Comp=Player
						print("Computer:",Comp)
						print(choice(out))
						print("OUT! You scored:",runs_player,"runs.")
						break
					else:
						Comp=randint(1,10)
						if Comp==Player:
							print("Computer:",Comp)
							print(choice(out))
							print("OUT! You scored:",runs_player,"runs.")
							break
						else:
							print("Computer:",Comp)
							runs_player+=Player
							print("                                    Score:",runs_player)
				while runs_player>=runs_computer:
					Player=int(input("Throw a ball:"))
					Comp=randint(1,10)
					print("Computer:",Comp)
					if Comp==Player:
						print(choice(out))
						print("OUT! Computer Scored:",runs_computer,"runs")
						break
					else:
						runs_computer+=Comp
						print("                                    Score:",runs_computer)
			else:
				print("Computer has choosen to Bat first")
				while True:
					Player=int(input("Throw a ball:"))
					Comp=randint(1,10)
					print("Computer:",Comp)
					if Comp==Player:
						print(choice(out))
						print("OUT! Computer Scored:",runs_computer,"runs")
						break
					else:
						runs_computer+=Comp
						print("                                    Score:",runs_computer)
				while runs_computer>=runs_player:
						Player=int(input("Play a shot:"))
						z=randint(1,4)
						#making probabilty of comp matching player high
						if z==1:
							Comp=Player
							print("Computer:",Comp)
							print(choice(out))
							print("OUT! You scored:",runs_player,"runs.")
							break
						else:
							Comp=randint(1,10)
						
							if Comp==Player:
								print("Computer:",Comp)
								print(choice(out))
								print("OUT! You scored:",runs_player,"runs.")
								break
							else:
								print("Computer:",Comp)
								runs_player+=Player
								print("                                    Score:",runs_player)

	if mode==1:	
		print("EASY MODE\n")
		easy()
	else:
		print("HARD MODE\n")
		hard()


	if runs_player>runs_computer:
		print("\nYOU WON! by",runs_player-runs_computer,"runs.",end="\n\n")
	elif runs_computer==runs_player:
		print("\nTIE!! You both scored",runs_player,"runs.",end="\n\n")
	else:
		print("\nBETTER LUCK NEXT TIME. YOU LOST by",runs_computer-runs_player,"runs.",end="\n\n")
	#to quit or play again..for exiting or re entering the main while loop
	r=int(input("Input 1 to Play Again\nInput anything else to Quit\n"))
	if r==1:
		continue
	else:
		exit()
