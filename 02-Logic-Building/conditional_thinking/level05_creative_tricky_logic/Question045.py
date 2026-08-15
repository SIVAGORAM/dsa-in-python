def main():
    # Question 45: Take three numbers and check if they are in arithmetic progression.

    a = 4
    b = 8
    c = 12

    if b - a == c - b:
        print("Arithmetic progression")
    else:
        print("Not an arithmetic progression")


if __name__ == "__main__":
    main()


"""
QUESTION:

Take three numbers and check if they are in arithmetic progression.


WHAT IS AN ARITHMETIC PROGRESSION?

An Arithmetic Progression (AP) is a sequence of numbers in which
the difference between consecutive numbers is the same.

For three numbers:

a, b, c

They form an arithmetic progression if:

b - a == c - b


Example:

4, 8, 12

Difference between the first and second number:

8 - 4 = 4

Difference between the second and third number:

12 - 8 = 4

Both differences are equal.

Therefore:

4, 8, 12

is an Arithmetic Progression.


--------------------------------------------------
THE MAIN LOGIC
--------------------------------------------------

We calculate two differences:

First difference:

b - a


Second difference:

c - b


Then compare them:

b - a == c - b


If they are equal:

Arithmetic progression

Otherwise:

Not an arithmetic progression.


--------------------------------------------------
DRY RUN
--------------------------------------------------

Given:

a = 4
b = 8
c = 12


STEP 1:

Calculate the first difference:

b - a

8 - 4 = 4


STEP 2:

Calculate the second difference:

c - b

12 - 8 = 4


STEP 3:

Compare:

4 == 4

True


Therefore:

Arithmetic progression


Output:

Arithmetic progression


--------------------------------------------------
ANOTHER EXAMPLE
--------------------------------------------------

Given:

a = 2
b = 5
c = 8


First difference:

5 - 2 = 3


Second difference:

8 - 5 = 3


Compare:

3 == 3

True


Output:

Arithmetic progression


--------------------------------------------------
NOT AN ARITHMETIC PROGRESSION
--------------------------------------------------

Given:

a = 2
b = 5
c = 10


First difference:

5 - 2 = 3


Second difference:

10 - 5 = 5


Compare:

3 == 5

False


Therefore:

Not an arithmetic progression


--------------------------------------------------
NEGATIVE NUMBERS
--------------------------------------------------

Arithmetic progression can also contain negative numbers.

Example:

-5, -2, 1


First difference:

-2 - (-5)

= -2 + 5

= 3


Second difference:

1 - (-2)

= 1 + 2

= 3


Therefore:

Arithmetic progression


--------------------------------------------------
DECREASING ARITHMETIC PROGRESSION
--------------------------------------------------

The numbers don't have to increase.

Example:

20, 15, 10


First difference:

15 - 20 = -5


Second difference:

10 - 15 = -5


Both differences are equal.

Therefore:

Arithmetic progression


--------------------------------------------------
ZERO DIFFERENCE
--------------------------------------------------

Example:

7, 7, 7


First difference:

7 - 7 = 0


Second difference:

7 - 7 = 0


Therefore:

Arithmetic progression


--------------------------------------------------
DRY RUN WITH DECREASING VALUES
--------------------------------------------------

Given:

a = 20
b = 15
c = 10


Check:

b - a == c - b


15 - 20 = -5

10 - 15 = -5


Therefore:

-5 == -5

True


Output:

Arithmetic progression


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

a = 4
b = 8
c = 12

Output:

Arithmetic progression


TEST CASE 2:

Input:

a = 2
b = 5
c = 8

Output:

Arithmetic progression


TEST CASE 3:

Input:

a = 2
b = 5
c = 10

Output:

Not an arithmetic progression


TEST CASE 4:

Input:

a = 20
b = 15
c = 10

Output:

Arithmetic progression


TEST CASE 5:

Input:

a = -5
b = -2
c = 1

Output:

Arithmetic progression


TEST CASE 6:

Input:

a = 7
b = 7
c = 7

Output:

Arithmetic progression


TEST CASE 7:

Input:

a = 1
b = 4
c = 7

Output:

Arithmetic progression


TEST CASE 8:

Input:

a = 10
b = 20
c = 31

Output:

Not an arithmetic progression


--------------------------------------------------
TEST CASE TABLE
--------------------------------------------------

| a  | b  | c  | Expected Output |
|----|----|----|------------------|
| 4  | 8  | 12 | Arithmetic progression |
| 2  | 5  | 8  | Arithmetic progression |
| 2  | 5  | 10 | Not an arithmetic progression |
| 20 | 15 | 10 | Arithmetic progression |
| -5 | -2 | 1  | Arithmetic progression |
| 7  | 7  | 7  | Arithmetic progression |
| 1  | 4  | 7  | Arithmetic progression |
| 10 | 20 | 31 | Not an arithmetic progression |


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Difference

Difference between two numbers is found using subtraction.

Example:

8 - 4 = 4


2. Arithmetic Progression

Consecutive differences must be equal.

For:

a, b, c

Condition:

b - a == c - b


3. Equality operator

`==` checks whether two values are equal.


--------------------------------------------------
IMPORTANT
--------------------------------------------------

Do NOT just check:

a + c == 2 * b

Although that is another mathematical way to identify an AP,
for this problem your current logic is much easier to understand:

b - a == c - b


Think:

First gap == Second gap


Example:

4 → 8 → 12

    +4   +4

Same gap → AP


Example:

2 → 5 → 10

    +3   +5

Different gap → Not AP


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How did you solve this problem?"

You can say:

"An arithmetic progression has a constant difference between
consecutive terms. So I calculate the difference between the
second and first numbers and compare it with the difference
between the third and second numbers. If both differences are
equal, the three numbers form an arithmetic progression."


--------------------------------------------------
MAIN LOGIC TO REMEMBER
--------------------------------------------------

Three numbers:

a, b, c

      ↓

Calculate:

b - a

      ↓

Calculate:

c - b

      ↓

Compare:

b - a == c - b

      ↓

YES → Arithmetic progression

NO  → Not an arithmetic progression


SIMPLE MEMORY TRICK:

Same gap = AP

Example:

4 → 8 → 12
    +4   +4

AP


Different gap:

2 → 5 → 10
    +3   +5

Not AP
"""