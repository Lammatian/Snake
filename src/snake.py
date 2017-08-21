from random import randint

class Snake():

	def __init__(self, canvas, width, height, blocksize):
		# width and height in no of blocks
		self.canvas = canvas
		self.blocksize = blocksize
		self.snek = [(width//2, height//2)]
		self.direction = "up"
		self.ate = 0
		self.last = (self.snek[0][0], self.snek[0][1]+1)

	def move(self):
		self.last = self.snek[-1]

		for i in range(len(self.snek)-1, 0, -1):
			self.snek[i] = self.snek[i-1]
		
		if self.direction == "up":
			self.snek[0] = (self.snek[0][0], self.snek[0][1]-1)
		elif self.direction == "down":
			self.snek[0] = (self.snek[0][0], self.snek[0][1]+1)
		elif self.direction == "right":
			self.snek[0] = (self.snek[0][0]+1, self.snek[0][1])
		elif self.direction == "left":
			self.snek[0] = (self.snek[0][0]-1, self.snek[0][1])

	def eat(self):
		self.snek.append(self.last)
		self.ate += 1

	def draw(self):
		self.canvas.delete("snake")

		for x,y in self.snek:
			self.canvas.create_rectangle(self.blocksize*x,\
										 self.blocksize*y,\
										 self.blocksize*(x+1),\
										 self.blocksize*(y+1),\
										 fill="white",\
										 tag="snake")