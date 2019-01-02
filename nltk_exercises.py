import nltk

malticorp = open('malti text.txt')
f = malticorp.read()
# after reading the file, the words must be tokenized
m = nltk.word_tokenize(f)
# now a freqdist can be made
fdist = nltk.FreqDist(m)
print(fdist[:40])

##### chapter 2 #####
# question 2
from nltk.corpus import gutenberg
words = gutenberg.words()
len(words)
len(set(words))

#question 3
#access some sample text in two different genres
from nltk.corpus import brown
cats = brown.categories()
adventures = brown.categories('adventure')
humor = brown.categories('humor')

'''
>>> humor = brown.words(categories=['adventure'])
>>> humor
[u'Dan', u'Morgan', u'told', u'himself', u'he', ...]
>>> quests = brown.words(categories=['humor'])
>>> quests[:100]
[u'It', u'was', u'among', u'these', u'that', u'Hinkle', ...]
'''
# question 4
from nltk.corpus import state_union
words = ['men', 'women', 'people']
cfd = nltk.ConditionalFreqDist(
   (word, len(word))
   for word in words
   for klma in state_union.words())
cfd.plot(cumulative=True)

# question 5
from nltk.corpus import wordnet as wn
dream = wn.synsets('dream')
language = wn.synsets('language')
spirit = wn.synsets('spirit')
wn.synset('car.n.01')
Synset('car.n.01')
wn.synset('car.n.01').part_meronyms()
[Synset('accelerator.n.01'), Synset('air_bag.n.01'), Synset('auto_accessory.n.01'), Synset('automobile_engine.n.01'), Synset('automobile_horn.n.01'), Synset('buffer.n.06'), Synset('bumper.n.02'), Synset('car_door.n.01'), Synset('car_mirror.n.01'), Synset('car_seat.n.01'), Synset('car_window.n.01'), Synset('fender.n.01'), Synset('first_gear.n.01'), Synset('floorboard.n.02'), Synset('gasoline_engine.n.01'), Synset('glove_compartment.n.01'), Synset('grille.n.02'), Synset('high_gear.n.01'), Synset('hood.n.09'), Synset('luggage_compartment.n.01'), Synset('rear_window.n.01'), Synset('reverse.n.02'), Synset('roof.n.02'), Synset('running_board.n.01'), Synset('stabilizer_bar.n.01'), Synset('sunroof.n.01'), Synset('tail_fin.n.02'), Synset('third_gear.n.01'), Synset('window.n.02')]
wn.synset('car.n.01').substance_meronyms()
[]
wn.synset('car.n.01').member_holonyms()
[]
wn.synset('accelerator.n.01').member_holonyms()
[]
wn.synset('accelerator.n.01').part_holonyms()
[Synset('airplane.n.01'), Synset('car.n.01')]
wn.synset('accelerator.n.01').part_holonyms()


#question 6 - need to answer the question by researching and writing a response

#question 7
# >>> words = state_union.words()
# >>> text = nltk.Text(words)
# >>> text.concordance('however')

# question 8
import nltk.corpus.names
names.words()[0]
names_files = nltk.corpus.names.fileids()
# cfd8 = nltk.ConditionalFreqDist(
# ...   (file, name[0])
# ...   for file in names_files
# ...   for name in nltk.corpus.names.words(file))
cfd8.plot()
cdf8.tabulate()

''' the letter S is the most common first letter for male names
# the letter M is the most common first letter for female names '''

# question 9
text1 = nltk.corpus.brown.fileids('cp28') # romance
text2 = nltk.corpus.brown.fileids('cr01') # humor

def lexversity(text):
   tokens = len(text)
   vocab_size = len(set(text))
   return tokens / vocab_size

# commented for instruction
# >>> lexversity(nltk.corpus.brown.words())
# 20
nltk.corpus.brown.categories()
[u'adventure', u'belles_lettres', u'editorial', u'fiction', u'government', u'hobbies', u'humor', u'learned', u'lore', u'mystery', u'news', u'religion', u'reviews', u'romance', u'science_fiction']
nltk.corpus.reuters.categories()
[u'acq', u'alum', u'barley', u'bop', u'carcass', u'castor-oil', u'cocoa', u'coconut', u'coconut-oil', u'coffee', u'copper', u'copra-cake', u'corn', u'cotton', u'cotton-oil', u'cpi', u'cpu', u'crude', u'dfl', u'dlr', u'dmk', u'earn', u'fuel', u'gas', u'gnp', u'gold', u'grain', u'groundnut', u'groundnut-oil', u'heat', u'hog', u'housing', u'income', u'instal-debt', u'interest', u'ipi', u'iron-steel', u'jet', u'jobs', u'l-cattle', u'lead', u'lei', u'lin-oil', u'livestock', u'lumber', u'meal-feed', u'money-fx', u'money-supply', u'naphtha', u'nat-gas', u'nickel', u'nkr', u'nzdlr', u'oat', u'oilseed', u'orange', u'palladium', u'palm-oil', u'palmkernel', u'pet-chem', u'platinum', u'potato', u'propane', u'rand', u'rape-oil', u'rapeseed', u'reserves', u'retail', u'rice', u'rubber', u'rye', u'ship', u'silver', u'sorghum', u'soy-meal', u'soy-oil', u'soybean', u'strategic-metal', u'sugar', u'sun-meal', u'sun-oil', u'sunseed', u'tea', u'tin', u'trade', u'veg-oil', u'wheat', u'wpi', u'yen', u'zinc']
lexversity(nltk.corpus.reuters.words())
41
rcc = nltk.Text(nltk.corpus.reuters.words())
bcc = nltk.Text(nltk.corpus.brown.words())
rcc.concordance('animal', 79, 7)
''' >>> Displaying 7 of 34 matches:
erv division . In pesticides and in animal health care products Agrimont maint
STARTS CASE AGAINST EC LEVY A major animal feed producer , Cehave NV Veghel ( 
 with the full backing of the Dutch animal grain and feed trade association , 
ught by the Association of European Animal Feed Manufacturers , FEFAC . CHINA 
ort is higher than the value of the animal , he said . U . S . Officials said 
s would rise by an average 50 pct , animal feeds by 38 pct and tractors by 25 
turated fats , but unlike saturated animal fats , they do not enter the blood 
>>> bcc.concordance('animal', 79, 7)
Displaying 7 of 68 matches:
enalized for the city's services to animal care . In reply , Deputy Police Com
d that the city's contributions for animal care included $67,000 to the Women'
m Mr. Burman's refreshing Louisiana animal community . The fox is all ingratia
s in his introduction to this brief animal fable that Mr. Burman ought to win 
ewhere between the Southern dialect animal stories of Joel Chandler Harris ( U
here has never been a more engaging animal in all literature . This is not onl
Doyle as Beatie has a great fund of animal spirits , a strong voice and a warm
'''

# question 10
>>> len(nltk.corpus.brown.words())
1161192
>>> len(nltk.corpus.reuters.words())
1720901
>>> len(nltk.corpus.webtext.words())
396733
>>> len(set(nltk.corpus.webtext.words())
... )
21538
>>> len(set(nltk.corpus.brown.words()))
56057
>>> len(set(nltk.corpus.reuters.words()))
41600
>>> set1 = len(set(nltk.corpus.reuters.words())) * .33
>>> set2 = len(set(nltk.corpus.webtext.words())) * .33
>>> set3 = len(set(nltk.corpus.state_union.words())) * .33
'''fq1.max() was 'the' 
how to get access to THIS freqdist in decreasing order of frequency
'''

# question 11
demos = ['this', 'those', 'these', 'that', 'the']

newstxt = nltk.corpus.brown.words(categories='news')
romancetxt = nltk.corpus.brown.words(categories='romance')
humortxt = nltk.corpus.brown.words(categories='humor')

fdist_news    = nltk.FreqDist([word.lower() for word in newstxt])
fdist_romance = nltk.FreqDist([word.lower() for word in romancetxt])
fdist_humor = nltk.FreqDist([word.lower() for word in humortxt])

for demo in demos:
    print(demo + "-news:", fdist_news[demo],)
    print(demo + "-rom:", fdist_romance[demo],)
    print(demo + "-hum:", fdist_humor[demo],)

'''
>>> for demo in demos:
...     print(demo + "-news:", fdist_news[demo],)
...     print(demo + "-rom:", fdist_romance[demo],)
...     print(demo + "-hum:", fdist_humor[demo],)
... 
('this-news:', 320)
('this-rom:', 187)
('this-hum:', 76)
('those-news:', 66)
('those-rom:', 58)
('those-hum:', 13)
('these-news:', 70)
('these-rom:', 31)
('these-hum:', 18)
('that-news:', 829)
('that-rom:', 612)
('that-hum:', 252)
('the-news:', 6386)
('the-rom:', 2988)
('the-hum:', 1027)
'''

cfd_brown = nltk.ConditionalFreqDist(
  (genre, word)
  for genre in nltk.corpus.brown.categories()
  for word in nltk.corpus.brown.words(categories=genre))

genres = ['news', 'romance', 'humor']
cfd_brown.tabulate(conditions=genres, samples=demos)

#          this those these  that   the 
#    news   250    58    59   802  5580 
# romance   149    53    30   583  2758 
#   humor    59    10    16   241   930 

# question 12
>>> phoneme_dict = nltk.corpus.cmudict.dict() # it contains 123455 words
>>> len(phoneme_dict)

phoneme_dict['fire']
[[u'F', u'AY1', u'ER0'], [u'F', u'AY1', u'R']]
>>> len(phoneme_dict['fire'])
2
>>> for word,pron in phoneme_dict:
...   if len(phoneme_dict[word]) < 2:
...     
... 
  
>>> for word in phoneme_dict:
...   count = 0
...   if len(phoneme_dict[word]) < 2:
...     count += 1
... 

########################################3
''' since we aren't getting actual pronunciations from phoneme_dict
it isn't necessary to loop over it, only to loop over the words
since the words are what we are grabbing stuff from
'''
>>> for word in phoneme_dict:
...   if len(phoneme_dict[word]) < 2:
...     wcount.append(word)
... 
>>> len(wcount)
114214
>>> len(nltk.corpus.cmudict.dict())
123455
>>> len(nltk.corpus.cmudict.dict()) - len(wcount)
9241
>>> from __future__ import division
>>> float((multiprons / len(nltk.corpus.cmudict.dict()) )) 
0.07485318537118789
>>> float((multiprons / len(nltk.corpus.cmudict.dict()) )) * 100
#7.485318537118789 % of the words have more than 1 pronunciation 

# question 13
from nltk.corpus import wordnet as wn
>>> allwnsynsets = 0
>>> for word in wn.all_synsets('n'):
...   allwnsynsets += 1
... 
>>> allwnsynsets
82115
no_hypowords = 0
>>> for word in wn.all_synsets('n'):
...   if len(word.hyponyms()) < 1:
...     no_hypowords += 1
... 
no_hypowords
65422

>>> (no_hypowords / allwnsynsets)*100
79.67119283931072


# question 14
def supergloss(s):
    definition = wn.synset(s).definition()
    hyponyms = wn.synset(s).hyponyms()
    hypernyms = wn.synset(s).hypernyms()
    hypdefs = []
    hyperdefs = []

    for hyponym in hyponyms:
        hypdefs.append(hyponym.definition())

    for hypernym in hypernyms:
        hyperdefs.append(hypernym.definition())
    
    definition = str(definition)
    hypdefs = str(hypdefs)
    hyperdefs = str(hyperdefs)    

    return definition + " hyponyms: " + hypdefs + " hypernyms: " + hyperdefs

# question 15
fdist1 = nltk.FreqDist(nltk.Text(brown.words()))
[word for word in fdist1 if fdist1[word] >= 3]

# question 16
>>> for genre in brown.categories():
...   tokens = len(brown.words(categories=genre))
...   vocab = len(set(brown.words(categories=genre)))
...   lexdiv = lexversity(brown.words(categories=genre))
...   print(genre, tokens, vocab, lexdiv)
... 
(u'adventure', 69342, 8874, 7)
(u'belles_lettres', 173096, 18421, 9)
(u'editorial', 61604, 9890, 6)
(u'fiction', 68488, 9302, 7)
(u'government', 70117, 8181, 8)
(u'hobbies', 82345, 11935, 6)
(u'humor', 21695, 5017, 4)
(u'learned', 181888, 16859, 10)
(u'lore', 110299, 14503, 7)
(u'mystery', 57169, 6982, 8)
(u'news', 100554, 14394, 6)
(u'religion', 39399, 6373, 6)
(u'reviews', 40704, 8626, 4)
(u'romance', 70022, 8452, 8)
(u'science_fiction', 14470, 3233, 4)

# question 17
def top50(text):
newtext = nltk.Text(text)
fdist = nltk.FreqDist(newtext)
wordlist = []
for word, freq in fdist.most_common(500):
    if word not in nltk.corpus.stopwords.words():
        wordlist.append(word)
        if len(wordlist) == 50:
            print(wordlist)

# question 18
from nltk import bigrams
def top50bigrams(text):
    bigrams = bigrams(text)
    fdist = nltk.FreqDist(bigrams)
    bigram_list = []
    for bigram in fdist.most_common(300):
        if bigram not in nltk.corpus.stopwords.words():
            bigram_list.append(bigram)
            if len(bigram_list) == 50:
                print(bigram_list)

# question 19
brown.categories()
[u'adventure', u'belles_lettres', u'editorial', u'fiction', u'government', u'hobbies', u'humor', u'learned', u'lore', u'mystery', u'news', u'religion', u'reviews', u'romance', u'science_fiction']
cfd = nltk.ConditionalFreqDist(
  (genre, word)
  for genre in brown.categories()
  for word in brown.words(categories=genre))

 
genres = ['adventure', 'editorial', 'religion', 'romance', 'humor']
verbs = ['run', 'walk', 'sin', 'laugh', 'love']
cfd.tabulate(conditions=genres, samples=verbs)
            run  walk   sin laugh  love 
adventure    11    17     0     3     9 
editorial    11     2     3     0    13 
 religion     8     1    30     2    13 
  romance    16    10     2     6    32 
    humor     4     2     0     2     4 

# question 20
def word_freq(word, section):
  cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
  )
cfd.tabulate(conditions=[section], samples=[word])

# question 21
def guess_num_of_syllables(word):
  entries = nltk.corpus.cmudict.dict()
  for pron in entries[word]:
    if len(entries[word]) < 2:
      if len(word) == 3:
        return "Guessed: 3 |" + "Actual: " + str(len(pron))
      if len(word) == 4:
        return "Guessed: 4 |" + "Actual: " + str(len(pron))
      if len(word) == 5:
        return "Guessed: 5 |" + "Actual: " + str(len(pron))
      if len(word) > 5:
        return "Quite a long word! " + "Actual: " + str(len(pron))
    elif len(entries[word]) > 1:
      for p in entries[word]:
        print("There was more than 1 entry for this word, it has " + str(len(p)) + " pronunciations.")

# question 22
def hedge(text):
  text = text.split()
   ids = [index-1 for index in list(range(3, len(text)+1, 3))]
   for id in ids:
     text.insert(id, 'like')
   return text

 question 23
# how the hell do you do this question?

# question 24
def generate_model(cfdist, word, num=15):
    for i in range(num):
        print(word)
        word = cfd[word].max()
        text = nltk.corpus.genesis.words('english-kjv.txt')
        bigrams = nltk.bigrams(text)
        cfd = nltk.ConditionalFreqDist(bigrams)
        # store the n most likely words, then randomly choose a word form the list using random.choice()
        
        ''' Then select a particular genre, such as a section of brown corpus or 
        train the model on that particular corpus and get it to generate random text
        how intelligible is the text? You may have to experiement with different start words, etc.
        Discuss the strengths and weaknesses of this method of generating random text'''

        # Now, train your system using two distinct genres, and experiement with generating text in the hybrid genre.
