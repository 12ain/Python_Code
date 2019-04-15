excludes = {"the","and","of","you","a","i","my","in","to","it","that","is","not","lord","his","this","but","her","with","for","your","me","be","as","he","what","him","she","so","king","have","will","do","no","we","are","on","all","our","by","queen","or","shall","if","o","good","come","thou","they","now","more","let","from","how","at","thy","like","was","most","would","well","there","them","sir","know","enter","'tis","may","go","as","us","love","did","very","first","then","which","which","speak","hath","why","must","thee","give","an","their","such","should","make","where","i'll","upon","out","say","when","some","here","am","father","than","too","man","much","'","these","night","think","clown"}
def getText():  
    txt = open('hamlet.txt', 'r').read()     
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        txt = txt.replace(ch, " ")
    return txt
hamletTxt = getText()
words = hamletTxt.split()   
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True) 
print(items)
for i in range(10):
    word, count = items[i]
    print('{0:<10}{1:>5}'.format(word, count))
