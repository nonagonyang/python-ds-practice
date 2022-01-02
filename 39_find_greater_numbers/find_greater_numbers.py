from os import X_OK


def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    result=0
    for num in nums:
        count=0
        slice_idx=nums.index(num)
        followed_li=nums[slice_idx:]
        for x in followed_li:
            if x>num:
                count=count+1
        result=result+count
    return result


