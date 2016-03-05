import random

class Move:
	def __init__(self, structure=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]):
		self.structure = structure

	def add_nb(self):
		cont = 1
		while cont < 50:
			rnd1 = random.randint(0, len(self.structure) - 1)
			rnd2 = random.randint(0, 3)
			if self.structure[rnd1][rnd2] == 0:
				self.structure[rnd1][rnd2] = 2
				cont = 100
				return True
			cont += 1
		for ligne in self.structure:
			for case in ligne:
				if case == 0:
					return False
		return True

	def right(self, structure='d'):
		if structure == "d": structure = self.structure
		for ligne in structure:
			move = False
			for i in range(len(ligne)):
				if i < len(ligne) - 1:
					if ligne[i] == ligne[i + 1] or ligne[i + 1] == 0:
						ligne[i + 1] += ligne[i]
						ligne[i] = 0
						move = True
				
			if move:
				for i in range(len(ligne)):
					if i < len(ligne) - 1:
						if ligne[i] == ligne[i + 1] or ligne[i + 1] == 0:
							ligne[i + 1] += ligne[i]
							ligne[i] = 0
							move = True
		
	def left(self, structure='d'):
		if structure == "d": structure = self.structure
		for ligne in structure:
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

	def up(self, structure='d'):
		if structure == "d": structure = self.structure
		move = False
		for I in reversed(range(len(structure))):
			for i in reversed(range(len(structure[I]))):
				if I > 0:
					if structure[I - 1][i] == structure[I][i] or structure[I - 1][i] == 0:
						structure[I - 1][i] += structure[I][i]
						structure[I][i] = 0
						move = True
		if move:
			for I in reversed(range(len(structure))):
				for i in reversed(range(len(structure[I]))):
					if I > 0:
						if structure[I - 1][i] == structure[I][i] or structure[I - 1][i] == 0:
							structure[I - 1][i] += structure[I][i]
							structure[I][i] = 0
							move = True

	def down(self, structure='d'):
		if structure == "d": structure = self.structure
		move = False
		for I in range(len(structure)):
			for i in range(len(structure[I])):
				if I < len(structure[i]) - 1:
					if structure[I + 1][i] == structure[I][i] or structure[I + 1][i] == 0:
						structure[I + 1][i] += structure[I][i]
						structure[I][i] = 0
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

	def check_win(self):
		for ligne in self.structure:
			for case in ligne:
				if case == 2048:
					return True
		return False