from tkinter import *
import random

#game class that handles all scores, and player moves
class game:
	def __init__(self):
		self._name = None
		self.playerScore = 0
		self.computerScore = 0
		self.draw = 0

	def display(self,name):
		self._name = name
		print(self._name)
		textWindow.insert(1.0,"Your choice: {}".format(name) +'\n')

	def playComputer(self,window,player):
		options = ["rock","paper","scissors"]
		num = random.randint(0,2)
		textWindow.insert(1.0,"Computers choice: {}".format(options[num] + '\n'))
		textWindow.insert(1.0,player+ '\n')

		#score lable for computer
		computerLabel = Label(window, text="Computer: ")
		computerLabel.place(x=130,y=130)
		#score lable for person
		personLabel = Label(window, text="Person: ")
		personLabel.place(x=250,y=130)
		#number of draws that occured
		drawLabel = Label(window, text="Draw: ")
		#personLabel.place(x=100,y=120)

		if player == "rock" and options[num] == "scissors":
			self.playerScore = self.playerScore + 1
			textWindow.insert(1.0,"Player beat computer with ",player + '\n')
			personLabel['text']= ("Person: ",self.playerScore)

		elif player == "rock" and options[num] == "paper":
			self.computerScore = self.computerScore + 1
			textWindow.insert(1.0,"Computer beat player with ",player + '\n')
			computerLabel['text']= ("Computer: ",self.computerScore)

		elif player == "rock" and options[num] == "rock":
			textWindow.insert(1.0,"Draw"+'\n')
			self.draw = self.draw + 1
			drawLabel['text']= ("draw: ",self.draw)
		elif player == "paper" and options[num] == "rock":
			self.playerScore = self.playerScore + 1
			textWindow.insert(1.0,"Player beat computer with ",player + '\n')
			personLabel['text']= ("Person: ",self.playerScore)

		elif player == "paper" and options[num] == "paper":
			textWindow.insert(1.0,"Draw"+'\n')
			self.draw = self.draw + 1
			drawLabel['text']= ("draw: ",self.draw)
		elif player == "paper" and options[num] == "scissors":
			self.computerScore = self.computerScore + 1
			textWindow.insert(1.0,"Computer beat player with ",player + '\n')
			computerLabel['text']= ("Computer: ",self.computerScore)

		elif player == "scissors" and options[num] == "rock":
			self.computerScore = self.computerScore + 1
			textWindow.insert(1.0,"Computer beat player with ",player + '\n')
			computerLabel['text']= ("Computer: ",self.computerScore)

		elif player == "scissors" and options[num] == "paper":
			self.playerScore = self.playerScore + 1
			textWindow.insert(1.0,"Player beat computer with ",player + '\n')
			personLabel['text']= ("Person: ",self.playerScore)

		else:
			textWindow.insert(1.0,"Draw"+'\n')
			self.draw = self.draw + 1
			drawLabel['text']= ("draw: ",self.draw)



#Creates a window
window = Tk()
#labels the window
window.title("Rock Paper Scissors")
#sets the window size
window.geometry("400x400")
#changes the background color
window.configure(bg='gray')
#instance of the game class
g = game()
#Creates a button
#lambda will execute commands one by one
rockButton = Button(window,text="Rock",fg='white',bg='blue',command=lambda:[g.display("rock"), g.playComputer(window,"rock")])
#places the button
rockButton.place(x=175,y=25)
#Creates a button
paperButton = Button(window,text="Paper",fg='black',bg='red',command=lambda:[g.display("paper"), g.playComputer(window,"paper")])
#places the button
paperButton.place(x=175,y=60)
#Creates a button
scissorsButton = Button(window,text="Scissors",fg='black',bg='green',command=lambda:[g.display("scissors"), g.playComputer(window,"scissors")])
#places the button
scissorsButton.place(x=175,y=95)
#creates a text widget
textWindow = Text(window, height=10, width=43)
#places the text widget
textWindow.place(x=25,y=160)


window.mainloop()

