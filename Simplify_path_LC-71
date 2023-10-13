class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split("/")
        stack=[]
        for i in range(len(path)):
            if(stack and path[i]==".."):
                stack.pop()
            else:
                if(path[i] not in["",".",".."]):
                    stack.append(path[i])
            
        return "/"+"/".join(stack)
'''
TIME COMPLEXITY:O(n)
SPACE COMPLEXITY:O(n)
'''
