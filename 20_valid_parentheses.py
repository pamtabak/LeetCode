class Solution:
    def isValid(self, s: str) -> bool:
        stack = ""
        for element in s:
            if (element == "(" or element == "[" or element == "{"):
                stack += element
                continue
            elif (len(stack) == 0):
                #we are trying to close before opening
                return False
            elif (element == ")" and stack[-1] != "("):
                return False
            elif (element == "]" and stack[-1] != "["):
                return False
            elif (element == "}" and stack[-1] != "{"):
                return False
            
            stack = stack[:-1]
            
        return len(stack) == 0