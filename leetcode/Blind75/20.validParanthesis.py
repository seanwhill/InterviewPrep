class Solution:
    def isValid(self, s: str) -> bool:
        Map = { ")":"(", "]":"[", "}":"{" }
        stack = []
        
        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]: #peaked into the stack. if it not the "correct paren" then false
                return False
            
            stack.pop()
        
        return not stack
            