def main():
    # Question 42: Take three numbers and check if they can form a Pythagorean triplet.

    a = 3
    b = 4
    c = 5

    if a * a + b * b == c * c or \
       a * a + c * c == b * b or \
       b * b + c * c == a * a:
        print("Pythagorean triplet")
    else:
        print("Not a Pythagorean triplet")


if __name__ == "__main__":
    main()


"""
QUESTION:

Take three numbers and check if they can form a Pythagorean triplet.


WHAT IS A PYTHAGOREAN TRIPLET?

Three positive numbers form a Pythagorean triplet if they satisfy
the Pythagorean theorem.

The Pythagorean theorem is:

a² + b² = c²

where `c` is the hypotenuse (the largest side).


Example:

3, 4, 5

Because:

3² + 4² = 5²

9 + 16 = 25

Therefore:

3, 4, 5 is a Pythagorean triplet.


--------------------------------------------------
WHY DO WE CHECK THREE CONDITIONS?
--------------------------------------------------

The three numbers can be given in ANY order.

For example:

3, 4, 5

Here:

3² + 4² = 5²


But the input could also be:

5, 3, 4

Now:

3² + 4² = 5²

So we need to check all three possibilities.

Condition 1:

a² + b² = c²

Condition 2:

a² + c² = b²

Condition 3:

b² + c² = a²


In Python:

a * a + b * b == c * c

OR:

a * a + c * c == b * b

OR:

b * b + c * c == a * a


If ANY ONE of these conditions is True,
the numbers form a Pythagorean triplet.


--------------------------------------------------
SOLUTION EXPLANATION
--------------------------------------------------

The program takes three numbers:

a
b
c

Then it checks all three possible combinations.

We use:

or

because only ONE valid Pythagorean relationship is required.


--------------------------------------------------
EXAMPLE 1
--------------------------------------------------

Given:

a = 3
b = 4
c = 5


Check the first condition:

a * a + b * b == c * c

Calculate:

3 * 3 + 4 * 4 == 5 * 5

9 + 16 == 25

25 == 25

True


Because the first condition is True:

Output:

Pythagorean triplet


--------------------------------------------------
DRY RUN
--------------------------------------------------

Given:

a = 3
b = 4
c = 5


STEP 1:

Calculate:

a * a

3 * 3 = 9


STEP 2:

Calculate:

b * b

4 * 4 = 16


STEP 3:

Calculate:

c * c

5 * 5 = 25


STEP 4:

Check:

9 + 16 == 25

25 == 25

True


Therefore:

Pythagorean triplet


Output:

Pythagorean triplet


--------------------------------------------------
EXAMPLE 2: NUMBERS IN DIFFERENT ORDER
--------------------------------------------------

Given:

a = 5
b = 3
c = 4


First condition:

5² + 3² = 4²

25 + 9 = 16

34 = 16

False


Second condition:

5² + 4² = 3²

25 + 16 = 9

41 = 9

False


Third condition:

3² + 4² = 5²

9 + 16 = 25

25 = 25

True


Therefore:

Pythagorean triplet


This is why we check all three possibilities.


--------------------------------------------------
EXAMPLE 3: NOT A PYTHAGOREAN TRIPLET
--------------------------------------------------

Given:

a = 2
b = 3
c = 4


Check:

2² + 3² = 4²

4 + 9 = 16

13 = 16

False


Second:

2² + 4² = 3²

4 + 16 = 9

20 = 9

False


Third:

3² + 4² = 2²

9 + 16 = 4

25 = 4

False


All three conditions are False.

Therefore:

Not a Pythagorean triplet


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

a = 3
b = 4
c = 5

Output:

Pythagorean triplet


TEST CASE 2:

Input:

a = 5
b = 3
c = 4

Output:

Pythagorean triplet


TEST CASE 3:

Input:

a = 4
b = 5
c = 3

Output:

Pythagorean triplet


TEST CASE 4:

Input:

a = 5
b = 12
c = 13

Output:

Pythagorean triplet


TEST CASE 5:

Input:

a = 8
b = 15
c = 17

Output:

Pythagorean triplet


TEST CASE 6:

Input:

a = 2
b = 3
c = 4

Output:

Not a Pythagorean triplet


TEST CASE 7:

Input:

a = 5
b = 5
c = 5

Output:

Not a Pythagorean triplet


--------------------------------------------------
TEST CASE TABLE
--------------------------------------------------

| a | b | c | Expected Output |
|---|---|---|------------------|
| 3 | 4 | 5 | Pythagorean triplet |
| 5 | 3 | 4 | Pythagorean triplet |
| 4 | 5 | 3 | Pythagorean triplet |
| 5 | 12 | 13 | Pythagorean triplet |
| 8 | 15 | 17 | Pythagorean triplet |
| 2 | 3 | 4 | Not a Pythagorean triplet |
| 5 | 5 | 5 | Not a Pythagorean triplet |


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Pythagorean Theorem

a² + b² = c²


2. Squaring a number

In Python:

a * a

Example:

5 * 5 = 25


3. `or`

The `or` operator means:

At least ONE condition must be True.


Example:

True or False → True

False or True → True

False or False → False


4. `==`

Checks whether two values are equal.


--------------------------------------------------
IMPORTANT PYTHON NOTE
--------------------------------------------------

Your original explanation used:

||

That is NOT the Python OR operator.

Python uses:

or


Correct:

if condition1 or condition2 or condition3:


Not:

if condition1 || condition2 || condition3:


--------------------------------------------------
IMPORTANT LOGIC
--------------------------------------------------

The key idea is:

Three numbers
      ↓
Check whether any two squared values
add up to the third squared value
      ↓
YES → Pythagorean triplet
NO  → Not a Pythagorean triplet


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How did you solve this problem?"

You can say:

"I used the Pythagorean theorem, a² + b² = c².
Since the three numbers can be given in any order, I check
all three possible combinations using the `or` operator.
If any one condition is true, the numbers form a
Pythagorean triplet."


--------------------------------------------------
IMPORTANT NOTE
--------------------------------------------------

For the usual mathematical definition, a Pythagorean triplet
consists of positive integers.

The current solution checks the three squared relationships,
which is the logic used for this practice question.
"""