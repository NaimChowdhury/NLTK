import nltk


# from NLTK's book module, load all items
from nltk.book import *

# To find out about texts, enter the text names
text1
text2

# concordance shows every occurence of a given word in a given text
text1.concordance("monstrous")
text2.concordance("affection")
text3.concordance("lived")

# 'text1 is moby dick'
# 'text2 is Sense and Sensibility'
# 'text3 is the Bible'
# 'text4 is Inaugural Address Corpus'
# 'text5 is NPS Chat Corpus, for unconvential words like im, ur, lol'

# similar will find words that are used in a similar range of contexts to the string entered as an argument
text1.similar("monstrous")
text2.similar("monstrous")

# common_contexts shows contexts that are shared by two or more words
text2.common_contexts(["monstrous", "very"])

# dispersion plots show positional information about the location of words in a text. we can use this to find patterns in word usage in a given text, or use it to find patterns of word usage over a period of history

text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

# generate will generate some random text "in the various styles" of the given texts. No argument required
text5.generate()
