from VocabularyBuilder import getTokenList, vocabularyLoader, extractContent
from collections import defaultdict

if __name__ == "__main__":
  corpus_file = file("TrainData")
	lines = corpus_file.readlines()

	vocabulary = vocabularyLoader()
	hamDict = defaultdict(int)
	spamDict = defaultdict(int)

	#accounting
	for line in lines:
		label, line = extractContent(line)
		if label == 'ham':
			classDict = hamDict
		else:
			classDict = spamDict
		tokenlist = getTokenList(line)
		for token, count in tokenlist.items():
			classDict[token] += count

	hamModel = open("hamModel", "w")
	spamModel = open("spamModel", "w")
	for token in vocabulary:
		if token == None:
			continue
		hamModel.write(token + " " + str(hamDict[token]+1) + "\n")
		spamModel.write(token + " " + str(spamDict[token]+1) + "\n")
	hamModel.close()
	hamModel.close()
