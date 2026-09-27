class Solution(object):
    def isPalindrome(self, s):

        cleaned = ""

        for char in s:
            if char.isalnum(): # only works for numerics and alphabet
                cleaned += char.lower() # will add the char in lower case

        return cleaned == cleaned[::-1]

        