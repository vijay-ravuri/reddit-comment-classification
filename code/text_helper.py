import string
import re
import numpy as np
import emoji # Found this library while looking for a way to check if emojis are in a string
from nltk.corpus import stopwords
punctuation = string.punctuation

def word_splitter(text):  # Number of words + average word length
    words = re.split(r'[\s\/]', re.sub(r'[\.]', '', text))
    return len(words), np.mean([len(word) for word in words])


def sentence_count(text): # Number of sentences + average sentence length (in words)
    sentences = re.split(r'\.\s', text)
    return len(sentences), np.mean([len(re.split(r'[\s\/]', sentence)) for sentence in sentences])

def emoji_checker(text): # Checks for presence of any emojis
    if len(emoji.emoji_list(text)) > 0:
        return True
    return False

def stop_word_counter(text): # Number of stopwords
    return sum([text.count(word) for word in stopwords.words('english')])

def punc_counter(text): # Counts the punctuation in text input
    return sum([text.count(punc) for punc in punctuation])