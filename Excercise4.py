def largestNumber(numbers):
    min = numbers[0]
    for a in numbers:
        if a < min:
            min = a
    return min
print(largestNumber([-61,3,4,2,3,4]))
