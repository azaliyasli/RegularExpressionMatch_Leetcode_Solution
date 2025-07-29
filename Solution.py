class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        tupple = {}
        
        def dp(i, j):
            #Memoization
            if (i, j) in tupple:
                return tupple[(i, j)]
            if j == len(p):
                return i == len(s) #Failed to match

            match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            #Recursion
            if j + 1 < len(p) and p[j + 1] == '*':
                tupple[(i, j)] = dp(i, j + 2) or (match and dp(i + 1, j))
                return tupple[(i, j)]
            else:
                tupple[(i, j)] = match and dp(i + 1, j + 1)
                return tupple[(i, j)]

        return dp(0, 0) #Base case
