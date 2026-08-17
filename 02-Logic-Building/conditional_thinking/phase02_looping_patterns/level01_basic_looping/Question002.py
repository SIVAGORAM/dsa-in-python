def main():
    # Question 2: Print all even numbers between 1 and 100.

    for number in range(1, 100 + 1):
        if number % 2 == 0:
            print(number)


if __name__ == "__main__":
    main()


"""
QUESTION:

Print all even numbers between 1 and 100.


WHAT DOES THE QUESTION MEAN?

We need to print only the even numbers from:

1 to 100

An even number is a number that is completely divisible by 2.

Examples:

2
4
6
8
10
12
...


--------------------------------------------------
HOW DO WE CHECK IF A NUMBER IS EVEN?
--------------------------------------------------

We use the modulo operator:

%


For example:

10 % 2 = 0

Therefore, 10 is even.


Another example:

7 % 2 = 1

Therefore, 7 is odd.


So the condition for an even number is:

number % 2 == 0


--------------------------------------------------
SOLUTION LOGIC
--------------------------------------------------

First, generate numbers from 1 to 100:

range(1, 100 + 1)


Then check every number:

if number % 2 == 0:


If the condition is True:

print(number)


If the condition is False:

do nothing and move to the next number.


--------------------------------------------------
HOW range() WORKS
--------------------------------------------------

Python uses:

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

The loop starts with:

number = 1


Check:

1 % 2 == 0

1 % 2 = 1

1 == 0 → False

So 1 is not printed.


--------------------------------------------------

Next:

number = 2


Check:

2 % 2 == 0

2 % 2 = 0

0 == 0 → True

Print:

2


--------------------------------------------------

Next:

number = 3


Check:

3 % 2 == 0

3 % 2 = 1

False

Do not print.


--------------------------------------------------

Next:

number = 4


Check:

4 % 2 == 0

4 % 2 = 0

True

Print:

4


The same process continues until 100.


--------------------------------------------------
SHORT DRY RUN TABLE
--------------------------------------------------

| number | number % 2 | Condition | Action |
|-------:|-----------:|-----------|--------|
| 1 | 1 | False | Don't print |
| 2 | 0 | True | Print 2 |
| 3 | 1 | False | Don't print |
| 4 | 0 | True | Print 4 |
| 5 | 1 | False | Don't print |
| 6 | 0 | True | Print 6 |
| 7 | 1 | False | Don't print |
| 8 | 0 | True | Print 8 |
| 9 | 1 | False | Don't print |
| 10 | 0 | True | Print 10 |


--------------------------------------------------
OUTPUT
--------------------------------------------------

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
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100


--------------------------------------------------
WHY DOES number % 2 WORK?
--------------------------------------------------

The `%` operator gives the remainder.

Examples:

10 % 2 = 0

11 % 2 = 1

12 % 2 = 0

13 % 2 = 1

14 % 2 = 0


So:

Remainder 0 → Even

Remainder 1 → Odd


For positive numbers, this gives us an easy way
to identify even numbers.


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Print even numbers from 1 to 10.

Code:

for number in range(1, 10 + 1):
    if number % 2 == 0:
        print(number)


Output:

2
4
6
8
10


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Print even numbers from 1 to 20.

Code:

for number in range(1, 20 + 1):
    if number % 2 == 0:
        print(number)


Output:

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


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

We can also start directly from 2:

for number in range(2, 101, 2):
    print(number)


This directly generates:

2
4
6
8
...
100


This is a more efficient approach because we don't
need to check the odd numbers.

However, your current solution is excellent for
learning the combination of:

FOR LOOP + IF CONDITION + MODULO.


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Range:

1 to 10

Expected:

2
4
6
8
10


TEST CASE 2:

Range:

1 to 20

Expected:

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


TEST CASE 3:

Range:

1 to 100

Expected:

2, 4, 6, ..., 100


TEST CASE 4:

If the range contains only:

1

Check:

1 % 2 == 0

False

No even number is printed.


TEST CASE 5:

If the range contains:

2

Check:

2 % 2 == 0

True

Output:

2


--------------------------------------------------
COMMON MISTAKE
--------------------------------------------------

WRONG:

if number % 2 == 1:
    print(number)


This prints odd numbers for positive integers.


For even numbers, use:

if number % 2 == 0:
    print(number)


--------------------------------------------------
ANOTHER WAY TO SOLVE IT
--------------------------------------------------

Instead of checking every number:

for number in range(1, 101):
    if number % 2 == 0:
        print(number)


We can directly generate even numbers:

for number in range(2, 101, 2):
    print(number)


Here:

range(start, stop, step)


means:

start = 2
stop = 101
step = 2


So the numbers are:

2
4
6
8
10
...


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

`range()` can have three arguments:

range(start, stop, step)


Example:

range(2, 11, 2)


produces:

2
4
6
8
10


The `step` tells Python how much to increase
the value each time.


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How did you solve this problem?"

You can say:

"I iterate through the numbers from 1 to 100 and use the modulo
operator to check whether each number is divisible by 2. If the
remainder is zero, the number is even, so I print it."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. `for` loop

Used to iterate through numbers.


2. `range()`

Generates numbers from the starting value up to,
but not including, the stopping value.


3. `%`

Returns the remainder.


4. Even number

A number is even when:

number % 2 == 0


5. `if`

Used to print only numbers that satisfy the condition.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

EVEN:

number % 2 == 0


ODD:

number % 2 != 0


Remember:

```text
Even → remainder 0
Odd  → remainder 1
```
"""