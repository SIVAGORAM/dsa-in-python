def main():
    # Question 23: Take a 4-digit number and check if the first and last digits are equal.
    number = 4554

    first_digit = number // 1000
    last_digit = number % 10

    if first_digit == last_digit:
        print("First and last digits are equal")
    else:
        print("First and last digits are not equal")


if __name__ == "__main__":
    main()


"""
Explanation:

The question asks us to take a 4-digit number and check whether
the first digit and the last digit are equal.

Example:
number = 4554


Step 1: Get the first digit.

first_digit = number // 1000

4554 // 1000 = 4

So:
first_digit = 4


Step 2: Get the last digit.

last_digit = number % 10

4554 % 10 = 4

So:
last_digit = 4


Step 3: Compare the first and last digits.

Condition:

first_digit == last_digit

For 4554:

4 == 4 → True

Therefore:
First and last digits are equal.


Another example:

number = 1234

First digit:
1234 // 1000 = 1

Last digit:
1234 % 10 = 4

Comparison:

1 == 4 → False

Therefore:
First and last digits are not equal.


Test Cases:

1. Input: 4554
   Output: First and last digits are equal

2. Input: 1234
   Output: First and last digits are not equal

3. Input: 1001
   Output: First and last digits are equal

4. Input: 5678
   Output: First and last digits are not equal

5. Input: 9999
   Output: First and last digits are equal

6. Input: 4321
   Output: First and last digits are not equal


Key Concepts:

//  → Integer division
%   → Remainder
==  → Equality comparison

Important:

For a 4-digit number:
- `number // 1000` gives the first digit.
- `number % 10` gives the last digit.
"""