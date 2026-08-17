def main():
    # Question 19: Print Fibonacci series up to n terms.
    terms = 10
    first = 0
    second = 1

    for count in range(1, terms + 1):
        print(str(first) + " ", end="")

        next = first + second
        first = second
        second = next

    print()


if __name__ == "__main__":
    main()


"""
QUESTION:

Print Fibonacci series up to n terms.


--------------------------------------------------
WHAT DOES THE QUESTION MEAN?
--------------------------------------------------

We are given the number of terms
we want to print.

The Fibonacci series is a sequence
where each number is calculated by
adding the previous two numbers.


The Fibonacci series starts with:


0
1


Then:


0 + 1 = 1

1 + 1 = 2

1 + 2 = 3

2 + 3 = 5

3 + 5 = 8

5 + 8 = 13


Therefore, the Fibonacci series is:


0 1 1 2 3 5 8 13 21 34 ...


If we are asked for 10 terms,
we need to print:


0 1 1 2 3 5 8 13 21 34


--------------------------------------------------
EXPECTED OUTPUT
--------------------------------------------------

0 1 1 2 3 5 8 13 21 34


--------------------------------------------------
SOLUTION
--------------------------------------------------

We use three important variables:


1. `first`

Stores the current Fibonacci number.


2. `second`

Stores the next Fibonacci number.


3. `next`

Stores the sum of the previous
two numbers.


The main formula is:


next = first + second


Then we move the values forward:


first = second

second = next


This allows us to generate
the next Fibonacci number.


--------------------------------------------------
STEP 1 — STORE THE NUMBER OF TERMS
--------------------------------------------------

Code:


terms = 10


This means we want to print
10 Fibonacci numbers.


--------------------------------------------------
STEP 2 — INITIALIZE THE FIRST TWO NUMBERS
--------------------------------------------------

Code:


first = 0

second = 1


The Fibonacci series starts with:


0

1


Therefore:


first = 0

second = 1


--------------------------------------------------
STEP 3 — START THE for LOOP
--------------------------------------------------

Code:


for count in range(1, terms + 1):


Since:


terms = 10


the range becomes:


range(1, 11)


Python's `range()` includes
the starting value but excludes
the stopping value.


Therefore it generates:


1, 2, 3, 4, 5, 6, 7, 8, 9, 10


So the loop runs exactly
10 times.


--------------------------------------------------
STEP 4 — PRINT first
--------------------------------------------------

Code:


print(str(first) + " ", end="")


We print the current value
stored in `first`.


The `end=""` prevents Python
from moving to a new line after
each number.


Therefore all Fibonacci numbers
are printed on the same line.


--------------------------------------------------
STEP 5 — CALCULATE next
--------------------------------------------------

Code:


next = first + second


This calculates the next
Fibonacci number.


Example:


first = 0

second = 1


Then:


next = 0 + 1

next = 1


--------------------------------------------------
STEP 6 — MOVE first FORWARD
--------------------------------------------------

Code:


first = second


The old `second` value becomes
the new `first` value.


For example:


first = 0

second = 1


After:


first = second


we get:


first = 1


--------------------------------------------------
STEP 7 — MOVE second FORWARD
--------------------------------------------------

Code:


second = next


The newly calculated value
becomes the new `second` value.


For example:


next = 1


Therefore:


second = 1


Now the values have moved forward.


--------------------------------------------------
DRY RUN
--------------------------------------------------

Input:


terms = 10


Initial:


first = 0

second = 1


--------------------------------------------------
ITERATION 1
--------------------------------------------------

Print:


first = 0


Output:


0


Calculate:


next = first + second

next = 0 + 1

next = 1


Update:


first = second

first = 1


second = next

second = 1


Now:


first = 1

second = 1


--------------------------------------------------
ITERATION 2
--------------------------------------------------

Print:


first = 1


Output:


0 1


Calculate:


next = 1 + 1

next = 2


Update:


first = 1

second = 2


Now:


first = 1

second = 2


--------------------------------------------------
ITERATION 3
--------------------------------------------------

Print:


first = 1


Output:


0 1 1


Calculate:


next = 1 + 2

next = 3


Update:


first = 2

second = 3


--------------------------------------------------
ITERATION 4
--------------------------------------------------

Print:


first = 2


Output:


0 1 1 2


Calculate:


next = 2 + 3

next = 5


Update:


first = 3

second = 5


--------------------------------------------------
ITERATION 5
--------------------------------------------------

Print:


first = 3


Output:


0 1 1 2 3


Calculate:


next = 3 + 5

next = 8


Update:


first = 5

second = 8


--------------------------------------------------
ITERATION 6
--------------------------------------------------

Print:


first = 5


Output:


0 1 1 2 3 5


Calculate:


next = 5 + 8

next = 13


Update:


first = 8

second = 13


--------------------------------------------------
ITERATION 7
--------------------------------------------------

Print:


first = 8


Output:


0 1 1 2 3 5 8


Calculate:


next = 8 + 13

next = 21


Update:


first = 13

second = 21


--------------------------------------------------
ITERATION 8
--------------------------------------------------

Print:


first = 13


Output:


0 1 1 2 3 5 8 13


Calculate:


next = 13 + 21

next = 34


Update:


first = 21

second = 34


--------------------------------------------------
ITERATION 9
--------------------------------------------------

Print:


first = 21


Output:


0 1 1 2 3 5 8 13 21


Calculate:


next = 21 + 34

next = 55


Update:


first = 34

second = 55


--------------------------------------------------
ITERATION 10
--------------------------------------------------

Print:


first = 34


Output:


0 1 1 2 3 5 8 13 21 34


Calculate:


next = 34 + 55

next = 89


Update:


first = 55

second = 89


The loop has completed
10 iterations.


Therefore, it stops.


--------------------------------------------------
OUTPUT
--------------------------------------------------

0 1 1 2 3 5 8 13 21 34


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

The most important concept
in this problem is:


next = first + second


Every Fibonacci number is
the sum of the previous
two numbers.


For example:


0 + 1 = 1

1 + 1 = 2

1 + 2 = 3

2 + 3 = 5

3 + 5 = 8


--------------------------------------------------
IMPORTANT CONCEPT — VARIABLE UPDATES
--------------------------------------------------

These two lines are very important:


first = second

second = next


They move the Fibonacci values
forward.


Suppose:


first = 3

second = 5

next = 8


After:


first = second


we get:


first = 5


Then:


second = next


we get:


second = 8


Now:


first = 5

second = 8


The next iteration can calculate:


5 + 8 = 13


--------------------------------------------------
WHY DO WE USE end=""?
--------------------------------------------------

Normally:


print(first)


moves to a new line after printing.


For example:


0
1
1
2


But we want the Fibonacci series
on one line:


0 1 1 2


So we use:


print(first, end=" ")


or in your code:


print(str(first) + " ", end="")


The:


end=""


prevents `print()` from
adding a newline.


The final:


print()


moves the cursor to the
next line after the series
is complete.


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Input:


terms = 5


Fibonacci terms:


0

1

1

2

3


Output:


0 1 1 2 3


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Input:


terms = 7


Fibonacci terms:


0

1

1

2

3

5

8


Output:


0 1 1 2 3 5 8


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

Input:


terms = 1


We only need one term.


The first term is:


0


Output:


0


--------------------------------------------------
EXAMPLE 5
--------------------------------------------------

Input:


terms = 2


The first two terms are:


0

1


Output:


0 1


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

terms = 10


Expected:

0 1 1 2 3 5 8 13 21 34


--------------------------------------------------

TEST CASE 2:

Input:

terms = 5


Expected:

0 1 1 2 3


--------------------------------------------------

TEST CASE 3:

Input:

terms = 7


Expected:

0 1 1 2 3 5 8


--------------------------------------------------

TEST CASE 4:

Input:

terms = 1


Expected:

0


--------------------------------------------------

TEST CASE 5:

Input:

terms = 2


Expected:

0 1


--------------------------------------------------
COMMON MISTAKE 1
--------------------------------------------------

Forgetting to update the variables.


If we only write:


next = first + second


without:


first = second

second = next


the same values will continue
to be used.


The Fibonacci sequence
would not progress correctly.


--------------------------------------------------
COMMON MISTAKE 2
--------------------------------------------------

Updating the variables in
the wrong order.


These lines:


first = second

second = next


must use the already calculated
`next` value.


The correct sequence is:


1. Calculate `next`.

2. Move `first`.

3. Move `second`.


--------------------------------------------------
COMMON MISTAKE 3
--------------------------------------------------

Using the wrong starting values.


The standard Fibonacci sequence
starts with:


first = 0

second = 1


--------------------------------------------------
COMMON MISTAKE 4
--------------------------------------------------

Using:


range(1, terms)


instead of:


range(1, terms + 1)


For:


terms = 10


`range(1, 10)` produces only:


1 through 9


So only 9 iterations occur.


Correct:


range(1, 10 + 1)


produces:


1 through 10


--------------------------------------------------
COMMON MISTAKE 5
--------------------------------------------------

Forgetting `end=""`.


If we write:


print(first)


each Fibonacci number appears
on a separate line.


If the requirement is to print
the series on one line, use:


print(first, end=" ")


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:


"How do you generate the Fibonacci
series?"


You can say:


"I initialize the first two Fibonacci
numbers as 0 and 1. In every iteration,
I calculate the next number by adding
the previous two numbers. Then I shift
the values forward and repeat this
process for the required number of terms."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Fibonacci series


Each number is the sum of
the previous two numbers.


2. `first`


Stores the current number.


3. `second`


Stores the next number.


4. `next`


Stores the sum of `first`
and `second`.


5. `for` loop


Controls the number of terms.


6. `range()`


Generates the required
number of iterations.


7. `end=""`


Keeps the output on the
same line.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

For Fibonacci:


START:


0, 1


Then:


ADD


0 + 1 = 1


Then:


ADD


1 + 1 = 2


Then:


ADD


1 + 2 = 3


Then:


ADD


2 + 3 = 5


Then:


ADD


3 + 5 = 8


Easy pattern:


FIRST + SECOND = NEXT


Then:


FIRST = SECOND

SECOND = NEXT


Repeat.


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

Question:

Print Fibonacci series
up to 10 terms.


        ↓


Start:


first = 0

second = 1


        ↓


Print first


        ↓


Calculate:


next = first + second


        ↓


Move values:


first = second

second = next


        ↓


Repeat 10 times


        ↓


0 1 1 2 3 5 8 13 21 34


--------------------------------------------------
MAIN THING TO REMEMBER
--------------------------------------------------

The Fibonacci series follows:


NEXT = FIRST + SECOND


After calculating the next number,
move the variables forward:


first = second

second = next


For example:


first = 3

second = 5


NEXT:


3 + 5 = 8


Then:


first = 5

second = 8


Next:


5 + 8 = 13


MOST IMPORTANT PATTERN:


next = first + second

first = second

second = next


MEMORY:


ADD → SHIFT → REPEAT


The standard Fibonacci sequence:


0 1 1 2 3 5 8 13 21 34 ...
"""