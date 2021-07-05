class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

        A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

        For example, "ace" is a subsequence of "abcde".
        A common subsequence of two strings is a subsequence that is common to both strings.
        
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        m = len(text1)
        n = len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        print(dp)
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        print(dp)
        return dp[m][n]
    
print(Solution().longestCommonSubsequence('QPQRR', 'PQPRQRP'))