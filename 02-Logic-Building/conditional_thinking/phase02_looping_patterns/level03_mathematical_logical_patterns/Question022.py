def main():
    # Question 22: Print cubes of numbers from 1 to n.
    n = 5

    for number in range(1, n + 1):
        print(number * number * number)


if __name__ == "__main__":
    main()


"""
QUESTION:

Print cubes of numbers from 1 to n.


--------------------------------------------------
WHAT DOES THE QUESTION MEAN?
--------------------------------------------------

We are given a number `n`.

We need to print the cube of every
number starting from 1 up to `n`.


For example:

n = 5


Numbers are:

1
2
3
4
5


Now calculate their cubes:


1 × 1 × 1 = 1

2 × 2 × 2 = 8

3 × 3 × 3 = 27

4 × 4 × 4 = 64

5 × 5 × 5 = 125


Therefore:


1
8
27
64
125


--------------------------------------------------
EXPECTED OUTPUT
--------------------------------------------------

1
8
27
64
125


--------------------------------------------------
SOLUTION
--------------------------------------------------

We use a `for` loop:


for number in range(1, n + 1):


The loop generates numbers
from 1 to `n`.


For each number, we calculate
its cube using:


number * number * number


--------------------------------------------------
WHAT IS A CUBE?
--------------------------------------------------

The cube of a number means
multiplying the number by itself
three times.


Examples:


1³ = 1 × 1 × 1 = 1

2³ = 2 × 2 × 2 = 8

3³ = 3 × 3 × 3 = 27

4³ = 4 × 4 × 4 = 64

5³ = 5 × 5 × 5 = 125


In Python, we can calculate
a cube in two ways:


number * number * number


or:


number ** 3


Both produce the same result.


Example:


5 * 5 * 5 = 125


and:


5 ** 3 = 125


--------------------------------------------------
STEP 1 — STORE n
--------------------------------------------------

Code:


n = 5


This means we need to print
the cubes from 1 through 5.


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
STEP 3 — CALCULATE THE CUBE
--------------------------------------------------

Code:


number * number * number


For example:


number = 3


Then:


3 * 3 * 3


= 27


--------------------------------------------------
STEP 4 — PRINT THE RESULT
--------------------------------------------------

Code:


print(number * number * number)


The calculated cube is
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


1 × 1 × 1 = 1


Print:


1


--------------------------------------------------
ITERATION 2
--------------------------------------------------

number = 2


Calculate:


2 × 2 × 2 = 8


Print:


8


--------------------------------------------------
ITERATION 3
--------------------------------------------------

number = 3


Calculate:


3 × 3 × 3 = 27


Print:


27


--------------------------------------------------
ITERATION 4
--------------------------------------------------

number = 4


Calculate:


4 × 4 × 4 = 64


Print:


64


--------------------------------------------------
ITERATION 5
--------------------------------------------------

number = 5


Calculate:


5 × 5 × 5 = 125


Print:


125


The loop has completed
5 iterations.


--------------------------------------------------
OUTPUT
--------------------------------------------------

1
8
27
64
125


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

The main concept in this problem
is:


number * number * number


This calculates the cube
of the current number.


Another way is:


number ** 3


Example:


5 * 5 * 5 = 125


or:


5 ** 3 = 125


Both are correct.


--------------------------------------------------
SQUARE VS CUBE
--------------------------------------------------

Square means:


number × number


or:


number ** 2


Cube means:


number × number × number


or:


number ** 3


Example:


5² = 25


5³ = 125


Remember:


** 2 → SQUARE


** 3 → CUBE


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


Cubes:


1 × 1 × 1 = 1

2 × 2 × 2 = 8

3 × 3 × 3 = 27


Output:


1
8
27


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Input:


n = 10


Cubes:


1
8
27
64
125
216
343
512
729
1000


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

Input:


n = 1


Only one number:


1


Cube:


1 × 1 × 1 = 1


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
8
27
64
125


--------------------------------------------------

TEST CASE 2:

Input:

n = 3


Expected:

1
8
27


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
8
27
64
125
216
343
512
729
1000


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

Calculating the square instead
of the cube.


Wrong:


print(number * number)


This calculates:


number²


Correct:


print(number * number * number)


This calculates:


number³


--------------------------------------------------
COMMON MISTAKE 3
--------------------------------------------------

Using the wrong exponent.


For cube:


number ** 3


not:


number ** 2


Remember:


** 2 → square


** 3 → cube


--------------------------------------------------
COMMON MISTAKE 4
--------------------------------------------------

Using addition instead of multiplication.


Wrong:


number + number + number


For:


5:


5 + 5 + 5 = 15


But:


5³ = 125


Correct:


number * number * number


--------------------------------------------------
COMMON MISTAKE 5
--------------------------------------------------

Thinking that:


number * number * number


changes the original variable.


For:


number = 5


This expression calculates:


125


But `number` is still:


5


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:


"How do you print the cubes
from 1 to n?"


You can say:


"I use a for loop from 1 through n.
For each number, I multiply it by
itself three times, or equivalently
raise it to the power of 3, and
print the result."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. `for` loop


Used to process every number
from 1 to n.


2. `range()`


Generates the numbers.


3. `n + 1`


Allows n to be included.


4. `number * number * number`


Calculates the cube.


5. `number ** 3`


Another way to calculate
the cube.


6. `print()`


Displays the result.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

Question:


Print cubes from 1 to n.


Think:


START 1


↓


GO TO n


↓


MULTIPLY NUMBER THREE TIMES


↓


PRINT


Easy pattern:


number × number × number = cube


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

Question:

Print cubes from 1 to 5.


        ↓


n = 5


        ↓


range(1, 6)


        ↓


1, 2, 3, 4, 5


        ↓


Cube each number


        ↓


1 × 1 × 1 = 1


2 × 2 × 2 = 8


3 × 3 × 3 = 27


4 × 4 × 4 = 64


5 × 5 × 5 = 125


        ↓


Print:


1
8
27
64
125


--------------------------------------------------
MAIN THING TO REMEMBER
--------------------------------------------------

To print cubes from 1 to n:


for number in range(1, n + 1):
    print(number * number * number)


You can also write:


for number in range(1, n + 1):
    print(number ** 3)


Remember:


range(1, n + 1)


→ 1 THROUGH n


and:


number ** 3


→ CUBE


MEMORY:


LOOP → CUBE → PRINT
"""