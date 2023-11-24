class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix_len=n*n
        matrix=[[0 for i in range(n)]for j in range(n)]
        val=1
        l=0
        t=0
        r=n
        b=n
        while(val<=matrix_len):
            for i in range(l,r):
                matrix[t][i]=val
                val+=1
            t+=1
            for i in range(t,b):
                matrix[i][r-1]=val
                val+=1
            r-=1
            for i in range(r-1,l-1,-1):
                matrix[b-1][i]=val
                val+=1
            b-=1
            for i in range(b-1,t-1,-1):
                matrix[i][l]=val
                val+=1
            l+=1
        return matrix
                    