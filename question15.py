import nltk

def splitCounter(sentence):
	splittedSentence = sentence.split()
	wordlist = [[]]

	for word in splittedSentence:
		wordlist.append(word)
		wordlist.append(len(word))
	
	return wordlist

