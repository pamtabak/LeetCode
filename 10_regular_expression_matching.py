class Solution:
    def isMatch(self, s, p):
        # it means we reached the end of the pattern
        if not p:
            return not s  # if we reached the end of s it returns true

        # checking if s is not empty and if the first char matches
        firstMatch = bool(s) and p[0] in {s[0], '.'}

        # if the current pattern has a wildcard there are two options:
        # to dont use the wildcard and continue with the next pattern or
        # to use it and continue from the next chat in the string
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    firstMatch and self.isMatch(s[1:], p))
        # if there is no wildcard it is simple. we just get the next pattern and the next char in the string
        else:
            return firstMatch and self.isMatch(s[1:], p[1:])
