import re

class Solution(object):
    def isPalindrome(self, s):
        combine = re.sub(r"[^a-zA-Z0-9]","",s).lower()
        return combine == combine[::-1]
    