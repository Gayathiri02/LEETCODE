#CHECK IF THE ANAGRAM OF STRING 'TARGET' IS PRESENT IN 'S'
from collections import Counter

def check_anagram(counter,d):
    if counter==d:
        return True
    
def anagram_substring(s,target):
    i=0
    while(i<len(s)):
        counter=Counter(target)
        d={}
        while s[i] in counter:
            if s[i] in d:
                d[s[i]]+=1
            else:
                d[s[i]]=1
            if check_anagram(counter,d):
                return True
            i+=1
        i+=1
    return False

s = "afdgzyaxkslxzydfm"
target = "xyz"
print(anagram_substring(s,target))



