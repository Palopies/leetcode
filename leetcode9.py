class Solution:
    def findAnagrams(self , s ,p ):
        need={}
        window={}
        for c in p :
            need[c] = need.get(c,0)+1
        left = 0
        res=[]
        valid=0
        for right in range(len(s)):
            c = s[right]
            if c in need:
                window[c] = window.get(c,0)+1
                if window[c] == need[c]:
                    valid +=1
            while right-left+1>= len(p):
                if valid == lend(need):
                    res.append(left)
                left_char = s[left]
                if left_char in need:
                    if window[left_char]==need[left_char]:
                        valid -=1
                    window[left_char] -=1 
                left +=1
        return res