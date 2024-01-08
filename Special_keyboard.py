#SPECIAL KEYBOARD
'''
Imagine you have a special keyboard with the following keys: 

Key 1:  Prints 'A' on screen
Key 2: (Ctrl-A): Select screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Find maximum numbers of A's that can be produced by pressing keys on the special keyboard N times. 

Example 1:

Input: N = 3
Output: 3
Explanation: Press key 1 three times.

Example 2:

Input: N = 7
Output: 9
Explanation: The best key sequence is 
key 1, key 1, key 1, key 2, key 3,
key4, key 4.

'''
class Solution:
    def optimalKeys(self, N):
        if N<=6:
            return N
        dp=[0]*(N+1)
        for i in range(7):
            dp[i]=i
        for i in range(7,N+1):
            k=2
            for j in range(i-3,0,-1):
                count=dp[j]*k
                k+=1
                if(count>dp[i]):
                    dp[i]=count
        return dp[N]

'''
TIME COMPLEXITY: O(n^2)
SPACE COMPLEXITY: O(n)
'''

