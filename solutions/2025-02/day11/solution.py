class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Using a Stack
        stack = []

        # length of part
        l = len(part) 

        for char in s:
            stack.append(char)
            if len(stack) >= l and "".join(stack[-l:]) == part: # if last l equals part
                for i in range(l): 
                    stack.pop()

        return "".join(stack)
            
        