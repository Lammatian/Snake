import sys

if sys.version_info[0] == 2:
	import Tkinter as tk
	import tkMessageBox as mbox
elif sys.version_info[0] == 3:
	import tkinter as tk
	import tkinter.messagebox as mbox

from random import randint, random
from snake import Snake
from apple import Apple
from treat import Treat
import math

widthpixels = 300
heightpixels = 300
gridwidth = 20
gridheight = 20
blockpixels = widthpixels/gridwidth
gamespeed = 100

class Game():

	def __init__(self, master):
		# init game with random snake position and random apple position
		# game will be 30x30 in size
		# each square will be 10 by 10 pixels 
		# window 300 by 300 pixels
		self.master = master
		self.master.geometry("{}x{}".format(widthpixels, heightpixels))

		self.canvas = tk.Canvas(self.master, width=widthpixels, height=heightpixels, bg="black")
		self.canvas.pack()

		self.treat_timer = 0
		self.score = 0

		with open("best.txt") as f:
			self.best_score = int(f.read())

		self.snake = Snake(self.canvas,\
						   gridwidth,\
						   gridheight,\
						   blockpixels)

		self.apple = Apple(self.canvas,\
						   gridwidth,\
						   gridheight,\
						   blockpixels,\
						   self.snake.snek)
		self.canvas.create_text(32, 10, text="Best score: ", fill="white")
		self.canvas.create_text(70, 10, text=str(self.best_score), fill="white", tag="best_score")
		
		self.canvas.create_text(20, 25, text="Score: ", fill="white")
		self.canvas.create_text(45, 25, text=str(self.score), fill="white", tag="score")

		self.master.bind("<Up>", self.snake_up)
		self.master.bind("<Down>", self.snake_down)
		self.master.bind("<Left>", self.snake_left)
		self.master.bind("<Right>", self.snake_right)
		self.master.bind("<Key-q>", lambda event: self.master.quit())

		self.master.focus_force()

		self.play()


	def play(self):

		sx = self.snake.snek[0][0]
		sy = self.snake.snek[0][1]

		if sx < 0 or sx >= gridwidth:
			self.game_over()
		elif sy < 0 or sy >= gridheight:
			self.game_over()
		elif self.snake.snek[0] in self.snake.snek[1:]:
			self.game_over()

		self.canvas.itemconfig("score", text=str(self.score))	
		self.snake.draw()
		self.apple.draw()

		if self.treat_timer <= 0:
			self.canvas.delete("treat")
			spawn_treat = random()

			if spawn_treat > 0.99:
				self.is_treat = True
				self.treat = Treat(self.canvas,\
								   gridwidth,\
								   gridheight,\
								   blockpixels,\
								   self.snake.snek,\
								   self.apple.pos)
				self.treat_timer = 3000
		else:
			self.treat.draw()
			self.treat_timer -= gamespeed
			self.canvas.itemconfig("treattime",\
								   text=str(int(math.ceil(self.treat_timer/1000))))

		if self.snake.snek[0] == self.apple.pos:
			self.snake.eat()
			self.score += 1
			self.canvas.delete("apple")
			self.apple = Apple(self.canvas,\
							   gridwidth,\
							   gridheight,\
							   blockpixels,\
							   self.snake.snek)
		elif self.treat_timer > 0 and self.snake.snek[0] == self.treat.pos:
			self.score += 5
			self.canvas.delete("treat")
			self.treat_timer = 0


		self.snake.move()
		self.master.after(gamespeed, self.play)


	def game_over(self):
		mbox.showinfo("Game over",\
					  "Snek is ded, your score"+\
					  " is {}.\nYou ate {} {}.".format(self.score,\
					  								   self.snake.ate,\
					  								   "apples" if self.snake.ate != 1\
					  								   			else "apple"))

		if self.score > self.best_score:
			with open("best.txt", 'w') as f:
				f.write(str(self.score))

		self.master.quit()


	def snake_up(self, event):
		if self.snake.direction != "down":
			self.snake.direction = "up"


	def snake_down(self, event):
		if self.snake.direction != "up":
			self.snake.direction = "down"


	def snake_left(self, event):
		if self.snake.direction != "right":
			self.snake.direction = "left"


	def snake_right(self, event):
		if self.snake.direction != "left":
			self.snake.direction = "right"

root = tk.Tk()

app = Game(root)

root.mainloop()