def main():
    # Question 6: Print the sum of first n natural numbers.

    n = 10
    total = 0

    for number in range(1, n + 1):
        total += number

    print("Sum = " + str(total))


if __name__ == "__main__":
    main()


"""
QUESTION:

Print the sum of the first n natural numbers.


WHAT DOES THE QUESTION MEAN?

Natural numbers start from:

1, 2, 3, 4, 5, ...


If:

n = 10

we need to calculate:

1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10


Answer:

55


--------------------------------------------------
WHAT IS AN ACCUMULATOR?
--------------------------------------------------

We need a variable that keeps collecting the sum.

We start with:

total = 0


Then we keep adding each number:

total = total + number


In Python, we can write:

total += number


This is the same as:

total = total + number


--------------------------------------------------
SOLUTION LOGIC
--------------------------------------------------

Given:

n = 10


Start:

total = 0


Loop through:

range(1, n + 1)


Since:

n = 10


this becomes:

range(1, 11)


So the loop processes:

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


For every number:

total += number


At the end, print total.


--------------------------------------------------
DRY RUN
--------------------------------------------------

Initial:

total = 0


ITERATION 1:

number = 1

total += number

total = 0 + 1

total = 1


ITERATION 2:

number = 2

total = 1 + 2

total = 3


ITERATION 3:

number = 3

total = 3 + 3

total = 6


ITERATION 4:

number = 4

total = 6 + 4

total = 10


ITERATION 5:

number = 5

total = 10 + 5

total = 15


ITERATION 6:

number = 6

total = 15 + 6

total = 21


ITERATION 7:

number = 7

total = 21 + 7

total = 28


ITERATION 8:

number = 8

total = 28 + 8

total = 36


ITERATION 9:

number = 9

total = 36 + 9

total = 45


ITERATION 10:

number = 10

total = 45 + 10

total = 55


Final:

total = 55


--------------------------------------------------
DRY RUN TABLE
--------------------------------------------------

| Iteration | number | Previous total | Calculation | New total |
|----------:|-------:|---------------:|-------------|----------:|
| 1 | 1 | 0 | 0 + 1 | 1 |
| 2 | 2 | 1 | 1 + 2 | 3 |
| 3 | 3 | 3 | 3 + 3 | 6 |
| 4 | 4 | 6 | 6 + 4 | 10 |
| 5 | 5 | 10 | 10 + 5 | 15 |
| 6 | 6 | 15 | 15 + 6 | 21 |
| 7 | 7 | 21 | 21 + 7 | 28 |
| 8 | 8 | 28 | 28 + 8 | 36 |
| 9 | 9 | 36 | 36 + 9 | 45 |
| 10 | 10 | 45 | 45 + 10 | 55 |


--------------------------------------------------
OUTPUT
--------------------------------------------------

Sum = 55


--------------------------------------------------
WHY DO WE START total WITH 0?
--------------------------------------------------

We are calculating a sum.

Before adding any numbers, the sum is:

0


Then:

0 + 1 = 1

1 + 2 = 3

3 + 3 = 6

...


This is why:

total = 0


is the correct starting point.


--------------------------------------------------
WHY range(1, n + 1)?
--------------------------------------------------

We want to include:

1 through n


But Python's `range()` excludes the stop value.

If:

n = 10


Then:

range(1, 10)


would produce only:

1 2 3 4 5 6 7 8 9


10 would be missing.


Therefore we use:

range(1, n + 1)


which becomes:

range(1, 11)


and produces:

1 2 3 4 5 6 7 8 9 10


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

n = 5


We calculate:

1 + 2 + 3 + 4 + 5


Dry run:

total = 0

0 + 1 = 1
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15


Output:

Sum = 15


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

n = 3


Calculation:

1 + 2 + 3

= 6


Output:

Sum = 6


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

n = 1


Calculation:

1


Output:

Sum = 1


--------------------------------------------------
EXAMPLE 5
--------------------------------------------------

n = 0


There are no positive natural numbers from 1 to 0.

The loop doesn't execute.

Initial:

total = 0


Output:

Sum = 0


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

n = 10

Expected:

Sum = 55


TEST CASE 2:

Input:

n = 5

Expected:

Sum = 15


TEST CASE 3:

Input:

n = 3

Expected:

Sum = 6


TEST CASE 4:

Input:

n = 1

Expected:

Sum = 1


TEST CASE 5:

Input:

n = 0

Expected:

Sum = 0


TEST CASE 6:

Input:

n = 100

Expected:

Sum = 5050


--------------------------------------------------
IMPORTANT PATTERN
--------------------------------------------------

This is called an:

ACCUMULATOR PATTERN


General structure:

total = 0

for number in range(...):
    total += number


Think:

Start
  ↓
Collect
  ↓
Collect
  ↓
Collect
  ↓
Final result


--------------------------------------------------
IMPORTANT PYTHON CORRECTION
--------------------------------------------------

Your original code uses:

sum = 0


It works, but it is better to avoid this.

Why?

Because Python already has a built-in function called:

sum()


For example:

sum([1, 2, 3])


returns:

6


If you create:

sum = 0


you replace the name of that built-in function in your
current scope.


So prefer:

total = 0


instead of:

sum = 0


--------------------------------------------------
YOUR ORIGINAL LOOP EXPLANATION
--------------------------------------------------

Your explanation says:

"number++"


Python does NOT use:

number++


The `range()` function generates the next number automatically.

For:

range(1, n + 1)


Python generates:

1
2
3
...
n


There is no need to manually write:

number++


--------------------------------------------------
ANOTHER WAY TO SOLVE IT
--------------------------------------------------

There is a mathematical formula:

n * (n + 1) // 2


For:

n = 10


Calculate:

10 * 11 // 2

= 110 // 2

= 55


So the answer is:

55


However, this question is specifically useful for
learning loops and accumulators, so your loop solution
is very important to understand.


--------------------------------------------------
LOOP SOLUTION VS FORMULA
--------------------------------------------------

LOOP:

total = 0

for number in range(1, n + 1):
    total += number


FORMULA:

total = n * (n + 1) // 2


For beginner logic-building practice, understand the
LOOP solution first.


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How did you solve this problem?"

You can say:

"I initialize an accumulator called total to zero.
Then I iterate from 1 through n using a for loop.
During each iteration, I add the current number to total.
After the loop finishes, total contains the sum of the
first n natural numbers."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. for loop

Used to iterate from 1 to n.


2. range()

Generates:

1, 2, 3, ..., n


3. Accumulator

`total` stores the running sum.


4. += operator

```text
total += number

means:

total = total + number
Integer addition

Each number is added to the running total.

```
"""