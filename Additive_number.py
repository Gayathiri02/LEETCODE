#ADDITIVE NUMBER(LEET CODE-306)

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if(len(num)<3):
            return False
        st=[]
        t=-1
        for i in range(len(num)):  
            for j in range(i+1,len(num)):
                n1=num[:i+1]
                n2=num[i+1:j+1]
                if((n1=="0" or n2=="0") or (n1[0]!="0" and n2[0]!="0")):
                    sums=int(n1)+int(n2)
                    sums=str(sums)
                    l=len(sums)
                    sq=j+1
                    seq=num[sq:sq+l]
                    
                    if(seq==sums):
                        st.clear()
                        st.append(n1)
                        st.append(n2)
                        st.append(seq)
                        t=sq+l
      
        while(t<len(num)):
            if(len(st)>=3):
                sums=int(st[-1])+int(st[-2])
                sums=str(sums)
                seq=num[t:t+len(sums)]
                
                if(len(st)>3 and len(st)==len(num)):
                    return True
                    
                elif(sums==seq):
                    st.append(seq)
                    t=t+len(sums)
                else:
                    return False
            else:
                return False
        
        return True
'''
TIME COMPLEXITY:O(n^2)
SPACE COMPLEXITY:O(n)
'''
