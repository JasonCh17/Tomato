class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        lengthOfSubstring = list()
        if s == []:
            return 0
        else:
            while len(s) > 0:
                substring = list()
                for i in range(len(s)):
                    if s[i] not in substring:
                        substring.append(s[i])
                    else:
                        lengthOfSubstring.append(len(substring))
                        indexOfRepeat = ''.join(substring).find(s[i])
                        s = s[indexOfRepeat+1:]
                        break
                lengthOfSubstring.append(len(substring))
                if len(substring)==len(s):
                    break
        return max(lengthOfSubstring)