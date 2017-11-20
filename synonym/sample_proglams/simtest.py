import nltk
from nltk.corpus import wordnet

a=wordnet.synset("A.n.01")
b=wordnet.synset("lineage.n.01")

print(a.wup_similarity(b))
print(a)
