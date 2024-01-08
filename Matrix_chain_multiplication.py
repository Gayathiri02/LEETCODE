'''                DYNAMIC PROGRAMMING
Given the dimension of a sequence of matrices in an array arr[],
where the dimension of the ith matrix is (arr[i-1] * arr[i]),
the task is to find the most efficient way to multiply these matrices together such that the total number
of element multiplications is minimum.

Examples:

Input: arr[] = {40, 20, 30, 10, 30}
Output: 26000
Explanation:There are 4 matrices of dimensions 40×20, 20×30, 30×10, 10×30.
Let the input 4 matrices be A, B, C and D.
The minimum number of  multiplications are obtained by 
putting parenthesis in following way (A(BC))D.
The minimum is 20*30*10 + 40*20*10 + 40*10*30
'''

class Solution:
    def matrixMultiplication(self, N, arr):
        dp=[[-1 for i in range(N)] for j in range(N)]
        def mcm(i,j,arr,dp):
            if i==j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            min_cost=float('inf')
            for k in range(i,j):
                current_cost=(arr[i-1]*arr[k]*arr[j])+mcm(i,k,arr,dp)+mcm(k+1,j,arr,dp)
                if(current_cost<min_cost):
                    min_cost=current_cost
                    dp[i][j]=min_cost
            return min_cost
        return mcm(1,N-1,arr,dp)

a=Solution()
N=5
arr=[40, 20, 30, 10, 30]
print(a.matrixMultiplication(N,arr))

'''
TIME COMPLEXITY :O(N^3)
SPACE COMPLEXITY :O(N^2) -> Memoization
'''
