def main():
    # Question 4: Print numbers from 10 down to 1.

    for number in range(10, 1 - 1, -1):
        print(number)


if __name__ == "__main__":
    main()


"""
QUESTION:

Print numbers from 10 down to 1.


WHAT DOES THE QUESTION MEAN?

Normally, a loop can move forward:

1
2
3
4
...

But this question asks us to move BACKWARD:

10
9
8
7
6
5
4
3
2
1

So we need a decreasing loop.


--------------------------------------------------
SOLUTION
--------------------------------------------------

We use:

range(10, 1 - 1, -1)


Which becomes:

range(10, 0, -1)


The three parts are:

range(start, stop, step)


start = 10
stop  = 0
step  = -1


--------------------------------------------------
HOW range() WORKS
--------------------------------------------------

The general syntax is:

range(start, stop, step)


START:

The starting value is included.


STOP:

The stopping value is excluded.


STEP:

The step tells Python how much to change
the value after every iteration.


Here:

range(10, 0, -1)


means:

Start at 10.

Decrease by 1 each time.

Stop before reaching 0.


Therefore:

10
9
8
7
6
5
4
3
2
1


--------------------------------------------------
WHY DO WE USE 1 - 1?
--------------------------------------------------

Your code has:

range(10, 1 - 1, -1)


Calculate:

1 - 1 = 0


So it becomes:

range(10, 0, -1)


We use 0 as the stopping value because
Python excludes the stop value.

Therefore 1 is still included:

10
9
8
7
6
5
4
3
2
1


--------------------------------------------------
DRY RUN
--------------------------------------------------

Code:

for number in range(10, 0, -1):
    print(number)


ITERATION 1:

number = 10

print(10)


ITERATION 2:

number = 9

print(9)


ITERATION 3:

number = 8

print(8)


ITERATION 4:

number = 7

print(7)


ITERATION 5:

number = 6

print(6)


ITERATION 6:

number = 5

print(5)


ITERATION 7:

number = 4

print(4)


ITERATION 8:

number = 3

print(3)


ITERATION 9:

number = 2

print(2)


ITERATION 10:

number = 1

print(1)


Next value would be:

0


But 0 is the STOP value, so it is excluded.

The loop ends.


--------------------------------------------------
DRY RUN TABLE
--------------------------------------------------

| Iteration | number | Action |
|----------:|-------:|--------|
| 1 | 10 | Print 10 |
| 2 | 9 | Print 9 |
| 3 | 8 | Print 8 |
| 4 | 7 | Print 7 |
| 5 | 6 | Print 6 |
| 6 | 5 | Print 5 |
| 7 | 4 | Print 4 |
| 8 | 3 | Print 3 |
| 9 | 2 | Print 2 |
| 10 | 1 | Print 1 |
| 11 | 0 | Stop |


--------------------------------------------------
OUTPUT
--------------------------------------------------

10
9
8
7
6
5
4
3
2
1


--------------------------------------------------
WHY DO WE USE -1?
--------------------------------------------------

Normally:

range(1, 11, 1)


moves forward:

1
2
3
4
...


But:

range(10, 0, -1)


moves backward:

10
9
8
7
...


The negative step tells Python:

"Decrease the value."


--------------------------------------------------
FORWARD VS BACKWARD
--------------------------------------------------

FORWARD:

range(1, 11, 1)

Output:

1
2
3
...
10


BACKWARD:

range(10, 0, -1)

Output:

10
9
8
...
1


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

Python does NOT use:

number--


Unlike languages such as C, C++, or Java,
Python does not support `--` as a decrement operator.


Instead, the range itself controls the decrement:

range(10, 0, -1)


The `-1` means:

"decrease by 1."


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Print numbers from 5 down to 1.

Code:

for number in range(5, 0, -1):
    print(number)


Output:

5
4
3
2
1


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Print numbers from 20 down to 10.

Code:

for number in range(20, 9, -1):
    print(number)


Output:

20
19
18
17
16
15
14
13
12
11
10


Notice:

We use 9 as the stop value because
the stop value is excluded.


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

Print even numbers backward from 10 to 2.

Code:

for number in range(10, 1, -2):
    print(number)


Output:

10
8
6
4
2


Here:

start = 10
stop = 1
step = -2


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Requirement:

Print 10 down to 1.

Code:

range(10, 0, -1)

Expected:

10
9
8
7
6
5
4
3
2
1


TEST CASE 2:

Requirement:

Print 5 down to 1.

Code:

range(5, 0, -1)

Expected:

5
4
3
2
1


TEST CASE 3:

Requirement:

Print 10 down to 5.

Code:

range(10, 4, -1)

Expected:

10
9
8
7
6
5


TEST CASE 4:

Requirement:

Print 1 down to 1.

Code:

range(1, 0, -1)

Expected:

1


--------------------------------------------------
COMMON MISTAKE
--------------------------------------------------

WRONG:

for number in range(10, 1):
    print(number)


This produces nothing.

Why?

Because the default step is:

+1


Python would try to move:

10 → 11 → 12 → ...


But the stop value is 1.

The direction doesn't make sense.


--------------------------------------------------
CORRECT
--------------------------------------------------

Use a negative step:

for number in range(10, 0, -1):
    print(number)


Now Python moves:

10 → 9 → 8 → ... → 1


--------------------------------------------------
ANOTHER COMMON MISTAKE
--------------------------------------------------

Wrong:

range(10, 1, -1)


This produces:

10
9
8
7
6
5
4
3
2


It does NOT print 1.

Why?

Because:

1 is the STOP value.

And Python excludes the stop value.


To include 1:

range(10, 0, -1)


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How does this loop work?"

You can say:

"I use a for loop with range starting at 10, stopping before 0,
and using a step of -1. The negative step makes the loop decrease
by one on every iteration, allowing it to print numbers from
10 down to 1."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. for loop

Used to repeat code.


2. range()

Generates a sequence of numbers.


3. Negative step

Used to move backward.


4. Stop value

The stop value is excluded.


5. -1

Means decrease by 1.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

FORWARD:

range(1, 11)

        ↓

1 2 3 4 ... 10


BACKWARD:

range(10, 0, -1)

        ↓

10 9 8 ... 1


Remember:

Forward → positive step

Backward → negative step


--------------------------------------------------
YOUR CODE SIMPLIFIED
--------------------------------------------------

Your code:

range(10, 1 - 1, -1)


can simply be written as:

range(10, 0, -1)


Both produce the same output.


--------------------------------------------------
YOUR CODE STRUCTURE
--------------------------------------------------

FOR LOOP
    ↓
Start at 10
    ↓
Decrease by 1
    ↓
10
9
8
7
6
5
4
3
2
1
    ↓
Stop before 0


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

range(10, 0, -1)

        ↓

Start = 10

        ↓

Step = -1

        ↓

Decrease by 1

        ↓

Stop before 0

        ↓

10, 9, 8, 7, ..., 1


MAIN THING TO REMEMBER:

`range(start, stop, step)`

For backward loops:

Use a NEGATIVE step.

Example:

range(10, 0, -1)
"""