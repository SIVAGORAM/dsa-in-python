def main():
    # Question 8: Print the sum of all odd numbers up to n.

    n = 20
    total = 0

    for number in range(1, n + 1):
        if number % 2 != 0:
            total += number

    print("Odd sum = " + str(total))


if __name__ == "__main__":
    main()


"""
QUESTION:

Print the sum of all odd numbers up to n.


WHAT DOES THE QUESTION MEAN?

We are given a number `n`.

We need to find all the ODD numbers from:

1 up to n

and then add them together.

For example:

n = 20

Odd numbers up to 20 are:

1
3
5
7
9
11
13
15
17
19

Now add them:

1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19

= 100

Therefore:

Odd sum = 100


--------------------------------------------------
HOW DO WE KNOW A NUMBER IS ODD?
--------------------------------------------------

We use the modulo operator:

%

For odd numbers:

number % 2 != 0

This means:

"The remainder after dividing the number by 2
is not zero."


Examples:

1 % 2 = 1 → Odd

2 % 2 = 0 → Even

3 % 2 = 1 → Odd

4 % 2 = 0 → Even

5 % 2 = 1 → Odd


Therefore:

if number % 2 != 0:


means:

"Only continue if the number is odd."


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

Check whether the number is odd:

number % 2 != 0


Step 5:

If it is odd, add it:

total += number


Step 6:

After the loop finishes, print total.


--------------------------------------------------
WHY total = 0?
--------------------------------------------------

We are calculating a sum.

Before adding anything:

total = 0


Then we add only odd numbers.

For example:

0 + 1 = 1

1 + 3 = 4

4 + 5 = 9

9 + 7 = 16

...


So `total` stores the running sum.


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

1 % 2 != 0

1 % 2 = 1

1 != 0 → True

Add:

total = 0 + 1

total = 1


--------------------------------------------------

ITERATION 2:

number = 2

Check:

2 % 2 != 0

2 % 2 = 0

0 != 0 → False

Do not add.


--------------------------------------------------

ITERATION 3:

number = 3

Check:

3 % 2 != 0

3 % 2 = 1

True

Add:

total = 1 + 3

total = 4


--------------------------------------------------

ITERATION 4:

number = 4

4 % 2 = 0

False

Do not add.


--------------------------------------------------

ITERATION 5:

number = 5

5 % 2 = 1

True

total = 4 + 5

total = 9


The same process continues until 20.


--------------------------------------------------
DRY RUN TABLE
--------------------------------------------------

| number | number % 2 | Odd? | total |
|-------:|-----------:|:----:|------:|
| 1 | 1 | Yes | 1 |
| 2 | 0 | No | 1 |
| 3 | 1 | Yes | 4 |
| 4 | 0 | No | 4 |
| 5 | 1 | Yes | 9 |
| 6 | 0 | No | 9 |
| 7 | 1 | Yes | 16 |
| 8 | 0 | No | 16 |
| 9 | 1 | Yes | 25 |
| 10 | 0 | No | 25 |
| 11 | 1 | Yes | 36 |
| 12 | 0 | No | 36 |
| 13 | 1 | Yes | 49 |
| 14 | 0 | No | 49 |
| 15 | 1 | Yes | 64 |
| 16 | 0 | No | 64 |
| 17 | 1 | Yes | 81 |
| 18 | 0 | No | 81 |
| 19 | 1 | Yes | 100 |
| 20 | 0 | No | 100 |


--------------------------------------------------
FINAL CALCULATION
--------------------------------------------------

Odd numbers:

1, 3, 5, 7, 9, 11, 13, 15, 17, 19


Sum:

1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19

= 100


Output:

Odd sum = 100


--------------------------------------------------
WHY range(1, n + 1)?
--------------------------------------------------

Suppose:

n = 20


We want:

1 through 20


Python's `range()` excludes the stop value.

Therefore:

range(1, 20)

would produce:

1, 2, 3, ..., 19


20 would be missing.


So we use:

range(1, n + 1)


which becomes:

range(1, 21)


This gives:

1 through 20.


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

n = 10


Odd numbers:

1
3
5
7
9


Sum:

1 + 3 + 5 + 7 + 9

= 25


Output:

Odd sum = 25


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

n = 5


Odd numbers:

1
3
5


Sum:

1 + 3 + 5

= 9


Output:

Odd sum = 9


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

n = 3


Odd numbers:

1
3


Sum:

1 + 3 = 4


Output:

Odd sum = 4


--------------------------------------------------
EXAMPLE 5
--------------------------------------------------

n = 1


Odd numbers:

1


Sum:

1


Output:

Odd sum = 1


--------------------------------------------------
EXAMPLE 6
--------------------------------------------------

n = 2


Odd numbers:

1


Sum:

1


Output:

Odd sum = 1


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

n = 20

Odd numbers:

1, 3, 5, ..., 19

Expected:

Odd sum = 100


TEST CASE 2:

Input:

n = 10

Expected:

Odd sum = 25


TEST CASE 3:

Input:

n = 5

Expected:

Odd sum = 9


TEST CASE 4:

Input:

n = 3

Expected:

Odd sum = 4


TEST CASE 5:

Input:

n = 1

Expected:

Odd sum = 1


TEST CASE 6:

Input:

n = 2

Expected:

Odd sum = 1


TEST CASE 7:

Input:

n = 0

Expected:

Odd sum = 0


--------------------------------------------------
COMMON MISTAKE
--------------------------------------------------

For odd numbers, don't use:

number % 2 == 0


That checks for EVEN numbers.


Correct:

number % 2 != 0


--------------------------------------------------
ANOTHER WAY TO CHECK ODD
--------------------------------------------------

For positive integers, you can also use:

number % 2 == 1


For example:

5 % 2 == 1

True


But:

number % 2 != 0

is a clear way to say:

"The remainder is not zero."


--------------------------------------------------
ANOTHER WAY TO SOLVE IT
--------------------------------------------------

Because we only need odd numbers, we can directly
generate them using `range()`:

for number in range(1, n + 1, 2):
    total += number


For:

n = 20


the loop directly generates:

1
3
5
7
9
11
13
15
17
19


This avoids checking the even numbers.


However, your current solution is very useful for
learning:

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

number % 2 != 0

        ↓

If odd:

total += number

        ↓

Continue

        ↓

Print total


--------------------------------------------------
OPTIMIZED APPROACH
--------------------------------------------------

for number in range(1, n + 1, 2):
    total += number


Both approaches give the same result.


--------------------------------------------------
IMPORTANT PYTHON CORRECTION
--------------------------------------------------

Your original code uses:

sum = 0


It works, but preferably use:

total = 0


because Python already has a built-in function:

sum()


For example:

sum([1, 2, 3])


returns:

6


So using `total` is clearer.


--------------------------------------------------
IMPORTANT LOOP CORRECTION
--------------------------------------------------

Your original explanation says:

"number++"


Python does NOT use:

number++


The `range()` function automatically generates
the next value.


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
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How did you solve this problem?"

You can say:

"I initialize an accumulator to zero and iterate from 1
through n. For each number, I check whether it is odd using
the modulo operator. If the remainder after division by 2
is not zero, I add that number to the accumulator. After
the loop, the accumulator contains the sum of all odd
numbers up to n."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. FOR LOOP

Used to iterate from 1 to n.


2. MODULO %

Used to identify odd numbers.


3. ODD CONDITION

number % 2 != 0


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

"Sum of odd numbers?"


Think:

1. Start total at 0.
2. Loop from 1 to n.
3. Check `% 2 != 0`.
4. Add the odd number.
5. Print total.


Pattern:

total = 0

for number in range(1, n + 1):

    if number % 2 != 0:

        total += number


--------------------------------------------------
Q7 VS Q8
--------------------------------------------------

Q7:

Sum of EVEN numbers.

Condition:

number % 2 == 0


Example:

n = 10

2 + 4 + 6 + 8 + 10

= 30


Q8:

Sum of ODD numbers.

Condition:

number % 2 != 0


Example:

n = 10

1 + 3 + 5 + 7 + 9

= 25


The main difference is:

Q7:

if number % 2 == 0:


Q8:

if number % 2 != 0:


--------------------------------------------------
Q6 VS Q7 VS Q8
--------------------------------------------------

Q6:

Sum of ALL numbers:

total += number


Q7:

Sum of EVEN numbers:

if number % 2 == 0:
    total += number


Q8:

Sum of ODD numbers:

if number % 2 != 0:
    total += number


This is an important pattern to remember.


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

n = 20

        ↓

Loop:

1 → 20

        ↓

Check each number

        ↓

Is number odd?

        ↓

YES → Add to total

NO  → Skip

        ↓

Final total:

100

        ↓

Output:

Odd sum = 100


MAIN THINGS TO REMEMBER:

1. Odd → number % 2 != 0
2. Start accumulator with 0.
3. Add only numbers that satisfy the condition.
4. Use range(1, n + 1) to include n.
5. `total += number` means `total = total + number`.
6. Python does not use `number++`.
7. Prefer `total` instead of `sum` as a variable name.
"""