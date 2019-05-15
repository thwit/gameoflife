import sys
import os
import pygame
import copy
from model.board import Board
from model.cell import Cell

def draw_grid(board):
	for column in range(0, w, colsz):
		for row in range(0, h, rowsz):
			if board.get_cell(column//colsz,row//rowsz).alive:
				pygame.draw.rect(screen,ALIVE,[column,row,colsz-1,rowsz-1])
			else:
				pygame.draw.rect(screen,DEAD,[column,row,colsz-1,rowsz-1])
			
def update_cell(cell):
	if cell.alive:
		pygame.draw.rect(screen,ALIVE,[cell.x*colsz,cell.y*rowsz,colsz-1,rowsz-1])
	else:
		pygame.draw.rect(screen,DEAD,[cell.x*colsz,cell.y*rowsz,colsz-1,rowsz-1])
	
def alive_neighbors(cell,board):
	cnt = 0
	
	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			if j == 0 and i == 0:
				continue
			if cell.x + i >= 0 and cell.x + i < cols and cell.y + j >= 0 and cell.y + j < rows:
				if board.get_cell(cell.x + i, cell.y + j).alive:
					cnt += 1
	return cnt
			
def next_state(cell,board):
	an = alive_neighbors(cell,board)
	if cell.alive:
		if an < 2 or an > 3:
			return False
		else:
			return True
			
	elif not cell.alive:
		if an == 3:
			return True
	
def draw_start_pattern(board):
	while True:
		to_update = []
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			# Right mouse click turns cells on
			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				x = pos[0] // colsz
				y = pos[1] // rowsz
				if not board.get_cell(x,y).alive:
					board.get_cell(x,y).alive = True
					to_update.append(board.get_cell(x,y))
			# Right mouse click turns cells off
			if pygame.mouse.get_pressed()[2]:
				pos = pygame.mouse.get_pos()
				x = pos[0] // colsz
				y = pos[1] // rowsz
				if board.get_cell(x,y).alive:
					board.get_cell(x,y).alive = False
					to_update.append(board.get_cell(x,y))
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RETURN:
					game_of_life_loop(board)
					return

		for s in to_update:
			update_cell(s)

		pygame.display.flip()
		clock.tick(60)
		
def game_of_life_loop(board):
	while True:
		to_update = []
		new_board = Board(cols,rows)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RETURN:
					board.reset()
					draw_grid(board)
					draw_start_pattern(board)
					return
		
		for x in range(cols):
			for y in range(rows):

				cell = board.get_cell(x,y)
				state = next_state(cell,board)
				if state:
					new_board.get_cell(x,y).alive = True
					to_update.append(new_board.get_cell(x,y))
				elif not state:
					new_board.get_cell(x,y).alive = False
					to_update.append(new_board.get_cell(x,y))
					
		board = new_board
	
	
	
		for s in to_update:
			update_cell(s)
	
		pygame.display.flip()
		# Higher number, higher speed
		clock.tick(12)
	
NEIGHBOURS = [ [-1,-1], [-1,0], [-1, 1], [0,-1], [0,1], [1,-1], [1,0], [1,1] ]

rowsz,colsz = 10,10

cols,rows = 60,60

size = w,h = rows*rowsz,cols*colsz

board = Board(cols,rows)

WHITE = (190, 190, 140)
ALIVE = (255, 0, 0)
DEAD = (180, 160, 100)

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


# Glider
# board.get_cell(20,10).alive = True
# board.get_cell(20,12).alive = True
# board.get_cell(21,11).alive = True
# board.get_cell(21,12).alive = True
# board.get_cell(22,11).alive = True

# Blinker
# board.get_cell(8,11).alive = True
# board.get_cell(8,12).alive = True
# board.get_cell(8,13).alive = True

# Rabbit thingy
# board.get_cell(30,30).alive = True
# board.get_cell(30,29).alive = True
# board.get_cell(30,28).alive = True
# board.get_cell(33,28).alive = True
# board.get_cell(34,27).alive = True
# board.get_cell(35,27).alive = True
# board.get_cell(30,26).alive = True
# board.get_cell(31,26).alive = True
# board.get_cell(33,26).alive = True
# board.get_cell(31,25).alive = True



draw_grid(board)

draw_start_pattern(board)
game_of_life_loop(board)	