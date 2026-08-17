def main():
    # Question 35: Take income and age, and check if eligible for tax
    # (age > 18 and income > 5 L).
    age = 25
    income = 600000

    if age > 18 and income > 500000:
        print("Eligible for tax")
    else:
        print("Not eligible for tax")


if __name__ == "__main__":
    main()


"""
Explanation:

The question gives us two values:

1. Age
2. Income

We need to check whether BOTH conditions are satisfied:

1. Age must be greater than 18.
2. Income must be greater than ₹5,00,000.

Because both conditions must be True, we use the `and` operator.


Example:

age = 25
income = 600000


Step 1: Check the age condition.

age > 18

25 > 18 → True


Step 2: Check the income condition.

income > 500000

600000 > 500000 → True


Step 3: Combine both conditions.

True and True → True

Therefore:

Eligible for tax


Dry Run:

Given:

age = 25
income = 600000

Check:

25 > 18 → True
600000 > 500000 → True

Both conditions are True.

Output:

Eligible for tax


Another Example:

age = 17
income = 600000

Age condition:

17 > 18 → False

Income condition:

600000 > 500000 → True

Combine:

False and True → False

Therefore:

Not eligible for tax


Another Example:

age = 25
income = 400000

Age condition:

25 > 18 → True

Income condition:

400000 > 500000 → False

Combine:

True and False → False

Therefore:

Not eligible for tax


Boundary Example:

age = 18
income = 600000

Age condition:

18 > 18 → False

Therefore:

Not eligible for tax

This is because the question says `age > 18`, not `age >= 18`.


Boundary Example:

age = 25
income = 500000

Income condition:

500000 > 500000 → False

Therefore:

Not eligible for tax

This is because the question says `income > 500000`, not
`income >= 500000`.


Test Cases:

1. Input:
   age = 25
   income = 600000

   Output:
   Eligible for tax


2. Input:
   age = 17
   income = 600000

   Output:
   Not eligible for tax


3. Input:
   age = 25
   income = 400000

   Output:
   Not eligible for tax


4. Input:
   age = 18
   income = 600000

   Output:
   Not eligible for tax


5. Input:
   age = 25
   income = 500000

   Output:
   Not eligible for tax


6. Input:
   age = 30
   income = 1000000

   Output:
   Eligible for tax


Key Concepts:

`>`   → Greater than

`and` → Both conditions must be True.

`if`  → Executes when the condition is True.

`else` → Executes when the condition is False.


Important:

The question uses:

age > 18
income > 500000

Therefore, exactly 18 and exactly 500000 do NOT satisfy the conditions.

Python uses:

and

Not:

&&
"""