from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    print(nums)
    n = len(nums)

    forward = [1] * n
    backward = [1] * n

    for i in range(n):
        if i == 0:
            forward[i] = nums[i]
        else:
            forward[i] = nums[i] * forward[i-1]

    for i in range(n-1, -1, -1):
        if i == n-1:
            backward[i] = nums[i]
        else:
            backward[i] = nums[i] * backward[i+1]

    print(forward)
    print(backward)

    result = [1] * n

    for i in range(n):
        if i == 0:
            result[i] = backward[i+1]
        elif i == n-1:
            result[i] = forward[n-2]
        else:
            result[i] = forward[i-1] * backward[i+1]

    return result


print(productExceptSelf(list(range(1,6))))