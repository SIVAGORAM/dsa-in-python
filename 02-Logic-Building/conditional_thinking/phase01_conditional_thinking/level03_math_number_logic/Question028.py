def main():
    # Question 28: Check if a number lies within the range [100, 999].
    number = 456

    if number >= 100 and number <= 999:
        print("Inside range")
    else:
        print("Outside range")


if __name__ == "__main__":
    main()


"""
Explanation:

The question asks us to check whether a given number lies within
the range [100, 999].

The notation [100, 999] means that both 100 and 999 are included.

So the number must satisfy two conditions:

number >= 100
number <= 999

Both conditions must be True.


Example:

number = 456

Step 1:
Check if the number is greater than or equal to 100.

456 >= 100 → True


Step 2:
Check if the number is less than or equal to 999.

456 <= 999 → True


Both conditions are True:

True and True → True

Therefore:
Inside range


Boundary Example 1:

number = 100

100 >= 100 → True
100 <= 999 → True

Therefore:
Inside range


Boundary Example 2:

number = 999

999 >= 100 → True
999 <= 999 → True

Therefore:
Inside range


Outside Example:

number = 50

50 >= 100 → False

Therefore:
Outside range


Another Outside Example:

number = 1000

1000 >= 100 → True
1000 <= 999 → False

Therefore:
Outside range


Test Cases:

1. Input: 456
   Output: Inside range

2. Input: 100
   Output: Inside range

3. Input: 999
   Output: Inside range

4. Input: 99
   Output: Outside range

5. Input: 1000
   Output: Outside range

6. Input: 500
   Output: Inside range

7. Input: 0
   Output: Outside range


Key Concepts:

`>=` → Greater than or equal to
`<=` → Less than or equal to
`and` → Both conditions must be True

Important:

The range `[100, 999]` is inclusive, meaning:

100 is included
999 is included

Python also allows a cleaner way to write this condition:

100 <= number <= 999

This means the same thing as:

number >= 100 and number <= 999

Python uses `and`, not `&&`.
"""