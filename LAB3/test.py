import os

import letters as letters
import un as un


dimensions = 100
dictionary = {}
n=3
pattern = r'[0-9“”–„‘’»«]'
s = {}
letters = " abcdefghijklmnopqrstuvwxyz"
a = 27
for filename in os.listdir("lang"):
    data = open("lang/" + filename, mode='r', encoding="utf8")

    for line in data:
        df = un.unidecode(line).lower()

        for x in df:
            if (x not in letters):
                df = df.replace(x, '')
        ngrams = [df[i:i + n] for i in range(len(df) - 1)]

        for ngram in ngrams:
            if (s.get(ngram) is None):
                s[ngram] = 1
            else:
                s[ngram] += 1


