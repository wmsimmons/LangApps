"""Converts Greek letters of Cypriot Arabic to Latin letters"""
import re

"""go through the alphabet section of the CMA grammar book, copy and paste each letter
   from the custom alphabet, paste the letter directly, return the result
   put the result (latin letters) into sanna_latined_words, put sanna_latined_words into
   a file that stores all the Cypriot Arabic latinized words for linguistic study

   """

letter_to_letter = 'β/v, α/a, ε/e, ι/i, ο/o, ου/ou, θ/i, γ/y, γ/gh, δ/th, δδ/dh, ζ/z, Δ/d, τζ'
new_letters = letter_to_letter.str2tuple()

def transliterate(text):
	sanna_latined_words = []
	[letter[1] for letter in new_letters]
	for word in text:
		for letter in word:
			#change the letter(the key) to the "value" of the tuple new_letters and add it to sanna_latined_letters
			if letter in letter_to_letter:
				#need to replace the letter to the latin one, re.sub() or something like is needed.
				letter.
		sanna_latined_words.append(word)