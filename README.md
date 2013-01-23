GibbsSampling4NaiveBayes
========================

A Naive Bayes classifier on spam SMS using Gibbs Sampling for inference.

Dataset is also available at [0].

These programs are just implementation of idea in [1], defaultly using 20% of the data for model generation.
Portion of ham/spam message in both train & test data are the same.

Repro
========================
python DataSeparation.py - for stochastically separating ham/spam messages to train/test data propotional to given parameter.

python VocabularyBuilder.py - for building uniform vocabulary for training, inference and testing.

python ModelGenerator.py - train model for inference

python inference.py - load model and inference ham/spam type for test message, accounting information is printed in console.

Feature Engineering
========================
1. all uppercase are transform to lower
2. long number is replaced by "[LongNumber]"
3. porter2 stemmer is used before step 2

Conclusion
========================
These naive model and simple features yields over 97% precision.

Reference
========================
[0] http://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection

[1] Resnik, Philip, and Eric Hardisty. Gibbs sampling for the uninitiated. No. CS-TR-4956. MARYLAND UNIV COLLEGE PARK INST FOR ADVANCED COMPUTER STUDIES, 2010.

Environment Requirement
========================
Python 2.7.3

Numpy 1.6.2

stemming 1.0
