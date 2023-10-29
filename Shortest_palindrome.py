class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r=s[::-1]
        st=s+r
        suffix=""
        prefix=""
        index=0
        r=len(st)-1
        for i in range(len(s)):
            suffix=st[:i+1]
            prefix=st[r:]
            if(suffix==prefix):
                index=r
            r-=1
        s=st[len(s):index]+s
        return s