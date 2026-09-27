class Solution(object):
    def isValid(self, s):

        stack = []

        for char in s:

            if char in "([{":
                stack.append(char)

            else:
                if not stack:  # to check wheather the stack is empty or not
                    return False

                top = stack.pop()

                if char == ")" and top != "(":
                    return False

                if char == "]" and top != "[":
                    return False

                if char =="}" and top != "{":
                    return False

        return len(stack) == 0 

        