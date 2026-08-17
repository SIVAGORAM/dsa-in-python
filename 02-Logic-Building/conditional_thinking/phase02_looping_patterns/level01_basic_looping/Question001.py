def main():
    # Question 1: Print numbers from 1 to 10.

    for number in range(1, 10 + 1):
        print(number)


if __name__ == "__main__":
    main()


"""
QUESTION:

Print numbers from 1 to 10.


WHAT DOES THE QUESTION MEAN?

We need to print every number starting from 1
and ending at 10.

Expected output:

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
SOLUTION
--------------------------------------------------

We use a `for` loop:

for number in range(1, 10 + 1):


`range()` generates the numbers that the loop
will process.


--------------------------------------------------
HOW range() WORKS
--------------------------------------------------

Python's range() follows:

range(start, stop)


The important point is:

The START value is included.

The STOP value is excluded.


Example:

range(1, 5)

generates:

1
2
3
4

It does NOT include 5.


--------------------------------------------------
WHY DO WE USE 10 + 1?
--------------------------------------------------

We want:

1 to 10

But the stop value in `range()` is excluded.

Therefore:

range(1, 10)

would produce:

1 2 3 4 5 6 7 8 9


To include 10:

range(1, 10 + 1)


which becomes:

range(1, 11)


So Python generates:

1 2 3 4 5 6 7 8 9 10


--------------------------------------------------
DRY RUN
--------------------------------------------------

Code:

for number in range(1, 10 + 1):
    print(number)


First:

range(1, 11)

produces:

1, 2, 3, 4, 5, 6, 7, 8, 9, 10


ITERATION 1:

number = 1

print(1)


ITERATION 2:

number = 2

print(2)


ITERATION 3:

number = 3

print(3)


ITERATION 4:

number = 4

print(4)


ITERATION 5:

number = 5

print(5)


ITERATION 6:

number = 6

print(6)


ITERATION 7:

number = 7

print(7)


ITERATION 8:

number = 8

print(8)


ITERATION 9:

number = 9

print(9)


ITERATION 10:

number = 10

print(10)


After number = 10, there are no more values
in the range, so the loop stops.


--------------------------------------------------
OUTPUT
--------------------------------------------------

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
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

In Python:

range(1, 11)

means:

Start at 1
Stop before 11


Therefore:

1 through 10


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Print numbers from 1 to 5.

Code:

for number in range(1, 5 + 1):
    print(number)


Output:

1
2
3
4
5


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Print numbers from 5 to 10.

Code:

for number in range(5, 10 + 1):
    print(number)


Output:

5
6
7
8
9
10


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

Using range directly:

for number in range(1, 11):
    print(number)


This is exactly the same as:

for number in range(1, 10 + 1):
    print(number)


Because:

10 + 1 = 11


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Requirement:

Print 1 to 10

Code:

range(1, 11)

Expected:

1 2 3 4 5 6 7 8 9 10


TEST CASE 2:

Requirement:

Print 1 to 5

Code:

range(1, 6)

Expected:

1 2 3 4 5


TEST CASE 3:

Requirement:

Print 5 to 10

Code:

range(5, 11)

Expected:

5 6 7 8 9 10


TEST CASE 4:

Requirement:

Print 1 to 1

Code:

range(1, 2)

Expected:

1


--------------------------------------------------
COMMON MISTAKE
--------------------------------------------------

WRONG:

for number in range(1, 10):
    print(number)


Output:

1
2
3
4
5
6
7
8
9


10 is missing.


CORRECT:

for number in range(1, 11):
    print(number)


or:

for number in range(1, 10 + 1):
    print(number)


--------------------------------------------------
ANOTHER IMPORTANT DIFFERENCE
--------------------------------------------------

In Java/C/C++ you may see:

number++


Python does NOT use:

number++


Instead, Python's `range()` automatically generates
the next number for the loop.


For example:

for number in range(1, 11):


Python gives:

1
2
3
4
...
10


You do not need to manually write:

number += 1


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How does this loop work?"

You can say:

"I use a for loop with range from 1 to 11. Python's range
includes the starting value but excludes the stopping value,
so using 11 allows me to print numbers from 1 through 10."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. `for` loop

Used to repeat a block of code for each value.


2. `range()`

Generates a sequence of numbers.


3. Start value

The first value is included.


4. Stop value

The stop value is excluded.


5. `print()`

Prints the current value.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

Python:

range(start, stop)

means:

START → included

STOP → excluded


Therefore:

Want 1 to 10?

Use:

range(1, 11)


Easy rule:

LAST NUMBER + 1


1 to 10:

range(1, 10 + 1)


1 to 100:

range(1, 100 + 1)


1 to 50:

range(1, 50 + 1)


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

Question:

Print 1 to 10

        ↓

Use for loop

        ↓

range(1, 11)

        ↓

1, 2, 3, ..., 10

        ↓

print each number


MAIN THING TO REMEMBER:

`range()` → START included, STOP excluded.
"""