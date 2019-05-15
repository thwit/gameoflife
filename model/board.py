from .cell import Cell

class Board:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.grid = [[Cell(j,i) for j in range(width)] for i in range(height)]
		
	def get_cell(self,x,y):
		return self.grid[y][x]