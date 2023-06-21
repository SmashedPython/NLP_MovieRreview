import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

from nltk.tokenize import PunktSentenceTokenizer

# example_string = """This is an example of the stopwords? Pythonly Pythoned python"""

# print(nltk.word_tokenize(example_string))
# stop_words = set(stopwords.words("english"))

# words = nltk.word_tokenize(example_string)

# filtered_sentence = [w for w in words if not w in stop_words ]

# print(filtered_sentence)

# ps = PorterStemmer()
# words = nltk.word_tokenize(example_string)
# for w in words:
#     print(ps.stem(w))



# sample_text = """When you are set up in China, then we should schedule a zoom, to see how it works in terms of timing/clarity etc.
# What data(s) would that be, very roughly?"""


# tokenized = nltk.word_tokenize(sample_text)

# all_words = nltk.FreqDist(tokenized)
# word_feature = list(all_words,keys)
# #print(all_words.most_common(3))


'''
def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            # chunkGram = """Chunk: {<.*>+}
            #                         }<VB.?|IN|DT>{"""
            # chunkParser = nltk.RegexpParser(chunkGram)
            # chunked = chunkParser.parse(tagged)
            # chunked.draw() #Chunk is grouping,chinking is removing.

            namedEnt = nltk.ne_chunk(tagged)
            namedEnt.draw()

    except Exception as e:
        print(str(e))

process_content()
'''

# lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize("geese"))
# print(lemmatizer.lemmatize("rocks"))
# print(lemmatizer.lemmatize("better",pos = "a"))
# print(lemmatizer.lemmatize("best",pos = "a"))
# print(lemmatizer.lemmatize("run",pos = "v"))

# print(nltk.__file__)

