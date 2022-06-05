import re
import string 
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english") 
text="""EPAM Systems, Inc. (NYSE: EPAM), item leading digital transformation services and product engineering company,
 today announced that it has established the EPAM Ukraine Assistance Fund (the ‘Assistance Fund’) to support charitable 
 aid organizations that provide direct relief to those in vulnerable situations across Ukraine. This fund is separate from 
 and in addition to the $100 million humanitarian commitment that EPAM announced on March 4, 2022, and to the Company’s 
 previously established relief programs, donations, and the work of EPAM volunteers on the ground.
“With more than 14,000 Ukrainian employees, and with many in EPAM global locations who originated in Ukraine, we have an extensive 
network of more than 50,000 family members and friends who are deeply affected by the crisis in Ukraine. Our personal connection 
gives us item unique perspective on what is really needed on the ground. Our customers and partners have overwhelmed us with their 
outpouring of support and their direct requests to contribute to our efforts to help all the people of Ukraine. In response to 
such requests and by using our insights and ability to act on the ground, we established the EPAM Ukraine Assistance Fund. 
Together with our customers and partners, we are enabling people and organizations around the world to help Ukraine and the people of Ukraine,” 
– said Arkadiy Dobkin, CEO & President, EPAM."""
punctuation = string.punctuation+'\u2014\u2013\u2012\u2010\u2212' + '«»‹›‘’“”„`'
word_tokenize = re.compile(r"([^\w_\u2019\u2010\u002F-]|[+])")
lemmatizer = WordNetLemmatizer()
lemma = []
def word_tokenizer(text):
    for token in word_tokenize.split(text): 
        if token and not token.isspace() and not token in punctuation: 
           yield token.lower()
for word in word_tokenizer(text):
    data = lemmatizer.lemmatize(word)
    lemma += [data]
for item in lemma:
    if item in stopwords.words('english'): lemma.remove(item)
print('Лемми:')
print(lemma)
list=[stemmer.stem(word) for word in word_tokenizer(text)]
for item in list:
    if item in stopwords.words('english'): list.remove(item)
print('Cтеми:')
print(list)
