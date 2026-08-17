def main():
    # Question 25: Find LCM of two numbers using loops.
    first = 12
    second = 18

    a = first
    b = second

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    lcm = abs(first * second) // abs(a)

    print("LCM = " + str(lcm))


if __name__ == "__main__":
    main()


"""
QUESTION:

Find LCM of two numbers using loops.


--------------------------------------------------
WHAT DOES THE QUESTION MEAN?
--------------------------------------------------

We are given two numbers.

We need to find their:


LCM → Least Common Multiple


The LCM is the smallest positive
number that is divisible by both
given numbers.


Example:


first = 12

second = 18


Multiples of 12:


12, 24, 36, 48, 60, ...


Multiples of 18:


18, 36, 54, 72, ...


The first common multiple is:


36


Therefore:


LCM = 36


--------------------------------------------------
EXPECTED OUTPUT
--------------------------------------------------

LCM = 36


--------------------------------------------------
SOLUTION
--------------------------------------------------

There are different ways to find
the LCM.


Here we use the relationship
between GCD and LCM:


LCM × GCD = first × second


Therefore:


LCM = (first × second) / GCD


We first find the GCD using the
Euclidean Algorithm.


Then we use the GCD to calculate
the LCM.


--------------------------------------------------
IMPORTANT CORRECTION
--------------------------------------------------

Your original code uses:


lcm = abs(first * second) / abs(a)


The `/` operator produces a float.


For example:


12 * 18 = 216


216 / 6 = 36.0


So the output may become:


LCM = 36.0


For an integer LCM, use:


//


Therefore:


lcm = abs(first * second) // abs(a)


Now the result is:


36


instead of:


36.0


--------------------------------------------------
IMPORTANT FORMULA
--------------------------------------------------

The main formula is:


LCM = (first × second) / GCD


For:


12 and 18


GCD:


6


Therefore:


LCM = (12 × 18) / 6


LCM = 216 / 6


LCM = 36


--------------------------------------------------
STEP 1 — STORE THE NUMBERS
--------------------------------------------------

Code:


first = 12

second = 18


These are the two numbers
whose LCM we want to find.


--------------------------------------------------
STEP 2 — COPY THE VALUES
--------------------------------------------------

Code:


a = first

b = second


Why do we copy them?


Because we need to find the GCD
using the Euclidean Algorithm.


We don't want to modify the
original values:


first

second


So we use:


a

b


for the GCD calculation.


Initially:


a = 12

b = 18


--------------------------------------------------
STEP 3 — FIND THE GCD
--------------------------------------------------

Code:


while b != 0:


We repeatedly calculate
the remainder.


The pattern is:


remainder = a % b

a = b

b = remainder


This is the Euclidean Algorithm.


--------------------------------------------------
STEP 4 — CALCULATE REMAINDER
--------------------------------------------------

Code:


remainder = a % b


For:


a = 12

b = 18


Calculate:


12 % 18 = 12


So:


remainder = 12


Then update:


a = 18

b = 12


--------------------------------------------------
STEP 5 — CONTINUE
--------------------------------------------------

Now:


a = 18

b = 12


Calculate:


18 % 12 = 6


Update:


a = 12

b = 6


Again:


12 % 6 = 0


Update:


a = 6

b = 0


Now the loop stops.


Therefore:


GCD = 6


--------------------------------------------------
STEP 6 — CALCULATE LCM
--------------------------------------------------

Formula:


LCM = (first × second) / GCD


Substitute:


first = 12

second = 18

GCD = 6


Therefore:


LCM = (12 × 18) / 6


= 216 / 6


= 36


--------------------------------------------------
DRY RUN — GCD PART
--------------------------------------------------

Initial:


first = 12

second = 18


Copies:


a = 12

b = 18


--------------------------------------------------
ITERATION 1
--------------------------------------------------

Current:


a = 12

b = 18


Calculate:


remainder = 12 % 18


= 12


Update:


a = 18

b = 12


--------------------------------------------------
ITERATION 2
--------------------------------------------------

Current:


a = 18

b = 12


Calculate:


remainder = 18 % 12


= 6


Update:


a = 12

b = 6


--------------------------------------------------
ITERATION 3
--------------------------------------------------

Current:


a = 12

b = 6


Calculate:


remainder = 12 % 6


= 0


Update:


a = 6

b = 0


--------------------------------------------------
LOOP CONDITION
--------------------------------------------------

Check:


b != 0


0 != 0


False.


Loop stops.


Therefore:


GCD = a


GCD = 6


--------------------------------------------------
DRY RUN — LCM PART
--------------------------------------------------

Now:


first = 12

second = 18

GCD = 6


Formula:


LCM = (first × second) // GCD


Substitute:


LCM = (12 × 18) // 6


Calculate multiplication:


12 × 18 = 216


Then:


216 // 6 = 36


Therefore:


LCM = 36


--------------------------------------------------
FINAL OUTPUT
--------------------------------------------------

```text
LCM = 36

IMPORTANT CONCEPT — GCD AND LCM

GCD and LCM are closely related.

For two positive numbers:

GCD × LCM = first × second

Therefore:

LCM = (first × second) / GCD

Example:

12 and 18

GCD = 6

LCM = 36

Check:

6 × 36 = 216

And:

12 × 18 = 216

Both are equal.

Therefore the formula is correct.

WHY DO WE FIND GCD FIRST?

Finding the LCM directly using
multiples is possible.

For example:

12:

12, 24, 36, ...

18:

18, 36, ...

But this can require checking
many numbers.

Using the GCD formula is much
more efficient:

LCM = (first × second) / GCD

So the process becomes:

FIND GCD

↓

USE GCD IN FORMULA

↓

FIND LCM

EXAMPLE 2

Input:

first = 20

second = 8

Find GCD:

20 % 8 = 4

8 % 4 = 0

Therefore:

GCD = 4

Now:

LCM = (20 × 8) / 4

= 160 / 4

= 40

Therefore:

LCM = 40

EXAMPLE 3

Input:

first = 15

second = 10

GCD:

15 % 10 = 5

10 % 5 = 0

GCD = 5

LCM:

(15 × 10) / 5

= 150 / 5

= 30

Therefore:

LCM = 30

EXAMPLE 4

Input:

first = 7

second = 3

GCD:

7 % 3 = 1

3 % 1 = 0

GCD = 1

LCM:

(7 × 3) / 1

= 21

Therefore:

LCM = 21

EXAMPLE 5

Input:

first = 12

second = 12

GCD:

12 % 12 = 0

GCD = 12

LCM:

(12 × 12) / 12

= 12

Therefore:

LCM = 12

When both numbers are equal,
their LCM is the same number.

EXAMPLE 6

Input:

first = 0

second = 18

This is an important edge case.

The standard mathematical definition
gives:

LCM(0, 18) = 0

However, the current formula:

(first * second) // GCD

would involve division by zero if
the GCD is also 0 in the case where
both inputs are 0.

For robust code, handle zero values
explicitly if zero can be an input.

ROBUST VERSION

If you want the function to handle
zero safely:

"""

def main():
    first = 12
    second = 18

    if first == 0 or second == 0:
        lcm = 0
    else:
        a = first
        b = second

        while b != 0:
            remainder = a % b
            a = b
            b = remainder

        lcm = abs(first * second) // abs(a)

    print("LCM = " + str(lcm))


if __name__ == "__main__":
    main()


    