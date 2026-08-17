def main():
    # Question 23: Print all numbers between a and b divisible by 7.
    a = 1
    b = 100

    for number in range(a, b + 1):
        if number % 7 == 0:
            print(number)


if __name__ == "__main__":
    main()


"""
QUESTION:

Print all numbers between a and b divisible by 7.


--------------------------------------------------
WHAT DOES THE QUESTION MEAN?
--------------------------------------------------

We are given two numbers:


a = starting number

b = ending number


We need to check every number
between `a` and `b`.

If a number is exactly divisible
by 7, we need to print it.


For example:


a = 1

b = 100


We check:


1, 2, 3, 4, 5, ... 100


Numbers divisible by 7 are:


7
14
21
28
35
42
49
56
63
70
77
84
91
98


Therefore, these numbers
should be printed.


--------------------------------------------------
EXPECTED OUTPUT
--------------------------------------------------

7
14
21
28
35
42
49
56
63
70
77
84
91
98


--------------------------------------------------
SOLUTION
--------------------------------------------------

We use a `for` loop to check
every number from `a` to `b`:


for number in range(a, b + 1):


Then we check whether the current
number is divisible by 7:


if number % 7 == 0:


If the remainder is 0, the number
is divisible by 7.


Then we print it:


print(number)


--------------------------------------------------
WHAT DOES "DIVISIBLE BY 7" MEAN?
--------------------------------------------------

A number is divisible by 7 if
dividing it by 7 leaves no remainder.


Examples:


7 ÷ 7 = 1

14 ÷ 7 = 2

21 ÷ 7 = 3

28 ÷ 7 = 4


There is no remainder.


Therefore:


7, 14, 21, 28


are divisible by 7.


But:


10 ÷ 7


leaves a remainder.


Therefore:


10 is NOT divisible by 7.


--------------------------------------------------
IMPORTANT `%` CONCEPT
--------------------------------------------------

The `%` operator gives the remainder.


For example:


14 % 7 = 0


Therefore:

14 is divisible by 7.


But:


15 % 7 = 1


Therefore:

15 is not divisible by 7.


So the condition:


number % 7 == 0


means:


"number is exactly divisible by 7."


--------------------------------------------------
STEP 1 — STORE a
--------------------------------------------------

Code:


a = 1


This is the starting number.


--------------------------------------------------
STEP 2 — STORE b
--------------------------------------------------

Code:


b = 100


This is the ending number.


--------------------------------------------------
STEP 3 — CREATE THE for LOOP
--------------------------------------------------

Code:


for number in range(a, b + 1):


Since:


a = 1

b = 100


the range becomes:


range(1, 101)


This generates:


1, 2, 3, ..., 100


Why `b + 1`?


Because Python's `range()` excludes
the stop value.


So:


range(1, 100)


would stop at:


99


To include 100:


range(1, 100 + 1)


--------------------------------------------------
STEP 4 — CHECK DIVISIBILITY
--------------------------------------------------

Code:


if number % 7 == 0:


For every number, Python calculates
the remainder after division by 7.


Example:


number = 7


7 % 7 = 0


Condition:


0 == 0


True.


Therefore, print 7.


--------------------------------------------------
STEP 5 — PRINT THE NUMBER
--------------------------------------------------

Code:


print(number)


If the condition is true,
the number is printed.


--------------------------------------------------
DRY RUN
--------------------------------------------------

Input:


a = 1

b = 100


The loop checks:


1, 2, 3, 4, ..., 100


--------------------------------------------------
NUMBER = 1
--------------------------------------------------

Check:


1 % 7


= 1


Condition:


1 == 0


False.


Do not print.


--------------------------------------------------
NUMBER = 2
--------------------------------------------------

Check:


2 % 7


= 2


False.


Do not print.


--------------------------------------------------
NUMBER = 3
--------------------------------------------------

Check:


3 % 7


= 3


False.


Do not print.


--------------------------------------------------
NUMBER = 4
--------------------------------------------------

Check:


4 % 7


= 4


False.


Do not print.


--------------------------------------------------
NUMBER = 5
--------------------------------------------------

Check:


5 % 7


= 5


False.


Do not print.


--------------------------------------------------
NUMBER = 6
--------------------------------------------------

Check:


6 % 7


= 6


False.


Do not print.


--------------------------------------------------
NUMBER = 7
--------------------------------------------------

Check:


7 % 7


= 0


Condition is:


0 == 0


True.


Print:


7


--------------------------------------------------
NUMBER = 8
--------------------------------------------------

Check:


8 % 7


= 1


False.


Do not print.


--------------------------------------------------
NUMBER = 9
--------------------------------------------------

Check:


9 % 7


= 2


False.


Do not print.


--------------------------------------------------
NUMBER = 10
--------------------------------------------------

Check:


10 % 7


= 3


False.


Do not print.


--------------------------------------------------
CONTINUING
--------------------------------------------------

The same process continues
until number reaches 100.


The numbers that satisfy:


number % 7 == 0


are:


7
14
21
28
35
42
49
56
63
70
77
84
91
98


--------------------------------------------------
OUTPUT
--------------------------------------------------

7
14
21
28
35
42
49
56
63
70
77
84
91
98


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

The most important concept
in this problem is:


number % 7 == 0


Remember:


% → remainder


If the remainder is 0:


DIVISIBLE


If the remainder is not 0:


NOT DIVISIBLE


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Input:


a = 10

b = 30


Numbers:


10, 11, 12, ..., 30


Numbers divisible by 7:


14
21
28


Output:


14
21
28


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Input:


a = 20

b = 50


Numbers divisible by 7:


21
28
35
42
49


Output:


21
28
35
42
49


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

Input:


a = 7

b = 7


Check:


7 % 7 = 0


Therefore:


7


is printed.


Output:


7


--------------------------------------------------
EXAMPLE 5
--------------------------------------------------

Input:


a = 8

b = 13


Check:


8 % 7 = 1

9 % 7 = 2

10 % 7 = 3

11 % 7 = 4

12 % 7 = 5

13 % 7 = 6


None are divisible by 7.


Output:


No output


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

a = 1
b = 100


Expected:

7
14
21
28
35
42
49
56
63
70
77
84
91
98


--------------------------------------------------

TEST CASE 2:

Input:

a = 10
b = 30


Expected:

14
21
28


--------------------------------------------------

TEST CASE 3:

Input:

a = 20
b = 50


Expected:

21
28
35
42
49


--------------------------------------------------

TEST CASE 4:

Input:

a = 7
b = 7


Expected:

7


--------------------------------------------------

TEST CASE 5:

Input:

a = 8
b = 13


Expected:

No output


--------------------------------------------------
COMMON MISTAKE 1
--------------------------------------------------

Forgetting `b + 1`.


Wrong:


range(a, b)


For:


a = 1

b = 100


the loop only goes up to:


99


Correct:


range(a, b + 1)


This includes 100.


--------------------------------------------------
COMMON MISTAKE 2
--------------------------------------------------

Using:


number / 7 == 0


This is not how we check
divisibility.


Correct:


number % 7 == 0


The `%` operator checks
the remainder.


--------------------------------------------------
COMMON MISTAKE 3
--------------------------------------------------

Using:


number % 7 == 1


This would find numbers
whose remainder is 1,
not numbers divisible by 7.


Correct:


number % 7 == 0


--------------------------------------------------
COMMON MISTAKE 4
--------------------------------------------------

Checking only multiples manually.


For example:


7
14
21
28
...


This can work for a fixed
range, but the loop approach
is better for understanding
the general logic.


We check every number and
apply the condition.


--------------------------------------------------
COMMON MISTAKE 5
--------------------------------------------------

Putting `print()` outside
the `if` block.


Wrong:


for number in range(a, b + 1):
    if number % 7 == 0:
        pass

    print(number)


This prints every number.


Correct:


for number in range(a, b + 1):
    if number % 7 == 0:
        print(number)


Only divisible numbers
are printed.


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:


"How do you print all numbers
between a and b that are
divisible by 7?"


You can say:


"I iterate from a through b and
use the modulo operator to check
whether the remainder after
division by 7 is zero. If it is
zero, I print the current number."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. `for` loop


Checks every number in
the given range.


2. `range(a, b + 1)`


Generates numbers from
a through b.


3. `%` operator


Returns the remainder.


4. `number % 7 == 0`


Checks divisibility by 7.


5. `if` statement


Decides whether to print
the current number.


6. `print()`


Displays matching numbers.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

Question:


Find numbers divisible by 7.


Think:


START a


↓


GO TO b


↓


CHECK:


number % 7 == 0?


↓


YES → PRINT


↓


NO → SKIP


Easy pattern:


LOOP → CHECK REMAINDER → PRINT


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

Question:

Print all numbers between
1 and 100 divisible by 7.


        ↓


a = 1


b = 100


        ↓


Loop from 1 to 100


        ↓


For every number:


number % 7 == 0?


        ↓


YES


        ↓


PRINT


        ↓


7
14
21
28
35
42
49
56
63
70
77
84
91
98


--------------------------------------------------
MAIN THING TO REMEMBER
--------------------------------------------------

Whenever you see:


"divisible by"


think:


%


For divisibility by 7:


number % 7 == 0


For divisibility by 5:


number % 5 == 0


For divisibility by 3:


number % 3 == 0


For divisibility by any number:


number % divisor == 0


The general pattern is:


for number in range(a, b + 1):

    if number % divisor == 0:
        print(number)


MEMORY:


DIVISIBLE → MODULO → REMAINDER 0

"""