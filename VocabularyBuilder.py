from stemming.porter2 import stem
from collections import defaultdict

def isLongNumber(token):
  result = True
	for ch in token:
		if not ch in '0987654321':
			return token
	if len(token) >= 6:
		return "[LongNumber]"

def getTokenList(line):
	chlist = []
	for ch in line:
		if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
			ch = chr(ord(ch)+32)
			chlist.append(ch)
		elif (ord(ch) >= ord('a') and ord(ch) <= ord('z')) or (ord(ch) >= ord('0') and ord(ch) <= ord('9')):
			chlist.append(ch)
		else:
			chlist.append(' ')

	line = ''.join(chlist)

	tokenlist = line.split(' ')

	vocabulary = defaultdict(int)

	for token in tokenlist:
		if token == '':
			continue
		token = stem(token)
		token = isLongNumber(token)
		vocabulary[token] += 1

	return vocabulary

def vocabularyLoader():
	voclines = file("vocabulary").readlines()
	voclines = [line.rstrip('\n\r').rstrip('\n') for line in voclines]
	return voclines

def extractContent(line):
	label, idx = ('ham', 3) if line[0] == 'h' else ('spam', 4)
	while line[idx] in "\n\r\t ":
		idx += 1
	content = line[idx:]
	content = content.rstrip("\n").rstrip('\n\r')
	return label, content

if __name__ == "__main__":
	corpus_file = file("SMSSpamCollection")
	lines = corpus_file.readlines()

	vocabulary = dict()
	for line in lines:
		label, line = extractContent(line)
		
		tokenlist = getTokenList(line)

		for token in tokenlist.keys():
			if not token in vocabulary:
				vocabulary[token] = True

	vocabulary_file = open("vocabulary", "w")
	for token in vocabulary.keys():
		if token == None:
			continue
		vocabulary_file.write(token + '\n')

	vocabulary_file.close()
