def main():
    # Question 26: Print all factors of a given number.
    number = 36

    for factor in range(1, number + 1):
        if number % factor == 0:
            print(factor)


if __name__ == "__main__":
    main()


"""
QUESTION:

Print all factors of a given number.


--------------------------------------------------
WHAT DOES THE QUESTION MEAN?
--------------------------------------------------

We are given a number.

We need to find and print all numbers
that divide the given number exactly
without leaving any remainder.


For example:


number = 36


Factors of 36 are:


1
2
3
4
6
9
12
18
36


Because each of these numbers
divides 36 exactly.


For example:


36 % 1 = 0

36 % 2 = 0

36 % 3 = 0

36 % 4 = 0

36 % 6 = 0

36 % 9 = 0

36 % 12 = 0

36 % 18 = 0

36 % 36 = 0


Therefore, all of them are
factors of 36.


--------------------------------------------------
EXPECTED OUTPUT
--------------------------------------------------

1
2
3
4
6
9
12
18
36


--------------------------------------------------
SOLUTION
--------------------------------------------------

We use a `for` loop:


for factor in range(1, number + 1):


This checks every possible factor
from 1 through the given number.


Then we check:


if number % factor == 0:


If the remainder is 0, the current
number is a factor.


Then:


print(factor)


prints the factor.


--------------------------------------------------
WHAT IS A FACTOR?
--------------------------------------------------

A factor is a number that divides
another number exactly.


For example:


36 ÷ 4 = 9


There is no remainder.


Therefore:


4 is a factor of 36.


But:


36 ÷ 5 = 7 remainder 1


Therefore:


5 is NOT a factor of 36.


--------------------------------------------------
IMPORTANT `%` CONCEPT
--------------------------------------------------

The `%` operator gives the remainder.


For example:


36 % 4 = 0


Therefore:


4 is a factor of 36.


But:


36 % 5 = 1


Therefore:


5 is not a factor of 36.


So the condition:


number % factor == 0


means:


"factor divides number exactly."


--------------------------------------------------
STEP 1 — STORE THE NUMBER
--------------------------------------------------

Code:


number = 36


This is the number
whose factors we want to find.


--------------------------------------------------
STEP 2 — CREATE THE LOOP
--------------------------------------------------

Code:


for factor in range(1, number + 1):


Since:


number = 36


the range becomes:


range(1, 37)


It generates:


1, 2, 3, ..., 36


We check every number
from 1 to 36.


--------------------------------------------------
STEP 3 — CHECK EACH POSSIBLE FACTOR
--------------------------------------------------

Code:


if number % factor == 0:


For every value of `factor`,
we calculate the remainder.


Example:


factor = 4


Then:


36 % 4 = 0


So 4 is a factor.


--------------------------------------------------
STEP 4 — PRINT THE FACTOR
--------------------------------------------------

Code:


print(factor)


If the condition is true,
the current factor is printed.


--------------------------------------------------
DRY RUN
--------------------------------------------------

Input:


number = 36


The loop checks:


1, 2, 3, 4, 5, ..., 36


--------------------------------------------------
FACTOR = 1
--------------------------------------------------

Check:


36 % 1 = 0


Condition:


0 == 0


True.


Print:


1


--------------------------------------------------
FACTOR = 2
--------------------------------------------------

Check:


36 % 2 = 0


True.


Print:


2


--------------------------------------------------
FACTOR = 3
--------------------------------------------------

Check:


36 % 3 = 0


True.


Print:


3


--------------------------------------------------
FACTOR = 4
--------------------------------------------------

Check:


36 % 4 = 0


True.


Print:


4


--------------------------------------------------
FACTOR = 5
--------------------------------------------------

Check:


36 % 5 = 1


False.


Do not print.


--------------------------------------------------
FACTOR = 6
--------------------------------------------------

Check:


36 % 6 = 0


True.


Print:


6


--------------------------------------------------
FACTOR = 7
--------------------------------------------------

Check:


36 % 7 = 1


False.


Do not print.


--------------------------------------------------
FACTOR = 8
--------------------------------------------------

Check:


36 % 8 = 4


False.


Do not print.


--------------------------------------------------
FACTOR = 9
--------------------------------------------------

Check:


36 % 9 = 0


True.


Print:


9


--------------------------------------------------
CONTINUING
--------------------------------------------------

The same process continues
for factors 10 through 36.


The numbers that divide 36
exactly are:


1
2
3
4
6
9
12
18
36


--------------------------------------------------
FINAL RESULT
--------------------------------------------------

Factors of 36:


1, 2, 3, 4, 6, 9, 12, 18, 36


--------------------------------------------------
OUTPUT
--------------------------------------------------

1
2
3
4
6
9
12
18
36


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

The most important pattern is:


number % factor == 0


Remember:


REMAINDER = 0


means:


FACTOR


For example:


24 % 6 = 0


So:


6 is a factor of 24.


--------------------------------------------------
WHY DO WE START FROM 1?
--------------------------------------------------

Every positive number is divisible
by 1.


For:


36


we know:


36 % 1 = 0


Therefore:


1 is always a factor of a
positive number.


--------------------------------------------------
WHY DO WE GO UP TO number?
--------------------------------------------------

Every positive number is also
divisible by itself.


For:


36:


36 % 36 = 0


Therefore:


36 is a factor of 36.


So checking from:


1 to number


guarantees that we don't miss
any factors.


--------------------------------------------------
WHY DO WE USE number + 1?
--------------------------------------------------

Python's `range()` excludes
the stop value.


If we write:


range(1, number)


and:


number = 36


the loop checks only:


1 through 35


It would miss:


36


Therefore:


range(1, number + 1)


checks:


1 through 36


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Input:


number = 10


Check:


10 % 1 = 0

10 % 2 = 0

10 % 3 = 1

10 % 4 = 2

10 % 5 = 0

...

10 % 10 = 0


Factors:


1
2
5
10


Output:


1
2
5
10


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Input:


number = 12


Factors:


1
2
3
4
6
12


Output:


1
2
3
4
6
12


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

Input:


number = 7


7 is a prime number.


Its factors are:


1
7


Output:


1
7


--------------------------------------------------
EXAMPLE 5
--------------------------------------------------

Input:


number = 1


The only factor of 1 is:


1


Output:


1


--------------------------------------------------
EXAMPLE 6
--------------------------------------------------

Input:


number = 16


Factors:


1
2
4
8
16


Output:


1
2
4
8
16


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

number = 36


Expected:

1
2
3
4
6
9
12
18
36


--------------------------------------------------

TEST CASE 2:

Input:

number = 10


Expected:

1
2
5
10


--------------------------------------------------

TEST CASE 3:

Input:

number = 12


Expected:

1
2
3
4
6
12


--------------------------------------------------

TEST CASE 4:

Input:

number = 7


Expected:

1
7


--------------------------------------------------

TEST CASE 5:

Input:

number = 1


Expected:

1


--------------------------------------------------

TEST CASE 6:

Input:

number = 16


Expected:

1
2
4
8
16


--------------------------------------------------
COMMON MISTAKE 1
--------------------------------------------------

Forgetting `number + 1`.


Wrong:


range(1, number)


This does not include
the number itself.


Correct:


range(1, number + 1)


--------------------------------------------------
COMMON MISTAKE 2
--------------------------------------------------

Using:


factor % number == 0


Wrong.


We want to know whether
the factor divides the number.


Correct:


number % factor == 0


--------------------------------------------------
COMMON MISTAKE 3
--------------------------------------------------

Using:


number / factor == 0


This does not check
divisibility.


Correct:


number % factor == 0


The modulo operator checks
the remainder.


--------------------------------------------------
COMMON MISTAKE 4
--------------------------------------------------

Printing every number.


Wrong:


for factor in range(1, number + 1):
    print(factor)


This prints all numbers,
not only factors.


Correct:


for factor in range(1, number + 1):
    if number % factor == 0:
        print(factor)


--------------------------------------------------
COMMON MISTAKE 5
--------------------------------------------------

Starting the loop from 0.


Wrong:


range(0, number + 1)


This causes:


number % 0


which results in a
division-by-zero error.


Start from:


1


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:


"How do you find all factors
of a number?"


You can say:


"I iterate from 1 through the
given number and use the modulo
operator to check whether the
number is exactly divisible by
the current value. If the
remainder is zero, I print that
value as a factor."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Factor


A number that divides another
number exactly.


2. `%`


Returns the remainder.


3. `number % factor == 0`


Checks whether `factor` divides
`number` exactly.


4. `for` loop


Checks all possible factors.


5. `range(1, number + 1)`


Checks from 1 through number.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

Question:


Find all factors of a number.


Think:


START FROM 1


↓


GO TO NUMBER


↓


CHECK:


number % factor == 0?


↓


YES → FACTOR


↓


PRINT


Easy pattern:


LOOP → MODULO → CHECK → PRINT


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

Question:

Find all factors of 36.


        ↓


number = 36


        ↓


Check 1 to 36


        ↓


36 % factor == 0?


        ↓


YES


        ↓


PRINT FACTOR


        ↓


1
2
3
4
6
9
12
18
36


--------------------------------------------------
MAIN THING TO REMEMBER
--------------------------------------------------

Whenever the question asks:


"Find factors"


think:


number % factor == 0


The general pattern is:


for factor in range(1, number + 1):

    if number % factor == 0:
        print(factor)


Remember:


REMAINDER 0 → FACTOR


--------------------------------------------------
IMPORTANT CONNECTION
--------------------------------------------------

Question 23:


Print numbers divisible by 7.


Pattern:


number % 7 == 0


Question 26:


Find factors of a number.


Pattern:


number % factor == 0


The idea is the same:


USE `%` TO CHECK DIVISIBILITY.


The difference is:


Question 23:


The divisor is fixed:


7


Question 26:


The divisor changes:


factor = 1, 2, 3, ..., number


--------------------------------------------------
OPTIMIZATION NOTE
--------------------------------------------------

The current solution checks
every number from 1 to `number`.


Time complexity:


O(n)


There is a faster approach
using pairs of factors and
checking only up to:


√number


But for this beginner
logic-building question,
the current solution is
excellent because it clearly
shows the divisibility pattern.


Later in DSA, we will optimize
this approach.


--------------------------------------------------
FINAL MEMORY
--------------------------------------------------

FACTOR QUESTION:


1 → number


        ↓


number % factor


        ↓


0?


        ↓


YES


        ↓


PRINT


MAIN PATTERN:


LOOP → MODULO → CHECK → PRINT


"""