class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        n1=0
        for c in num1:
            n1=n1*10+(num[c])
        n2=0
        for c in num2:
            n2=n2*10+(num[c])
        product=n1*n2
        
        key=list(num.keys())
        res=""
        if product==0:
            return "0"
        while(product>0):
            rem=product%10
            res=key[rem]+res
            product//=10
        return res
num1="123"
num2="456"
a=Solution(num1,num2)