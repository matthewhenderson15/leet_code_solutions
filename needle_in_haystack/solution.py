class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
    #  Two approaches come to mind. The first is to compare each substring of len(needle) in haystack
    #  to needle. The downfall of this is that you are recalculating the new substring to compare on
    #  each loop iteration. Therefore, a more efficient approach is to find the start of the string  


# Sliding window algo
        n = len(needle)
        h = len(haystack)
        
        if n == 0:
            return 0

        for i in range(h-n+1):
            if haystack[i:i+n] == needle:
                return i
        
        return -1

# Two pointer approach
        n = len(needle)
        h = len(haystack)
        pN = 0
        pH = 0
        
        if n == 0:
            return 0
        
        while pH < n-h+1:
            while pH < n-h+1 and haystack[pH] != needle[0]:
                pH += 1
            length = pN = 0
            while pN < n and pH < h and haystack[pH] == needle[pN]:
                length += 1
                pN += 1
                pH += 1
            if length == n:
                return pH - n
            pH = pH - length
        
        return -1
