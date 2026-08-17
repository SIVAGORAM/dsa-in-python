def main():
    # Question 46: Take three numbers and check if they are in geometric progression.

    a = 3
    b = 9
    c = 27

    if b * b == a * c:
        print("Geometric progression")
    else:
        print("Not a geometric progression")


if __name__ == "__main__":
    main()


"""
QUESTION:

Take three numbers and check if they are in geometric progression.


WHAT IS A GEOMETRIC PROGRESSION?

A Geometric Progression (GP) is a sequence of numbers where the
ratio between consecutive terms is the same.

For three numbers:

a, b, c

They form a GP when:

b / a == c / b

For example:

3, 9, 27

Ratio between first and second:

9 / 3 = 3

Ratio between second and third:

27 / 9 = 3

Both ratios are equal.

Therefore:

3, 9, 27

is a Geometric Progression.


--------------------------------------------------
THE FORMULA USED IN THE CODE
--------------------------------------------------

Instead of directly using division:

b / a == c / b

we use:

b * b == a * c


Why?

Starting from:

b / a = c / b

Cross multiply:

b × b = a × c

Therefore:

b² = a × c


This allows us to check GP using multiplication.


--------------------------------------------------
EXAMPLE
--------------------------------------------------

Given:

a = 3
b = 9
c = 27


Calculate:

b * b

9 * 9 = 81


Calculate:

a * c

3 * 27 = 81


Compare:

81 == 81

True


Therefore:

Geometric progression


Output:

Geometric progression


--------------------------------------------------
DRY RUN
--------------------------------------------------

Given:

a = 3
b = 9
c = 27


STEP 1:

Calculate:

b * b

9 * 9 = 81


STEP 2:

Calculate:

a * c

3 * 27 = 81


STEP 3:

Compare:

81 == 81

True


Therefore:

print("Geometric progression")


Output:

Geometric progression


--------------------------------------------------
ANOTHER EXAMPLE
--------------------------------------------------

Given:

a = 2
b = 6
c = 18


Check:

b * b == a * c


6 * 6 = 36

2 * 18 = 36


Therefore:

36 == 36

True


Output:

Geometric progression


--------------------------------------------------
NOT A GEOMETRIC PROGRESSION
--------------------------------------------------

Given:

a = 2
b = 6
c = 20


Calculate:

b * b

6 * 6 = 36


Calculate:

a * c

2 * 20 = 40


Compare:

36 == 40

False


Therefore:

Not a geometric progression


--------------------------------------------------
DRY RUN: NOT GP
--------------------------------------------------

Given:

a = 2
b = 6
c = 20


b * b:

6 * 6 = 36


a * c:

2 * 20 = 40


Check:

36 == 40

False


Output:

Not a geometric progression


--------------------------------------------------
ANOTHER IMPORTANT EXAMPLE
--------------------------------------------------

Consider:

4, 2, 1


Ratio:

2 / 4 = 0.5

1 / 2 = 0.5


Both ratios are equal.

Therefore:

4, 2, 1

is a Geometric Progression.


Using the formula:

b * b == a * c

2 * 2 == 4 * 1

4 == 4

True


Therefore:

Geometric progression


--------------------------------------------------
NEGATIVE NUMBERS
--------------------------------------------------

GP can also contain negative numbers.

Example:

2, -6, 18


Ratios:

-6 / 2 = -3

18 / -6 = -3


Both ratios are equal.

Therefore:

Geometric progression


Using the formula:

b * b == a * c

(-6) * (-6) = 2 * 18

36 = 36

True


--------------------------------------------------
ZERO EXAMPLE
--------------------------------------------------

Example:

0, 0, 0


Using the formula:

b * b == a * c

0 * 0 == 0 * 0

0 == 0

True


So the current mathematical check returns:

Geometric progression


However, when defining GP using a common ratio, division by zero
would not be valid. For this beginner exercise, use the formula
given in the solution.


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

a = 3
b = 9
c = 27

Output:

Geometric progression


TEST CASE 2:

Input:

a = 2
b = 6
c = 18

Output:

Geometric progression


TEST CASE 3:

Input:

a = 4
b = 2
c = 1

Output:

Geometric progression


TEST CASE 4:

Input:

a = 2
b = 6
c = 20

Output:

Not a geometric progression


TEST CASE 5:

Input:

a = 5
b = 10
c = 20

Output:

Geometric progression


TEST CASE 6:

Input:

a = 10
b = 20
c = 30

Output:

Not a geometric progression


TEST CASE 7:

Input:

a = 2
b = -6
c = 18

Output:

Geometric progression


TEST CASE 8:

Input:

a = 7
b = 7
c = 7

Output:

Geometric progression


--------------------------------------------------
TEST CASE TABLE
--------------------------------------------------

| a  | b  | c  | Expected Output |
|----|----|----|------------------|
| 3  | 9  | 27 | Geometric progression |
| 2  | 6  | 18 | Geometric progression |
| 4  | 2  | 1  | Geometric progression |
| 2  | 6  | 20 | Not a geometric progression |
| 5  | 10 | 20 | Geometric progression |
| 10 | 20 | 30 | Not a geometric progression |
| 2  | -6 | 18 | Geometric progression |
| 7  | 7  | 7  | Geometric progression |


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Geometric Progression

A sequence where the ratio between consecutive terms is constant.

Example:

3, 9, 27

Ratio:

9 / 3 = 3

27 / 9 = 3


2. Common Ratio

The common ratio is the value obtained by dividing one term
by the previous term.

Example:

3, 9, 27

Common ratio = 3


3. Cross Multiplication

Instead of:

b / a == c / b

we use:

b * b == a * c


4. `*`

Multiplication operator.


5. `==`

Equality comparison operator.


--------------------------------------------------
AP VS GP
--------------------------------------------------

This is VERY important because Question 45 and Question 46
are related.

Arithmetic Progression (AP):

The DIFFERENCE is constant.

Example:

4, 8, 12

8 - 4 = 4
12 - 8 = 4


Condition:

b - a == c - b


Geometric Progression (GP):

The RATIO is constant.

Example:

3, 9, 27

9 / 3 = 3
27 / 9 = 3


Condition:

b * b == a * c


Remember:

AP → Same difference

GP → Same ratio


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How did you solve this problem?"

You can say:

"A geometric progression has a constant ratio between consecutive
terms. For three terms a, b, and c, the condition is b/a = c/b.
Instead of using division, I cross multiply it to get b² = a*c,
so I check whether b*b equals a*c."


--------------------------------------------------
MAIN LOGIC TO REMEMBER
--------------------------------------------------

Three numbers:

a, b, c

        ↓

GP means:

b / a == c / b

        ↓

Cross multiply:

b × b == a × c

        ↓

YES → Geometric progression

NO  → Not a geometric progression


SIMPLE MEMORY TRICK:

AP → Difference

GP → Ratio


AP:

4 → 8 → 12
   +4   +4


GP:

3 → 9 → 27
   ×3   ×3
"""