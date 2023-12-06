class Solution:
    def palindromePairs(self, words):
        res=[]
        d={}
        for i,j in enumerate(words):
            d[j]=i
        for i in range(len(words)):
            if words[i]==words[i][::-1] and "" in words and i!=d[""]:
                res.append((i,d[""]))
                res.append((d[""],i))
            
            s=words[i]
            j=0
            while(j<len(s)):
                prefix=s[:j]
                suffix=s[j:]
                if prefix==prefix[::-1]:
                    if suffix[::-1] in d and i!=d[suffix[::-1]]:
                        res.append((d[suffix[::-1]],i))
                if suffix==suffix[::-1]:
                    if prefix[::-1] in d and i!=d[prefix[::-1]]:
                        res.append((i,d[prefix[::-1]]))
                j+=1
            
        return list(set(res))
words=["abcd","dcba","lls","s","sssll",""]
a=Solution() 
print(a.palindromePairs(words))