def main():
    # Question 27: Find the sum of all factors of a number.
    number = 36
    sum = 0

    for factor in range(1, number + 1):
        if number % factor == 0:
            sum += factor

    print("Factor sum = " + str(sum))


if __name__ == "__main__":
    main()


"""
QUESTION:

Find the sum of all factors of a number.


--------------------------------------------------
WHAT DOES THE QUESTION MEAN?
--------------------------------------------------

We are given a number.

We need to:

1. Find all factors of the number.
2. Add all those factors together.
3. Print the final sum.


For example:


number = 36


The factors of 36 are:


1
2
3
4
6
9
12
18
36


Now add them:


1 + 2 + 3 + 4 + 6 + 9 + 12 + 18 + 36


= 91


Therefore:


Factor sum = 91


--------------------------------------------------
EXPECTED OUTPUT
--------------------------------------------------

Factor sum = 91


--------------------------------------------------
SOLUTION
--------------------------------------------------

We use a `for` loop to check
every possible factor:


for factor in range(1, number + 1):


Then we check:


if number % factor == 0:


If the remainder is 0, the
current number is a factor.


Then we add that factor
to the running sum:


sum += factor


--------------------------------------------------
IMPORTANT NEW CONCEPT
--------------------------------------------------

This question introduces an
important programming pattern:


ACCUMULATOR


We create:


sum = 0


Then whenever we find a valid
factor, we add it:


sum += factor


This means:


sum = sum + factor


The variable `sum` keeps
collecting the factors.


--------------------------------------------------
EXAMPLE
--------------------------------------------------

Suppose the factors are:


1, 2, 3


Start:


sum = 0


Add 1:


sum = 0 + 1

sum = 1


Add 2:


sum = 1 + 2

sum = 3


Add 3:


sum = 3 + 3

sum = 6


Final:


sum = 6


--------------------------------------------------
STEP 1 — STORE THE NUMBER
--------------------------------------------------

Code:


number = 36


This is the number whose
factors we need to find.


--------------------------------------------------
STEP 2 — CREATE THE SUM VARIABLE
--------------------------------------------------

Code:


sum = 0


Initially, we have not found
any factors yet.


Therefore:


sum = 0


This is our accumulator.


--------------------------------------------------
STEP 3 — LOOP THROUGH POSSIBLE FACTORS
--------------------------------------------------

Code:


for factor in range(1, number + 1):


Since:


number = 36


the range becomes:


range(1, 37)


It checks:


1, 2, 3, ..., 36


--------------------------------------------------
STEP 4 — CHECK IF factor IS A FACTOR
--------------------------------------------------

Code:


if number % factor == 0:


If the remainder is 0,
the factor divides the number
exactly.


Example:


36 % 4 = 0


Therefore:


4 is a factor.


--------------------------------------------------
STEP 5 — ADD THE FACTOR
--------------------------------------------------

Code:


sum += factor


This means:


sum = sum + factor


For example, if:


sum = 10

factor = 6


Then:


sum = 10 + 6


= 16


--------------------------------------------------
STEP 6 — PRINT THE FINAL SUM
--------------------------------------------------

After the loop finishes:


print("Factor sum = " + str(sum))


The variable `sum` now contains
the sum of all factors.


--------------------------------------------------
DRY RUN
--------------------------------------------------

Input:


number = 36


Initial:


sum = 0


The loop checks:


1 through 36


--------------------------------------------------
FACTOR = 1
--------------------------------------------------

Check:


36 % 1 = 0


So 1 is a factor.


Add:


sum = 0 + 1


sum = 1


--------------------------------------------------
FACTOR = 2
--------------------------------------------------

Check:


36 % 2 = 0


2 is a factor.


Add:


sum = 1 + 2


sum = 3


--------------------------------------------------
FACTOR = 3
--------------------------------------------------

Check:


36 % 3 = 0


3 is a factor.


Add:


sum = 3 + 3


sum = 6


--------------------------------------------------
FACTOR = 4
--------------------------------------------------

Check:


36 % 4 = 0


4 is a factor.


Add:


sum = 6 + 4


sum = 10


--------------------------------------------------
FACTOR = 5
--------------------------------------------------

Check:


36 % 5 = 1


5 is NOT a factor.


Do not add anything.


sum remains:


10


--------------------------------------------------
FACTOR = 6
--------------------------------------------------

Check:


36 % 6 = 0


6 is a factor.


Add:


sum = 10 + 6


sum = 16


--------------------------------------------------
FACTOR = 7
--------------------------------------------------

Check:


36 % 7 = 1


7 is NOT a factor.


sum remains:


16


--------------------------------------------------
FACTOR = 8
--------------------------------------------------

Check:


36 % 8 = 4


8 is NOT a factor.


sum remains:


16


--------------------------------------------------
FACTOR = 9
--------------------------------------------------

Check:


36 % 9 = 0


9 is a factor.


Add:


sum = 16 + 9


sum = 25


--------------------------------------------------
FACTOR = 10
--------------------------------------------------

Check:


36 % 10 = 6


Not a factor.


sum remains:


25


--------------------------------------------------
CONTINUING
--------------------------------------------------

The same process continues.


The remaining factors are:


12
18
36


Add 12:


sum = 25 + 12


= 37


Add 18:


sum = 37 + 18


= 55


Add 36:


sum = 55 + 36


= 91


--------------------------------------------------
FINAL RESULT
--------------------------------------------------

Factors:


1
2
3
4
6
9
12
18
36


Sum:


1 + 2 + 3 + 4 + 6 + 9 + 12 + 18 + 36


= 91


Therefore:


sum = 91


--------------------------------------------------
OUTPUT
--------------------------------------------------

Factor sum = 91


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

There are TWO important patterns
in this question.


PATTERN 1 — FIND FACTORS


number % factor == 0


PATTERN 2 — ACCUMULATE THE SUM


sum += factor


Together:


if number % factor == 0:
    sum += factor


This means:


"If the current number is a
factor, add it to the sum."


--------------------------------------------------
WHY DOES sum START AT 0?
--------------------------------------------------

We are adding numbers.


The neutral starting value
for addition is:


0


Example:


0 + 1 = 1

0 + 2 = 2


Therefore:


sum = 0


is the correct starting point.


--------------------------------------------------
WHY DO WE USE number + 1?
--------------------------------------------------

We need to check the number
itself because every positive
number is a factor of itself.


For:


36


36 % 36 = 0


Therefore:


36 is a factor.


Python's `range()` excludes
the stop value.


So we use:


range(1, number + 1)


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Input:


number = 10


Factors:


1
2
5
10


Sum:


1 + 2 + 5 + 10


= 18


Output:


Factor sum = 18


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


Sum:


1 + 2 + 3 + 4 + 6 + 12


= 28


Output:


Factor sum = 28


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

Input:


number = 7


Factors:


1
7


Sum:


1 + 7


= 8


Output:


Factor sum = 8


--------------------------------------------------
EXAMPLE 5
--------------------------------------------------

Input:


number = 1


Factor:


1


Sum:


1


Output:


Factor sum = 1


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


Sum:


1 + 2 + 4 + 8 + 16


= 31


Output:


Factor sum = 31


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

number = 36


Expected:


Factor sum = 91


--------------------------------------------------

TEST CASE 2:

Input:

number = 10


Expected:


Factor sum = 18


--------------------------------------------------

TEST CASE 3:

Input:

number = 12


Expected:


Factor sum = 28


--------------------------------------------------

TEST CASE 4:

Input:

number = 7


Expected:


Factor sum = 8


--------------------------------------------------

TEST CASE 5:

Input:

number = 1


Expected:


Factor sum = 1


--------------------------------------------------

TEST CASE 6:

Input:

number = 16


Expected:


Factor sum = 31


--------------------------------------------------
COMMON MISTAKE 1
--------------------------------------------------

Forgetting to initialize:


sum = 0


Without initialization,
Python does not know the initial
value of `sum`.


Correct:


sum = 0


--------------------------------------------------
COMMON MISTAKE 2
--------------------------------------------------

Using:


sum = 1


This can cause incorrect
results because 1 would be
counted twice when it is found
as a factor.


Correct:


sum = 0


--------------------------------------------------
COMMON MISTAKE 3
--------------------------------------------------

Adding every number.


Wrong:


for factor in range(1, number + 1):
    sum += factor


This adds every number from
1 to `number`.


We only want factors.


Correct:


for factor in range(1, number + 1):
    if number % factor == 0:
        sum += factor


--------------------------------------------------
COMMON MISTAKE 4
--------------------------------------------------

Using the wrong modulo condition.


Wrong:


if factor % number == 0:


Correct:


if number % factor == 0:


We want to know whether
`factor` divides `number`.


--------------------------------------------------
COMMON MISTAKE 5
--------------------------------------------------

Forgetting `number + 1`.


Wrong:


range(1, number)


This excludes the number itself.


Correct:


range(1, number + 1)


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:


"How do you find the sum of all
factors of a number?"


You can say:


"I iterate from 1 through the
given number. For every value,
I check whether it divides the
number exactly using the modulo
operator. If it is a factor, I
add it to a running sum."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Factor


A number that divides another
number exactly.


2. `%`


Returns the remainder.


3. `number % factor == 0`


Checks whether the current
number is a factor.


4. Accumulator


Stores a running result.


5. `sum += factor`


Adds the current factor to
the running total.


6. `for` loop


Checks all possible factors.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

Question:


Find the sum of all factors.


Think:


FIND FACTOR


↓


CHECK:


number % factor == 0


↓


YES


↓


ADD:


sum += factor


↓


REPEAT


Easy pattern:


LOOP → CHECK → ADD → REPEAT


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

Question:

Find the sum of all factors
of 36.


        ↓


number = 36


        ↓


sum = 0


        ↓


Check 1 to 36


        ↓


Is:


36 % factor == 0?


        ↓


YES


        ↓


Add factor to sum


        ↓


Factors:


1, 2, 3, 4, 6, 9, 12, 18, 36


        ↓


Add:


1 + 2 + 3 + 4 + 6 + 9 + 12 + 18 + 36


        ↓


91


        ↓


Print:


Factor sum = 91


--------------------------------------------------
MAIN THING TO REMEMBER
--------------------------------------------------

This question combines
TWO patterns:


FACTOR:


number % factor == 0


ACCUMULATOR:


sum += factor


Together:


for factor in range(1, number + 1):

    if number % factor == 0:
        sum += factor


Remember:


FACTOR → ADD → REPEAT


--------------------------------------------------
IMPORTANT CONNECTION WITH QUESTION 26
--------------------------------------------------

Question 26:


Print all factors.


Pattern:


if number % factor == 0:
    print(factor)


Question 27:


Find sum of all factors.


Pattern:


if number % factor == 0:
    sum += factor


The factor-finding logic
is exactly the same.


The only difference is
what we do when we find
a factor.


Question 26:


FACTOR FOUND → PRINT


Question 27:


FACTOR FOUND → ADD


This is a very important
logic-building pattern.


--------------------------------------------------
IMPORTANT CONNECTION WITH ACCUMULATORS
--------------------------------------------------

You have already seen an
accumulator in Fibonacci sum.


Fibonacci:


total += first


Factor sum:


sum += factor


The idea is exactly the same:


START WITH 0


↓


FIND A VALUE


↓


ADD IT TO TOTAL


↓


REPEAT


This pattern appears
everywhere in DSA.


--------------------------------------------------
OPTIMIZATION NOTE
--------------------------------------------------

The current solution checks
every number from 1 to `number`.


Time complexity:


O(n)


Later, we can optimize factor
finding by checking only up to:


√number


and finding factors in pairs.


For example, for 36:


1 × 36

2 × 18

3 × 12

4 × 9

6 × 6


This allows us to find all
factors much faster.


For beginner logic building,
the current O(n) approach is
excellent because it makes the
factor and accumulator pattern
very clear.


--------------------------------------------------
FINAL MEMORY
--------------------------------------------------

FACTOR SUM:


1 → number


        ↓


number % factor == 0


        ↓


YES


        ↓


sum += factor


        ↓


REPEAT


MAIN PATTERN:


LOOP → CHECK → ADD → REPEAT


MOST IMPORTANT CODE:


sum = 0

for factor in range(1, number + 1):

    if number % factor == 0:
        sum += factor


Then:


print(sum)


Remember:


`number % factor == 0`

→ FACTOR


`sum += factor`

→ ACCUMULATE


FACTOR + ACCUMULATOR

=

SUM OF ALL FACTORS

"""