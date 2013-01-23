import random

corpus_file = file("SMSSpamCollection")
lines = corpus_file.readlines()

#separate
hams = [line for line in lines if line[0] == 'h']
random.shuffle(hams)
spams = [line for line in lines if line[0] == 's']
random.shuffle(spams)

test_portion = 0.8

#generate data set
test_file = open("TestData","w")
train_file = open("TrainData","w")

for data in [hams, spams]:
  for idx, line in enumerate(data):
		if idx <= test_portion * len(data):
			test_file.write(line)
		else:
			train_file.write(line)

test_file.close()
train_file.close()
