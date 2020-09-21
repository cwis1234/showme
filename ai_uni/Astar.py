import pygame, sys
import queue
import math
from pygame.locals import *
import random

pygame.init()
DISPLAYSURF = pygame.display.set_mode((1100,1000))
pygame.display.set_caption('Hello World')
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GRAY = (123,123,123)
GREEN = (0,255,0)
BLUE = (0,0,255)
RIGHT = (255,255,0)
a = 800/30
grid = [[BLACK]*30 for i in range(30)]
map = [[0]*30 for i in range(30)]

startx=0
starty=0
endx=0
endy=0
closelist = queue.Queue()
for i in range(0,30):
	for j in range(0,30):
		grid[i][j] = BLACK

DISPLAYSURF.fill(WHITE)
hf = 0

bcolor = GREEN

#start = 9, end = 8, block = 1

def manhattan(x,y,ax,ay):
	return abs(x-ax)+abs(y-ay)
def euclidean(x,y,ax,ay):
	g = (abs(ax-x)**2)+(abs(ay-y)**2)
	return math.sqrt(g)

def drawpath(startx,starty,endx,endy):

	ta = [[0] for i in range(closelist.qsize())]
	ind=0
	
	while closelist.qsize() != 0:
		ta[ind] = closelist.get()
		ind = ind + 1

	x = endx
	y = endy
	grid[x][y] = RIGHT
	while 1:	
		if x==startx and y == starty:
			break
		for i in range(0,ind):
			arr = ta[i]
			if x==arr[0] and y==arr[1]:
				grid[x][y] = RIGHT
				x=arr[2]
				y=arr[3]
				break
	

	redraw()
	return

def Astar():
	result=0
	openlist = queue.PriorityQueue()
	if hf == 0:
		func = manhattan
	else:
		func = euclidean
	for x in range(0,30):
		for y in range(0,30):
			if grid[x][y] == BLACK:
				map[x][y] = 0
			if grid[x][y] == GREEN:
				startx=x
				starty=y
				map[x][y] = 9
				continue
			if grid[x][y] == RED:
				endx=x
				endy=y
				map[x][y] = 8
				continue
			if grid[x][y] == GRAY:
				map[x][y] = 1
				closelist.put([x,y])
	ab = [startx,starty,0,0]
	openlist.put((0,ab))
	while openlist.qsize() != 0:
		(h,arr) = openlist.get()
		print(arr)
		x = arr[0]
		y = arr[1]
		px = arr[2]
		py = arr[3]
		closelist.put([x,y,px,py])
		if endx == x and endy == y:
			drawpath(startx,starty,endx,endy)
			result=1
			break
		grid[x][y] = BLUE
		redraw()

		ta = [[0] for i in range(closelist.qsize())]
		ind=0


		while closelist.qsize() != 0:
			ta[ind] = closelist.get()
			ind = ind + 1
		for i in range (0,ind):
			closelist.put(ta[i])
		

		up = 0
		left = 0
		right = 0
		down = 0


		for i in range (0,ind):
			tx = ta[i][0]
			ty = ta[i][1]
			if tx == x-1 and tx == y:
				left = 1
			if tx == x and ty == y-1:
				up = 1
			if tx == x+1 and ty == y:
				right = 1
			if tx == x and ty == y+1:
				down = 1

		
		ta1 = [[0] for i in range(openlist.qsize())]
		ind1 = 0

		
		while openlist.qsize() != 0:
			ta1[ind1] = openlist.get()
			ind1 = ind1 + 1
		
		for i in range (0,ind1):
			openlist.put(ta1[i])

			

		for i in range (0,ind1):
			tx = ta1[i][0]
			ty = ta1[i][1]
			if tx == x-1 and tx == y:
				left = 1
			if tx == x and ty == y-1:
				up = 1
			if tx == x+1 and ty == y:
				right = 1
			if tx == x and ty == y+1:
				down = 1


		if left != 1 and x-1 >= 0:#map[x-1][y] != 1:
			if map[x-1][y] != 1:
				h = h+1
				openlist.put((h+func(x-1,y,endx,endy),[x-1,y,x,y]))
		if up != 1 and y-1 >= 0:#map[x][y-1] != 1:
			if map[x][y-1] != 1:
				h = h+1
				openlist.put((h+func(x,y-1,endx,endy),[x,y-1,x,y]))
		if right != 1 and x+1 <= 29: #map[x+1][y] != 1:
			if map[x+1][y] != 1:
				h = h+1
				openlist.put((h+func(x+1,y,endx,endy),[x+1,y,x,y]))
		if down != 1 and y+2<=29: #map[x][y+1] != 1:
			if map[x][y+1] != 1:
				h = h+1
				openlist.put((h+func(x,y+1,endx,endy),[x,y+1,x,y]))
	
	
	if result == 0:
		print("can't find path")
	
	return


def redraw():
	
			
	DISPLAYSURF.fill(WHITE)		
			
	pygame.draw.rect(DISPLAYSURF,BLACK,[850,200,200,50],1)
	pygame.draw.rect(DISPLAYSURF,BLACK,[850,250,200,50],1)
	pygame.draw.rect(DISPLAYSURF,BLACK,[850,300,200,50],1)
	pygame.draw.rect(DISPLAYSURF,BLACK,[850,600,200,50],1)
	pygame.draw.rect(DISPLAYSURF,BLACK,[850,400,200,50],1)
	
	fontObj = pygame.font.SysFont("Monospace",40)
	text = fontObj.render('Manhattan',True,BLACK)
	DISPLAYSURF.blit(text,(850,100))
	fontObj = pygame.font.SysFont("Monospace",40)
	text = fontObj.render('Euclid',True,BLACK)
	DISPLAYSURF.blit(text,(850,150))
	fontObj = pygame.font.SysFont("Monospace",40)
	text = fontObj.render('START',True,BLACK)
	DISPLAYSURF.blit(text,(850,200))
	fontObj = pygame.font.SysFont("Monospace",40)
	text = fontObj.render('WALL',True,BLACK)
	DISPLAYSURF.blit(text,(850,250))
	fontObj = pygame.font.SysFont("Monospace",40)
	text = fontObj.render('END',True,BLACK)
	DISPLAYSURF.blit(text,(850,300))
	fontObj = pygame.font.SysFont("Monospace",40)
	text = fontObj.render('RANDOM',True,BLACK)
	DISPLAYSURF.blit(text,(850,400))
	fontObj = pygame.font.SysFont("Monospace",40)
	text = fontObj.render('START',True,BLACK)
	DISPLAYSURF.blit(text,(850,600))
			
			
			
	for i in range(0,30):
		for j in range(0,30):
			if grid[i][j] == BLACK:
				pygame.draw.rect(DISPLAYSURF,grid[i][j],[i*a,j*a,a,a],1)
			else:
				pygame.draw.rect(DISPLAYSURF,grid[i][j],[i*a,j*a,a,a])
				
			
	return


def rand():
	for i in range(120):
		x = random.randrange(0,30)
		y = random.randrange(0,30)
		grid[x][y] = GRAY
	redraw()

	return
	
		
while True: # main game Loop
	DISPLAYSURF.fill(WHITE)		
	for event in pygame.event.get():
		
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == MOUSEBUTTONDOWN:
			x = int(event.pos[0]//a)
			y = int(event.pos[1]//a)
			if x<30 and y<30:
				if bcolor == GRAY:
					grid[x][y] = bcolor
				else:
					for xi in range(0,30):
						for yi in range(0,30):
							if grid[xi][yi] == bcolor:
								grid[xi][yi] = BLACK
								break
					grid[x][y] = bcolor
				
			if (event.pos[0]>850 and event.pos[0]<1050) and (event.pos[1] > 100 and event.pos[1] < 150):
				hf = 0
				pygame.draw.rect(DISPLAYSURF,GREEN,[850,100,200,50])
				pygame.draw.rect(DISPLAYSURF,RED,[850,150,200,50])
			if (event.pos[0]>850 and event.pos[0]<1050) and (event.pos[1] > 150 and event.pos[1] < 200):
				hf = 1
				pygame.draw.rect(DISPLAYSURF,RED,[850,100,200,50])
				pygame.draw.rect(DISPLAYSURF,GREEN,[850,150,200,50])
			if (event.pos[0]>850 and event.pos[0]<1050) and (event.pos[1] > 200 and event.pos[1] < 250): #start
				bcolor = GREEN
			if (event.pos[0]>850 and event.pos[0]<1050) and (event.pos[1] > 250 and event.pos[1] < 300): #block
				bcolor = GRAY
			if (event.pos[0]>850 and event.pos[0]<1050) and (event.pos[1] > 300 and event.pos[1] < 350): #end
				bcolor = RED
			if (event.pos[0]>850 and event.pos[0]<1050) and (event.pos[1] > 600 and event.pos[1] < 650): #end
				Astar()
			if (event.pos[0]>850 and event.pos[0]<1050) and (event.pos[1] > 400 and event.pos[1] < 450): #end
				rand()

			
	if hf == 0:
		pygame.draw.rect(DISPLAYSURF,GREEN,[850,100,200,50])
		pygame.draw.rect(DISPLAYSURF,RED,[850,150,200,50])
	elif hf == 1:
		pygame.draw.rect(DISPLAYSURF,RED,[850,100,200,50])
		pygame.draw.rect(DISPLAYSURF,GREEN,[850,150,200,50])

			
	pygame.draw.rect(DISPLAYSURF,BLACK,[850,200,200,50],1)
	pygame.draw.rect(DISPLAYSURF,BLACK,[850,250,200,50],1)
	pygame.draw.rect(DISPLAYSURF,BLACK,[850,300,200,50],1)
	pygame.draw.rect(DISPLAYSURF,BLACK,[850,600,200,50],1)
	pygame.draw.rect(DISPLAYSURF,BLACK,[850,400,200,50],1)
	
	fontObj = pygame.font.SysFont("Monospace",40)
	text = fontObj.render('Manhattan',True,BLACK)
	DISPLAYSURF.blit(text,(850,100))
	fontObj = pygame.font.SysFont("Monospace",40)
	text = fontObj.render('Euclid',True,BLACK)
	DISPLAYSURF.blit(text,(850,150))
	fontObj = pygame.font.SysFont("Monospace",40)
	text = fontObj.render('START',True,BLACK)
	DISPLAYSURF.blit(text,(850,200))
	fontObj = pygame.font.SysFont("Monospace",40)
	text = fontObj.render('WALL',True,BLACK)
	DISPLAYSURF.blit(text,(850,250))
	fontObj = pygame.font.SysFont("Monospace",40)
	text = fontObj.render('END',True,BLACK)
	DISPLAYSURF.blit(text,(850,300))
	fontObj = pygame.font.SysFont("Monospace",40)
	text = fontObj.render('RANDOM',True,BLACK)
	DISPLAYSURF.blit(text,(850,400))
	fontObj = pygame.font.SysFont("Monospace",40)
	text = fontObj.render('START',True,BLACK)
	DISPLAYSURF.blit(text,(850,600))
			
	for i in range(0,30):
		for j in range(0,30):
			if grid[i][j] == BLACK:
				pygame.draw.rect(DISPLAYSURF,grid[i][j],[i*a,j*a,a,a],1)
			else:
				pygame.draw.rect(DISPLAYSURF,grid[i][j],[i*a,j*a,a,a])
				
			
			
	pygame.display.update()

