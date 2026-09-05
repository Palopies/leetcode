class Solution:
    def lengthOfLongestSubstring(self, s):
        char_map={}
        left=0
        max_len=0
        for right in range(len(s)):
            c=s[right]
            if c in char_map and char_map[c]>= left:
                left= char_map[c]+1
            char_map[c]= right
            max_len = max(max_len,right-left+1)
        return max_len