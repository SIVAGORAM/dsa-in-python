def main():
    # Question 41: Take coordinates (x, y) and check if the point
    # lies on the X-axis, Y-axis, or at the origin.

    x = 0
    y = 5

    if x == 0 and y == 0:
        print("Origin")
    elif y == 0:
        print("X-axis")
    elif x == 0:
        print("Y-axis")
    else:
        print("Not on an axis")


if __name__ == "__main__":
    main()


"""
QUESTION:

Take coordinates (x, y) and check if the point lies on the
X-axis, Y-axis, or at the origin.


WHAT DOES THE QUESTION MEAN?

A coordinate point is represented as:

(x, y)

For example:

(3, 5)

Here:

x = 3
y = 5


We need to determine where the point is located.

There are four possible cases:

1. Origin
2. X-axis
3. Y-axis
4. Not on an axis


RULES:

Origin:

x = 0 AND y = 0

Example:

(0, 0)

Output:

Origin


X-axis:

y = 0

Example:

(5, 0)

Output:

X-axis


Y-axis:

x = 0

Example:

(0, 5)

Output:

Y-axis


Not on an axis:

x != 0 AND y != 0

Example:

(5, 3)

Output:

Not on an axis


--------------------------------------------------
SOLUTION EXPLANATION
--------------------------------------------------

We check the conditions in a specific order.


STEP 1: CHECK ORIGIN

Condition:

x == 0 and y == 0

Both x and y must be zero.

Example:

x = 0
y = 0

Check:

0 == 0 → True
0 == 0 → True

True and True → True

Therefore:

Origin


--------------------------------------------------
STEP 2: CHECK X-AXIS
--------------------------------------------------

Condition:

y == 0

If y is zero, the point lies on the X-axis.

Example:

x = 5
y = 0

Check:

y == 0

0 == 0 → True

Therefore:

X-axis


--------------------------------------------------
STEP 3: CHECK Y-AXIS
--------------------------------------------------

Condition:

x == 0

If x is zero, the point lies on the Y-axis.

Example:

x = 0
y = 5

Check:

x == 0

0 == 0 → True

Therefore:

Y-axis


--------------------------------------------------
STEP 4: NOT ON AN AXIS
--------------------------------------------------

If x is not zero AND y is not zero, the point is not
on either axis.

Example:

x = 5
y = 3

Check:

x == 0 → False
y == 0 → False

Therefore:

Not on an axis


--------------------------------------------------
DRY RUN
--------------------------------------------------

Given:

x = 0
y = 5


STEP 1:

Check:

x == 0 and y == 0

0 == 0 → True
5 == 0 → False

True and False → False

So the Origin block is skipped.


STEP 2:

Check:

y == 0

5 == 0 → False

So the X-axis block is skipped.


STEP 3:

Check:

x == 0

0 == 0 → True

Therefore:

print("Y-axis")


OUTPUT:

Y-axis


--------------------------------------------------
DRY RUN 2: ORIGIN
--------------------------------------------------

Given:

x = 0
y = 0


Check:

x == 0 and y == 0

0 == 0 → True
0 == 0 → True

True and True → True

Output:

Origin


--------------------------------------------------
DRY RUN 3: X-AXIS
--------------------------------------------------

Given:

x = 7
y = 0


STEP 1:

x == 0 and y == 0

7 == 0 → False

Condition is False.


STEP 2:

y == 0

0 == 0 → True

Output:

X-axis


--------------------------------------------------
DRY RUN 4: NOT ON AN AXIS
--------------------------------------------------

Given:

x = 4
y = 6


STEP 1:

x == 0 and y == 0

4 == 0 → False

Skip.


STEP 2:

y == 0

6 == 0 → False

Skip.


STEP 3:

x == 0

4 == 0 → False

Skip.


STEP 4:

else block executes.

Output:

Not on an axis


--------------------------------------------------
WHY DO WE CHECK ORIGIN FIRST?
--------------------------------------------------

This is VERY important.

Consider:

x = 0
y = 0

This point satisfies:

x == 0

AND

y == 0

So it technically satisfies both the X-axis and Y-axis
conditions.

But `(0, 0)` is specifically called the ORIGIN.

Therefore, we must check:

x == 0 and y == 0

BEFORE checking:

y == 0

or:

x == 0


Correct order:

1. Origin
2. X-axis
3. Y-axis
4. Not on an axis


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

x = 0
y = 0

Output:

Origin


TEST CASE 2:

Input:

x = 0
y = 5

Output:

Y-axis


TEST CASE 3:

Input:

x = 0
y = -5

Output:

Y-axis


TEST CASE 4:

Input:

x = 5
y = 0

Output:

X-axis


TEST CASE 5:

Input:

x = -5
y = 0

Output:

X-axis


TEST CASE 6:

Input:

x = 5
y = 3

Output:

Not on an axis


TEST CASE 7:

Input:

x = -5
y = -3

Output:

Not on an axis


TEST CASE 8:

Input:

x = 10
y = -4

Output:

Not on an axis


--------------------------------------------------
QUICK TEST CASE TABLE
--------------------------------------------------

| x  | y  | Expected Output       |
|----|----|------------------------|
| 0  | 0  | Origin                 |
| 0  | 5  | Y-axis                 |
| 0  | -5 | Y-axis                 |
| 5  | 0  | X-axis                 |
| -5 | 0  | X-axis                 |
| 5  | 3  | Not on an axis         |
| -5 | -3 | Not on an axis         |
| 10 | -4 | Not on an axis         |


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Coordinates

A point is represented as:

(x, y)


2. Origin

The origin is:

(0, 0)


3. X-axis

A point lies on the X-axis when:

y == 0


4. Y-axis

A point lies on the Y-axis when:

x == 0


5. AND operator

The `and` operator requires both conditions to be True.

Example:

x == 0 and y == 0


6. Equality operator

`==` checks whether two values are equal.

Example:

x == 0


--------------------------------------------------
IMPORTANT PYTHON NOTE
--------------------------------------------------

Python uses:

and

NOT:

&&


Correct:

if x == 0 and y == 0:


Incorrect Python syntax:

if x == 0 && y == 0:


--------------------------------------------------
MAIN LOGIC TO REMEMBER
--------------------------------------------------

Point
  |
  ├── x == 0 AND y == 0
  |       ↓
  |     Origin
  |
  ├── y == 0
  |       ↓
  |     X-axis
  |
  ├── x == 0
  |       ↓
  |     Y-axis
  |
  └── Otherwise
          ↓
      Not on an axis


INTERVIEW EXPLANATION:

If an interviewer asks:

"How did you solve this problem?"

You can say:

"I first check whether both x and y are zero, because that
represents the origin. Then I check whether y is zero, which
means the point is on the X-axis. Next I check whether x is
zero, which means the point is on the Y-axis. If none of these
conditions is true, the point is not on an axis."


IMPORTANT:

The most important part of this question is understanding
WHY the origin is checked first.

(0, 0) is the origin, and it also satisfies both axis conditions.

Therefore:

Origin → checked first.
"""