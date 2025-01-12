class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in closeToOpen: # Closing parenthese's (checking keys)
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else: # Parentheses do not match
                    return False
            else: # Open parenthese
                stack.append(char)
        return True if not stack else False
