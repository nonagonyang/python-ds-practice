 def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
    result=0
    
    for num in nums[:-2]:
        num_idx=nums.index(num)
        sub_sum=num+nums[num_idx+1]+nums[num_idx+2]
        result=result+sub_sum
    return result%2!=0
