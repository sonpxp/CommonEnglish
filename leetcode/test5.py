def numSquares(n: int) -> int:
    dp = [n] * (n + 1)
    squares = []
    dp[0] = 0

    i = 1
    while i * i <= n:
        squares.append(i * i)
        i += 1

    for i in range(1, n + 1):
        for s in squares:
            if s > i:
                break
            dp[i] = min(dp[i], dp[i - s] + 1)

    return dp[n]


numSquares(13)

print(numSquares(13))
