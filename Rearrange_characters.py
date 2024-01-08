'''
Given a string S with repeated characters. 
The task is to rearrange characters in a string such that no two adjacent characters are the same.

Example 1:

Input : str = "geeksforgeeks"
Output: 1
Explanation: All the repeated characters of the
given string can be rearranged so that no 
adjacent characters in the string is equal.
Any correct rearrangement will show a output
of 1.

Example 2:

Input : str = "bbbbb"
Output: 0
Explanation: Repeated characters in the string
cannot be rearranged such that there should not
be any adjacent repeated character.
'''

import heapq
class Solution :
    def rearrangeString(self, str):
        s=str
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
        return "-1"
    
a=Solution()
s="geeksforgeeks"
print(a.rearrangeString(s))

'''
n=length(str)
TIME COMPLEXITY :O(n + n log k)
SPACE COMPLEXITY :O(k)
'''