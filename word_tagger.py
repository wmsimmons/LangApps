"this is to tag words"
import nltk

def annotator(text):
	processedText = text.split()
	annotatedText = []
	"ask the user what p.o.s a word is, for every word in the text"
		for word in processedText:
			word_pos = input("Insert the POS of the word" + word + ": ")
				if word:
					annotatedText.append(word + "/" + word_pos)

	"take the input from the user and add a '/' between the pos and the word"

	"""punctuation may be a problem, how to deal with seperating words from punctuation
	and tag them as a punc mark"""



