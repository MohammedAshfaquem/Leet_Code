class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Mapping of closing brackets to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_map:  # It's a closing bracket
                top_element = stack.pop() if stack else '#'  # Pop from stack or use dummy
                if bracket_map[char] != top_element:
                    return False
            else:  # It's an opening bracket
                stack.append(char)
        
        return not stack

# Example usage:
sol = Solution()
print(sol.isValid("()"))        # True
print(sol.isValid("()[]{}"))    # True
print(sol.isValid("(]"))        # False
print(sol.isValid("([])"))      # True
print(sol.isValid("([)]"))      # False
