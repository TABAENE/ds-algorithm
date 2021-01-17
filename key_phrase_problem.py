# Amazon: key phrase problem TF-IDF.

import re

text = "Suppose we have a set of English documents and wish to rank which is most relevant to the query, the brown cow." \
       "A simple way to start out is by eliminating document that do not contain all three words the brown, and cow, " \
       "but this still leaves many documents"

# These are common english word, which you will find in every document.
words_to_exclude = ["the", "a", "we", "have", "," ,".","to", "and", "by", "of", "is"]

word_frequence = {}

input_text = re.split(" |\.|,", text)

max_frequency = 0

for word in input_text:
    if word in words_to_exclude or not word:
        continue
    if word in word_frequence:
        word_frequence[word] += 1
    else:
        word_frequence[word] = 1
    if word_frequence.get(word) > max_frequency:
        max_frequency = word_frequence[word]

for key, val in word_frequence.items():
    if val == max_frequency:
        print("{}:{}".format(key, val))

print("word frequence", word_frequence)

"""
Output:
documents:2
brown:2
cow:2
word frequence {'Suppose': 1, 'set': 1, 'English': 1, 'documents': 2, 'wish': 1, 'rank': 1, 'which': 1, 'most': 1, 'relevant': 1, 'query': 1, 'brown': 2, 'cow': 2, 'A': 1, 'simple': 1, 'way': 1, 'start': 1, 'out': 1, 'eliminating': 1, 'document': 1, 'that': 1, 'do': 1, 'not': 1, 'contain': 1, 'all': 1, 'three': 1, 'words': 1, 'but': 1, 'this': 1, 'still': 1, 'leaves': 1, 'many': 1}

"""
