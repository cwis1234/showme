import pygame
from pygame.locals import *
import tkinter
from rectpack import newPacker
import random
import queue

class arccon:
	worklist = queue.Queue()

	def __init__(self,arcs:list,domains:dict,constraint:dict):
		self.arcs = arcs
		self.domains = domains
		self.constraints = constraint

	def solve(self,generate = False) -> dict:
		result = self.arcsolve()

		return result

	def arcsolve(self) -> dict:
		[self.worklist.put(arc) for arc in self.arcs]

		while not self.worklist.empty():
			(xi,xj) = self.worklist.get()

			if self.revise(xi,xj):
				if len(self.domains[xi]) == 0:
					yield None
					break

				neighbors = [neighbor for neighbor in self.arcs if neighbor[0] == xj]

				[self.worklist.put(neighbor) for neighbor in neighbors]

				yield ((xi,xj),self.domains,neighbors)
			else:
				yield (None,self.domains,None)

	def revise(self,xi:object,xj:object) -> bool:
		revised = False

		xi_domain = self.domains[xi]
		xj_domain = self.domains[xj]

		constraints = [constraint for constraint in self.constraints if constraint[0] == xi and constraint[1] == xj]
		
		for x in xi_domain[:]:
			statisfies = False

			for y in xj_domain:
				for constraint in constraints:
					check_function = self.constraints[constraint]

					if check_function(x,y):
						statisfies = True

			if not statisfies:
				xi_domain.remove(x)
				revised = True

		return revised















colors = []
locals = []

map = [[0] * 30 for i in range(30)]

WHITE = (255,255,255)
BLACK = (0,0,0)
neighbor = {}

colors_of_states = {}

colorset = {}
colorset['RED'] = (255,0,0)
colorset['BLUE'] = (0,0,255)
colorset['GREEN'] = (0,255,0)
colorset['YELLOW'] = (255,127,0)
huri = 3
uukkk = 0
k = 4










def promising(state, color):
    for neighbor1 in neighbor.get(state): 
        local_color_set1 = colors_of_states.get(neighbor1)
        if local_color_set1 == color:
            return False

    return True


def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color


def draw(surf):
	for y in range(30):
		for x in range(30):
			xx = 15*x
			yy = 15*y


			if map[y][x] == 0:
				pygame.draw.rect(surf,(0,0,0),pygame.Rect(xx,yy,15,15),1)
			elif map[y][x] == 1:
				pygame.draw.rect(surf,(127,127,127),pygame.Rect(xx,yy,15,15))
			else:
				if uukkk ==1:
					a = map[y][x]-2
					b = colors_of_states[a]
					if(colorset[b] == None):
						pygame.draw.rect(surf,WHITE,pygame.Rect(xx,yy,15,15))
					else:
						pygame.draw.rect(surf,colorset[b],pygame.Rect(xx,yy,15,15))
				else:
					pygame.draw.rect(surf,BLACK,pygame.Rect(xx,yy,15,15))

	font = pygame.font.Font(None,32)
	textSurfaceObj = font.render("CSP Solver",True,(0,0,0))
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (630,20)
	surf.blit(textSurfaceObj,textRectObj)


	if huri == 1:
		pygame.draw.rect(surf,(0,255,0),pygame.Rect(480,50,300,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(480,110,300,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(480,170,300,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(480,230,300,50),1)
	elif huri == 2:
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(480,50,300,50),1)
		pygame.draw.rect(surf,(0,255,0),pygame.Rect(480,110,300,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(480,170,300,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(480,230,300,50),1)
	elif huri == 3:
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(480,50,300,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(480,110,300,50),1)
		pygame.draw.rect(surf,(0,255,0),pygame.Rect(480,170,300,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(480,230,300,50),1)
	elif huri == 4:
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(480,50,300,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(480,110,300,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(480,170,300,50),1)
		pygame.draw.rect(surf,(0,255,0),pygame.Rect(480,230,300,50),1)


	font = pygame.font.Font(None,32)
	textSurfaceObj = font.render("K",True,(0,0,0))
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (480,300)
	surf.blit(textSurfaceObj,textRectObj)

	
	font = pygame.font.Font(None,32)
	textSurfaceObj = font.render("AC + Backtracking",True,(0,0,0))
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (630,75)
	surf.blit(textSurfaceObj,textRectObj)

	textSurfaceObj = font.render("AC + Localsearch",True,(0,0,0))
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (630,135)
	surf.blit(textSurfaceObj,textRectObj)

	textSurfaceObj = font.render("Backtracking",True,(0,0,0))
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (630,195)
	surf.blit(textSurfaceObj,textRectObj)

	textSurfaceObj = font.render("Localsearch",True,(0,0,0))
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (630,255)
	surf.blit(textSurfaceObj,textRectObj)
	
	if k == 1:
		pygame.draw.rect(surf,(0,255,0),pygame.Rect(500,290,50,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(560,290,50,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(620,290,50,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(680,290,50,50),1)
	elif k == 2:
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(500,290,50,50),1)
		pygame.draw.rect(surf,(0,255,0),pygame.Rect(560,290,50,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(620,290,50,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(680,290,50,50),1)
	elif k == 3:
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(500,290,50,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(560,290,50,50),1)
		pygame.draw.rect(surf,(0,255,0),pygame.Rect(620,290,50,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(680,290,50,50),1)
	elif k == 4:
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(500,290,50,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(560,290,50,50),1)
		pygame.draw.rect(surf,(255,0,0),pygame.Rect(620,290,50,50),1)
		pygame.draw.rect(surf,(0,255,0),pygame.Rect(680,290,50,50),1)
	
	textSurfaceObj = font.render("1",True,(0,0,0))
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (525,315)
	surf.blit(textSurfaceObj,textRectObj)
	textSurfaceObj = font.render("2",True,(0,0,0))
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (585,315)
	surf.blit(textSurfaceObj,textRectObj)
	textSurfaceObj = font.render("3",True,(0,0,0))
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (645,315)
	surf.blit(textSurfaceObj,textRectObj)
	textSurfaceObj = font.render("4",True,(0,0,0))
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (705,315)
	surf.blit(textSurfaceObj,textRectObj)

	
	pygame.draw.rect(surf,(0,0,255),pygame.Rect(10,460,100,50))
	pygame.draw.rect(surf,(0,0,255),pygame.Rect(120,460,100,50))
	pygame.draw.rect(surf,(0,0,255),pygame.Rect(230,460,100,50))
	textSurfaceObj = font.render("GRM",True,(0,0,0))
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (60,485)
	surf.blit(textSurfaceObj,textRectObj)
	textSurfaceObj = font.render("Do",True,(0,0,0))
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (170,485)
	surf.blit(textSurfaceObj,textRectObj)
	textSurfaceObj = font.render("Save",True,(0,0,0))
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (280,485)
	surf.blit(textSurfaceObj,textRectObj)



	return

def Save():
	print("save...")
	return

def GRM():
	packer = newPacker()
	packer.add_bin(*(29,29))
	rts = []
	ok = True
	older = 0
	new = 0
	while ok:
		x = random.randrange(5,15)
		y = random.randrange(5,15)
		packer.add_rect(*(x,y))
		packer.pack()
		new = len(packer[0])
		if new == older:
			ok = False
		else:
			older = new
		

	all_rects = packer.rect_list()
	for i in range(30):
			map[0][i] = 1
			map[29][i] = 1
			map[i][0] = 1
			map[i][29] = 1
	gx=1
	gy=1
	for rect in all_rects:
		print(rect)
		b,x,y,w,h,rid = rect
		if x+w == 28:
			w+=1
		if y+h == 28:
			h+=1
		for i in range(0,w):
			kxr=1
			kxrr=1

			map[y][x+i] = kxr
			map[y+h][x+i] = kxrr
		for i in range(0,h):
			kxr=1
			kxrr=1
			map[y+i][x] = kxr
			map[y+i][x+w] = kxrr
	for y in range(1,30):
		for x in range(1,30):
			if map[x-1][y] == 1 and map[x][y-1] and x > 1 and y > 1 and map[x-1][y-1] != 1:
				map[x][y] = 1


	return

def doarc():
	global neighbor,locals
	arcs = []
	domains = {}
	constraints = {}
	for i in range(len(locals)):
		for j in range(len(neighbor[i])):
			arcs.append((''+str(i)+'',''+str(neighbor[i][j])+''))
	for i in range(len(locals)):
		for j in neighbor[i]:
			a = {(''+str(i)+'',''+str(j)+''): lambda i,j: i!=j}
			constraints.update(a)
	for i in range(len(locals)):
		if i == 0:
			domains.update({''+str(i)+'': ['RED']})
		else:
			domains.update({''+str(i)+'': ['RED', 'GREEN']})
	solver = arccon(arcs,domains,constraints)
	result = solver.solve()
	for step in result:
		edge = step[0]
		if edge == None:
			fd = step[1]
			print(fd)
	return

def doK():
	print("do k-coloring..")
	global colors_of_states
	if huri == 3:
		for local in locals:
			colors_of_states[local] = get_color_for_state(local)
	if huri == 1:
		print("backtracking with arc-consistency")
		colors_of_states = doarc()

	print(colors_of_states)
	return

def gusung():
	kk=2
	xj=0
	xxx=0
	for i in range(1,29):
		for j in range(1,29):
			xxx=0
			xj=0
			if map[i][j] == 0:
				if map[i-1][j] != 1 and map[i-1][j] != 0:
					xj+=1
					xxx=0
				if map[i][j-1] != 1 and map[i][j-1] != 0:
					xj+=1
					xxx=1

				if xj == 0:
					map[i][j] = kk
					kk+=1
				elif xj == 1:
					if xxx==0:
						map[i][j] = map[i-1][j]
					else:
						map[i][j] = map[i][j-1]
				else:
					if map[i-1][j] == map[i][j-1]:
						map[i][j] = map[i-1][j]
					else:
						if map[i][j-1] < map[i-1][j]:
							map[i][j] = map[i][j-1]
							recon(map[i-1],[j],map[i][j-1])
						else:
							map[i][j] = map[i-1][j]
							recon(map[i][j-1],map[i-1][j])



	print(kk-2)
	for i in range(30):
		print(map[i])
	mat = []
	toc = 0
	result = 0
	for i in range(30):
		for j in range(30):
			toc = 0
			if map[i][j] == 0 or map[i][j] == 1:
				continue
			for f in mat:
				if map[i][j] == f:
					toc = 1
					break
			if toc == 1:
				continue
			mat.append(map[i][j])
			result += 1
	print(result)
	print(mat)

	rut = []
	for i in range(result):
		rut.append(50+i)
	print(rut)

	for i in range(result):
		recon(mat[i],rut[i])
	for i in range(30):
		for j in range(30):
			if map[i][j] == 0 or map[i][j] == 1:
				continue
			map[i][j] -= 48
	for i in range(30):
		print(map[i])

	graph = [[0] * (result) for i in range(result)]

	for i in range(29):
		for j in range(29):
			if map[i][j] == 0 or map[i][j] == 1:
				continue
			if i==28 and j == 28:
				continue
			elif i == 28:
				if map[i][j] != map[i][j+2] and map[i][j+2] != 1:
					graph[map[i][j]-2][map[i][j+2]-2] = 1
					graph[map[i][j+2]-2][map[i][j]-2] = 1
			elif j == 28:
				if map[i][j] != map[i+2][j]and map[i+2][j] != 1:
					graph[map[i][j]-2][map[i+2][j]-2] = 1
					graph[map[i+2][j]-2][map[i][j]-2] = 1
			else:
				if map[i][j] != map[i][j+2] and map[i][j+2] != 1:
					graph[map[i][j]-2][map[i][j+2]-2] = 1
					graph[map[i][j+2]-2][map[i][j]-2] = 1
				if map[i][j] != map[i+2][j]and map[i+2][j] != 1:
					graph[map[i][j]-2][map[i+2][j]-2] = 1
					graph[map[i+2][j]-2][map[i][j]-2] = 1
	for i in range(result):
		print(graph[i])

	for i in range(result):
		a = []
		for j in range(result):
			if graph[i][j] == 1:
				a.append(j)
		neighbor[i] = a
		locals.append(i)
	print(neighbor,locals)
	return graph


def recon(x,y):
	for i in range(30):
		for j in range(30):
			if map[i][j] == x:
				map[i][j] = y
	return


if __name__=='__main__':
	pygame.init()
	surf = pygame.display.set_mode((800,800))
	pygame.display.set_caption("k-coloring")
	surf.fill(WHITE)
	draw(surf)
	ok = True
	while ok:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				ok = False
			elif event.type == MOUSEBUTTONDOWN:
				x = event.pos[0]
				y = event.pos[1]
				if (x > 480 and x < 780) and (y > 50 and y < 100):
					huri = 1
					draw(surf)
				elif (x > 480 and x < 780) and (y > 110 and y < 160):
					huri = 2
					draw(surf)
				elif (x > 480 and x < 780) and (y > 170 and y < 220):
					huri = 3
					draw(surf)
				elif (x > 480 and x < 780) and (y > 230 and y < 280):
					huri = 4
					draw(surf) #500,290,50,50
				elif (x > 500 and x < 550) and (y > 290 and y < 340):
					k = 1
					draw(surf)
				elif (x > 560 and x < 610) and (y > 290 and y < 340):
					k = 2
					draw(surf)
				elif (x > 620 and x < 670) and (y > 290 and y < 340):
					k = 3
					draw(surf)
				elif (x > 680 and x < 720) and (y > 290 and y < 340):
					k = 4
					draw(surf)#10,460,100,50

				elif (x > 10 and x < 110) and (y > 460 and y < 510):
					GRM()
					draw(surf)
					graph = gusung()
					draw(surf)
				elif (x > 120 and x < 220) and (y > 460 and y < 510):
					if(k == 1):
						colors = ['RED']
					elif(k==2):
						colors = ['RED','BLUE']
					elif(k==3):
						colors = ['RED','BLUE','GREEN']
					elif(k==4):
						colors = ['RED','BLUE','GREEN','YELLOW']
					doK()
					uukkk = 1
					x=True
					for i in colors_of_states:
						if colors_of_states[i] == None:
							x=False
							break
					if x:
						draw(surf)
					else:
						print("false")
				elif (x > 230 and x < 330) and (y > 460 and y < 510):
					Save()
				

		pygame.display.update()
	pygame.quite()