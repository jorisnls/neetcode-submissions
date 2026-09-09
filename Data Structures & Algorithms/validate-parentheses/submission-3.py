class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]"
        } 
        
        stack = []
        opening = "({["
        closing = ")}]"
        for c in s:
            if c in opening:
                stack.append(pairs[c])
            if c in closing:  
                if stack == []:
                    return False    
                if not stack.pop() == c:
                    return False

        return stack == []


        