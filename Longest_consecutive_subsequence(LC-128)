#LONGEST CONSECUTIVE SUBSEQUENCE(LEETCODE-128)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            if(len(nums)==0):
                return 0
            s=set(nums)
            count=1
            c=1
            for i in s:
                c=1
                if(i-1 not in s):
                    current_value=i
                    while(current_value+1 in s):
                        c+=1
                        current_value+=1
                    if(count<c):
                        count=c
            return count
'''
TIME COMPLEXITY:O(n)
SPACE COMPLEXITY:O(n)
'''
