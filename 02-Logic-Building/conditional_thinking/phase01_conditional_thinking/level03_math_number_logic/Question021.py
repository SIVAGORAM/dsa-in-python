def main():
    # Question 21: Take a 3-digit number and check if all digits are distinct.
    number = 427

    hundreds = number // 100
    tens = (number // 10) % 10
    ones = number % 10

    if hundreds != tens and tens != ones and hundreds != ones:
        print("All digits are distinct")
    else:
        print("Digits are not distinct")


if __name__ == "__main__":
    main()


"""
Explanation:
The variables `hundreds`, `tens`, and `ones` store the three digits
of the given 3-digit number.

For 427:
- `hundreds = 4`
- `tens = 2`
- `ones = 7`

The condition checks that every pair of digits is different:
- `hundreds != tens`
- `tens != ones`
- `hundreds != ones`

All three conditions must be True for the digits to be distinct.
"""


"""
Explanation:

The number is a 3-digit number, so we first separate it into
hundreds, tens, and ones digits.

For example:
number = 427

1. Get the hundreds digit:
   hundreds = number // 100
   427 // 100 = 4
   So, hundreds = 4

2. Get the tens digit:
   tens = (number // 10) % 10
   427 // 10 = 42
   42 % 10 = 2
   So, tens = 2

3. Get the ones digit:
   ones = number % 10
   427 % 10 = 7
   So, ones = 7

Now the digits are:
hundreds = 4
tens = 2
ones = 7

To check whether all digits are distinct, we compare every pair:

hundreds != tens
tens != ones
hundreds != ones

For 427:
4 != 2 → True
2 != 7 → True
4 != 7 → True

All three conditions are True, so the digits are distinct.

Example:
number = 121

hundreds = 1
tens = 2
ones = 1

1 != 2 → True
2 != 1 → True
1 != 1 → False

Since one condition is False:
Digits are not distinct.


Test Cases:

1. Input: 427
   Output: All digits are distinct

2. Input: 123
   Output: All digits are distinct

3. Input: 121
   Output: Digits are not distinct

4. Input: 111
   Output: Digits are not distinct

5. Input: 455
   Output: Digits are not distinct

6. Input: 987
   Output: All digits are distinct


Key Concepts:

//  → Integer division
%   → Remainder
!=  → Not equal
and → All conditions must be True
"""