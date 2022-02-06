# Given an array of integers, we are going to find the length of the largest subarray with sum k in Python
# 'Nested Loops'
def longest_len(arr, k):
    max_len = 0
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum == k:
                max_len = max(max_len, j-i+1)
    return max_len
arr = [15, -2, -8, 1, 7, 10, 13, 5, 6, 2]
print(arr)
k = int(input("k value: "))
print(f"Length of longest subarray, k = {longest_len(arr, k)} \n")

### 'Hash Map' 
def longest_len(arr, k):
    hash_map = {}
    max_len = 0 
    current_sum = 0
    for i in range(len(arr)):
        current_sum += arr[i]

        if arr[i] == k and max_len == 1:
            max_len = 1

        if current_sum == k:
            max_len = i+1

        if current_sum in hash_map:
            max_len = max(max_len, i-hash_map[current_sum])
        else:
            hash_map[current_sum] = i
    return max_len
arr = [15, -2, 2, -8, 1, 7, 10, 13]
k = int(input("K value: "))
print(f"Length of longest subarray, k = {longest_len(arr, k)} \n")

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSums = {0:1}

        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res
