case1 = [2,7,11,15]
case2 = [3,2,4]
case3 = [3,3]

# brute force
# def twoSum(nums: list[int], target: int) -> list[int]:
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i,j]

# hash table
def twoSum(nums: list[int], target: int) -> list[int]:
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num    
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i

    return []

print(twoSum(case1, 9))
print(twoSum(case2, 6))
print(twoSum(case3, 6))

