# for i in range(1, 11, 3):
#     print(i)


def numSquares(n: int) -> int:
    dp = [n] * (n + 1)
    dp[0] = 0

    for target in range(1, n):
        print(f"target: {target}")
        for s in range(1, target + 1):
            print(f"s: {s}")
            square = s * s
            if target - square < 0:
                break
            dp[target] = min(dp[target], dp[target - square] + 1)
    return dp[n]


print(numSquares(12))

nums = [2, 7, 11, -7, 15]
target = 13


def twoSum(nums: [], target: int) -> []:
    check = {nums[i]: i for i in range(len(nums))}
    for i in range(len(nums)):
        if check.get(target - nums[i]) is not None:
            return check[target - nums[i]], i

    # result = {}
    # for i in range(len(nums)):
    #     if target - nums[i] in result:
    #         return [result[target - nums[i]], i]
    #     else:
    #         result[nums[i]] = i

# print(twoSum(nums, target))
