#model validation
hamlines = file('hamModel').readlines()
spamlines = file('spamModel').readlines()

isSame = True

for idx, hamline in enumerate(hamlines):
  spamline = spamlines[idx]
	if not hamline.split(' ')[0] == spamline.split(' ')[0]:
		isSame = False
		break

print isSame
