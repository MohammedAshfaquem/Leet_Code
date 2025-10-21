class Solution(object):
    def detectCapitalUse(self, name):
        """
        :type name: str
        :rtype: bool
        """
        if name.isupper() or name.islower() or (name[0].isupper() and name[1:].islower()):
            return True
        else:
            return False
