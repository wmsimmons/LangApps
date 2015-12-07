"this is to tag words"
import nltk

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
	annotatedText = annotatedText.lower()
	#this needs to be joined before list conversion #annotatedText = list(annotatedText)
	return annotatedText

	"take the input from the user and add a '/' between the pos and the word"

	"""punctuation may be a problem, how to deal with seperating words from punctuation
	and tag them as a punc mark"""


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


