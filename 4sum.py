class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if(len(nums)<4):
            return []
        if(len(nums)==4 and sum(nums)==target):
            return [nums]
        if(len(nums)==4 and sum(nums)!=target):
            return[]
        res=set()
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                if(j>i+1 and nums[j]==nums[j-1]):
                    continue
                left=j+1
                right=len(nums)-1
                while(left<right):
                    s=nums[i]+nums[j]+nums[left]+nums[right]
                    if(s==target):
                        res.add((nums[i],nums[j],nums[left],nums[right]))
                        while(left<right and nums[left]==nums[left+1]):
                            left+=1
                        while(left<right and nums[right]==nums[right-1]):
                            right-=1
                        left+=1
                        right-=1
                    elif(s<target):
                         left+=1
                    elif(s>target):
                          right-=1

        return res
'''
TIME COMPLEXITY:O(n^3)
SPACE COMPLEXITY:O(n^3)
'''
