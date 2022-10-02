"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

numbers.sort()
length = len(numbers)
if length % 2 == 1:
    position = int((length - 1) / 2)
    median = numbers[position]
else:
    position1 = int(length / 2)
    position2 = int((length / 2) - 1)
    median = (numbers[position1] + numbers[position2]) / 2
print(f'{median} is the median of this list')
