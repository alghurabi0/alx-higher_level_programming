#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    else:
        chars = list(roman_string)
        nums = []
        for char in chars:
            if char == 'I':
                nums.append(1)
            elif char == 'V':
                nums.append(5)
            elif char == 'X':
                nums.append(10)
            elif char == 'L':
                nums.append(50)
            elif char == 'C':
                nums.append(100)
            elif char == 'D':
                nums.append(500)
            elif char == 'M':
                nums.append(1000)
        if nums[0] == 1:
            nums[0] = -1
        finalSum = 0
        for num in nums:
            finalSum += num
        return finalSum
