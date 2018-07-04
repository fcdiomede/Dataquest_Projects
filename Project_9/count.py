import read
import collections

data = read.load_data()
headlines = data["headline"]

string = ""
for i in range(len(headlines)):
    string = string + str(headlines[i]) + " "
    
string = string.lower()

word_list = string.split()

c= collections.Counter(word_list).most_common(100)
print(c)
    