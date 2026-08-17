def main():
    # Question 25: Check if a number is a multiple of 7 or ends with 7.
    number = 147

    if number % 7 == 0 or abs(number) % 10 == 7:
        print("Matches condition")
    else:
        print("Does not match condition")


if __name__ == "__main__":
    main()


"""
Explanation:

The question asks us to check whether a number satisfies at least
one of these two conditions:

1. The number is a multiple of 7.
2. The number ends with 7.

We use the `or` operator because only one condition needs to be True.


Step 1: Check if the number is a multiple of 7.

Condition:

number % 7 == 0

For:
number = 147

147 % 7 = 0

So:
147 % 7 == 0 → True


Step 2: Check if the number ends with 7.

Condition:

abs(number) % 10 == 7

For:
number = 147

abs(147) = 147

147 % 10 = 7

So:
147 % 10 == 7 → True


Since at least one condition is True:

True or True → True

Therefore:
Matches condition


Example 2:

number = 21

21 % 7 = 0

So:
21 is a multiple of 7.

Therefore:
Matches condition


Example 3:

number = 27

27 % 7 != 0

But:

27 % 10 = 7

So:
27 ends with 7.

Therefore:
Matches condition


Example 4:

number = 25

25 % 7 != 0
25 % 10 != 7

Both conditions are False.

Therefore:
Does not match condition


Test Cases:

1. Input: 147
   Output: Matches condition

2. Input: 21
   Output: Matches condition

3. Input: 27
   Output: Matches condition

4. Input: 25
   Output: Does not match condition

5. Input: 77
   Output: Matches condition

6. Input: 70
   Output: Matches condition

7. Input: -27
   Output: Matches condition


Key Concepts:

`%` → Returns the remainder.

`or` → At least one condition must be True.

`abs()` → Returns the absolute value.

Examples:

147 % 7 → 0
147 % 10 → 7
abs(-27) → 27

Important:

Python uses:
`or`

Not:
`||`

Python uses:
`abs(number)`

Not:
`Math.abs(number)`
"""