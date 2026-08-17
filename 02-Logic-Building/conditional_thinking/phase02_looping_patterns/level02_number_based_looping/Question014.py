def sumDigits(number):
    value = abs(number)
    sum = 0

    while True:
        sum += value % 10
        value //= 10

        if not (value > 0):
            break

    return sum


def main():
    # Question 14: Find the sum of digits of a number.
    number = 9876
    print("Sum of digits = " + str(sumDigits(number)))


if __name__ == "__main__":
    main()


"""
QUESTION:

Find the sum of digits of a number.


--------------------------------------------------
WHAT DOES THE QUESTION MEAN?
--------------------------------------------------

We are given a number.

We need to add all the digits
of that number together.


Example:

9876


The digits are:

9
8
7
6


We need to calculate:

9 + 8 + 7 + 6


Therefore:

9 + 8 + 7 + 6 = 30


Expected output:

Sum of digits = 30


--------------------------------------------------
SOLUTION
--------------------------------------------------

We use:

1. `abs()`
2. `% 10`
3. `// 10`
4. `while` loop
5. `sum` variable


The main logic is:

sum += value % 10


This gets the last digit
and adds it to the total sum.


Then:

value //= 10


removes the last digit.


We repeat this until
all digits are processed.


--------------------------------------------------
STEP 1 — STORE THE NUMBER
--------------------------------------------------

Code:

number = 9876


The variable `number` stores
the original number.


--------------------------------------------------
STEP 2 — USE abs()
--------------------------------------------------

Code:

value = abs(number)


`abs()` returns the absolute
value of a number.


Example:

abs(9876) = 9876

abs(-9876) = 9876


We use `abs()` so that the
negative sign is not processed
as part of the digit logic.


For example:

-9876


has the digits:

9, 8, 7, 6


The negative sign is not a digit.


--------------------------------------------------
STEP 3 — CREATE THE SUM VARIABLE
--------------------------------------------------

Code:

sum = 0


The variable `sum` stores
the total of all processed digits.


Initially:

sum = 0


Every time we extract a digit,
we add it to `sum`.


--------------------------------------------------
STEP 4 — START THE LOOP
--------------------------------------------------

Code:

while True:


The loop repeatedly processes
one digit at a time.


The loop stops when the
value becomes 0.


--------------------------------------------------
STEP 5 — GET THE LAST DIGIT
--------------------------------------------------

Code:

value % 10


The `%` operator gives
the remainder.


When we use:

value % 10


we get the last digit.


Examples:

9876 % 10 = 6

987 % 10 = 7

98 % 10 = 8

9 % 10 = 9


IMPORTANT:


`% 10` → GET THE LAST DIGIT


--------------------------------------------------
STEP 6 — ADD THE DIGIT TO SUM
--------------------------------------------------

Code:

sum += value % 10


This means:

sum = sum + value % 10


Suppose:

sum = 6


and:

value % 10 = 7


Then:

sum = 6 + 7

sum = 13


So each extracted digit
is added to the total.


--------------------------------------------------
STEP 7 — REMOVE THE LAST DIGIT
--------------------------------------------------

Code:

value //= 10


This means:

value = value // 10


Integer division by 10
removes the last digit.


Examples:

9876 // 10 = 987

987 // 10 = 98

98 // 10 = 9

9 // 10 = 0


IMPORTANT:


`// 10` → REMOVE THE LAST DIGIT


--------------------------------------------------
DRY RUN
--------------------------------------------------

Input:

number = 9876


Initial values:

value = 9876

sum = 0


--------------------------------------------------
ITERATION 1
--------------------------------------------------

value = 9876

Get last digit:

9876 % 10 = 6


Add to sum:

sum = 0 + 6

sum = 6


Remove last digit:

9876 // 10 = 987


Now:

value = 987

sum = 6


--------------------------------------------------
ITERATION 2
--------------------------------------------------

value = 987

Get last digit:

987 % 10 = 7


Add to sum:

sum = 6 + 7

sum = 13


Remove last digit:

987 // 10 = 98


Now:

value = 98

sum = 13


--------------------------------------------------
ITERATION 3
--------------------------------------------------

value = 98

Get last digit:

98 % 10 = 8


Add to sum:

sum = 13 + 8

sum = 21


Remove last digit:

98 // 10 = 9


Now:

value = 9

sum = 21


--------------------------------------------------
ITERATION 4
--------------------------------------------------

value = 9

Get last digit:

9 % 10 = 9


Add to sum:

sum = 21 + 9

sum = 30


Remove last digit:

9 // 10 = 0


Now:

value = 0

sum = 30


--------------------------------------------------
CHECK THE CONDITION
--------------------------------------------------

Code:

if not (value > 0):
    break


Now:

value = 0


Check:

0 > 0


This is:

False


Then:

not False


becomes:

True


Therefore:

break


The loop stops.


--------------------------------------------------
FINAL VALUE
--------------------------------------------------

sum = 30


Therefore:

Sum of digits = 30


--------------------------------------------------
OUTPUT
--------------------------------------------------

Sum of digits = 30


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

This problem uses two
very important operations:


1. `% 10`

Gets the last digit.


Example:

9876 % 10 = 6


Memory:

`% 10` → GET


--------------------------------------------------

2. `// 10`

Removes the last digit.


Example:

9876 // 10 = 987


Memory:

`// 10` → REMOVE


--------------------------------------------------
THE MAIN PATTERN
--------------------------------------------------

For digit-processing problems:


digit = value % 10

value = value // 10


For this problem:


sum += value % 10

value //= 10


Therefore:


GET DIGIT

↓

ADD DIGIT

↓

REMOVE DIGIT

↓

REPEAT


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Input:

1234


Digits:

1, 2, 3, 4


Calculation:

1 + 2 + 3 + 4


= 10


Output:

Sum of digits = 10


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Input:

555


Calculation:

5 + 5 + 5


= 15


Output:

Sum of digits = 15


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

Input:

1000


Calculation:

1 + 0 + 0 + 0


= 1


Output:

Sum of digits = 1


--------------------------------------------------
EXAMPLE 5 — NEGATIVE NUMBER
--------------------------------------------------

Input:

-1234


First:

abs(-1234)


becomes:

1234


Then:

1 + 2 + 3 + 4


= 10


Output:

Sum of digits = 10


The negative sign is not
included in the sum.


--------------------------------------------------
EXAMPLE 6 — SINGLE DIGIT
--------------------------------------------------

Input:

7


Calculation:

7


Output:

Sum of digits = 7


--------------------------------------------------
EXAMPLE 7 — ZERO
--------------------------------------------------

Input:

0


The number contains one digit:

0


Therefore:

Sum of digits = 0


Our current logic correctly
returns:

0


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

9876


Expected:

Sum of digits = 30


--------------------------------------------------

TEST CASE 2:

Input:

1234


Expected:

Sum of digits = 10


--------------------------------------------------

TEST CASE 3:

Input:

555


Expected:

Sum of digits = 15


--------------------------------------------------

TEST CASE 4:

Input:

1000


Expected:

Sum of digits = 1


--------------------------------------------------

TEST CASE 5:

Input:

-1234


Expected:

Sum of digits = 10


--------------------------------------------------

TEST CASE 6:

Input:

7


Expected:

Sum of digits = 7


--------------------------------------------------

TEST CASE 7:

Input:

0


Expected:

Sum of digits = 0


--------------------------------------------------
COMMON MISTAKE 1
--------------------------------------------------

Confusing `% 10` and `// 10`.


Remember:


`% 10`

→ GET last digit


`// 10`

→ REMOVE last digit


--------------------------------------------------
COMMON MISTAKE 2
--------------------------------------------------

Forgetting to add the digit
to the sum.


Wrong:

value % 10


This only gets the digit.


Correct:

sum += value % 10


This gets the digit and
adds it to the total.


--------------------------------------------------
COMMON MISTAKE 3
--------------------------------------------------

Forgetting to remove the digit.


If we don't use:

value //= 10


the same digit will continue
to be processed repeatedly.


The value must become smaller
after every iteration.


--------------------------------------------------
COMMON MISTAKE 4
--------------------------------------------------

Using `/` instead of `//`.


Wrong:

value /= 10


Correct:

value //= 10


For this integer-based logic,
we use integer division.


--------------------------------------------------
COMMON MISTAKE 5
--------------------------------------------------

Forgetting `abs()` for negative numbers.


If:

number = -1234


we want:

1 + 2 + 3 + 4


not a calculation involving
the negative sign.


Using:

value = abs(number)


makes the logic easier.


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How do you find the sum of digits
of a number?"


You can say:


"I repeatedly extract the last digit
using `% 10` and add it to a running
sum. Then I remove the last digit
using integer division by 10. I repeat
this process until the number becomes
zero."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. `abs()`

Gets the positive version
of the number.


2. `% 10`

Gets the last digit.


3. `// 10`

Removes the last digit.


4. `sum += digit`

Adds the digit to the total.


5. `while True`

Repeats the process.


6. `break`

Stops the loop.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

For sum of digits:


NUMBER

↓

`% 10`

↓

GET LAST DIGIT

↓

ADD TO SUM

↓

`// 10`

↓

REMOVE LAST DIGIT

↓

REPEAT


Easy pattern:


GET

↓

ADD

↓

REMOVE

↓

REPEAT


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

Question:

Find the sum of digits of 9876.


        ↓


Take absolute value


        ↓


9876


        ↓


Get last digit


        ↓


6


        ↓


Add to sum


        ↓


sum = 6


        ↓


Remove last digit


        ↓


987


        ↓


Get 7


        ↓


sum = 13


        ↓


Remove 7


        ↓


98


        ↓


Get 8


        ↓


sum = 21


        ↓


Remove 8


        ↓


9


        ↓


Get 9


        ↓


sum = 30


        ↓


Remove 9


        ↓


0


        ↓


Stop


        ↓


Answer:

30


--------------------------------------------------
MAIN THING TO REMEMBER
--------------------------------------------------

To find the sum of digits:


1. Get the last digit using `% 10`.

2. Add it to `sum`.

3. Remove the last digit using `// 10`.

4. Repeat until the value becomes 0.

5. The final `sum` is the answer.


MOST IMPORTANT PATTERN:


sum += number % 10

number //= 10


Remember:


`% 10` → GET

`// 10` → REMOVE

`sum +=` → ADD


GET → ADD → REMOVE → REPEAT
"""