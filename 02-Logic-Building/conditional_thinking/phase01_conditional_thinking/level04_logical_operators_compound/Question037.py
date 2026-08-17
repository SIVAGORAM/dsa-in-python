def main():
    # Question 37: Take a single digit (0-9) and print its word form ("Zero" to "Nine").
    digit = 7

    words = [
        "Zero",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine"
    ]

    if digit >= 0 and digit <= 9:
        print(words[digit])
    else:
        print("Invalid digit")


if __name__ == "__main__":
    main()


"""
Explanation:

The question asks us to take a single digit from 0 to 9 and print
its corresponding word.

For example:

0 → Zero
1 → One
2 → Two
3 → Three
...
9 → Nine


We store the words in a list.

The list is:

words = [
    "Zero",    # index 0
    "One",     # index 1
    "Two",     # index 2
    "Three",   # index 3
    "Four",    # index 4
    "Five",    # index 5
    "Six",     # index 6
    "Seven",   # index 7
    "Eight",   # index 8
    "Nine"     # index 9
]


Python lists use zero-based indexing.

That means:

words[0] → "Zero"
words[1] → "One"
words[2] → "Two"
words[3] → "Three"
...
words[9] → "Nine"


Example:

digit = 7

First we check whether the digit is valid:

digit >= 0 and digit <= 9

7 >= 0 → True
7 <= 9 → True

Both conditions are True.

Therefore, we can safely use:

words[7]

words[7] → "Seven"

Output:

Seven


Dry Run:

Given:

digit = 7

Step 1:

Check:

7 >= 0 → True

Step 2:

Check:

7 <= 9 → True

Therefore:

True and True → True


Step 3:

Access the list using the digit as the index:

words[7]

Result:

"Seven"


Output:

Seven


Another Example:

digit = 3

Check:

3 >= 0 → True
3 <= 9 → True

Access:

words[3]

Result:

"Three"

Output:

Three


Boundary Example:

digit = 0

Check:

0 >= 0 → True
0 <= 9 → True

Access:

words[0]

Result:

"Zero"

Output:

Zero


Boundary Example:

digit = 9

Check:

9 >= 0 → True
9 <= 9 → True

Access:

words[9]

Result:

"Nine"

Output:

Nine


Invalid Example:

digit = 12

Check:

12 >= 0 → True
12 <= 9 → False

Because the condition is False:

Output:

Invalid digit


Another Invalid Example:

digit = -1

Check:

-1 >= 0 → False

Therefore:

Invalid digit


Test Cases:

1. Input:
   digit = 0

   Output:
   Zero


2. Input:
   digit = 1

   Output:
   One


3. Input:
   digit = 5

   Output:
   Five


4. Input:
   digit = 7

   Output:
   Seven


5. Input:
   digit = 9

   Output:
   Nine


6. Input:
   digit = 10

   Output:
   Invalid digit


7. Input:
   digit = -1

   Output:
   Invalid digit


Key Concepts:

List → Ordered collection of values.

Index → Position of an item in a list.

Python uses zero-based indexing:

words[0] → First item
words[1] → Second item
words[9] → Tenth item


Important Python Difference:

Your original code used:

words = {"Zero", "One", "Two", ...}

This creates a SET.

A set is unordered and cannot be accessed like:

words[digit]

So this would cause an error.

Use a LIST:

words = ["Zero", "One", "Two", ...]


Also remember:

Python uses:

and

Not:

&&
"""