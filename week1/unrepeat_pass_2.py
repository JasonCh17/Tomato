class Solution:
    """
    @param: s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring( self,s):
        start =0
        d ={}
        l=[]
        if len(s)==0:
            return 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >=start:
                start = d[s[i]] +1
                d[s[i]] =i
            else:
                d[s[i]] =i
                l.append(i-start+1)            
        return max(l)