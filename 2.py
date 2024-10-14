def lcs_length(str1, str2):
    m, n = len(str1), len(str2)
    # Create a 2D array to store lengths of longest common subsequence
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def min_operations(str1, str2):
    lcs_len = lcs_length(str1, str2)
    deletions = len(str1) - lcs_len
    insertions = len(str2) - lcs_len
    return deletions, insertions

# Example usage
str1 = "heap"
str2 = "pea"
deletions, insertions = min_operations(str1, str2)

print(f"Minimum Deletion = {deletions} and Minimum Insertion = {insertions}")
