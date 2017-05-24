from nltk import * 
from nltk.text import Text
from nltk.tokenize import sent_tokenize, word_tokenize
from imp import reload
import sys

def lookup(word):
	text = open("C:/Users/langu/Desktop/qafasTaMalti/sanna/sannadictsite/cypriotArabic.txt", "rU", encoding="utf-8").read()
	tokens = word_tokenize(text)
	text = Text(tokens)
	result = text.concordance(word)

	return result

lookup("sallu")