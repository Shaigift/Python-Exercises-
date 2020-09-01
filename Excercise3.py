def largestNumber(numbers):
    max = numbers[0]
    for a in numbers:
        if a > max:
            max = a
    return max
print(largestNumber([1,3,4,2,3,4]))
