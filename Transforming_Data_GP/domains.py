import read
import collections
import pandas as pd
import pprint

data = read.load_data()
urls = data["url"]

string = ""
for i in range(len(urls)):
    string = string + str(urls[i]) + " "
    
string = string.lower()

word_list = string.split()
for item in range(word_list.count("nan")):
    word_list.remove("nan")

c= collections.Counter(word_list).most_common(100)
pprint.pprint(c)