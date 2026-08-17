def main():
    # Question 20: Print the sum of first n terms of Fibonacci series.
    terms = 10
    first = 0
    second = 1
    total = 0

    for count in range(1, terms + 1):
        total += first

        next = first + second
        first = second
        second = next

    print("Sum of Fibonacci series = " + str(total))


if __name__ == "__main__":
    main()


"""
QUESTION:

Print the sum of first n terms of Fibonacci series.


--------------------------------------------------
WHAT DOES THE QUESTION MEAN?
--------------------------------------------------

We are given the number of Fibonacci
terms we need to consider.

We need to generate the first `n`
Fibonacci numbers and calculate
their total sum.


Example:

terms = 10


The first 10 Fibonacci terms are:


0
1
1
2
3
5
8
13
21
34


Now add them:


0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34


= 88


Therefore:


Sum = 88


--------------------------------------------------
EXPECTED OUTPUT
--------------------------------------------------

Sum of Fibonacci series = 88


--------------------------------------------------
IMPORTANT CORRECTION
--------------------------------------------------

The original code was printing
the Fibonacci series, but it was
NOT calculating the sum.


The original code had:


print(str(first) + " ", end="")


This prints every Fibonacci number.


But the question asks for:


SUM of the first n Fibonacci terms.


Therefore, we need an additional
variable:


total = 0


Then, in every iteration:


total += first


This adds the current Fibonacci
number to the total.


--------------------------------------------------
SOLUTION
--------------------------------------------------

We use:


1. `first`

Stores the current Fibonacci number.


2. `second`

Stores the next Fibonacci number.


3. `next`

Calculates the next Fibonacci number.


4. `total`

Stores the sum of all Fibonacci
numbers processed so far.


The main logic is:


total += first


Then we generate the next
Fibonacci number:


next = first + second


And move the values forward:


first = second

second = next


--------------------------------------------------
STEP 1 — STORE NUMBER OF TERMS
--------------------------------------------------

Code:


terms = 10


This means we need to process
10 Fibonacci terms.


--------------------------------------------------
STEP 2 — INITIALIZE FIBONACCI VALUES
--------------------------------------------------

Code:


first = 0

second = 1


The Fibonacci series starts with:


0, 1


Therefore:


first = 0

second = 1


--------------------------------------------------
STEP 3 — CREATE total
--------------------------------------------------

Code:


total = 0


This variable stores the
running sum.


Initially:


total = 0


As each Fibonacci number is
processed, it is added to `total`.


--------------------------------------------------
STEP 4 — START THE LOOP
--------------------------------------------------

Code:


for count in range(1, terms + 1):


Since:


terms = 10


we get:


range(1, 11)


which generates:


1, 2, 3, 4, 5, 6, 7, 8, 9, 10


Therefore, the loop runs
10 times.


--------------------------------------------------
STEP 5 — ADD CURRENT NUMBER
--------------------------------------------------

Code:


total += first


This means:


total = total + first


The current Fibonacci number
is added to the running total.


For the first iteration:


first = 0


Therefore:


total = 0 + 0

total = 0


--------------------------------------------------
STEP 6 — CALCULATE NEXT NUMBER
--------------------------------------------------

Code:


next = first + second


This follows the Fibonacci rule:


NEXT = FIRST + SECOND


For example:


first = 0

second = 1


Therefore:


next = 0 + 1

next = 1


--------------------------------------------------
STEP 7 — MOVE THE VALUES FORWARD
--------------------------------------------------

Code:


first = second

second = next


This moves the Fibonacci sequence
to the next pair of numbers.


For example:


Before:


first = 0

second = 1

next = 1


After:


first = 1

second = 1


The next Fibonacci number
can now be calculated.


--------------------------------------------------
DRY RUN
--------------------------------------------------

Input:


terms = 10


Initial values:


first = 0

second = 1

total = 0


--------------------------------------------------
ITERATION 1
--------------------------------------------------

Current:


first = 0


Add to total:


total = 0 + 0

total = 0


Calculate next:


next = 0 + 1

next = 1


Update:


first = 1

second = 1


--------------------------------------------------
ITERATION 2
--------------------------------------------------

Current:


first = 1


Add:


total = 0 + 1

total = 1


Calculate:


next = 1 + 1

next = 2


Update:


first = 1

second = 2


--------------------------------------------------
ITERATION 3
--------------------------------------------------

Current:


first = 1


Add:


total = 1 + 1

total = 2


Calculate:


next = 1 + 2

next = 3


Update:


first = 2

second = 3


--------------------------------------------------
ITERATION 4
--------------------------------------------------

Current:


first = 2


Add:


total = 2 + 2

total = 4


Calculate:


next = 2 + 3

next = 5


Update:


first = 3

second = 5


--------------------------------------------------
ITERATION 5
--------------------------------------------------

Current:


first = 3


Add:


total = 4 + 3

total = 7


Calculate:


next = 3 + 5

next = 8


Update:


first = 5

second = 8


--------------------------------------------------
ITERATION 6
--------------------------------------------------

Current:


first = 5


Add:


total = 7 + 5

total = 12


Calculate:


next = 5 + 8

next = 13


Update:


first = 8

second = 13


--------------------------------------------------
ITERATION 7
--------------------------------------------------

Current:


first = 8


Add:


total = 12 + 8

total = 20


Calculate:


next = 8 + 13

next = 21


Update:


first = 13

second = 21


--------------------------------------------------
ITERATION 8
--------------------------------------------------

Current:


first = 13


Add:


total = 20 + 13

total = 33


Calculate:


next = 13 + 21

next = 34


Update:


first = 21

second = 34


--------------------------------------------------
ITERATION 9
--------------------------------------------------

Current:


first = 21


Add:


total = 33 + 21

total = 54


Calculate:


next = 21 + 34

next = 55


Update:


first = 34

second = 55


--------------------------------------------------
ITERATION 10
--------------------------------------------------

Current:


first = 34


Add:


total = 54 + 34

total = 88


Calculate:


next = 34 + 55

next = 89


Update:


first = 55

second = 89


The loop has completed
10 iterations.


--------------------------------------------------
FINAL VALUE
--------------------------------------------------

The first 10 Fibonacci terms are:


0 1 1 2 3 5 8 13 21 34


Their sum is:


0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34


= 88


Therefore:


total = 88


--------------------------------------------------
OUTPUT
--------------------------------------------------

Sum of Fibonacci series = 88


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

The most important new concept
in this question is:


total += first


This is called an accumulator.


It keeps adding values
to a running total.


Example:


total = 0


Add 5:


total = 0 + 5

total = 5


Add 8:


total = 5 + 8

total = 13


Add 13:


total = 13 + 13

total = 26


Therefore:


`total` remembers the
sum calculated so far.


--------------------------------------------------
IMPORTANT FIBONACCI CONCEPT
--------------------------------------------------

The Fibonacci sequence follows:


NEXT = FIRST + SECOND


Then:


FIRST = SECOND

SECOND = NEXT


So the complete pattern is:


next = first + second

first = second

second = next


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Input:


terms = 5


First 5 Fibonacci terms:


0 1 1 2 3


Calculate:


0 + 1 + 1 + 2 + 3


= 7


Output:


Sum of Fibonacci series = 7


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Input:


terms = 7


First 7 Fibonacci terms:


0 1 1 2 3 5 8


Calculate:


0 + 1 + 1 + 2 + 3 + 5 + 8


= 20


Output:


Sum of Fibonacci series = 20


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

Input:


terms = 2


First 2 terms:


0 1


Sum:


0 + 1 = 1


Output:


Sum of Fibonacci series = 1


--------------------------------------------------
EXAMPLE 5
--------------------------------------------------

Input:


terms = 1


First term:


0


Sum:


0


Output:


Sum of Fibonacci series = 0


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

terms = 10


Expected:

Sum of Fibonacci series = 88


--------------------------------------------------

TEST CASE 2:

Input:

terms = 5


Expected:

Sum of Fibonacci series = 7


--------------------------------------------------

TEST CASE 3:

Input:

terms = 7


Expected:

Sum of Fibonacci series = 20


--------------------------------------------------

TEST CASE 4:

Input:

terms = 2


Expected:

Sum of Fibonacci series = 1


--------------------------------------------------

TEST CASE 5:

Input:

terms = 1


Expected:

Sum of Fibonacci series = 0


--------------------------------------------------
COMMON MISTAKE 1
--------------------------------------------------

Only printing the Fibonacci numbers.


For example:


print(first)


This generates the series,
but it does not calculate
the sum.


We need:


total += first


--------------------------------------------------
COMMON MISTAKE 2
--------------------------------------------------

Forgetting to initialize:


total = 0


The accumulator must have
an initial value.


--------------------------------------------------
COMMON MISTAKE 3
--------------------------------------------------

Adding `next` instead of `first`.


We want to add the Fibonacci
term currently being processed:


total += first


The `next` value is the
following Fibonacci number.


--------------------------------------------------
COMMON MISTAKE 4
--------------------------------------------------

Updating Fibonacci variables
before adding the current term.


The clean order is:


1. Add current `first`
   to `total`.

2. Calculate `next`.

3. Update `first`.

4. Update `second`.


--------------------------------------------------
COMMON MISTAKE 5
--------------------------------------------------

Using:


range(1, terms)


instead of:


range(1, terms + 1)


For:


terms = 10


`range(1, 10)` gives only
9 iterations.


Correct:


range(1, 11)


gives 10 iterations.


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:


"How do you find the sum of the
first n Fibonacci numbers?"


You can say:


"I initialize the Fibonacci sequence
with 0 and 1 and maintain a running
sum. In each iteration, I add the
current Fibonacci number to the sum,
then calculate the next Fibonacci
number by adding the previous two
numbers. I repeat this for n terms."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Fibonacci series


Each number is the sum of
the previous two numbers.


2. `total`


Stores the running sum.


3. `total += first`


Adds the current Fibonacci
number to the total.


4. `first`


Stores the current term.


5. `second`


Stores the next term.


6. `next`


Stores the newly calculated term.


7. `for` loop


Controls the number of terms.


8. `range()`


Generates the required iterations.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

For Fibonacci:


FIRST + SECOND = NEXT


Then:


FIRST = SECOND

SECOND = NEXT


For the sum:


TOTAL = TOTAL + FIRST


So remember:


ADD → CALCULATE → SHIFT → REPEAT


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

Question:

Find the sum of the first
10 Fibonacci terms.


        ↓


Start:


first = 0

second = 1

total = 0


        ↓


Add first:


total = 0


        ↓


Calculate next:


0 + 1 = 1


        ↓


Shift:


first = 1

second = 1


        ↓


Repeat for 10 terms


        ↓


Fibonacci terms:


0 1 1 2 3 5 8 13 21 34


        ↓


Add:


0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34


        ↓


88


        ↓


Print:


Sum of Fibonacci series = 88


--------------------------------------------------
MAIN THING TO REMEMBER
--------------------------------------------------

This question combines
two important patterns:


FIBONACCI:


next = first + second

first = second

second = next


SUM:


total += first


Therefore:


ADD CURRENT TERM

↓

CALCULATE NEXT TERM

↓

SHIFT VALUES

↓

REPEAT


MOST IMPORTANT CODE:


total = 0

for count in range(1, terms + 1):

    total += first

    next = first + second
    first = second
    second = next


The final:


total


contains the sum of the first
`terms` Fibonacci numbers.


MEMORY:


FIBONACCI + ACCUMULATOR

=

GENERATE → ADD → SHIFT → REPEAT
"""