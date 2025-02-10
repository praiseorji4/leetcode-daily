class Solution:
    def clearDigits(self, s: str) -> str:
        stack = [] # To hold the letters. the top would always be the closest non-digit to the left

        for l in s:
            if l.isdigit() and stack: # If the current ele is a digit, pop from the stack
                stack.pop()
            else:
                stack.append(l) # if it is a non-digit, append to the stack

        return "".join(stack) # create string from the stack
        
        