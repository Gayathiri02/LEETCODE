class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        left_max=[0]*len(height)
        right_max=[0]*len(height)
        
        left_max[0]=height[0]
        right_max[-1]=height[-1]
    
        j=len(height)-1
        for i in range(1,len(height)):
            left_max[i]=max(left_max[i-1],height[i])
            right_max[j-1]=max(right_max[j],height[j-1])
            j-=1
            
        for i in range(len(height)):
            res+=min(left_max[i],right_max[i])-height[i]
        
        return res