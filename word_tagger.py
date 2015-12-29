"this is to tag words"
import nltk
import sys

def save():
	#takes the result from annotator and adds it to a file
	nameOfFile = raw_input("Which file is this to be placed in? ")

	filename  = open(nameOfFile + '.txt','w')
	sys.stdout = filename
	#do work

def annotator(text):
	#processedText = text.split()
	annotatedText = []
	"""annotator needs to tag the punc marks seperate from the words"""

	"ask the user what p.o.s a word is, for every word in the text"
	for word in processedText:
		word_pos = raw_input("Insert the POS of the word " + word + ": ")
		if word:
			annotatedText.append(word + "/" + word_pos)
		
	annotatedText = str(annotatedText)
	annotatedText = annotatedText.lower().encode('utf-8')
	#this needs to be joined before list conversion #annotatedText = list(annotatedText)

	nameOfFile = raw_input("Which file is this to be placed in? ")

	filename = open('C:/Users/wkeil/Desktop/qafastamalti/qafasTaMalti/hawaiianCorpus/' + nameOfFile + '.txt','a')
	filename.write(annotatedText)

	print(filename)
	return annotatedText

	"take the input from the user and add a '/' between the pos and the word"

	"""punctuation may be a problem, how to deal with seperating words from punctuation
	and tag them as a punc mark"""

<<<<<<< HEAD
=======

<<<<<<< HEAD
def a(text):
	#processedText = text.split()
	annotatedText = []
	"""annotator needs to tag the punc marks seperate from the words"""

	"ask the user what p.o.s a word is, for every word in the text"
	for word in text:
		word_pos = raw_input("Insert the POS of the word " + word + ": ")
		if word:
			annotatedText.append(word + "/" + word_pos)

	annotatedText = str(annotatedText)
	annotatedText = annotatedText.lower()
	#this needs to be joined before list conversion #annotatedText = list(annotatedText)
	return annotatedText


=======
>>>>>>> c753ff2fc42fd775fc414bc9c17459e8f45a4d93
>>>>>>> b1c13b833b21c59a497ab405b17fd77b21a327e9
