def main():
    # Question 3: Print all odd numbers between 1 and 100.

    for number in range(1, 100 + 1):
        if number % 2 != 0:
            print(number)


if __name__ == "__main__":
    main()


"""
QUESTION:

Print all odd numbers between 1 and 100.


WHAT DOES THE QUESTION MEAN?

We need to print only the odd numbers from:

1 to 100.

The odd numbers are:

1
3
5
7
9
11
13
...


--------------------------------------------------
HOW DO WE CHECK IF A NUMBER IS ODD?
--------------------------------------------------

We use the modulo operator:

%


For example:

7 % 2 = 1

Therefore, 7 is odd.


Another example:

10 % 2 = 0

Therefore, 10 is even.


For an odd number:

number % 2 != 0


This means:

"The remainder after dividing the number by 2
is NOT zero."


--------------------------------------------------
SOLUTION LOGIC
--------------------------------------------------

Step 1:

Generate numbers from 1 to 100:

range(1, 100 + 1)


Step 2:

Check every number:

number % 2 != 0


Step 3:

If the condition is True:

print(number)


Step 4:

If the condition is False:

skip the number.


--------------------------------------------------
HOW range() WORKS
--------------------------------------------------

Python:

range(start, stop)


The start value is included.

The stop value is excluded.


Therefore:

range(1, 100 + 1)


becomes:

range(1, 101)


This generates:

1, 2, 3, ..., 100


--------------------------------------------------
DRY RUN
--------------------------------------------------

First:

number = 1

Check:

1 % 2 != 0

1 % 2 = 1

1 != 0 → True

Therefore:

print(1)


--------------------------------------------------

Next:

number = 2

Check:

2 % 2 != 0

2 % 2 = 0

0 != 0 → False

Do not print.


--------------------------------------------------

Next:

number = 3

Check:

3 % 2 != 0

3 % 2 = 1

1 != 0 → True

Print:

3


--------------------------------------------------

Next:

number = 4

Check:

4 % 2 != 0

4 % 2 = 0

False

Do not print.


--------------------------------------------------
DRY RUN TABLE
--------------------------------------------------

| number | number % 2 | Condition | Action |
|-------:|-----------:|-----------|--------|
| 1 | 1 | True | Print 1 |
| 2 | 0 | False | Skip |
| 3 | 1 | True | Print 3 |
| 4 | 0 | False | Skip |
| 5 | 1 | True | Print 5 |
| 6 | 0 | False | Skip |
| 7 | 1 | True | Print 7 |
| 8 | 0 | False | Skip |
| 9 | 1 | True | Print 9 |
| 10 | 0 | False | Skip |


--------------------------------------------------
OUTPUT
--------------------------------------------------

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
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99


--------------------------------------------------
WHY DOES number % 2 != 0 WORK?
--------------------------------------------------

The `%` operator gives the remainder.

Examples:

1 % 2 = 1
2 % 2 = 0
3 % 2 = 1
4 % 2 = 0
5 % 2 = 1
6 % 2 = 0


So:

Remainder 0 → Even

Remainder 1 → Odd


Therefore:

number % 2 != 0

means:

"The number has a non-zero remainder when divided by 2."


--------------------------------------------------
EVEN VS ODD
--------------------------------------------------

Even:

number % 2 == 0


Odd:

number % 2 != 0


Example:

10 % 2 = 0
→ Even


11 % 2 = 1
→ Odd


12 % 2 = 0
→ Even


13 % 2 = 1
→ Odd


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Print odd numbers from 1 to 10.

Code:

for number in range(1, 10 + 1):
    if number % 2 != 0:
        print(number)


Output:

1
3
5
7
9


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Print odd numbers from 1 to 20.

Code:

for number in range(1, 20 + 1):
    if number % 2 != 0:
        print(number)


Output:

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


--------------------------------------------------
ANOTHER WAY TO SOLVE IT
--------------------------------------------------

We can directly generate odd numbers using
the step argument of range():

for number in range(1, 101, 2):
    print(number)


Here:

start = 1
stop = 101
step = 2


So Python generates:

1
3
5
7
9
...


This is more direct because we don't need to
check the even numbers.


However, your current solution is very good for
learning:

FOR LOOP + IF CONDITION + MODULO.


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Range:

1 to 10

Expected:

1
3
5
7
9


TEST CASE 2:

Range:

1 to 20

Expected:

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


TEST CASE 3:

Range:

1 to 100

Expected:

1, 3, 5, ..., 99


TEST CASE 4:

If the number is:

1

Check:

1 % 2 != 0

True

Output:

1


TEST CASE 5:

If the number is:

2

Check:

2 % 2 != 0

False

No output.


--------------------------------------------------
COMMON MISTAKE
--------------------------------------------------

For odd numbers, don't use:

number % 2 == 0


That condition checks for EVEN numbers.


For odd numbers, use:

number % 2 != 0


You can also use:

number % 2 == 1

for positive numbers.


But:

number % 2 != 0

is a better general way to express:

"remainder is not zero."


--------------------------------------------------
PYTHON range() NOTE
--------------------------------------------------

Your original explanation says:

"number++"


Python does NOT use:

number++


Instead:

for number in range(1, 101):


`range()` automatically gives the next value.


For example:

1
2
3
4
...
100


You do not need to manually increment `number`.


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How did you solve this problem?"

You can say:

"I iterate through the numbers from 1 to 100 and use
the modulo operator to check whether each number leaves
a non-zero remainder when divided by 2. If the remainder
is not zero, the number is odd, so I print it."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. for loop

Used to iterate through the numbers.


2. range()

Generates numbers from the start value up to,
but not including, the stop value.


3. modulo %

Returns the remainder.


4. Odd number

For positive integers:

number % 2 != 0


5. if condition

Used to print only numbers that satisfy the condition.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

EVEN:

number % 2 == 0


ODD:

number % 2 != 0


Remember:

Even → remainder 0

Odd → remainder not 0


--------------------------------------------------
YOUR CODE STRUCTURE
--------------------------------------------------

FOR LOOP
    ↓
1 to 100
    ↓
Check each number
    ↓
number % 2 != 0
    ↓
YES → Print
NO  → Skip
    ↓
Continue until 100


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

for number in range(1, 101):

        ↓

check:

number % 2 != 0

        ↓

True:

print(number)

        ↓

Result:

1, 3, 5, 7, ..., 99


MAIN THING TO REMEMBER:

number % 2 == 0 → Even

number % 2 != 0 → Odd
"""