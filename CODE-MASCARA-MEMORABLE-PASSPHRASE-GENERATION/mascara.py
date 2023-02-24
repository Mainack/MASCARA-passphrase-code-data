import pickle
import os, random

import nltk
import numpy as np
from nltk.corpus import stopwords


# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')


# data import
UNIGRAM = os.path.join('data', 'unigram-5p.pkl')
BIGRAM = os.path.join('data', 'biprob.pkl')
MARKOV = os.path.join('data', 'bigram.pickle')
STOPWORDS = set(stopwords.words('english'))

# CONSTANTS
THETA_1 = 0.65
THETA_2 = 0.45
AL1 = -3.4279e-02
AL2 = -6.4687e-03
MIN_BIGRAM = 0
MAX_NUM_TRIES_FOR_WORD_CHOICE = 5

def val_string(string):

    if len(string.split()) > 1:
        return all(val_string(x) for x in string.split())

    try:
        string.encode('ascii')
        if string.isalpha() and len(string) >= 3:
            return True
        if string == '<begin>':
            return True

    except UnicodeError:
        pass
    
    return False

def cal(x, y):
    return AL1 * x + AL2 * y


def get_unigram():
    with open(UNIGRAM, 'rb') as hold:
        the_dict = pickle.load(hold)
    
    for el in list(the_dict.keys()):
        if not val_string(el):
            del the_dict[el]

    total = sum(the_dict.values())
    for key, value in the_dict.items():
        the_dict[key] = value / total
    
    return the_dict


def get_bigram():
    global MIN_BIGRAM
    with open(BIGRAM, 'rb') as hold:
        the_dict = pickle.load(hold)
    
    for el in list(the_dict.keys()):
        if not val_string(el):
            del the_dict[el]
        else:
            MIN_BIGRAM = min(MIN_BIGRAM, np.log(the_dict[el]))

    return the_dict


def get_graph(unigram, bigram):
    with open(MARKOV, 'rb') as hold:
        the_dict = pickle.load(hold)

    def valid(words, key):
        if np.log(bigram[" ".join([words, key])]) >= THETA_1 * MIN_BIGRAM:
            return False
        if cal(np.log(unigram[key]), np.log(bigram[" ".join([words, key])])) > THETA_2:
            return False
        return True

    # Building a dictionary of valid graph with the corresponding weights
    ret_dict = dict()
    for words in the_dict:
        if val_string(words):
            for key in the_dict[words]:
                if val_string(key) and valid(words, key):
                    if words not in ret_dict:
                        ret_dict[words] = list()
                    ret_dict[words].append([key, the_dict[words][key]])    # NOTE: Decide on the weight of the choice
    
    # Converting the built dictionary into a CDF distribution
    for key in ret_dict:
        print(key)
        total = sum([item[1] for item in ret_dict[key]])
        for ind in range(len(ret_dict[key])):
            ret_dict[key][ind][1] /= total
            if ind > 0:
                ret_dict[key][ind][1] += ret_dict[key][ind - 1][1]

    return ret_dict


def makesent(unigram, bigram, graph, size):
    
    def next_move(word):
        pos = random.uniform(0, 1)          # Choose a random number
        
        # Binary search for the correct one
        low, high, ans = 0, len(graph[word]) - 1, 0
        while low <= high:
            mid = low + high >> 1
            if graph[word][mid][1] >= pos:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        
        return graph[word][ans][0]

    passphrase = ['<begin>']    
    while len(passphrase) - 1 < size and passphrase[-1] != '<end>':
        passphrase.append(next_move(passphrase[-1]))

    return " ".join(passphrase)


if __name__ == '__main__':
    #lengths of passphraes to be generated
    lengths=[4, 4, 5, 4, 5, 6, 6, 7, 8, 9, 10, 11, 12, 15, 6, 8, 9, 5, 6, 4, 4, 7, 9, 5, 12, 10, 15]
    uni, bi = get_unigram(), get_bigram()
    graph = get_graph(uni, bi)

    for item in lengths[:20]:              
        # call to generate passphrase
        string = ""
        while len(string.split()) != item:
            string = makesent(uni, bi, graph, item)
            string = string.replace("<begin>", "").replace("<end>", "").strip()
        
        print(string)
