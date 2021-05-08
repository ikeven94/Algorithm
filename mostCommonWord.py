# Most Common Word

# input 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]

# output
# "ball"
import re, collections
def MostCommonWord(paragraph,banned):
    words = []
    preprocessing = re.sub('[^\w]',' ',paragraph).lower().split()
        
    for word in preprocessing:
        if not word in banned:
            words.append(word)
    # print(collections.Counter(words))
    return collections.Counter(words).most_common(1)[0][0]

print(MostCommonWord(paragraph,banned))