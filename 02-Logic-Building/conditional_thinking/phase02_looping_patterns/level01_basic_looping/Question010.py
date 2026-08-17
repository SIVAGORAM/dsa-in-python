def productDigits(number):
    value = abs(number)
    product = 1

    if value == 0:
        return 0

    while value > 0:
        product *= value % 10
        value //= 10

    return product


def main():
    # Question 10: Print the product of digits of a given number.

    number = 2345

    print("Product of digits = " + str(productDigits(number)))


if __name__ == "__main__":
    main()


"""
QUESTION:

Print the product of digits of a given number.


WHAT DOES THE QUESTION MEAN?

We are given a number.

We need to take each digit of that number
and multiply all the digits together.


For example:

number = 2345


Its digits are:

2
3
4
5


Multiply them:

2 × 3 × 4 × 5

= 120


Therefore:

Product of digits = 120


--------------------------------------------------
WHAT IS A DIGIT?
--------------------------------------------------

For the number:

2345


The individual digits are:

Thousands → 2
Hundreds  → 3
Tens      → 4
Ones      → 5


We need to process these digits one by one.


--------------------------------------------------
MAIN CONCEPT:
EXTRACTING DIGITS
--------------------------------------------------

To get the LAST digit of a number:

number % 10


To REMOVE the LAST digit:

number // 10


These two operations are extremely important
for number-based logic problems.


--------------------------------------------------
HOW % 10 WORKS
--------------------------------------------------

Suppose:

value = 2345


Then:

2345 % 10


gives:

5


So:

value % 10

means:

"Give me the last digit."


--------------------------------------------------
HOW // 10 WORKS
--------------------------------------------------

Suppose:

value = 2345


Then:

2345 // 10


gives:

234


So:

value // 10

means:

"Remove the last digit."


--------------------------------------------------
DIGIT EXTRACTION PATTERN
--------------------------------------------------

For:

2345


First:

2345 % 10 = 5

Last digit = 5


Then:

2345 // 10 = 234


Next:

234 % 10 = 4

Last digit = 4


Then:

234 // 10 = 23


Next:

23 % 10 = 3


Then:

23 // 10 = 2


Next:

2 % 10 = 2


Then:

2 // 10 = 0


Now the number has become 0,
so the loop stops.


--------------------------------------------------
SOLUTION LOGIC
--------------------------------------------------

Step 1:

Take the absolute value:

value = abs(number)


Step 2:

Start product with:

product = 1


Step 3:

While there are still digits:

while value > 0:


Step 4:

Extract the last digit:

value % 10


Step 5:

Multiply it with product:

product *= value % 10


Step 6:

Remove the last digit:

value //= 10


Step 7:

Repeat until value becomes 0.


Step 8:

Return product.


--------------------------------------------------
WHY product = 1?
--------------------------------------------------

We are multiplying values.

Therefore, we start with:

product = 1


For example:

1 × 5 = 5

5 × 4 = 20

20 × 3 = 60

60 × 2 = 120


If we started with:

product = 0


then:

0 × 5 = 0

0 × 4 = 0

0 × 3 = 0

0 × 2 = 0


The answer would always become 0.


Therefore:

For multiplication → start with 1.


--------------------------------------------------
DRY RUN
--------------------------------------------------

Given:

number = 2345


First:

value = abs(2345)

value = 2345


Initial:

product = 1


--------------------------------------------------
ITERATION 1
--------------------------------------------------

value = 2345

Extract last digit:

2345 % 10 = 5


So:

product *= 5


product:

1 × 5 = 5


Now remove the last digit:

2345 // 10 = 234


State:

value = 234
product = 5


--------------------------------------------------
ITERATION 2
--------------------------------------------------

value = 234

Extract:

234 % 10 = 4


Multiply:

product = 5 × 4

product = 20


Remove last digit:

234 // 10 = 23


State:

value = 23
product = 20


--------------------------------------------------
ITERATION 3
--------------------------------------------------

value = 23

Extract:

23 % 10 = 3


Multiply:

product = 20 × 3

product = 60


Remove last digit:

23 // 10 = 2


State:

value = 2
product = 60


--------------------------------------------------
ITERATION 4
--------------------------------------------------

value = 2

Extract:

2 % 10 = 2


Multiply:

product = 60 × 2

product = 120


Remove last digit:

2 // 10 = 0


State:

value = 0
product = 120


--------------------------------------------------
LOOP ENDS
--------------------------------------------------

Condition:

while value > 0


Now:

value = 0


So:

0 > 0

is False.


The loop stops.


Finally:

return product


returns:

120


--------------------------------------------------
DRY RUN TABLE
--------------------------------------------------

| Iteration | value before | Last digit (`value % 10`) | Product | value after (`value // 10`) |
|----------:|-------------:|--------------------------:|--------:|----------------------------:|
| Start | 2345 | - | 1 | - |
| 1 | 2345 | 5 | 5 | 234 |
| 2 | 234 | 4 | 20 | 23 |
| 3 | 23 | 3 | 60 | 2 |
| 4 | 2 | 2 | 120 | 0 |


--------------------------------------------------
FINAL CALCULATION
--------------------------------------------------

Digits:

2, 3, 4, 5


Product:

2 × 3 × 4 × 5

= 6 × 4 × 5

= 24 × 5

= 120


Output:

Product of digits = 120


--------------------------------------------------
WHY DO WE USE abs()?
--------------------------------------------------

The code contains:

value = abs(number)


This handles negative numbers.


For example:

number = -2345


Without `abs()`:

value = -2345


The condition:

while value > 0


would immediately be False.


The loop would not process the digits.


With:

abs(-2345)


we get:

2345


Then the digits can be processed normally.


Therefore:

-2345

is treated as:

2345


and the product is:

2 × 3 × 4 × 5 = 120


--------------------------------------------------
WHY DO WE HAVE THIS CONDITION?
--------------------------------------------------

The code contains:

if value == 0:
    return 0


This is important.


Suppose:

number = 0


The only digit is:

0


Therefore:

Product = 0


But if we started with:

product = 1


and the loop condition was:

while value > 0


then:

value = 0


would mean the loop never runs.


The function would incorrectly return:

1


So we explicitly handle zero:

if value == 0:
    return 0


Correct answer:

0


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

number = 123


Digits:

1
2
3


Product:

1 × 2 × 3

= 6


Output:

Product of digits = 6


Dry run:

product = 1

1 × 3 = 3

3 × 2 = 6

6 × 1 = 6


Final:

6


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

number = 456


Digits:

4
5
6


Product:

4 × 5 × 6

= 120


Output:

Product of digits = 120


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

number = 1111


Product:

1 × 1 × 1 × 1

= 1


Output:

Product of digits = 1


--------------------------------------------------
EXAMPLE 5
--------------------------------------------------

number = 0


Digit:

0


Product:

0


Output:

Product of digits = 0


--------------------------------------------------
EXAMPLE 6
--------------------------------------------------

number = 25


Digits:

2
5


Product:

2 × 5

= 10


Output:

Product of digits = 10


--------------------------------------------------
EXAMPLE 7
--------------------------------------------------

number = -234


abs(-234)

= 234


Digits:

2
3
4


Product:

2 × 3 × 4

= 24


Output:

Product of digits = 24


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

number = 2345


Calculation:

2 × 3 × 4 × 5


Expected:

Product of digits = 120


--------------------------------------------------

TEST CASE 2:

Input:

number = 123


Calculation:

1 × 2 × 3


Expected:

Product of digits = 6


--------------------------------------------------

TEST CASE 3:

Input:

number = 456


Calculation:

4 × 5 × 6


Expected:

Product of digits = 120


--------------------------------------------------

TEST CASE 4:

Input:

number = 1111


Calculation:

1 × 1 × 1 × 1


Expected:

Product of digits = 1


--------------------------------------------------

TEST CASE 5:

Input:

number = 0


Expected:

Product of digits = 0


--------------------------------------------------

TEST CASE 6:

Input:

number = 25


Calculation:

2 × 5


Expected:

Product of digits = 10


--------------------------------------------------

TEST CASE 7:

Input:

number = -234


Calculation:

2 × 3 × 4


Expected:

Product of digits = 24


--------------------------------------------------
IMPORTANT PATTERN:
% 10 AND // 10
--------------------------------------------------

This is one of the most important patterns
for number-based programming problems.


To get the last digit:

number % 10


To remove the last digit:

number // 10


Example:

number = 572


Last digit:

572 % 10 = 2


Remove last digit:

572 // 10 = 57


Again:

57 % 10 = 7


Remove:

57 // 10 = 5


Again:

5 % 10 = 5


Remove:

5 // 10 = 0


Finished.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

Think:

% 10
    ↓
GET LAST DIGIT


// 10
    ↓
REMOVE LAST DIGIT


So:

digit = number % 10

number = number // 10


This pattern is extremely important.


--------------------------------------------------
ADDITION VS MULTIPLICATION
--------------------------------------------------

For SUM OF DIGITS:

total = 0

while value > 0:
    digit = value % 10
    total += digit
    value //= 10


For PRODUCT OF DIGITS:

product = 1

while value > 0:
    digit = value % 10
    product *= digit
    value //= 10


The digit extraction logic is the same.


Only the accumulator operation changes.


SUM:

total += digit


PRODUCT:

product *= digit


--------------------------------------------------
Q10 CONNECTION TO FACTORIAL
--------------------------------------------------

In Q9, we learned:

result = 1

result *= value


In Q10, we again use:

product = 1

product *= digit


Both are multiplication accumulators.


The difference is:

Q9:

Multiply a sequence of numbers.


Q10:

Multiply the digits of a number.


--------------------------------------------------
IMPORTANT EDGE CASE:
NUMBER CONTAINS ZERO
--------------------------------------------------

Suppose:

number = 203


Digits:

2
0
3


Product:

2 × 0 × 3

= 0


As soon as a digit is zero,
the final product will be zero.


This is a useful observation,
but we still need to process the number correctly.


--------------------------------------------------
EXAMPLE:
203
--------------------------------------------------

Initial:

product = 1


Extract:

203 % 10 = 3

product = 1 × 3 = 3


Remove:

203 // 10 = 20


Next:

20 % 10 = 0

product = 3 × 0 = 0


Remove:

20 // 10 = 2


Next:

2 % 10 = 2

product = 0 × 2 = 0


Final:

0


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How did you find the product of digits?"

You can say:

"I repeatedly extract the last digit using `% 10`,
multiply it into an accumulator, and then remove the
last digit using integer division by 10. I continue
until the number becomes zero."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. `% 10`

Extracts the last digit.


2. `// 10`

Removes the last digit.


3. `while` loop

Repeats the process until all digits are processed.


4. `product = 1`

Initial value for multiplication.


5. `product *= digit`

Multiplies the extracted digit into the product.


6. `abs()`

Allows negative numbers to be processed using
their positive digit representation.


7. `return`

Returns the final product.


--------------------------------------------------
YOUR CODE STRUCTURE
--------------------------------------------------

number
   ↓
abs(number)
   ↓
value
   ↓
product = 1
   ↓
while value > 0
   ↓
Get last digit
   ↓
value % 10
   ↓
Multiply
   ↓
product *= digit
   ↓
Remove last digit
   ↓
value //= 10
   ↓
Repeat
   ↓
return product


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

number = 2345

        ↓

value = 2345

        ↓

product = 1

        ↓

2345 % 10 = 5

1 × 5 = 5

        ↓

2345 // 10 = 234

        ↓

234 % 10 = 4

5 × 4 = 20

        ↓

234 // 10 = 23

        ↓

23 % 10 = 3

20 × 3 = 60

        ↓

23 // 10 = 2

        ↓

2 % 10 = 2

60 × 2 = 120

        ↓

2 // 10 = 0

        ↓

Loop ends

        ↓

Return 120

        ↓

Product of digits = 120


MAIN THINGS TO REMEMBER:

1. `% 10` → get the last digit.
2. `// 10` → remove the last digit.
3. Start multiplication with `product = 1`.
4. Use `product *= digit`.
5. Use `abs()` for negative numbers.
6. Handle `0` separately.
7. Repeat until the number becomes 0.
"""