class Solution:
    def isValid(s: str) -> bool:
        d = []
        for i in s:
            if not d:
                d.append(i)
            elif i == ')' and d[-1] == '(':
                d.pop()
            elif i == ']' and d[-1] == '[':
                d.pop()
            elif i == '}' and d[-1] == '{':
                d.pop()
            elif i == '(' or i == '{' or i == '[' :
                d.append(i)
            else:
                return False    
        if len(d) == 0:
            return True
        return False

print(Solution.isValid('{}'))