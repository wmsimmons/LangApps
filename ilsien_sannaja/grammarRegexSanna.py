import re 
import nltk
from nltk.tokenize import word_tokenize 

def cmaStopWord(text):
	"""To search and filter out stop words"""
	
def openFile(filename):
	f = open('C:/Users/wkeil/Desktop/qafastamalti/qafasTaMalti/ilsien_sannaja/' + filename
	 + '.txt', 'r')
	text = f.read()
	f.close()
	# tokens = word_tokenize(text)
	# words = [w.lower() for w in tokens]
	# vocab = sorted(set(words))
	#text1 = text.split()
	#abstracts = nltk.Text(text1) #attach NLTK funcc
	# return set(vocab)
	return text

def cmaPresVerb(text):
	"""To find possible present and progressive verbs"""
	allVerbs = []

	matches = re.findall(r'\bpk[a-zA-Z]+', text, re.I)
	for match in matches:
		allVerbs.append(match)
	return allVerbs
