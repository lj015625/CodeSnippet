class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        balance = 0
        remove = []
        for i, c in enumerate(s):
            if c == '(':
                balance = balance + 1
            elif c == ')':
                if balance > 0:
                    balance = balance - 1
                else:
                    remove.append(i)
        # remove all char in remove list
        if len(remove) > 0:
            s = ''.join([s[i] for i in range(len(s)) if i not in remove])
        # remove the last few (
        if balance > 0:
            s = s[::-1].replace('(', '', balance)
            s = s[::-1]
        # remove the first few )
        elif balance < 0:
            s = s.replace(')', '', 0 - balance)
        return s

solution = Solution()
print(solution.minRemoveToMakeValid("())()((("))  # expect "()()"