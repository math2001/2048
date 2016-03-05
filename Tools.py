def list_print(liste):

	print '['
	for i, el in enumerate(liste):
		coma = ', ' if i < len(liste) - 1 else ""
		print '    ', str(el) + coma
	print ']'