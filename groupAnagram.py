## Group Anagram

# input
# ["eat","tea","tan","ate","nat","bat"]

# output
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]    
# ]
from collections import defaultdict
a = ["eat","tea","tan","ate","nat","bat"]

def groupAnagram(wordlist):
    anagrams = defaultdict(list)
    for word in wordlist:
        # print(''.join(sorted(word)))
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()

print(groupAnagram(a))

