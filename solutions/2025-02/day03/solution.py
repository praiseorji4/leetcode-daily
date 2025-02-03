class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closes_dict = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c not in closes_dict:
                stack.append(c)

            else:
                if stack and stack[-1] == closes_dict[c]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False