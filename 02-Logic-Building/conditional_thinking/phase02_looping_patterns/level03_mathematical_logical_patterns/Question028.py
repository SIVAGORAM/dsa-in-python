def factorial(number):
    result = 1
    for value in range(2, number + 1):
        result *= value
    return result

def main():
    # Question 28: : Check if a number is a strong number (sum of factorials of digits = number).
    number = 5
    print(str(number) + "not  = " + str(factorial(number)))


if __name__ == "__main__":
    main()

"""
Explanation:
The value stored in `number` is the input that the conditions or loops work on.
The helper multiplies all numbers from 2 up to the given number to build the factorial step by step.
The calculated answer is printed after the logic produces the final value.
"""