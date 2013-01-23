import numpy as np
from VocabularyBuilder import getTokenList, extractContent
import math

def thetaSample(hyperparameter):
  return np.random.dirichlet(hyperparameter, 1)

def getLikelihood(tokenDict, theta, reverseIdx):
	likelihood = 1.0
	for token, count in tokenDict.items():
		if token == None:
			continue
		try:
			likelihood *= math.pow(theta[0][reverseIdx[token]], count)
		except:
			print token
			print reverseIdx[token]
			print theta[0][reverseIdx[token]]
			raw_input()
	return likelihood

#load model
gamma = 0.01
reverseIdx = dict()
hamHyper = list()
spamHyper = list()
for idx, line in enumerate(file("hamModel").readlines()):
	word, count = line.rstrip('\n\r').rstrip('\n').split(' ')
	count = int(count)
	reverseIdx[word] = idx
	hamHyper.append(count+gamma)
for line in file("spamModel").readlines():
	word, count = line.rstrip('\n\r').rstrip('\n').split(' ')
	count = int(count)
	spamHyper.append(count+gamma)

#prior info
hamPrior = 0.866
spamPrior = 1 - hamPrior

#Gibbs Sampler Configuration
iternum = 10

#Accounter
ham_correct = ham_wrong = spam_correct = spam_wrong = 0

#testing phase
corpus_file = file("TestData")
lines = corpus_file.readlines()

for idx, line in enumerate(lines):
	label, line = extractContent(line)

	#Sampling Accounter
	hamProb = .0
	spamProb = .0

	#Gibbs Inference
	for i in xrange(iternum):
		#sampling theta
		hamTheta = thetaSample(hamHyper)
		spamTheta = thetaSample(spamHyper)
		
		#get likelihood
		tokenDict = getTokenList(line)
		hamLikelihood = getLikelihood(tokenDict, hamTheta, reverseIdx)
		spamLikelihood = getLikelihood(tokenDict, spamTheta, reverseIdx)

		#get numerator
		hamNumerator = hamLikelihood * hamPrior
		spamNumerator = spamLikelihood * spamPrior
		normalizer = hamNumerator + spamNumerator + 0.0000000000000000000001

		#get probability
		hamProb += hamNumerator / normalizer
		spamProb += spamNumerator / normalizer

	#approximation
	hamProb /= iternum
	spamProb /= iternum

	expected = label
	actual = 'ham' if hamProb > spamProb else 'spam'
	if expected == actual and expected == 'ham':
		ham_correct += 1
	if (not expected == actual) and expected == 'ham':
		ham_wrong += 1
	if expected == actual and expected == 'spam':
		spam_correct += 1
	if (not expected == actual) and expected == 'spam':
		spam_wrong += 1
	
	if idx % 100 == 0:
		print "Correct: ", ham_correct + spam_correct, " Wrong: ", spam_wrong + ham_wrong

precision = float(spam_correct + ham_correct) / len(lines)
print precision
