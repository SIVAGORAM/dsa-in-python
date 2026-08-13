def main():
    # Question 22: Take a 3-digit number and determine if the middle digit
    # is the largest, smallest, or neither.
    number = 582

    hundreds = number // 100
    middle = (number // 10) % 10
    ones = number % 10

    if middle > hundreds and middle > ones:
        print("Middle digit is largest")
    elif middle < hundreds and middle < ones:
        print("Middle digit is smallest")
    else:
        print("Middle digit is neither")


if __name__ == "__main__":
    main()


"""
Explanation:

The question asks us to take a 3-digit number and determine whether
the middle digit is the largest, smallest, or neither.

Example:
number = 582

Step 1: Get the hundreds digit.

hundreds = number // 100
582 // 100 = 5

So:
hundreds = 5


Step 2: Get the middle digit.

middle = (number // 10) % 10

582 // 10 = 58
58 % 10 = 8

So:
middle = 8


Step 3: Get the ones digit.

ones = number % 10
582 % 10 = 2

So:
ones = 2


Now we have:

hundreds = 5
middle = 8
ones = 2


Step 4: Check if the middle digit is the largest.

Condition:

middle > hundreds and middle > ones

For 582:

8 > 5 → True
8 > 2 → True

Both conditions are True.

Therefore:
Middle digit is largest


Step 5: Check if the middle digit is the smallest.

Condition:

middle < hundreds and middle < ones

Example:
number = 318

hundreds = 3
middle = 1
ones = 8

1 < 3 → True
1 < 8 → True

Therefore:
Middle digit is smallest


Step 6: If neither condition is True.

The `else` block executes.

This happens when the middle digit is not strictly larger
than both digits and not strictly smaller than both digits.

For example:
number = 555

hundreds = 5
middle = 5
ones = 5

5 > 5 → False
5 < 5 → False

Therefore:
Middle digit is neither


Test Cases:

1. Input: 582
   Output: Middle digit is largest

2. Input: 318
   Output: Middle digit is smallest

3. Input: 555
   Output: Middle digit is neither

4. Input: 123
   Output: Middle digit is largest

5. Input: 321
   Output: Middle digit is smallest

6. Input: 585
   Output: Middle digit is largest

7. Input: 525
   Output: Middle digit is smallest


Key Concepts:

//  → Integer division
%   → Remainder
>   → Greater than
<   → Less than
and → Both conditions must be True

Important:
Python uses `and`, not `&&`.
"""