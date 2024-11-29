class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:  
                stack.append(i) #Appending open brackets
            elif len(stack) == 0 or d[stack.pop()] != i: #checking if stack is empty
                return False
        return len(stack) == 0
