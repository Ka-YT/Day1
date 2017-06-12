

import codecs

stopwords = set(codecs.open('stopwords.txt', encoding='utf8').readlines())


    return outputwords



countedwords = {}
in_file = codecs.open('le-musee.txt', encoding='utf8')
for line in in_file:
    tokenizedwords = tokenize_words(line)
    for word in tokenizedwords:
        tokenizedwords.setdefault(word, 0)
        countedwords[word] +=1

file = codecs.open('output.txt', 'w', encoding='utf8')
for key, value in sorted(countedwords.items(), key=lambda x: x[1]):
    out_file.write(key + ':' + str(value) + '\n')