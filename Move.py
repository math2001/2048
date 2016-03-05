import random

class Move:
	def __init__(self, structure=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]):
		self.structure = structure

	def add_random_case(self):
		nb = random.randint(0, 5)
		return None

	def right(self):
		for ligne in self.structure:
			move = False
			for i in range(len(ligne)):
				if i < len(ligne) - 1:
					if ligne[i] == ligne[i + 1] or ligne[i + 1] == 0:
						ligne[i + 1] += ligne[i]
						ligne[i] = 0
						move = True
			if move:
				print "more ! PB"
				for i in range(len(ligne)):
					if i < len(ligne) - 1:
						if ligne[i] == ligne[i + 1] or ligne[i + 1] == 0:
							ligne[i + 1] += ligne[i]
							ligne[i] = 0
							move = True

	def left(self):
		for ligne in self.structure:
			move = False
			for i in reversed(range(len(ligne))):
				if i > 0:
					if ligne[i] == ligne[i - 1] or ligne[i - 1] == 0:
						ligne[i - 1] += ligne[i]
						ligne[i] = 0
						move = True
			if move:
				for i in reversed(range(len(ligne))):
					if i > 0:
						if ligne[i] == ligne[i - 1] or ligne[i - 1] == 0:
							ligne[i - 1] += ligne[i]
							ligne[i] = 0
							move = True

	def up(self):
		move = False
		for I in reversed(range(len(self.structure))):
			for i in reversed(range(len(self.structure[I]))):
				if I > 0:
					if self.structure[I - 1][i] == self.structure[I][i] or self.structure[I - 1][i] == 0:
						self.structure[I - 1][i] += self.structure[I][i]
						self.structure[I][i] = 0
						move = True
		if move:
			for I in reversed(range(len(self.structure))):
				for i in reversed(range(len(self.structure[I]))):
					if I > 0:
						if self.structure[I - 1][i] == self.structure[I][i] or self.structure[I - 1][i] == 0:
							self.structure[I - 1][i] += self.structure[I][i]
							self.structure[I][i] = 0
							move = True

	def down(self):
		move = False
		for I in range(len(self.structure)):
			for i in range(len(self.structure[I])):
				if I < len(self.structure[i]) - 1:
					if self.structure[I + 1][i] == self.structure[I][i] or self.structure[I + 1][i] == 0:
						self.structure[I + 1][i] += self.structure[I][i]
						self.structure[I][i] = 0
						move = True
		if move:
			for I in range(len(self.structure)):
				for i in range(len(self.structure[I])):
					if I < len(self.structure[i]) - 1:
						if self.structure[I + 1][i] == self.structure[I][i] or self.structure[I + 1][i] == 0:
							self.structure[I + 1][i] += self.structure[I][i]
							self.structure[I][i] = 0

	def get(self):
		return self.structure