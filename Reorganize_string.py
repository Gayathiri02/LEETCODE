import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        f={}
        for char in s:
            if char in f:
                f[char]+=1
            else:
                f[char]=1
        heap=[]
        for i in f:
            heapq.heappush(heap,(-f[i],i))
        res=""
        prev=heapq.heappop(heap)
        res+=prev[1]
        while(heap):
            current=heapq.heappop(heap)
            res+=current[1]
            if prev[0]+1<=-1:
                heapq.heappush(heap,(prev[0]+1,prev[1]))
            prev=current
        if len(res)==len(s):
            return res
        return "Not possible to re-organize the given string"

a=Solution()
#s="aab"
s="aaab"
print(a.reorganizeString(s))
      