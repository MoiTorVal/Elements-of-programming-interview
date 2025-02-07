nums = [1,2,5,7]
target = 9
hash_map = {}
for index, num in enumerate(nums):
    complement = target - num
    if complement in hash_map:
         print([hash_map[complement], index])
    else:
        hash_map[num] = index
        

