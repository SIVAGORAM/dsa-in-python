def main():
    # Question 7: Print the sum of all even numbers up to n.

    n = 20
    total = 0

    for number in range(1, n + 1):
        if number % 2 == 0:
            total += number

    print("Even sum = " + str(total))


if __name__ == "__main__":
    main()


"""
QUESTION:

Print the sum of all even numbers up to n.


WHAT DOES THE QUESTION MEAN?

We are given a number `n`.

We need to find all the EVEN numbers from:

1 up to n

and then add them together.


For example:

n = 20


Even numbers up to 20 are:

2
4
6
8
10
12
14
16
18
20


Now add them:

2 + 4 + 6 + 8 + 10 + 12 + 14 + 16 + 18 + 20

= 110


Therefore:

Even sum = 110


--------------------------------------------------
HOW DO WE KNOW A NUMBER IS EVEN?
--------------------------------------------------

A number is even when it is completely divisible by 2.

We use:

number % 2 == 0


Examples:

2 % 2 = 0 → Even

4 % 2 = 0 → Even

7 % 2 = 1 → Odd

9 % 2 = 1 → Odd


Therefore:

if number % 2 == 0:


means:

"Only continue if the number is even."


--------------------------------------------------
SOLUTION LOGIC
--------------------------------------------------

Step 1:

Store the limit:

n = 20


Step 2:

Create an accumulator:

total = 0


Step 3:

Loop from 1 to n:

range(1, n + 1)


Step 4:

Check whether each number is even:

number % 2 == 0


Step 5:

If it is even, add it:

total += number


Step 6:

After the loop finishes, print total.


--------------------------------------------------
WHY total = 0?
--------------------------------------------------

We need to calculate a sum.

Before adding anything:

total = 0


Then we add only even numbers.

For example:

0 + 2 = 2

2 + 4 = 6

6 + 6 = 12

...


So `total` keeps the running sum.


--------------------------------------------------
DRY RUN
--------------------------------------------------

Given:

n = 20

Initial:

total = 0


ITERATION 1:

number = 1

Check:

1 % 2 == 0

1 % 2 = 1

False

Do not add.


--------------------------------------------------

ITERATION 2:

number = 2

Check:

2 % 2 == 0

2 % 2 = 0

True

Add:

total = 0 + 2

total = 2


--------------------------------------------------

ITERATION 3:

number = 3

Check:

3 % 2 == 0

False

Do not add.


--------------------------------------------------

ITERATION 4:

number = 4

Check:

4 % 2 == 0

True

total = 2 + 4

total = 6


--------------------------------------------------

ITERATION 5:

number = 5

Odd.

Do not add.


--------------------------------------------------

ITERATION 6:

number = 6

Even.

total = 6 + 6

total = 12


The same process continues.


--------------------------------------------------
DRY RUN TABLE
--------------------------------------------------

| number | number % 2 | Even? | total |
|-------:|-----------:|:-----:|------:|
| 1 | 1 | No | 0 |
| 2 | 0 | Yes | 2 |
| 3 | 1 | No | 2 |
| 4 | 0 | Yes | 6 |
| 5 | 1 | No | 6 |
| 6 | 0 | Yes | 12 |
| 7 | 1 | No | 12 |
| 8 | 0 | Yes | 20 |
| 9 | 1 | No | 20 |
| 10 | 0 | Yes | 30 |
| 11 | 1 | No | 30 |
| 12 | 0 | Yes | 42 |
| 13 | 1 | No | 42 |
| 14 | 0 | Yes | 56 |
| 15 | 1 | No | 56 |
| 16 | 0 | Yes | 72 |
| 17 | 1 | No | 72 |
| 18 | 0 | Yes | 90 |
| 19 | 1 | No | 90 |
| 20 | 0 | Yes | 110 |


--------------------------------------------------
FINAL CALCULATION
--------------------------------------------------

Even numbers:

2, 4, 6, 8, 10, 12, 14, 16, 18, 20


Sum:

2 + 4 + 6 + 8 + 10 + 12 + 14 + 16 + 18 + 20

= 110


Output:

Even sum = 110


--------------------------------------------------
WHY range(1, n + 1)?
--------------------------------------------------

Suppose:

n = 20


We want:

1 through 20


Python's:

range(start, stop)


does NOT include the stop value.


Therefore:

range(1, 20)

would give:

1, 2, 3, ..., 19


20 would be missing.


So we use:

range(1, n + 1)


which becomes:

range(1, 21)


Now we get:

1 through 20.


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

n = 10


Even numbers:

2
4
6
8
10


Sum:

2 + 4 + 6 + 8 + 10

= 30


Output:

Even sum = 30


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

n = 5


Even numbers:

2
4


Sum:

2 + 4 = 6


Output:

Even sum = 6


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

n = 1


There are no even numbers between 1 and 1.


Therefore:

total = 0


Output:

Even sum = 0


--------------------------------------------------
EXAMPLE 5
--------------------------------------------------

n = 2


Even numbers:

2


Sum:

2


Output:

Even sum = 2


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

n = 20

Even numbers:

2, 4, 6, ..., 20

Expected:

Even sum = 110


TEST CASE 2:

Input:

n = 10

Expected:

Even sum = 30


TEST CASE 3:

Input:

n = 5

Expected:

Even sum = 6


TEST CASE 4:

Input:

n = 2

Expected:

Even sum = 2


TEST CASE 5:

Input:

n = 1

Expected:

Even sum = 0


TEST CASE 6:

Input:

n = 0

Expected:

Even sum = 0


TEST CASE 7:

Input:

n = 100

Even numbers:

2, 4, 6, ..., 100

Expected:

Even sum = 2550


--------------------------------------------------
COMMON MISTAKE
--------------------------------------------------

If the question asks:

"Sum of EVEN numbers"

Do NOT use:

number % 2 != 0


That checks for odd numbers.


Correct:

number % 2 == 0


--------------------------------------------------
ANOTHER COMMON MISTAKE
--------------------------------------------------

Don't forget to initialize:

total = 0


If you don't create the accumulator, you have nowhere
to store the running sum.


--------------------------------------------------
IMPORTANT PYTHON CORRECTION
--------------------------------------------------

Your original code uses:

sum = 0


This works, but preferably use:

total = 0


because Python already has a built-in function:

sum()


For example:

sum([1, 2, 3])


returns:

6


So avoid overwriting the name `sum` when possible.


--------------------------------------------------
IMPORTANT LOOP EXPLANATION
--------------------------------------------------

Your original explanation says:

"number++"


Python does NOT use:

number++


The `range()` function automatically generates the
next number.


For:

range(1, n + 1)


Python generates:

1
2
3
...
n


You don't manually increment `number`.


--------------------------------------------------
ANOTHER WAY TO SOLVE IT
--------------------------------------------------

Because we only need even numbers, we can directly
generate them:

for number in range(2, n + 1, 2):
    total += number


For:

n = 20


the loop directly generates:

2
4
6
8
10
12
14
16
18
20


This avoids checking odd numbers.


However, your current solution is VERY IMPORTANT
for learning:

FOR LOOP
+
IF CONDITION
+
MODULO
+
ACCUMULATOR


--------------------------------------------------
CURRENT APPROACH
--------------------------------------------------

for number in range(1, n + 1):

        ↓

Check:

number % 2 == 0

        ↓

If even:

total += number

        ↓

Continue

        ↓

Print total


--------------------------------------------------
OPTIMIZED APPROACH
--------------------------------------------------

for number in range(2, n + 1, 2):

        ↓

Only even numbers are generated

        ↓

total += number


Both approaches produce the same answer.


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How did you solve this problem?"

You can say:

"I initialize an accumulator to zero and iterate from 1
through n. For every number, I check whether it is even
using modulo 2. If the remainder is zero, I add that
number to the accumulator. After the loop, the accumulator
contains the sum of all even numbers up to n."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. FOR LOOP

Used to iterate from 1 to n.


2. MODULO %

Used to identify even numbers.


3. EVEN CONDITION

number % 2 == 0


4. ACCUMULATOR

total = 0


5. ADD AND UPDATE

total += number


6. range()

range(1, n + 1)


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

Question:

"Sum of even numbers?"


Think:

1. Start total at 0.
2. Loop through the range.
3. Check `% 2 == 0`.
4. Add the number.
5. Print total.


Pattern:

total = 0

for number in range(1, n + 1):

    if number % 2 == 0:

        total += number


--------------------------------------------------
Q6 VS Q7
--------------------------------------------------

Q6:

Sum of ALL numbers from 1 to n.

Example:

n = 5

1 + 2 + 3 + 4 + 5

= 15


Q7:

Sum of ONLY EVEN numbers from 1 to n.

Example:

n = 5

2 + 4

= 6


So the important difference is:

Q6:

total += number


Q7:

if number % 2 == 0:
    total += number


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

n = 20

        ↓

Loop:

1 → 20

        ↓

Check every number

        ↓

Is number even?

        ↓

YES → Add to total

NO  → Skip

        ↓

Final total:

110

        ↓

Output:

Even sum = 110


MAIN THINGS TO REMEMBER:

1. Even → number % 2 == 0
2. Start accumulator with 0.
3. Add only numbers that satisfy the condition.
4. Use range(1, n + 1) to include n.
5. `total += number` means `total = total + number`.
6. Python does not use `number++`.
7. Prefer `total` instead of `sum` as a variable name.
"""