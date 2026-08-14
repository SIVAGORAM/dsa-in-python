def main():
    # Question 33: Take three numbers and print the median value
    # (neither maximum nor minimum).
    a = 12
    b = 5
    c = 20

    median = 0

    if (a >= b and a <= c) or (a >= c and a <= b):
        median = a
    elif (b >= a and b <= c) or (b >= c and b <= a):
        median = b
    else:
        median = c

    print("Median =", median)


if __name__ == "__main__":
    main()


"""
Explanation:

The question asks us to take three numbers and find the median.

The median is the value that lies between the other two values.

For three different numbers:

Smallest < Median < Largest


Example:

a = 12
b = 5
c = 20

If we arrange them in ascending order:

5, 12, 20

Therefore:

Median = 12


Step 1: Check whether `a` is the median.

We check:

(a >= b and a <= c)
or
(a >= c and a <= b)

This means:

`a` must be greater than or equal to one number
AND less than or equal to the other number.

For:

a = 12
b = 5
c = 20

Check:

12 >= 5 → True
12 <= 20 → True

So:

True and True → True

Therefore:

median = 12


Another Example:

a = 5
b = 12
c = 20

Check whether `a` is the median:

5 >= 12 → False

So `a` is not the median.


Step 2: Check whether `b` is the median.

Condition:

(b >= a and b <= c)
or
(b >= c and b <= a)

For:

a = 5
b = 12
c = 20

Check:

12 >= 5 → True
12 <= 20 → True

Therefore:

median = 12


Step 3:

If neither `a` nor `b` is the median, then `c` must be
the median.

So we use:

else:
    median = c


Dry Run:

Given:

a = 12
b = 5
c = 20


First condition:

(a >= b and a <= c)

12 >= 5 → True
12 <= 20 → True

True and True → True

Therefore:

median = 12


Output:

Median = 12


Another Example:

a = 30
b = 10
c = 20

Sorted order:

10, 20, 30

Median = 20

The program checks:

`a` → Not median
`b` → Not median
`c` → Median

Output:

Median = 20


Another Example:

a = 7
b = 3
c = 5

Sorted order:

3, 5, 7

Median = 5

Output:

Median = 5


Test Cases:

1. Input:
   a = 12
   b = 5
   c = 20

   Output:
   Median = 12


2. Input:
   a = 30
   b = 10
   c = 20

   Output:
   Median = 20


3. Input:
   a = 7
   b = 3
   c = 5

   Output:
   Median = 5


4. Input:
   a = 1
   b = 2
   c = 3

   Output:
   Median = 2


5. Input:
   a = 20
   b = 10
   c = 15

   Output:
   Median = 15


6. Input:
   a = 5
   b = 5
   c = 10

   Output:
   Median = 5


7. Input:
   a = 10
   b = 20
   c = 20

   Output:
   Median = 20


Key Concepts:

`>=` → Greater than or equal to

`<=` → Less than or equal to

`and` → Both conditions must be True

`or` → At least one condition must be True

`if` → Checks the first possibility

`elif` → Checks another possibility

`else` → Used when neither previous condition is True


Important:

Python uses:

and
or

Not:

&&
||

The main idea is:

The median is the number that lies between the other two numbers.
"""