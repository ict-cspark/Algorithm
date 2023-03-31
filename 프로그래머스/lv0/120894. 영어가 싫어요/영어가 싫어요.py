num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def solution(numbers):
    
    for i in range(10):
        numbers = numbers.replace(num[i], str(i))
    
    return int(numbers)