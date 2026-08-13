def main():
    # Question 24: Check whether a given integer is single-digit, double-digit, or multi-digit.
    number = 87

    value = abs(number)

    if value <= 9:
        print("Single-digit")
    elif value <= 99:
        print("Double-digit")
    else:
        print("Multi-digit")


if __name__ == "__main__":
    main()


"""
Explanation:

The question asks us to determine whether a given integer is
single-digit, double-digit, or multi-digit.

We use `abs()` to ignore the negative sign when checking the
number of digits.

Example:
number = 87

Step 1: Convert the number to its absolute value.

value = abs(number)

abs(87) = 87

So:
value = 87


Step 2: Check whether it is a single-digit number.

Condition:

value <= 9

For 87:

87 <= 9 → False

So it is not a single-digit number.


Step 3: Check whether it is a double-digit number.

Condition:

value <= 99

For 87:

87 <= 99 → True

Therefore:
Double-digit


Another example:

number = -7

value = abs(-7)
value = 7

7 <= 9 → True

Therefore:
Single-digit


Another example:

number = 125

value = 125

125 <= 9 → False
125 <= 99 → False

Therefore:
Multi-digit


Test Cases:

1. Input: 7
   Output: Single-digit

2. Input: -7
   Output: Single-digit

3. Input: 87
   Output: Double-digit

4. Input: -99
   Output: Double-digit

5. Input: 100
   Output: Multi-digit

6. Input: -125
   Output: Multi-digit

7. Input: 0
   Output: Single-digit


Key Concepts:

`abs()` → Returns the absolute value of a number.

For example:
abs(-7) → 7
abs(7)  → 7

`<=` → Less than or equal to

Important:

We use `abs(number)` so that negative numbers are classified
based on their number of digits, ignoring the negative sign.
"""