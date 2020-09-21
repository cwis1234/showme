import pygame as pg
from pygame.locals import *
import math as mt
import time
import copy
import random
import numpy as np
import random as rd
x1xx=""
BLA=(0,0,0)
WHI=(255,255,255,)
RED=(255,0,0,)
GRE=(0,200,0,)
ORA=(247,100,30)
BLU=(0,0,255)
YEL=(247,221,43)

CX=175
CY=175
S=100
FOCAL=10


colorind = [WHI,RED,GRE,YEL,ORA,BLU]


strstr = []



hO = np.ones(2186, dtype=np.int) * 12
hP = np.ones(823543, dtype=np.int) * 12


moveStrs = {0: "U", 1: "U'", 2: "U2", 3: "R", 4: "R'", 5: "R2", 6: "F", 7: "F'", 8: "F2"}



moveDefs = np.array([ \
  [  2,  0,  3,  1, 20, 21,  6,  7,  4,  5, 10, 11, 12, 13, 14, 15,  8,  9, 18, 19, 16, 17, 22, 23], \
  [  1,  3,  0,  2,  8,  9,  6,  7, 16, 17, 10, 11, 12, 13, 14, 15, 20, 21, 18, 19,  4,  5, 22, 23], \
  [  3,  2,  1,  0, 16, 17,  6,  7, 20, 21, 10, 11, 12, 13, 14, 15,  4,  5, 18, 19,  8,  9, 22, 23], \
  [  0,  9,  2, 11,  6,  4,  7,  5,  8, 13, 10, 15, 12, 22, 14, 20, 16, 17, 18, 19,  3, 21,  1, 23], \
  [  0, 22,  2, 20,  5,  7,  4,  6,  8,  1, 10,  3, 12,  9, 14, 11, 16, 17, 18, 19, 15, 21, 13, 23], \
  [  0, 13,  2, 15,  7,  6,  5,  4,  8, 22, 10, 20, 12,  1, 14,  3, 16, 17, 18, 19, 11, 21,  9, 23], \
  [  0,  1, 19, 17,  2,  5,  3,  7, 10,  8, 11,  9,  6,  4, 14, 15, 16, 12, 18, 13, 20, 21, 22, 23], \
  [  0,  1,  4,  6, 13,  5, 12,  7,  9, 11,  8, 10, 17, 19, 14, 15, 16,  3, 18,  2, 20, 21, 22, 23], \
  [  0,  1, 13, 12, 19,  5, 17,  7, 11, 10,  9,  8,  3,  2, 14, 15, 16,  6, 18,  4, 20, 21, 22, 23], \
  [  0,  1,  2,  3,  4,  5, 10, 11,  8,  9, 18, 19, 14, 12, 15, 13, 16, 17, 22, 23, 20, 21,  6,  7], \
  [  0,  1,  2,  3,  4,  5, 22, 23,  8,  9,  6,  7, 13, 15, 12, 14, 16, 17, 10, 11, 20, 21, 18, 19], \
  [  0,  1,  2,  3,  4,  5, 18, 19,  8,  9, 22, 23, 15, 14, 13, 12, 16, 17,  6,  7, 20, 21, 10, 11], \
  [ 23,  1, 21,  3,  4,  5,  6,  7,  0,  9,  2, 11,  8, 13, 10, 15, 18, 16, 19, 17, 20, 14, 22, 12], \
  [  8,  1, 10,  3,  4,  5,  6,  7, 12,  9, 14, 11, 23, 13, 21, 15, 17, 19, 16, 18, 20,  2, 22,  0], \
  [ 12,  1, 14,  3,  4,  5,  6,  7, 23,  9, 21, 11,  0, 13,  2, 15, 19, 18, 17, 16, 20, 10, 22,  8], \
  [  5,  7,  2,  3,  4, 15,  6, 14,  8,  9, 10, 11, 12, 13, 16, 18,  1, 17,  0, 19, 22, 20, 23, 21], \
  [ 18, 16,  2,  3,  4,  0,  6,  1,  8,  9, 10, 11, 12, 13,  7,  5, 14, 17, 15, 19, 21, 23, 20, 22], \
  [ 15, 14,  2,  3,  4, 18,  6, 16,  8,  9, 10, 11, 12, 13,  1,  0,  7, 17,  5, 19, 23, 22, 21, 20], \
  [  8,  9, 10, 11,  6,  4,  7,  5, 12, 13, 14, 15, 23, 22, 21, 20, 17, 19, 16, 18,  3,  2,  1,  0], \
  [ 23, 22, 21, 20,  5,  7,  4,  6,  0,  1,  2,  3,  8,  9, 10, 11, 18, 16, 19, 17, 15, 14, 13, 12], \
  [ 12, 13, 14, 15,  7,  6,  5,  4, 23, 22, 21, 20,  0,  1,  2,  3, 19, 18, 17, 16, 11, 10,  9,  8], \
  [  2,  0,  3,  1, 20, 21, 22, 23,  4,  5,  6,  7, 13, 15, 12, 14,  8,  9, 10, 11, 16, 17, 18, 19], \
  [  1,  3,  0,  2,  8,  9, 10, 11, 16, 17, 18, 19, 14, 12, 15, 13, 20, 21, 22, 23,  4,  5,  6,  7], \
  [  3,  2,  1,  0, 16, 17, 18, 19, 20, 21, 22, 23, 15, 14, 13, 12,  4,  5,  6,  7,  8,  9, 10, 11], \
  [ 18, 16, 19, 17,  2,  0,  3,  1, 10,  8, 11,  9,  6,  4,  7,  5, 14, 12, 15, 13, 21, 23, 20, 22], \
  [  5,  7,  4,  6, 13, 15, 12, 14,  9, 11,  8, 10, 17, 19, 16, 18,  1,  3,  0,  2, 22, 20, 23, 21], \
  [ 15, 14, 13, 12, 19, 18, 17, 16, 11, 10,  9,  8,  3,  2,  1,  0,  7,  6,  5,  4, 23, 22, 21, 20]  \
])

moveInds = { \
  "U": 0, "U'": 1, "U2": 2, "R": 3, "R'": 4, "R2": 5, "F": 6, "F'": 7, "F2": 8, \
  "D": 9, "D'": 10, "D2": 11, "L": 12, "L'": 13, "L2": 14, "B": 15, "B'": 16, "B2": 17, \
  "x": 18, "x'": 19, "x2": 20, "y": 21, "y'": 22, "y2": 23, "z": 24, "z'": 25, "z2": 26 \
}

pieceDefs = np.array([ \
  [  0, 21, 16], \
  [  2, 17,  8], \
  [  3,  9,  4], \
  [  1,  5, 20], \
  [ 12, 10, 19], \
  [ 13,  6, 11], \
  [ 15, 22,  7], \
])

pieceInds = np.zeros([58, 2], dtype=np.int)
pieceInds[50] = [0, 0]; pieceInds[54] = [0, 1]; pieceInds[13] = [0, 2]
pieceInds[28] = [1, 0]; pieceInds[42] = [1, 1]; pieceInds[ 8] = [1, 2]
pieceInds[14] = [2, 0]; pieceInds[21] = [2, 1]; pieceInds[ 4] = [2, 2]
pieceInds[52] = [3, 0]; pieceInds[15] = [3, 1]; pieceInds[11] = [3, 2]
pieceInds[47] = [4, 0]; pieceInds[30] = [4, 1]; pieceInds[40] = [4, 2]
pieceInds[25] = [5, 0]; pieceInds[18] = [5, 1]; pieceInds[35] = [5, 2]
pieceInds[23] = [6, 0]; pieceInds[57] = [6, 1]; pieceInds[37] = [6, 2]

pieceCols = np.zeros([7, 3, 3], dtype=np.int)
pieceCols[0, 0, :] = [0, 5, 4]; pieceCols[0, 1, :] = [4, 0, 5]; pieceCols[0, 2, :] = [5, 4, 0]
pieceCols[1, 0, :] = [0, 4, 2]; pieceCols[1, 1, :] = [2, 0, 4]; pieceCols[1, 2, :] = [4, 2, 0]
pieceCols[2, 0, :] = [0, 2, 1]; pieceCols[2, 1, :] = [1, 0, 2]; pieceCols[2, 2, :] = [2, 1, 0]
pieceCols[3, 0, :] = [0, 1, 5]; pieceCols[3, 1, :] = [5, 0, 1]; pieceCols[3, 2, :] = [1, 5, 0]
pieceCols[4, 0, :] = [3, 2, 4]; pieceCols[4, 1, :] = [4, 3, 2]; pieceCols[4, 2, :] = [2, 4, 3]
pieceCols[5, 0, :] = [3, 1, 2]; pieceCols[5, 1, :] = [2, 3, 1]; pieceCols[5, 2, :] = [1, 2, 3]
pieceCols[6, 0, :] = [3, 5, 1]; pieceCols[6, 1, :] = [1, 3, 5]; pieceCols[6, 2, :] = [5, 1, 3]

hashOP = np.array([1, 2, 10])
pow3 = np.array([1, 3, 9, 27, 81, 243, 729])
pow7 = np.array([1, 7, 49, 343, 2401, 16807, 117649])
fact6 = np.array([720, 120, 24, 6, 2, 1, 1])


def doMove(s, move):
  return s[moveDefs[move]]

# apply a string sequence of moves to a state
def doAlgStr(s, alg):
  moves = alg.split(" ")
  for m in moves:
    if m in moveInds:
      s = doMove(s, moveInds[m])
  return s

# check if state is solved
def isSolved(s):
  for i in range(6):
    if not (s[4 * i:4 * i + 4] == s[4 * i]).all():
      return False
  return True

# normalize stickers relative to a fixed DLB corner
def normFC(s):
  normCols = np.zeros(6, dtype=np.int)
  normCols[s[18] - 3] = 1
  normCols[s[23] - 3] = 2
  normCols[s[14]] = 3
  normCols[s[18]] = 4
  normCols[s[23]] = 5
  return normCols[s]

# get OP representation given FC-normalized sticker representation
def getOP(s):
  return pieceInds[np.dot(s[pieceDefs], hashOP)]

# get sticker representation from OP representation
def getStickers(sOP):
  s = np.zeros(24, dtype=np.int)
  s[[14, 18, 23]] = [3, 4, 5]
  for i in range(7):
    s[pieceDefs[i]] = pieceCols[sOP[i, 0], sOP[i, 1], :]
  return s

# get a unique index for the piece orientation state (0-2186)
def indexO(sOP):
  return np.dot(sOP[:, 1], pow3)

# get a unique index for the piece permutation state (0-823542)
def indexP(sOP):
  return np.dot(sOP[:, 0], pow7)

# get a (gap-free) unique index for the piece permutation state (0-5039)
def indexP2(sOP):
  ps = np.arange(7)
  P = 0
  for i, p in enumerate(sOP[:, 0]):
    P += fact6[i] * np.where(ps == p)[0][0]
    ps = ps[ps != p]
  return P

# get a unique index for the piece orientation and permutation state (0-11017439)
def indexOP(sOP):
  return indexO(sOP) * 5040 + indexP2(sOP)

def initState():
  return np.array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5])

def printCube(s):
  print("      ┌──┬──┐")
  print("      │ {}│ {}│".format(s[0], s[1]))
  print("      ├──┼──┤")
  print("      │ {}│ {}│".format(s[2], s[3]))
  print("┌──┬──┼──┼──┼──┬──┬──┬──┐")
  print("│ {}│ {}│ {}│ {}│ {}│ {}│ {}│ {}│".format(s[16], s[17], s[8], s[9], s[4], s[5], s[20], s[21]))
  print("├──┼──┼──┼──┼──┼──┼──┼──┤")
  print("│ {}│ {}│ {}│ {}│ {}│ {}│ {}│ {}│".format(s[18], s[19], s[10], s[11], s[6], s[7], s[22], s[23]))
  print("└──┴──┼──┼──┼──┴──┴──┴──┘")
  print("      │ {}│ {}│".format(s[12], s[13]))
  print("      ├──┼──┤")
  print("      │ {}│ {}│".format(s[14], s[15]))
  print("      └──┴──┘")

# generate pruning table for the piece orientation states
def genOTable(s, d, lm=-3):
  index =  indexO( getOP(s))
  if d < hO[index]:
    hO[index] = d
    for m in range(9):
      if int(m / 3) == int(lm / 3):
        continue
      genOTable( doMove(s, m), d + 1, m)

# generate pruning table for the piece permutation states
def genPTable(s, d, lm=-3):
  index =  indexP( getOP(s))
  if d < hP[index]:
    hP[index] = d
    for m in range(9):
      if int(m / 3) == int(lm / 3):
        continue
      genPTable( doMove(s, m), d + 1, m)
abcdefg=""
# IDA* which prints all optimal solutions
def IDAStar(s, d, moves, lm=-3):
  if  isSolved(s):
    moves
    printMoves(moves)
    return True
  else:
    sOP =  getOP(s)
    if d > 0 and d >= hO[ indexO(sOP)] and d >= hP[ indexP(sOP)]:
      dOptimal = False
      for m in range(9):
        if int(m / 3) == int(lm / 3):
          continue
        newMoves = moves[:]; newMoves.append(m)
        solved = IDAStar( doMove(s, m), d - 1, newMoves, m)
        if solved and not dOptimal:
          dOptimal = True
      if dOptimal:
        return True
  return False

# print a move sequence from an array of move indices
def printMoves(moves):
  moveStr = ""
  for m in moves:
    moveStr += moveStrs[m] + " "
  strstr.append(moveStr)
  print(moveStr)

# solve a cube state
def solveCube(s):
  # print cube state
  printCube(s)

  # FC-normalize stickers
  print("normalizing stickers...")
  s =  normFC(s)

  # generate pruning tables
  print("generating pruning tables...")
  genOTable( initState(), 0)
  genPTable( initState(), 0)

  # run IDA*
  print("searching...")
  solved = False
  depth = 1
  while depth <= 11 and not solved:
    print("depth {}".format(depth))
    solved = IDAStar(s, depth, [])
    depth += 1














class Point:
	def __init__(self,x,y,z):
		self.x=x
		self.y=y
		self.z=z

	def rotateX(self,a):
		a = mt.radians(a)
		(self.y , self.z) = (self.y * mt.cos(a) - self.z * mt.sin(a) , self.y * mt.sin(a) + self.z * mt.cos(a))
		return self
	
	def rotateY(self,b):
		b = mt.radians(b)
		(self.x , self.z) = (self.z * mt.sin(b) + self.x * mt.cos(b) , self.z * mt.cos(b) - self.x * mt.sin(b))
		return self
	def rotateXY(self,a,b):
		return self.rotateX(a).rotateY(b)
	def project(self):
		return [self.x*(1+self.z/FOCAL)*S+CX , self.y*(1+self.z/FOCAL)*S+CY]

class Face:
	def __init__(self,corners,color):
		self.corners = corners
		self.color = color

	def __lt__(self,other):
		return self.zAvrg() < other.zAvrg()

	def center(self):
		pa=self.corners[0]
		pb = self.corners[2]
		return Point((pa.x+pb.x)/2,(pa.y+pb.y)/2,(pa.z+pb.z)/2)

	def zAvrg(self):
		return sum([p.z for p in self.corners])/4

	def rotateXY(self,a,b):
		self.corners = [p.rotateXY(a,b) for p in self.corners]
		return self

	def project(self):
		return [p.project() for p in self.corners]

	def draw(self,surf):
		pg.draw.polygon(surf,self.color,self.project())
		pg.draw.polygon(surf,BLA,self.project(),3)

class cube:
	def __init__(self):
		self.faces=[]
		self.layer=[[],[],[],[],[],[]] # U R F D L B
		self.cubie=[[],[],[],[],[],[],[],[]] # UBL UBR UFL UFR DBL DBR DFL DFR / correct rocation
		colors=[WHI,RED,GRE,YEL,ORA,BLU]
		r=-1
		for f in range(0,6):
			c = -1 if f % 2 == 0 else 1
			for i in range(2):
				b = i - 1
				for j in range(2):
					a = j - 1
					r+=1
					if f == 0:
						self.faces.append(Face([Point(b,c,a),Point(b,c,a+1),Point(b+1,c,a+1),Point(b+1,c,a)],colors[f]))
					elif f==1:
						self.faces.append(Face([Point(c,a,b),Point(c,a+1,b),Point(c,a+1,b+1),Point(c,a,b+1)],colors[f]))
					elif f==2:
						self.faces.append(Face([Point(a,b,-c),Point(a+1,b,-c),Point(a+1,b+1,-c),Point(a,b+1,-c)],colors[f]))
					elif f==3:
						self.faces.append(Face([Point(b,c,a),Point(b,c,a+1),Point(b+1,c,a+1),Point(b+1,c,a)],colors[f]))
					elif f==4:
						self.faces.append(Face([Point(c,a,b),Point(c,a+1,b),Point(c,a+1,b+1),Point(c,a,b+1)],colors[f]))
					elif f==5:
						self.faces.append(Face([Point(a,b,-c),Point(a+1,b,-c),Point(a+1,b+1,-c),Point(a,b+1,-c)],colors[f]))
					self.layer[f].append(r)

		self.rotateXY(0,-40)
		self.rotateXY(-26,0)


	def rotateLayer(self,l,d,surf):
		"""Rotation of the 1 layer, clock-> d=1, counterclock-> d=-1"""
		def liRot(l,n):
			return l[n:1]+l[:n]

		sl = self.layer[l]
		sf_old = copy.deepcopy(self.faces)
		u=Point((self.faces[sl[0]].center().x + self.faces[sl[3]].center().x)/2.0,
		  (self.faces[sl[0]].center().y + self.faces[sl[3]].center().y)/2.0,
		  (self.faces[sl[0]].center().z + self.faces[sl[3]].center().z)/2.0)
		a = mt.radians(3*d)
		#d = d if l%2 == 0 else -d
		c = mt.cos(a)
		s = mt.sin(a)
		R=[[u.x**2+c*(1-u.x**2) , u.x*u.y*(1-c)-u.z*s , u.x*u.z*(1-c)+u.y*s],
			 [u.x*u.y*(1-c)+u.z*s , u.y**2+c*(1-u.y**2) , u.y*u.z*(1-c)-u.x*s],
			 [u.x*u.z*(1-c)-u.y*s , u.y*u.z*(1-c)+u.x*s , u.z**2+c*(1-u.z**2)]] 
		d = d if l<3 else -d
		bct = []
		fct = []
		rct = []
		lct = []
		uct = []
		dct = []
		for i in range(30):
			for f in sl:
				self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
			if l==0: # UP
				back = self.layer[5][:2]
				front = self.layer[2][:2]
				right = []
				right.append(self.layer[1][0])
				right.append(self.layer[1][2])
				left = []
				left.append(self.layer[4][0])
				left.append(self.layer[4][2])
				up = self.layer[0][:4]
				if i==0:
					bct.append(self.faces[back[0]].color)
					bct.append(self.faces[back[1]].color)
					fct.append(self.faces[front[0]].color)
					fct.append(self.faces[front[1]].color)
					rct.append(self.faces[right[0]].color)
					rct.append(self.faces[right[1]].color)
					lct.append(self.faces[left[0]].color)
					lct.append(self.faces[left[1]].color)
					for xx in range(4):
						uct.append(self.faces[up[xx]].color)
				for f in back:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in front:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in right:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in left:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
			elif l==1: #right
				up = self.layer[0][2:4]
				down = self.layer[3][2:4]
				front = []
				front.append(self.layer[2][1])
				front.append(self.layer[2][3])
				back = []
				back.append(self.layer[5][1])
				back.append(self.layer[5][3])
				right = self.layer[1][:4]
				if i == 0:
					uct.append(self.faces[up[0]].color)
					uct.append(self.faces[up[1]].color)
					dct.append(self.faces[down[0]].color)
					dct.append(self.faces[down[1]].color)
					fct.append(self.faces[front[0]].color)
					fct.append(self.faces[front[1]].color)
					bct.append(self.faces[back[0]].color)
					bct.append(self.faces[back[1]].color)
					for xx in range(4):
						rct.append(self.faces[right[xx]].color)
				for f in up:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in down:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in front:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in back:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
			elif l==2: #front
				front = self.layer[2][:4]
				up = []
				up.append(self.layer[0][1])
				up.append(self.layer[0][3])
				down = []
				down.append(self.layer[3][1])
				down.append(self.layer[3][3])
				left = self.layer[4][2:4]
				right = self.layer[1][2:4]
				if i == 0:
					uct.append(self.faces[up[0]].color)
					uct.append(self.faces[up[1]].color)
					dct.append(self.faces[down[0]].color)
					dct.append(self.faces[down[1]].color)
					lct.append(self.faces[left[0]].color)
					lct.append(self.faces[left[1]].color)
					rct.append(self.faces[right[0]].color)
					rct.append(self.faces[right[1]].color)
					for xx in range(4):
						fct.append(self.faces[front[xx]].color)
				for f in up:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in down:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in left:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in right:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
			elif l==3: #down
				left = []
				left.append(self.layer[4][1])
				left.append(self.layer[4][3])
				right = []
				right.append(self.layer[1][1])
				right.append(self.layer[1][3])
				front = self.layer[2][2:4]
				back = self.layer[5][2:4]
				down = self.layer[3][:4]
				if i==0:
					lct.append(self.faces[left[0]].color)
					lct.append(self.faces[left[1]].color)
					rct.append(self.faces[right[0]].color)
					rct.append(self.faces[right[1]].color)
					fct.append(self.faces[front[0]].color)
					fct.append(self.faces[front[1]].color)
					bct.append(self.faces[back[0]].color)
					bct.append(self.faces[back[1]].color)
					for xx in range(4):
						dct.append(self.faces[down[xx]].color)
				for f in front:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in back:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in left:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in right:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
			elif l==4: # left
				front = []
				front.append(self.layer[2][0])
				front.append(self.layer[2][2])
				back = []
				back.append(self.layer[5][0])
				back.append(self.layer[5][2])
				up = self.layer[0][:2]
				down = self.layer[3][:2]
				left = self.layer[4][:4]
				if i==0:
					fct.append(self.faces[front[0]].color)
					fct.append(self.faces[front[1]].color)
					bct.append(self.faces[back[0]].color)
					bct.append(self.faces[back[1]].color)
					uct.append(self.faces[up[0]].color)
					uct.append(self.faces[up[1]].color)
					dct.append(self.faces[down[0]].color)
					dct.append(self.faces[down[1]].color)
					for xx in range(4):
						lct.append(self.faces[left[xx]].color)
				for f in front:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in back:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in up:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in down:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
			elif l==5: #back
				up = []
				up.append(self.layer[0][0])
				up.append(self.layer[0][2])
				down = []
				down.append(self.layer[3][0])
				down.append(self.layer[3][2])
				right = self.layer[1][:2]
				left = self.layer[4][:2]
				back = self.layer[5][:4]
				if i==0:
					for xx in range(4):
						bct.append(self.faces[back[xx]].color)
					uct.append(self.faces[up[0]].color)
					uct.append(self.faces[up[1]].color)
					dct.append(self.faces[down[0]].color)
					dct.append(self.faces[down[1]].color)
					rct.append(self.faces[right[0]].color)
					rct.append(self.faces[right[1]].color)
					lct.append(self.faces[left[0]].color)
					lct.append(self.faces[left[1]].color)
				for f in right:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in left:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in up:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]
				for f in down:
					self.faces[f].corners = [Point(p.x*R[0][0]+p.y*R[0][1]+p.z*R[0][2],
								   p.x*R[1][0]+p.y*R[1][1]+p.z*R[1][2],
								   p.x*R[2][0]+p.y*R[2][1]+p.z*R[2][2]) for p in self.faces[f].corners]


			surf.fill(BLA)
			self.draw(surf)
			pg.display.flip()
			time.sleep(0.01)
		
		self.faces = sf_old
		if d == 1:
			if l == 0:
				back = self.layer[5][:2]
				front = self.layer[2][:2]
				right = []
				right.append(self.layer[1][0])
				right.append(self.layer[1][2])
				left = []
				left.append(self.layer[4][0])
				left.append(self.layer[4][2])
				up = self.layer[0][:4]
				self.faces[back[0]].color = lct[1]
				self.faces[back[1]].color = lct[0]
				self.faces[front[0]].color = rct[1]
				self.faces[front[1]].color = rct[0]
				self.faces[right[0]].color = bct[0]
				self.faces[right[1]].color = bct[1]
				self.faces[left[0]].color = fct[0]
				self.faces[left[1]].color = fct[1]
				self.faces[up[0]].color = uct[1]
				self.faces[up[1]].color = uct[3]
				self.faces[up[2]].color = uct[0]
				self.faces[up[3]].color = uct[2] 
			elif l==1:
				up = self.layer[0][2:4]
				down = self.layer[3][2:4]
				front = []
				front.append(self.layer[2][1])
				front.append(self.layer[2][3])
				back = []
				back.append(self.layer[5][1])
				back.append(self.layer[5][3])
				right = self.layer[1][:4]
				self.faces[up[0]].color = fct[0]
				self.faces[up[1]].color = fct[1]
				self.faces[down[0]].color = bct[0]
				self.faces[down[1]].color = bct[1]
				self.faces[front[0]].color = dct[1]
				self.faces[front[1]].color = dct[0]
				self.faces[back[0]].color = uct[1]
				self.faces[back[1]].color = uct[0]
				self.faces[right[0]].color = rct[2]
				self.faces[right[1]].color = rct[0]
				self.faces[right[2]].color = rct[3]
				self.faces[right[3]].color = rct[1]
			elif l==2:
				front = self.layer[2][:4]
				up = []
				up.append(self.layer[0][1])
				up.append(self.layer[0][3])
				down = []
				down.append(self.layer[3][1])
				down.append(self.layer[3][3])
				left = self.layer[4][2:4]
				right = self.layer[1][2:4]
				self.faces[up[0]].color = lct[1]
				self.faces[up[1]].color = lct[0]
				self.faces[down[0]].color = rct[1]
				self.faces[down[1]].color = rct[0]
				self.faces[right[0]].color = uct[0]
				self.faces[right[1]].color = uct[1]
				self.faces[left[0]].color = dct[0]
				self.faces[left[1]].color = dct[1]
				self.faces[front[0]].color = fct[2]
				self.faces[front[1]].color = fct[0]
				self.faces[front[2]].color = fct[3]
				self.faces[front[3]].color = fct[1]
			elif l==3:
				left = []
				left.append(self.layer[4][1])
				left.append(self.layer[4][3])
				right = []
				right.append(self.layer[1][1])
				right.append(self.layer[1][3])
				front = self.layer[2][2:4]
				back = self.layer[5][2:4]
				down = self.layer[3][:4]
				self.faces[left[0]].color = fct[0]
				self.faces[left[1]].color = fct[1]
				self.faces[front[0]].color = rct[1]
				self.faces[front[1]].color = rct[0]
				self.faces[right[0]].color = bct[0]
				self.faces[right[1]].color = bct[1]
				self.faces[back[0]].color = lct[1]
				self.faces[back[1]].color = lct[0]

				self.faces[down[0]].color = dct[1]
				self.faces[down[1]].color = dct[3]
				self.faces[down[2]].color = dct[0]
				self.faces[down[3]].color = dct[2]
			elif l==4:
				front = []
				front.append(self.layer[2][0])
				front.append(self.layer[2][2])
				back = []
				back.append(self.layer[5][0])
				back.append(self.layer[5][2])
				up = self.layer[0][:2]
				down = self.layer[3][:2]
				left = self.layer[4][:4]
				self.faces[front[0]].color = dct[1]
				self.faces[front[1]].color = dct[0]
				self.faces[back[0]].color = uct[1]
				self.faces[back[1]].color = uct[0]
				self.faces[up[0]].color = fct[0]
				self.faces[up[1]].color = fct[1]
				self.faces[down[0]].color = bct[0]
				self.faces[down[1]].color = bct[1]

				self.faces[left[0]].color = lct[2]
				self.faces[left[1]].color = lct[0]
				self.faces[left[2]].color = lct[3]
				self.faces[left[3]].color = lct[1]
			elif l==5:
				up = []
				up.append(self.layer[0][0])
				up.append(self.layer[0][2])
				down = []
				down.append(self.layer[3][0])
				down.append(self.layer[3][2])
				right = self.layer[1][:2]
				left = self.layer[4][:2]
				back = self.layer[5][:4]
				self.faces[up[0]].color = lct[1]
				self.faces[up[1]].color = lct[0]
				self.faces[down[0]].color = rct[1]
				self.faces[down[1]].color = rct[0]
				self.faces[right[0]].color = uct[0]
				self.faces[right[1]].color = uct[1]
				self.faces[left[0]].color = dct[0]
				self.faces[left[1]].color = dct[1]

				self.faces[back[0]].color = bct[2]
				self.faces[back[1]].color = bct[0]
				self.faces[back[2]].color = bct[3]
				self.faces[back[3]].color = bct[1]


		elif d == -1:
			if l == 0:
				back = self.layer[5][:2]
				front = self.layer[2][:2]
				right = []
				right.append(self.layer[1][0])
				right.append(self.layer[1][2])
				left = []
				left.append(self.layer[4][0])
				left.append(self.layer[4][2])
				up = self.layer[0][:4]
				self.faces[back[0]].color = rct[0]
				self.faces[back[1]].color = rct[1]
				self.faces[front[0]].color = lct[0]
				self.faces[front[1]].color = lct[1]
				self.faces[right[0]].color = fct[1]
				self.faces[right[1]].color = fct[0]
				self.faces[left[0]].color = bct[1]
				self.faces[left[1]].color = bct[0]
				self.faces[up[0]].color = uct[2]
				self.faces[up[1]].color = uct[0]
				self.faces[up[2]].color = uct[3]
				self.faces[up[3]].color = uct[1] 
			elif l==1:
				up = self.layer[0][2:4]
				down = self.layer[3][2:4]
				front = []
				front.append(self.layer[2][1])
				front.append(self.layer[2][3])
				back = []
				back.append(self.layer[5][1])
				back.append(self.layer[5][3])
				right = self.layer[1][:4]
				self.faces[up[0]].color = bct[1]
				self.faces[up[1]].color = bct[0]
				self.faces[down[0]].color = fct[1]
				self.faces[down[1]].color = fct[0]
				self.faces[front[0]].color = uct[0]
				self.faces[front[1]].color = uct[1]
				self.faces[back[0]].color = dct[0]
				self.faces[back[1]].color = dct[1]
				self.faces[right[0]].color = rct[1]
				self.faces[right[1]].color = rct[3]
				self.faces[right[2]].color = rct[0]
				self.faces[right[3]].color = rct[2]
			elif l==2:
				front = self.layer[2][:4]
				up = []
				up.append(self.layer[0][1])
				up.append(self.layer[0][3])
				down = []
				down.append(self.layer[3][1])
				down.append(self.layer[3][3])
				left = self.layer[4][2:4]
				right = self.layer[1][2:4]
				self.faces[up[0]].color = rct[0]
				self.faces[up[1]].color = rct[1]
				self.faces[down[0]].color = lct[0]
				self.faces[down[1]].color = lct[1]
				self.faces[right[0]].color = dct[1]
				self.faces[right[1]].color = dct[0]
				self.faces[left[0]].color = uct[1]
				self.faces[left[1]].color = uct[0]
				self.faces[front[0]].color = fct[1]
				self.faces[front[1]].color = fct[3]
				self.faces[front[2]].color = fct[0]
				self.faces[front[3]].color = fct[2]
			elif l==3:
				left = []
				left.append(self.layer[4][1])
				left.append(self.layer[4][3])
				right = []
				right.append(self.layer[1][1])
				right.append(self.layer[1][3])
				front = self.layer[2][2:4]
				back = self.layer[5][2:4]
				down = self.layer[3][:4]
				self.faces[left[0]].color = bct[1]
				self.faces[left[1]].color = bct[0]
				self.faces[front[0]].color = lct[0]
				self.faces[front[1]].color = lct[1]
				self.faces[right[0]].color = fct[1]
				self.faces[right[1]].color = fct[0]
				self.faces[back[0]].color = rct[0]
				self.faces[back[1]].color = rct[1]
				self.faces[down[0]].color = dct[2]
				self.faces[down[1]].color = dct[0]
				self.faces[down[2]].color = dct[3]
				self.faces[down[3]].color = dct[1]
			elif l==4:
				front = []
				front.append(self.layer[2][0])
				front.append(self.layer[2][2])
				back = []
				back.append(self.layer[5][0])
				back.append(self.layer[5][2])
				up = self.layer[0][:2]
				down = self.layer[3][:2]
				left = self.layer[4][:4]
				self.faces[front[0]].color = uct[0]
				self.faces[front[1]].color = uct[1]
				self.faces[back[0]].color = dct[0]
				self.faces[back[1]].color = dct[1]
				self.faces[up[0]].color = bct[1]
				self.faces[up[1]].color = bct[0]
				self.faces[down[0]].color = fct[1]
				self.faces[down[1]].color = fct[0]
				self.faces[left[0]].color = lct[1]
				self.faces[left[1]].color = lct[3]
				self.faces[left[2]].color = lct[0]
				self.faces[left[3]].color = lct[2]

			elif l==5:
				up = []
				up.append(self.layer[0][0])
				up.append(self.layer[0][2])
				down = []
				down.append(self.layer[3][0])
				down.append(self.layer[3][2])
				right = self.layer[1][:2]
				left = self.layer[4][:2]
				back = self.layer[5][:4]
				self.faces[up[0]].color = rct[0]
				self.faces[up[1]].color = rct[1]
				self.faces[down[0]].color = lct[0]
				self.faces[down[1]].color = lct[1]
				self.faces[right[0]].color = dct[1]
				self.faces[right[1]].color = dct[0]
				self.faces[left[0]].color = uct[1]
				self.faces[left[1]].color = uct[0]
				self.faces[back[0]].color = bct[1]
				self.faces[back[1]].color = bct[3]
				self.faces[back[2]].color = bct[0]
				self.faces[back[3]].color = bct[2]
		
		surf.fill(BLA)
		self.draw(surf)
		pg.display.flip()


	def draw(self,surf):
		faces = list(self.faces)
		faces.sort()
		for face in faces:
			face.draw(surf)

	def rotateXY(self,a,b):
		self.faces = [f.rotateXY(a,b) for f in self.faces]


def __rec_solve(cube):
	if check(cube):
		return True


def check(cube):
	for i in range(6):
		checkcolor = colorind[i]
		for j in range(4):
			if checkcolor != cube.faces[(i*4)+j].color:
				print("false")
				return False
	print("solve")
	return True

def minmove(cube,currentlocation,currentori,goallocation,goalori=0):
	a=1
	return a

def solver(cube):
	state = []
	b = []
	for i in range(8):
		for j in range(3):
			state.append(cube.faces[origincubie[i][j]].color)
		for j in range(8):
			res = 0
			a = gorigincubiecolor[j]
			for x in range(3):
				for xx in range(3):
					if a[x] == state[xx]:
						res+=1
						break
			if res == 3:
				if a[0] == state[1]: #clockwise
					ori = 1
				elif a[0] == state[2]: #counterclockwise
					ori = 2
				else: #correct
					ori = 0
				b.append((i,j,ori))
				break
		state = []
		
	print(b)
	minmove(cube,b[0][1],b[0][2],b[0][0],0)


def abc(cube):
	s = []
	
	for i in range(6):
		if cube.faces[0].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[2].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[1].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[3].color == colorind[i]:
			s.append(i)
			
	for i in range(6):
		if cube.faces[6].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[4].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[7].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[5].color == colorind[i]:
			s.append(i)
			
	for i in range(6):
		if cube.faces[8].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[9].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[10].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[11].color == colorind[i]:
			s.append(i)
			
	for i in range(6):
		if cube.faces[13].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[15].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[12].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[14].color == colorind[i]:
			s.append(i)
			
	for i in range(6):
		if cube.faces[16].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[18].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[17].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[19].color == colorind[i]:
			s.append(i)
			
	for i in range(6):
		if cube.faces[21].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[20].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[23].color == colorind[i]:
			s.append(i)
	for i in range(6):
		if cube.faces[22].color == colorind[i]:
			s.append(i)

	return s


def random(cube,surf,s):
	for i in range(12):
		d=0
		x = rd.randrange(0,12)
		if x >= 0 and x <= 2:
			d = 1
		elif x>=3 and x<=5:
			d = -1
		elif x>=6 and x<=8:
			x -= 6
			d = -1
		elif x>=9 and x<=11:
			x -= 6
			d = 1
		cube.rotateLayer(x,d,surf)
	s = abc(cube)
		
	d1 = "      ┌──┬──┐\n"
	d2 = "      │ {}│ {}│\n".format(s[0], s[1])
	d3 = "      ├──┼──┤\n"
	d4 = "      │ {}│ {}│\n".format(s[2], s[3])
	d5 = "┌──┬──┼──┼──┼──┬──┬──┬──┐\n"
	d6 = "│ {}│ {}│ {}│ {}│ {}│ {}│ {}│ {}│\n".format(s[16], s[17], s[8], s[9], s[4], s[5], s[20], s[21])
	d7 = "├──┼──┼──┼──┼──┼──┼──┼──┤\n"
	d8 = "│ {}│ {}│ {}│ {}│ {}│ {}│ {}│ {}│\n".format(s[18], s[19], s[10], s[11], s[6], s[7], s[22], s[23])
	d9 = "└──┴──┼──┼──┼──┴──┴──┴──┘\n"
	d10 = "      │ {}│ {}│\n".format(s[12], s[13])
	d11 = "      ├──┼──┤\n"
	d12 = "      │ {}│ {}│\n".format(s[14], s[15])
	d13 = "      └──┴──┘\n"
	f = open("cubestate.txt","w")
	f.write(d1)
	f.write(d2)
	f.write(d3)
	f.write(d4)
	f.write(d5)
	f.write(d6)
	f.write(d7)
	f.write(d8)
	f.write(d9)
	f.write(d10)
	f.write(d11)
	f.write(d12)
	f.write(d13)
	return


if __name__=='__main__':
	pg.init()
	pg.key.set_repeat(100,10)
	surf=pg.display.set_mode((350,350))
	rc=cube()
	rc.draw(surf)
	pg.display.flip()
	pg.display.set_caption("cube")
	ok=True
	while ok:
		time.sleep(0.001)
		for evt in pg.event.get():
			if evt.type == quit:
				ok = False
			elif evt.type == pg.KEYDOWN:
				kL = pg.key.get_pressed()
				k = evt.key
				d = -1 if kL[K_KP1] else 1
				if k == pg.K_KP6:
					rc.rotateLayer(1,d,surf)
				elif k == pg.K_KP8:
					rc.rotateLayer(0,d,surf)
				elif k == pg.K_KP5:
					rc.rotateLayer(2,d,surf)
				elif k == pg.K_KP2:
					rc.rotateLayer(3,d,surf)
				elif k == pg.K_KP4:
					rc.rotateLayer(4,d,surf)
				elif k == pg.K_KP0:
					rc.rotateLayer(5,d,surf)
				elif k==pg.K_KP3:
					check(rc)
				elif k==pg.K_KP9:
					s = abc(rc)
					print(s)
					solveCube(s)
					print(x1xx)
					aw = strstr[0].split(" ")
					strstr = []
					for m in aw:
						if m == 'U':
							rc.rotateLayer(0,1,surf)
						elif m == 'U\'':
							rc.rotateLayer(0,-1,surf)
						elif m == 'R':
							rc.rotateLayer(1,1,surf)
						elif m == 'R\'':
							rc.rotateLayer(1,-1,surf)
						elif m == 'F':
							rc.rotateLayer(2,1,surf)
						elif m == 'F\'':
							rc.rotateLayer(2,-1,surf)
						elif m == 'U2':
							rc.rotateLayer(0,1,surf)
							rc.rotateLayer(0,1,surf)
						elif m == 'R2':
							rc.rotateLayer(1,1,surf)
							rc.rotateLayer(1,1,surf)
						elif m == 'F2':
							rc.rotateLayer(2,1,surf)
							rc.rotateLayer(2,1,surf)
				elif k==ord('n'):
					s = abc(rc)
					random(rc,surf,s)


