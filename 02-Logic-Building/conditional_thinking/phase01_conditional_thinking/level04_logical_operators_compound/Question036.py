def main():
    # Question 36: Take two numbers and check if both are positive
    # and their sum is less than 100.
    first = 30
    second = 40

    if first > 0 and second > 0 and first + second < 100:
        print("Condition satisfied")
    else:
        print("Condition not satisfied")


if __name__ == "__main__":
    main()


"""
Explanation:

The question gives us two numbers:

1. first
2. second

We need to check THREE conditions:

1. The first number must be positive.
2. The second number must be positive.
3. Their sum must be less than 100.

Because ALL three conditions must be True, we use `and`.


Example:

first = 30
second = 40


Step 1: Check whether the first number is positive.

first > 0

30 > 0 → True


Step 2: Check whether the second number is positive.

second > 0

40 > 0 → True


Step 3: Calculate their sum.

first + second

30 + 40 = 70


Step 4: Check whether the sum is less than 100.

70 < 100 → True


Now combine all three conditions:

True and True and True → True

Therefore:

Condition satisfied


Dry Run:

Given:

first = 30
second = 40

Check:

30 > 0 → True
40 > 0 → True
30 + 40 = 70
70 < 100 → True

All conditions are True.

Output:

Condition satisfied


Another Example:

first = 50
second = 60

Check:

50 > 0 → True
60 > 0 → True

Sum:

50 + 60 = 110

Check:

110 < 100 → False

Therefore:

Condition not satisfied


Another Example:

first = -10
second = 20

Check:

-10 > 0 → False
20 > 0 → True

Since one condition is False:

False and True → False

Therefore:

Condition not satisfied


Boundary Example:

first = 50
second = 50

Both numbers are positive:

50 > 0 → True
50 > 0 → True

Sum:

50 + 50 = 100

Check:

100 < 100 → False

Therefore:

Condition not satisfied

This is because the question says the sum must be LESS THAN 100,
not less than or equal to 100.


Test Cases:

1. Input:
   first = 30
   second = 40

   Output:
   Condition satisfied


2. Input:
   first = 10
   second = 20

   Output:
   Condition satisfied


3. Input:
   first = 50
   second = 50

   Output:
   Condition not satisfied


4. Input:
   first = 60
   second = 40

   Output:
   Condition not satisfied


5. Input:
   first = -10
   second = 20

   Output:
   Condition not satisfied


6. Input:
   first = 0
   second = 20

   Output:
   Condition not satisfied


7. Input:
   first = 99
   second = 1

   Output:
   Condition not satisfied


Key Concepts:

`>`   → Greater than

`<`   → Less than

`+`   → Addition

`and` → All conditions must be True.

Important:

The condition:

first > 0 and second > 0 and first + second < 100

means:

Both numbers must be positive
AND
Their sum must be less than 100.

Python uses:

and

Not:

&&
"""