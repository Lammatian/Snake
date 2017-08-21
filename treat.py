from random import randint

class Treat():

	def __init__(self, canvas, width, height, blocksize, snek, apple):
		self.canvas = canvas
		self.blocksize = blocksize
		self.x = randint(0, width-1)
		self.y = randint(0, height-1)
		while (self.x, self.y) in snek or (self.x, self.y) == apple:
			self.x = randint(0, width-1)
			self.y = randint(0, height-1)
		self.pos = (self.x, self.y)

	def draw(self):
		self.canvas.create_rectangle(self.blocksize*self.x,\
									 self.blocksize*self.y,\
									 self.blocksize*(self.x+1),\
									 self.blocksize*(self.y+1),\
									 fill="green",\
									 tag="treat")
		self.canvas.create_text(self.blocksize*(self.x+0.5),\
								self.blocksize*(self.y+0.5),\
								fill="white",\
								text="5",\
								tag=("treat", "treattime"))