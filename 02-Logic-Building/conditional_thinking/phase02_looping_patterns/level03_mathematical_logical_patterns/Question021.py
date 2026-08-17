def main():
    # Question 21: Print the squares of numbers from 1 to n.
    n = 5

    for number in range(1, n + 1):
        print(number * number)


if __name__ == "__main__":
    main()


"""
QUESTION:

Print the squares of numbers from 1 to n.


--------------------------------------------------
WHAT DOES THE QUESTION MEAN?
--------------------------------------------------

We are given a number `n`.

We need to print the square of every
number starting from 1 up to `n`.


For example:

n = 5


Numbers are:

1
2
3
4
5


Now calculate their squares:


1 × 1 = 1

2 × 2 = 4

3 × 3 = 9

4 × 4 = 16

5 × 5 = 25


Therefore:


1
4
9
16
25


--------------------------------------------------
EXPECTED OUTPUT
--------------------------------------------------

1
4
9
16
25


--------------------------------------------------
SOLUTION
--------------------------------------------------

We use a `for` loop:


for number in range(1, n + 1):


The loop generates numbers
from 1 to `n`.


For each number:


number * number


calculates its square.


--------------------------------------------------
WHAT IS A SQUARE?
--------------------------------------------------

The square of a number means
multiplying the number by itself.


Examples:


1² = 1 × 1 = 1

2² = 2 × 2 = 4

3² = 3 × 3 = 9

4² = 4 × 4 = 16

5² = 5 × 5 = 25


In Python:


number * number


is used to calculate the square.


You can also use:


number ** 2


Both produce the same result.


Example:


5 * 5 = 25


and:


5 ** 2 = 25


--------------------------------------------------
STEP 1 — STORE n
--------------------------------------------------

Code:


n = 5


This means we need to print
the squares from 1 through 5.


--------------------------------------------------
STEP 2 — CREATE THE for LOOP
--------------------------------------------------

Code:


for number in range(1, n + 1):


Since:


n = 5


the range becomes:


range(1, 6)


Python's `range()` includes
the start value but excludes
the stop value.


Therefore it generates:


1, 2, 3, 4, 5


--------------------------------------------------
STEP 3 — CALCULATE THE SQUARE
--------------------------------------------------

Code:


number * number


For example:


number = 3


Then:


3 * 3


= 9


--------------------------------------------------
STEP 4 — PRINT THE RESULT
--------------------------------------------------

Code:


print(number * number)


The calculated square is
printed immediately.


--------------------------------------------------
DRY RUN
--------------------------------------------------

Input:


n = 5


The loop becomes:


range(1, 6)


Values:


1, 2, 3, 4, 5


--------------------------------------------------
ITERATION 1
--------------------------------------------------

number = 1


Calculate:


1 * 1 = 1


Print:


1


--------------------------------------------------
ITERATION 2
--------------------------------------------------

number = 2


Calculate:


2 * 2 = 4


Print:


4


--------------------------------------------------
ITERATION 3
--------------------------------------------------

number = 3


Calculate:


3 * 3 = 9


Print:


9


--------------------------------------------------
ITERATION 4
--------------------------------------------------

number = 4


Calculate:


4 * 4 = 16


Print:


16


--------------------------------------------------
ITERATION 5
--------------------------------------------------

number = 5


Calculate:


5 * 5 = 25


Print:


25


The loop has now completed
5 iterations.


--------------------------------------------------
OUTPUT
--------------------------------------------------

1
4
9
16
25


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

The main concept in this problem
is:


number * number


This calculates the square
of the current number.


Another way is:


number ** 2


Example:


5 * 5 = 25


or:


5 ** 2 = 25


Both are correct.


--------------------------------------------------
WHY DO WE USE n + 1?
--------------------------------------------------

We want numbers from:


1 to n


But Python's `range()` excludes
the stop value.


For:


n = 5


If we write:


range(1, 5)


we get:


1, 2, 3, 4


5 is missing.


Therefore we use:


range(1, 5 + 1)


which becomes:


range(1, 6)


Now we get:


1, 2, 3, 4, 5


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Input:


n = 3


Numbers:


1
2
3


Squares:


1 × 1 = 1

2 × 2 = 4

3 × 3 = 9


Output:


1
4
9


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Input:


n = 10


Squares:


1
4
9
16
25
36
49
64
81
100


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

Input:


n = 1


Only one number:


1


Square:


1 × 1 = 1


Output:


1


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

n = 5


Expected:

1
4
9
16
25


--------------------------------------------------

TEST CASE 2:

Input:

n = 3


Expected:

1
4
9


--------------------------------------------------

TEST CASE 3:

Input:

n = 1


Expected:

1


--------------------------------------------------

TEST CASE 4:

Input:

n = 10


Expected:

1
4
9
16
25
36
49
64
81
100


--------------------------------------------------

TEST CASE 5:

Input:

n = 0


Expected:

No output


Because:


range(1, 0 + 1)


becomes:


range(1, 1)


which contains no values.


--------------------------------------------------
COMMON MISTAKE 1
--------------------------------------------------

Forgetting `+ 1`.


Wrong:


for number in range(1, n):


For:


n = 5


this produces:


1, 2, 3, 4


5 is missing.


Correct:


for number in range(1, n + 1):


--------------------------------------------------
COMMON MISTAKE 2
--------------------------------------------------

Using addition instead of multiplication.


Wrong:


print(number + number)


For:


5:


5 + 5 = 10


But the square is:


5 × 5 = 25


Correct:


print(number * number)


--------------------------------------------------
COMMON MISTAKE 3
--------------------------------------------------

Using the wrong exponent.


For square:


number ** 2


not:


number ** 3


Because:


** 2 → square


** 3 → cube


--------------------------------------------------
COMMON MISTAKE 4
--------------------------------------------------

Thinking that `number * number`
changes the original variable.


For:


number = 5


This:


number * number


only calculates:


25


It does not change:


number


`number` is still:


5


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:


"How do you print the squares
from 1 to n?"


You can say:


"I use a for loop from 1 through n.
For each number, I multiply it by
itself and print the result."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. `for` loop


Used to process every number
from 1 to n.


2. `range()`


Generates the numbers.


3. `n + 1`


Allows `n` to be included.


4. `number * number`


Calculates the square.


5. `** 2`


Another way to calculate
the square.


6. `print()`


Displays the result.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

Question:


Print squares from 1 to n.


Think:


START 1


↓


GO TO n


↓


MULTIPLY NUMBER BY ITSELF


↓


PRINT


Easy pattern:


number × number = square


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

Question:

Print squares from 1 to 5.


        ↓


n = 5


        ↓


range(1, 6)


        ↓


1, 2, 3, 4, 5


        ↓


Square each number


        ↓


1 × 1 = 1


2 × 2 = 4


3 × 3 = 9


4 × 4 = 16


5 × 5 = 25


        ↓


Print:


1
4
9
16
25


--------------------------------------------------
MAIN THING TO REMEMBER
--------------------------------------------------

To print squares from 1 to n:


for number in range(1, n + 1):
    print(number * number)


You can also write:


for number in range(1, n + 1):
    print(number ** 2)


Remember:


range(1, n + 1)


→ 1 THROUGH n


and:


number * number


→ SQUARE


MEMORY:


LOOP → SQUARE → PRINT
"""