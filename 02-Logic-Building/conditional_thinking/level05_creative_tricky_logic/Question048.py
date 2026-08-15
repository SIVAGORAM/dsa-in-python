def sum_digits(number):
    value = abs(number)
    digit_sum = 0

    while True:
        digit_sum += value % 10
        value //= 10

        if not (value > 0):
            break

    return digit_sum


def product_digits(number):
    value = abs(number)
    digit_product = 1

    if value == 0:
        return 0

    while value > 0:
        digit_product *= value % 10
        value //= 10

    return digit_product


def main():
    # Question 48: Take an integer (1-9999) and check if the sum
    # of its digits is greater than the product of its digits.

    number = 1234

    digit_sum = sum_digits(number)
    digit_product = product_digits(number)

    if digit_sum > digit_product:
        print("Digit sum is greater")
    else:
        print("Digit product is greater or equal")


if __name__ == "__main__":
    main()


"""
QUESTION:

Take an integer (1-9999) and check if the sum of its digits is
greater than the product of its digits.


WHAT DOES THE QUESTION MEAN?

We are given a number.

Example:

1234

We need to:

1. Find the sum of all digits.
2. Find the product of all digits.
3. Compare the two results.


For 1234:

Digits:

1, 2, 3, 4


Digit sum:

1 + 2 + 3 + 4 = 10


Digit product:

1 * 2 * 3 * 4 = 24


Compare:

10 > 24

False


Therefore:

Digit product is greater or equal.


--------------------------------------------------
HOW DO WE EXTRACT DIGITS?
--------------------------------------------------

We use two important operators:

% 10
// 10


`number % 10`

gives the LAST digit.


Example:

1234 % 10 = 4


`number // 10`

removes the LAST digit.


Example:

1234 // 10 = 123


Therefore, we can process every digit one by one.


--------------------------------------------------
DIGIT EXTRACTION EXAMPLE
--------------------------------------------------

number = 1234


Step 1:

1234 % 10 = 4

Last digit = 4


Remove 4:

1234 // 10 = 123


Step 2:

123 % 10 = 3

Last digit = 3


Remove 3:

123 // 10 = 12


Step 3:

12 % 10 = 2

Last digit = 2


Remove 2:

12 // 10 = 1


Step 4:

1 % 10 = 1

Last digit = 1


Remove 1:

1 // 10 = 0


Now there are no digits left.


--------------------------------------------------
HOW SUM OF DIGITS WORKS
--------------------------------------------------

We start with:

digit_sum = 0


For 1234:

First digit:

4

digit_sum = 0 + 4

digit_sum = 4


Second digit:

3

digit_sum = 4 + 3

digit_sum = 7


Third digit:

2

digit_sum = 7 + 2

digit_sum = 9


Fourth digit:

1

digit_sum = 9 + 1

digit_sum = 10


Final:

digit_sum = 10


--------------------------------------------------
HOW PRODUCT OF DIGITS WORKS
--------------------------------------------------

We start with:

digit_product = 1


Why 1?

Because multiplying by 1 does not change the result.


For 1234:

First digit:

4

product = 1 * 4

product = 4


Second digit:

3

product = 4 * 3

product = 12


Third digit:

2

product = 12 * 2

product = 24


Fourth digit:

1

product = 24 * 1

product = 24


Final:

digit_product = 24


--------------------------------------------------
DRY RUN — SUM
--------------------------------------------------

number = 1234


Initial:

value = 1234
digit_sum = 0


Loop 1:

value % 10 = 4

digit_sum = 0 + 4 = 4

value //= 10

value = 123


Loop 2:

value % 10 = 3

digit_sum = 4 + 3 = 7

value = 12


Loop 3:

value % 10 = 2

digit_sum = 7 + 2 = 9

value = 1


Loop 4:

value % 10 = 1

digit_sum = 9 + 1 = 10

value = 0


Final:

digit_sum = 10


--------------------------------------------------
DRY RUN — PRODUCT
--------------------------------------------------

number = 1234


Initial:

value = 1234
digit_product = 1


Loop 1:

1234 % 10 = 4

product = 1 * 4

product = 4

value = 123


Loop 2:

123 % 10 = 3

product = 4 * 3

product = 12

value = 12


Loop 3:

12 % 10 = 2

product = 12 * 2

product = 24

value = 1


Loop 4:

1 % 10 = 1

product = 24 * 1

product = 24

value = 0


Final:

digit_product = 24


--------------------------------------------------
FINAL COMPARISON
--------------------------------------------------

digit_sum = 10

digit_product = 24


Condition:

digit_sum > digit_product


10 > 24

False


Therefore:

Digit product is greater or equal.


Output:

Digit product is greater or equal


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

number = 123


Digits:

1, 2, 3


Sum:

1 + 2 + 3 = 6


Product:

1 * 2 * 3 = 6


Compare:

6 > 6

False


Output:

Digit product is greater or equal.


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

number = 111


Sum:

1 + 1 + 1 = 3


Product:

1 * 1 * 1 = 1


Compare:

3 > 1

True


Output:

Digit sum is greater


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

number = 222


Sum:

2 + 2 + 2 = 6


Product:

2 * 2 * 2 = 8


Compare:

6 > 8

False


Output:

Digit product is greater or equal.


--------------------------------------------------
EXAMPLE 5 — NUMBER CONTAINS ZERO
--------------------------------------------------

number = 120


Digits:

1, 2, 0


Sum:

1 + 2 + 0 = 3


Product:

1 * 2 * 0 = 0


Compare:

3 > 0

True


Output:

Digit sum is greater


IMPORTANT:

If any digit is zero, the digit product becomes zero.


--------------------------------------------------
WHY DO WE HAVE A SPECIAL CASE FOR ZERO?
--------------------------------------------------

The function starts with:

digit_product = 1


If the number itself is:

0


There is one digit:

0


The product should be:

0


Therefore we explicitly handle:

if value == 0:
    return 0


This makes the function correctly handle zero.


--------------------------------------------------
NEGATIVE NUMBERS
--------------------------------------------------

The question says:

1-9999

So normally we are dealing with positive numbers.

But the function uses:

abs(number)


This means if someone passes:

-123


it becomes:

123


and the digits are processed as:

1, 2, 3.


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

1234

Sum:

1 + 2 + 3 + 4 = 10

Product:

1 * 2 * 3 * 4 = 24

Output:

Digit product is greater or equal.


TEST CASE 2:

Input:

123

Sum:

6

Product:

6

Output:

Digit product is greater or equal.


TEST CASE 3:

Input:

111

Sum:

3

Product:

1

Output:

Digit sum is greater


TEST CASE 4:

Input:

222

Sum:

6

Product:

8

Output:

Digit product is greater or equal.


TEST CASE 5:

Input:

120

Sum:

3

Product:

0

Output:

Digit sum is greater


TEST CASE 6:

Input:

101

Sum:

2

Product:

0

Output:

Digit sum is greater


TEST CASE 7:

Input:

999

Sum:

27

Product:

729

Output:

Digit product is greater or equal.


TEST CASE 8:

Input:

1000

Sum:

1

Product:

0

Output:

Digit sum is greater


--------------------------------------------------
TEST CASE TABLE
--------------------------------------------------

| Number | Digit Sum | Digit Product | Expected Output |
|-------:|----------:|--------------:|-----------------|
| 1234 | 10 | 24 | Digit product is greater or equal |
| 123 | 6 | 6 | Digit product is greater or equal |
| 111 | 3 | 1 | Digit sum is greater |
| 222 | 6 | 8 | Digit product is greater or equal |
| 120 | 3 | 0 | Digit sum is greater |
| 101 | 2 | 0 | Digit sum is greater |
| 999 | 27 | 729 | Digit product is greater or equal |
| 1000 | 1 | 0 | Digit sum is greater |


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. `% 10`

Extracts the last digit.

Example:

1234 % 10 = 4


2. `// 10`

Removes the last digit.

Example:

1234 // 10 = 123


3. `while`

Used to process the number until all digits are removed.


4. Accumulator

For sum:

digit_sum = 0


For product:

digit_product = 1


These variables keep the running result.


5. Function

We created separate functions:

sum_digits()
product_digits()


This makes the program easier to understand and reuse.


--------------------------------------------------
IMPORTANT PATTERN TO REMEMBER
--------------------------------------------------

Whenever you need to process every digit of a number:

while number > 0:

    digit = number % 10

    number //= 10


This is a VERY important pattern for DSA.


--------------------------------------------------
DIGIT PROCESSING PATTERN
--------------------------------------------------

Number
  ↓
% 10
  ↓
Get last digit
  ↓
Process digit
  ↓
// 10
  ↓
Remove last digit
  ↓
Repeat
  ↓
Number becomes 0
  ↓
Stop


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How did you solve this problem?"

You can say:

"I process the number digit by digit. I use modulo 10 to extract
the last digit and integer division by 10 to remove the last digit.
I maintain one accumulator for the digit sum and another for the
digit product. After processing all digits, I compare the two
results."


--------------------------------------------------
IMPORTANT PYTHON NOTE
--------------------------------------------------

Avoid naming a variable:

sum

because Python already provides a built-in function called:

sum()


Instead, use:

digit_sum


Similarly, using:

digit_product

makes the purpose clearer.


--------------------------------------------------
MAIN LOGIC TO REMEMBER
--------------------------------------------------

Number
   ↓
Extract last digit using `% 10`
   ↓
Add it to sum
   ↓
Multiply it into product
   ↓
Remove digit using `// 10`
   ↓
Repeat until number becomes 0
   ↓
Compare:
sum > product
   ↓
Print result


MEMORY TRICK:

% 10  → TAKE the last digit

// 10 → REMOVE the last digit


This pattern is extremely important for upcoming
number and DSA problems.
"""