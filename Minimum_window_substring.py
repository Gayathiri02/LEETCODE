class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minlength=float('inf')
        left=0
        left_res_index=0
        t_char=Counter(t)
        found_char=len(t_char)
        for right,c in enumerate(s):
            if c in t_char:
                t_char[c]-=1
                if t_char[c]==0:
                    found_char-=1
            
            while(found_char==0 and left<=right):
                if right-left+1<minlength:
                    minlength=right-left+1
                    left_res_index=left
                
                current_left=s[left]
                if current_left in t_char:
                    t_char[current_left]+=1
                    if(t_char[current_left]>0):
                        found_char+=1
                left+=1
        if minlength < float('infinity'):
            return s[left_res_index:left_res_index+minlength]
        return "" 
s="ADOBECODEBANC"
t="ABC"
a=Solution()
a.minWindow(s,t)
