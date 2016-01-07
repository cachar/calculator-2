def add(numbers):
    final_answer = 0
    for num in numbers:
        final_answer += num
    return final_answer



def subtract(numbers):
    final_answer = numbers[0]
    for num in numbers[1:]:
        final_answer -= num
    return final_answer


def multiply(numbers):
    final_answer = 1
    for num in numbers:
        final_answer *= num
    return final_answer


def divide(numbers):
    final_answer = numbers[0]
    for num in numbers[1:]:
        final_answer /= float(num)
    return final_answer


def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(numbers):
    final_answer = numbers[0]
    for num in numbers[1:]:
        if num < 0:
            num = 1/float(-num)
        final_answer **= float(num)
    return final_answer


def mod(numbers):
    final_answer = numbers[0]
    for num in numbers[1]:
        final_answer %= float(num)
    return final_answer
