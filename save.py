def move_right():
	for ligne in structure:
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

def move_left():
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

def move_top():
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

def move_bottom():
	move = False
	for I in range(len(structure)):
		for i in range(len(structure[I])):
			if I < len(structure[i]) - 1:
				if structure[I + 1][i] == structure[I][i] or structure[I + 1][i] == 0:
					structure[I + 1][i] += structure[I][i]
					structure[I][i] = 0
					move = True
	if move:
		for I in range(len(structure)):
			for i in range(len(structure[I])):
				if I < len(structure[i]) - 1:
					if structure[I + 1][i] == structure[I][i] or structure[I + 1][i] == 0:
						structure[I + 1][i] += structure[I][i]
						structure[I][i] = 0