def main():
    # Question 5: Print the table of a given number (n x 1 to n x 10).

    n = 7

    for multiplier in range(1, 10 + 1):
        print(str(n) + " x " + str(multiplier) + " = " + str(n * multiplier))


if __name__ == "__main__":
    main()


"""
QUESTION:

Print the multiplication table of a given number
from n × 1 to n × 10.


WHAT DOES THE QUESTION MEAN?

If the given number is:

n = 7

We need to print:

7 × 1 = 7
7 × 2 = 14
7 × 3 = 21
...
7 × 10 = 70


--------------------------------------------------
SOLUTION LOGIC
--------------------------------------------------

We have two things:

n
    ↓
The number whose table we want.

multiplier
    ↓
The numbers 1 to 10.


We use:

for multiplier in range(1, 10 + 1):


This gives:

1
2
3
4
5
6
7
8
9
10


For every multiplier, calculate:

n * multiplier


Then print the result.


--------------------------------------------------
DRY RUN
--------------------------------------------------

Given:

n = 7


ITERATION 1:

multiplier = 1

7 * 1 = 7

Output:

7 x 1 = 7


ITERATION 2:

multiplier = 2

7 * 2 = 14

Output:

7 x 2 = 14


ITERATION 3:

multiplier = 3

7 * 3 = 21

Output:

7 x 3 = 21


ITERATION 4:

multiplier = 4

7 * 4 = 28

Output:

7 x 4 = 28


ITERATION 5:

multiplier = 5

7 * 5 = 35

Output:

7 x 5 = 35


ITERATION 6:

multiplier = 6

7 * 6 = 42

Output:

7 x 6 = 42


ITERATION 7:

multiplier = 7

7 * 7 = 49

Output:

7 x 7 = 49


ITERATION 8:

multiplier = 8

7 * 8 = 56

Output:

7 x 8 = 56


ITERATION 9:

multiplier = 9

7 * 9 = 63

Output:

7 x 9 = 63


ITERATION 10:

multiplier = 10

7 * 10 = 70

Output:

7 x 10 = 70


--------------------------------------------------
DRY RUN TABLE
--------------------------------------------------

| n | multiplier | n * multiplier | Output |
|---:|---:|---:|---|
| 7 | 1 | 7 | 7 x 1 = 7 |
| 7 | 2 | 14 | 7 x 2 = 14 |
| 7 | 3 | 21 | 7 x 3 = 21 |
| 7 | 4 | 28 | 7 x 4 = 28 |
| 7 | 5 | 35 | 7 x 5 = 35 |
| 7 | 6 | 42 | 7 x 6 = 42 |
| 7 | 7 | 49 | 7 x 7 = 49 |
| 7 | 8 | 56 | 7 x 8 = 56 |
| 7 | 9 | 63 | 7 x 9 = 63 |
| 7 | 10 | 70 | 7 x 10 = 70 |


--------------------------------------------------
OUTPUT
--------------------------------------------------

7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70


--------------------------------------------------
HOW range() WORKS
--------------------------------------------------

We use:

range(1, 10 + 1)


First calculate:

10 + 1 = 11


So this becomes:

range(1, 11)


Python includes the starting value:

1


but excludes the stopping value:

11


Therefore:

1
2
3
4
5
6
7
8
9
10


--------------------------------------------------
WHY DO WE NEED 10 + 1?
--------------------------------------------------

If we write:

range(1, 10)


Python produces:

1
2
3
4
5
6
7
8
9


It does NOT include 10.


Since we need the table up to:

n × 10


we use:

range(1, 11)


or:

range(1, 10 + 1)


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Suppose:

n = 5


The loop produces:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Suppose:

n = 10


Output:

10 x 1 = 10
10 x 2 = 20
10 x 3 = 30
10 x 4 = 40
10 x 5 = 50
10 x 6 = 60
10 x 7 = 70
10 x 8 = 80
10 x 9 = 90
10 x 10 = 100


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

Suppose:

n = 12


Output:

12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
12 x 5 = 60
12 x 6 = 72
12 x 7 = 84
12 x 8 = 96
12 x 9 = 108
12 x 10 = 120


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

n = 7

Expected:

7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70


TEST CASE 2:

Input:

n = 5

Expected:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50


TEST CASE 3:

Input:

n = 10

Expected:

10 x 1 = 10
...
10 x 10 = 100


TEST CASE 4:

Input:

n = 0

Expected:

0 x 1 = 0
0 x 2 = 0
...
0 x 10 = 0


TEST CASE 5:

Input:

n = -5

Expected:

-5 x 1 = -5
-5 x 2 = -10
...
-5 x 10 = -50


--------------------------------------------------
IMPORTANT CONCEPT
--------------------------------------------------

The variable `n` does NOT change.

For:

n = 7


it stays:

7


The variable that changes is:

multiplier


It goes:

1 → 2 → 3 → ... → 10


Then we calculate:

n * multiplier


So:

7 * 1
7 * 2
7 * 3
...
7 * 10


--------------------------------------------------
WHY USE A LOOP?
--------------------------------------------------

Without a loop, we would have to write:

print(7 * 1)
print(7 * 2)
print(7 * 3)
print(7 * 4)
...
print(7 * 10)


That would be repetitive.


A loop allows us to write the logic once:

for multiplier in range(1, 11):
    print(n * multiplier)


The loop handles the repetition.


--------------------------------------------------
PYTHON STRING CONVERSION
--------------------------------------------------

Your original code uses:

str()


For example:

str(n)


converts the number into a string.

If:

n = 7


then:

str(n)

becomes:

"7"


Similarly:

str(multiplier)


converts:

1

into:

"1"


This allows us to combine the values with text.


--------------------------------------------------
SIMPLER PYTHON VERSION
--------------------------------------------------

Your current code is correct.

However, Python has f-strings, which make this
kind of output easier to read:

for multiplier in range(1, 11):
    print(f"{n} x {multiplier} = {n * multiplier}")


For example:

n = 7
multiplier = 3


Output:

7 x 3 = 21


For now, your original approach is completely fine
for understanding string conversion and loops.


--------------------------------------------------
IMPORTANT PYTHON CORRECTION
--------------------------------------------------

Your original explanation says:

"multiplier++"


Python does NOT use:

multiplier++


Instead:

range(1, 11)


automatically gives:

1
2
3
4
...
10


You don't manually increment the variable.


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How did you solve this?"

You can say:

"I store the given number in `n` and use a for loop to
iterate the multiplier from 1 through 10. For each
iteration, I multiply `n` by the current multiplier
and print the result."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. for loop

Used to repeat the multiplication.


2. range()

Generates multipliers from 1 to 10.


3. Multiplication

The actual table calculation:

n * multiplier


4. str()

Converts numbers to strings when using string
concatenation.


5. Loop variable

`multiplier` changes during each iteration.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

Table of n:

n × 1
n × 2
n × 3
n × 4
...
n × 10


Think:

FIXED NUMBER
     ↓
     n

CHANGING NUMBER
     ↓
     multiplier

CALCULATION
     ↓
n × multiplier


--------------------------------------------------
YOUR CODE STRUCTURE
--------------------------------------------------

n = 7
    ↓
for multiplier from 1 to 10
    ↓
calculate n * multiplier
    ↓
print result
    ↓
next multiplier
    ↓
repeat until 10


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

n = 7

        ↓

multiplier = 1
        ↓
7 × 1 = 7

multiplier = 2
        ↓
7 × 2 = 14

multiplier = 3
        ↓
7 × 3 = 21

...

multiplier = 10
        ↓
7 × 10 = 70


MAIN THINGS TO REMEMBER:

1. `n` is the fixed number.
2. `multiplier` goes from 1 to 10.
3. Calculate `n * multiplier`.
4. `range(1, 11)` includes 1 through 10.
5. Python does not use `multiplier++`.
"""