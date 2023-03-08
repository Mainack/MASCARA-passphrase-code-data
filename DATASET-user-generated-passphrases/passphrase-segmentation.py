#!/usr/bin/python3

'''
Symspell doc: https://symspellpy.readthedocs.io/en/latest/users/installing.html

symspell data: 
curl -LJO https://raw.githubusercontent.com/mammothb/symspellpy/master/symspellpy/frequency_dictionary_en_82_765.txt
curl -LJO https://raw.githubusercontent.com/mammothb/symspellpy/master/symspellpy/frequency_bigramdictionary_en_243_342.txt

'''
import sys
import nltk
import re
import csv
import pickle
import json
nltk.download('words')
from nltk.corpus import words
from itertools import combinations
from symspellpy import SymSpell


sym_spell = SymSpell()
dictionary_path = 'data/frequency_dictionary_en_82_765.txt'
sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
dictionary_path = 'data/frequency_dictionary_en_243_342.txt'
sym_spell.load_bigram_dictionary(dictionary_path, 0, 2)

def symspellSegment(w): #use it when greedy fails
    w = re.sub('[^A-Za-z]+', '', w)
    result = sym_spell.word_segmentation(w, max_segmentation_word_length=12, max_edit_distance=0)
    return result.segmented_string

def loadWords():
    names, cities, countries, gerunds = [], [], [], []
    for coun in open('data/first-names.txt'):names.append(coun.strip().lower())
    cities = pickle.load( open( 'data/cities.pkl' , "rb" ) )
    countries = pickle.load( open( 'data/country.pkl' , "rb" ) )
    gerunds = pickle.load( open( 'data/gerunds.pkl' , "rb" ))
    lw = words.words()
    return names, cities, countries, gerunds, lw

def getPotentialSubwords(w, names, cities, countries, gerunds, lw):
    subs = []
    for w in lw:
        if w in word and (len(w)>2):subs.append(w)
    for nam in names:
        if nam in word:subs.append(nam)
    for city in cities:
        if city in word:subs.append(city)
    for ger in gerunds:
        if ger in word:subs.append(ger)
    for cy in countries:
        if cy in word:subs.append(city)
    subs=list(set(subs))
    return subs

def segment(word, names, cities, countries, gerunds, lw):#Greedy segment
    dic={}
    subs=[]
    k=[]
    segment = None
    originalpw=word.encode("ascii", "ignore").decode()
    word=word.encode("ascii", "ignore").decode().lower()
    word = word.replace('_','').replace('.','').replace('-','').lower()
    wordClean=''.join(filter(str.isalpha, word))
    subs = getPotentialSubwords(word, names, cities, countries, gerunds, lw)
    if len(subs)>=3:
        l = sorted(subs, key = len)
        wordCopy=word
        l.reverse()
        l=[x for x in l if x]
        if len(l[0])<3:return segment
        for ind in l:
            if ind in wordCopy:
                k.append(ind)
                wordCopy= re.sub(ind, '', wordCopy)
        k1=[len(v) for v in k]
        if len(''.join(k)) == len(wordClean) and k1.count(2) < 2 and len(k) > 2:
            for i in k:
                dic[i]=wordClean.find(i)
            di=sorted(dic, key=dic.get)
            if ''.join(di)!=wordClean:return segment
            if len(min(di, key=len))<3 or 'isa' in di or 'ismy' in di or 'ina' in di or 'ilo' in di:return segment
            if 'ion' in di:
                x=di.index("ion")
                di[x-1:x+1]=[''.join(di[x-1:x+1])]
                #print(' '.join(di),originalpw)
            if 'ess' in di:
                x=di.index("ess")
                di[x-1:x+1]=[''.join(di[x-1:x+1])]
                #print(' '.join(di),originalpw)
            #print(' '.join(di),originalpw)
            if len(di)<3:return segment
            segment = ' '.join(di)
        print(word, segment)
        return segment

if __name__ == '__main__':
    loop = 0
    names, cities, countries, gerunds, lw = loadWords()
    out = open('segmented-passphrases.csv','w', newline='')
    writer = csv.writer(out)
    writer.writerow(["Original Password", "Passphrase", "count"])
    for line in open('data/orig-pw-w-freq.txt'):
        loop+=1
        line = line.strip()
        l1 = line.split()
        count = l1[0]
        word = line.replace(count, '').strip()
        print(word)
        seg = segment(word, names, cities, countries, gerunds, lw)
        if seg==None:
            seg=symspellSegment(word)
            print('Symspell', word, seg)
        res = [word, seg, count]
        print(loop, res)
        writer.writerow(res)
    out.close()
