from bs4 import BeautifulSoup
import re
def bersih(expr):
    cleanr = re.compile('<.*?>')
    expr = str(expr)
    hsl = re.sub(cleanr,"",expr)
    hsl = re.sub("\n","",hsl)
    return hsl

def parsePostag(sentences):
    itemxml = BeautifulSoup(sentences, 'html.parser')
    itemword = itemxml.find_all('word')
    itemword = re.sub("[\[\]]","",str(itemword))
    itempost = itemxml.find_all('postag')
    itempost = re.sub("[\[\]]","",str(itempost))
    word = bersih(itemword).split(",")
    tag = bersih(itempost).split(",")
    dictword={}
    for i in range(0,len(word)):
        # print(word[i]+" "+tag[i]+"\n")
        dictword[word[i]] = tag[i]
    return dictword