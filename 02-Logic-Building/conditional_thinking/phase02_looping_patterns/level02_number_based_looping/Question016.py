def isPerfect(number):
    if number <= 1:
        return False

    sum = 1

    for factor in range(2, number // 2 + 1):
        if number % factor == 0:
            sum += factor

    return sum == number


def main():
    # Question 16: Check if a number is a perfect number.
    number = 28
    print("Perfect number" if isPerfect(number) else "Not perfect number")


if __name__ == "__main__":
    main()


"""
QUESTION:

Check if a number is a perfect number.


--------------------------------------------------
WHAT DOES THE QUESTION MEAN?
--------------------------------------------------

A perfect number is a positive number
that is equal to the sum of all its
proper positive divisors.

A proper divisor is a number that
divides the given number exactly,
excluding the number itself.


Example:

28


The factors of 28 excluding 28 are:

1
2
4
7
14


Now add them:

1 + 2 + 4 + 7 + 14


= 28


The sum is equal to the original number.


Therefore:

28 is a Perfect Number.


--------------------------------------------------
EXPECTED OUTPUT
--------------------------------------------------

Perfect number


--------------------------------------------------
SOLUTION
--------------------------------------------------

To check whether a number is
a perfect number:


1. Check if the number is valid.

2. Start the sum with 1 because
   1 is a proper divisor of every
   number greater than 1.

3. Check all possible factors
   from 2 to number / 2.

4. If a number divides the given
   number exactly, add it to `sum`.

5. Finally, compare `sum` with
   the original number.


If:

sum == number


Then:


Perfect number


Otherwise:


Not perfect number


--------------------------------------------------
IMPORTANT CORRECTION IN THE ORIGINAL CODE
--------------------------------------------------

Your original code had:


range(2, number / 2 + 1)


This is NOT correct in Python.


Why?


The `/` operator produces a float.


Example:

28 / 2


produces:


14.0


So:


range(2, 15.0)


causes a TypeError because
`range()` requires integer values.


The correct code is:


range(2, number // 2 + 1)


Because `//` performs integer division.


For:

28 // 2


the result is:


14


Therefore:


range(2, 15)


works correctly.


--------------------------------------------------
STEP 1 — CHECK number <= 1
--------------------------------------------------

Code:

if number <= 1:
    return False


Numbers less than or equal to 1
are not perfect numbers.


For example:

0

1


are not perfect numbers.


Therefore, we immediately return:

False


--------------------------------------------------
STEP 2 — START sum WITH 1
--------------------------------------------------

Code:

sum = 1


Why start with 1?


Because:

1


is a proper divisor of every
number greater than 1.


For:

28


1 divides 28 exactly.


So we already know that:

sum = 1


--------------------------------------------------
STEP 3 — START THE for LOOP
--------------------------------------------------

Code:

for factor in range(2, number // 2 + 1):


We check possible factors
starting from 2.


Why stop at:

number // 2?


Because no proper divisor
of a number greater than 1
can be greater than half
of that number.


For example:

28 / 2 = 14


A proper divisor of 28
cannot be between 15 and 27.


So checking up to 14 is enough.


--------------------------------------------------
STEP 4 — CHECK WHETHER factor
IS A DIVISOR
--------------------------------------------------

Code:

if number % factor == 0:


The `%` operator gives
the remainder.


If:

number % factor == 0


then the number divides evenly
by `factor`.


Therefore:

factor is a divisor.


Example:

28 % 2 = 0


So:

2 is a divisor of 28.


But:

28 % 3 = 1


So:

3 is not a divisor of 28.


--------------------------------------------------
STEP 5 — ADD THE FACTOR
--------------------------------------------------

Code:

sum += factor


If `factor` is a proper divisor,
we add it to the total.


For example:


sum = 1


When factor = 2:


sum = 1 + 2

sum = 3


When factor = 4:


sum = 3 + 4

sum = 7


And so on.


--------------------------------------------------
STEP 6 — COMPARE THE SUM
--------------------------------------------------

Code:

return sum == number


At the end:


sum = 28

number = 28


Therefore:


28 == 28


This is:

True


So the function returns:

True


--------------------------------------------------
DRY RUN
--------------------------------------------------

Input:

number = 28


--------------------------------------------------
STEP 1
--------------------------------------------------

Check:

number <= 1


28 <= 1


False


So we continue.


--------------------------------------------------
STEP 2
--------------------------------------------------

Initialize:

sum = 1


--------------------------------------------------
STEP 3
--------------------------------------------------

The loop is:


range(2, 28 // 2 + 1)


Calculate:


28 // 2 = 14


Therefore:


range(2, 15)


The values are:


2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14


--------------------------------------------------
FACTOR = 2
--------------------------------------------------

Check:


28 % 2 == 0


28 % 2 = 0


True.


Therefore:

2 is a divisor.


Add:


sum = 1 + 2

sum = 3


--------------------------------------------------
FACTOR = 3
--------------------------------------------------

Check:


28 % 3


= 1


Not equal to 0.


So:

3 is not a divisor.


sum remains:

3


--------------------------------------------------
FACTOR = 4
--------------------------------------------------

Check:


28 % 4 = 0


So 4 is a divisor.


Add:


sum = 3 + 4

sum = 7


--------------------------------------------------
FACTOR = 5
--------------------------------------------------

Check:


28 % 5 = 3


Not a divisor.


sum = 7


--------------------------------------------------
FACTOR = 6
--------------------------------------------------

Check:


28 % 6 = 4


Not a divisor.


sum = 7


--------------------------------------------------
FACTOR = 7
--------------------------------------------------

Check:


28 % 7 = 0


So 7 is a divisor.


Add:


sum = 7 + 7

sum = 14


--------------------------------------------------
FACTOR = 8
--------------------------------------------------

28 % 8 = 4


Not a divisor.


sum = 14


--------------------------------------------------
FACTOR = 9
--------------------------------------------------

28 % 9 = 1


Not a divisor.


sum = 14


--------------------------------------------------
FACTOR = 10
--------------------------------------------------

28 % 10 = 8


Not a divisor.


sum = 14


--------------------------------------------------
FACTOR = 11
--------------------------------------------------

28 % 11 = 6


Not a divisor.


sum = 14


--------------------------------------------------
FACTOR = 12
--------------------------------------------------

28 % 12 = 4


Not a divisor.


sum = 14


--------------------------------------------------
FACTOR = 13
--------------------------------------------------

28 % 13 = 2


Not a divisor.


sum = 14


--------------------------------------------------
FACTOR = 14
--------------------------------------------------

28 % 14 = 0


So 14 is a divisor.


Add:


sum = 14 + 14

sum = 28


--------------------------------------------------
FINAL COMPARISON
--------------------------------------------------

Original number:

28


Sum of proper divisors:

28


Compare:


sum == number


28 == 28


Result:


True


Therefore:


28 is a Perfect Number.


--------------------------------------------------
OUTPUT
--------------------------------------------------

Perfect number


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

The most important concept
in this problem is:


number % factor == 0


This checks whether `factor`
is a divisor of `number`.


Example:


28 % 2 = 0


Therefore:

2 is a divisor.


But:


28 % 3 = 1


Therefore:

3 is not a divisor.


--------------------------------------------------
WHAT IS A DIVISOR?
--------------------------------------------------

A divisor is a number that
divides another number exactly
without leaving a remainder.


Example:


28 ÷ 4 = 7


There is no remainder.


Therefore:

4 is a divisor of 28.


Another example:


28 ÷ 5


leaves a remainder.


Therefore:

5 is not a divisor of 28.


--------------------------------------------------
WHY DO WE START sum AT 1?
--------------------------------------------------

For every number greater than 1:


1


is always a proper divisor.


For example:


28 ÷ 1 = 28


Therefore:

1 is definitely part of
the divisor sum.


So instead of checking 1
inside the loop, we start with:


sum = 1


Then we check:

2, 3, 4, ...


--------------------------------------------------
WHY DO WE STOP AT number // 2?
--------------------------------------------------

Suppose:


number = 28


Half of 28 is:


14


A proper divisor cannot be
greater than 14.


For example:


28 ÷ 14 = 2


But a number such as 15
cannot divide 28 exactly
and produce another positive
integer greater than 1.


Therefore, checking up to:


number // 2


is enough for this approach.


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Input:


6


Proper divisors:


1, 2, 3


Calculate:


1 + 2 + 3


= 6


Original:

6


Sum:

6


Therefore:


Perfect number


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Input:


10


Proper divisors:


1, 2, 5


Calculate:


1 + 2 + 5


= 8


Original:

10


Sum:

8


They are different.


Therefore:


Not perfect number


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

Input:


12


Proper divisors:


1, 2, 3, 4, 6


Calculate:


1 + 2 + 3 + 4 + 6


= 16


Original:

12


Sum:

16


Therefore:


Not perfect number


--------------------------------------------------
EXAMPLE 5
--------------------------------------------------

Input:


28


Proper divisors:


1, 2, 4, 7, 14


Calculate:


1 + 2 + 4 + 7 + 14


= 28


Therefore:


Perfect number


--------------------------------------------------
EXAMPLE 6
--------------------------------------------------

Input:


1


Check:


number <= 1


1 <= 1


True


Return:


False


Therefore:


Not perfect number


--------------------------------------------------
EXAMPLE 7
--------------------------------------------------

Input:


0


Check:


number <= 1


0 <= 1


True


Return:


False


Therefore:


Not perfect number


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

28


Proper divisors:

1, 2, 4, 7, 14


Expected:

Perfect number


--------------------------------------------------

TEST CASE 2:

Input:

6


Proper divisors:

1, 2, 3


Expected:

Perfect number


--------------------------------------------------

TEST CASE 3:

Input:

10


Proper divisors:

1, 2, 5


Expected:

Not perfect number


--------------------------------------------------

TEST CASE 4:

Input:

12


Proper divisors:

1, 2, 3, 4, 6


Expected:

Not perfect number


--------------------------------------------------

TEST CASE 5:

Input:

1


Expected:

Not perfect number


--------------------------------------------------

TEST CASE 6:

Input:

0


Expected:

Not perfect number


--------------------------------------------------

TEST CASE 7:

Input:

496


Expected:

Perfect number


--------------------------------------------------
COMMON MISTAKE 1
--------------------------------------------------

Using `/` inside `range()`.


Wrong:


range(2, number / 2 + 1)


Why?


`/` produces a float.


Example:


28 / 2 = 14.0


Correct:


range(2, number // 2 + 1)


Because:


28 // 2 = 14


--------------------------------------------------
COMMON MISTAKE 2
--------------------------------------------------

Including the number itself
in the sum.


For:


28


If we add 28 itself:


1 + 2 + 4 + 7 + 14 + 28


= 56


That is not how a perfect
number is defined.


We only add proper divisors.


--------------------------------------------------
COMMON MISTAKE 3
--------------------------------------------------

Starting with:


sum = 0


and then looping from 1.


This can work, but your current
approach is simpler:


sum = 1


Then start checking from 2.


--------------------------------------------------
COMMON MISTAKE 4
--------------------------------------------------

Using:


number % factor == 1


This is incorrect.


A divisor must leave:

0 remainder


Therefore:


number % factor == 0


--------------------------------------------------
COMMON MISTAKE 5
--------------------------------------------------

Forgetting the condition:


if number <= 1:
    return False


Numbers such as 0 and 1
are not perfect numbers.


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How do you check whether a number
is a perfect number?"


You can say:


"I find all proper divisors of the
number and add them together. I start
the sum with 1 and check possible
divisors from 2 up to half of the
number. Whenever the number is
divisible by the current factor,
I add that factor to the sum.
Finally, I compare the divisor sum
with the original number."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Divisor

A number that divides another
number without a remainder.


2. `%`

Used to check divisibility.


3. `number % factor == 0`

Means `factor` is a divisor.


4. `//`

Integer division.


5. `for` loop

Checks possible factors.


6. `sum`

Stores the total of proper divisors.


7. `==`

Compares the divisor sum
with the original number.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

For perfect numbers:


NUMBER

↓

FIND DIVISORS

↓

ADD PROPER DIVISORS

↓

COMPARE WITH NUMBER


If:


SUM == NUMBER


↓

PERFECT NUMBER


Otherwise:


NOT PERFECT NUMBER


Easy pattern:


CHECK → ADD → COMPARE


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

Question:

Check whether 28 is
a perfect number.


        ↓


number = 28


        ↓


Start:

sum = 1


        ↓


Check factors:


2 → divisor → add

3 → not divisor

4 → divisor → add

5 → not divisor

6 → not divisor

7 → divisor → add

...

14 → divisor → add


        ↓


Proper divisors:


1, 2, 4, 7, 14


        ↓


Add:


1 + 2 + 4 + 7 + 14


        ↓


28


        ↓


Compare:


28 == 28


        ↓


True


        ↓


Perfect number


--------------------------------------------------
MAIN THING TO REMEMBER
--------------------------------------------------

A perfect number is a number
whose proper divisors add up
exactly to the number itself.


Example:


28


Proper divisors:


1, 2, 4, 7, 14


Sum:


1 + 2 + 4 + 7 + 14 = 28


Therefore:


28 is a Perfect Number.


MOST IMPORTANT PATTERN:


number % factor == 0


→ FACTOR IS A DIVISOR


Then:


sum += factor


→ ADD THE DIVISOR


Finally:


sum == number


→ CHECK FOR PERFECT NUMBER


MEMORY:


FIND DIVISORS → ADD THEM → COMPARE
"""