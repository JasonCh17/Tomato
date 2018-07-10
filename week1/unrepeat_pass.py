class Solution:
    """
    @param: s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring( self,s):
        res =0
        start =0
        d ={}
        tmp =0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >=start:
                start = d[s[i]] +1
                d[s[i]] =i
            else:
                d[s[i]] =i
                tmp =i -start +1
                res =max(res,tmp)
        return res