def move_zeros_to_end(nums):
    # Initialize the pointer for placing the next non-zero element
    place_non_zero = 0

    # First pass: Move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[place_non_zero] = nums[i]
            place_non_zero += 1

    # Second pass: Fill the remaining positions with zeros
    for i in range(place_non_zero, len(nums)):
        nums[i] = 0

    return nums

# Example usage
arr = [0, 1, 0, 3, 12]
print("Original array:", arr)
move_zeros_to_end(arr)
print("Array after moving zeros to the end:", arr)