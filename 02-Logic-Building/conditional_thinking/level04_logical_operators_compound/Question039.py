def main():
    # Question 39: Calculate electricity bill based on units using slab rates.
    units = 150

    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

    print("Bill =", bill)


if __name__ == "__main__":
    main()


"""
Explanation:

The question asks us to calculate an electricity bill based on
the number of units consumed.

The electricity charges are divided into slabs:

First 100 units:
₹5 per unit

Next 100 units (101 to 200):
₹7 per unit

Above 200 units:
₹10 per unit


The important idea is that when the usage goes into a higher slab,
we do NOT charge all the units at the higher rate.

Each slab has its own rate.


Example:

units = 150


Step 1:

150 is greater than 100, but less than or equal to 200.

Therefore, the `elif` block runs:

bill = 100 * 5 + (units - 100) * 7


Step 2:

Calculate the first 100 units:

100 * 5 = 500


Step 3:

Calculate the remaining units:

150 - 100 = 50

These 50 units belong to the second slab.

50 * 7 = 350


Step 4:

Add both amounts:

500 + 350 = 850


Therefore:

Bill = 850


Dry Run:

Given:

units = 150

Check:

150 <= 100 → False

Move to `elif`:

150 <= 200 → True

Calculate:

100 * 5 = 500
150 - 100 = 50
50 * 7 = 350

Total:

500 + 350 = 850

Output:

Bill = 850


Another Example:

units = 80

Since:

80 <= 100 → True

Calculate:

80 * 5 = 400

Output:

Bill = 400


Another Example:

units = 250

250 <= 100 → False
250 <= 200 → False

Therefore, the `else` block runs.

First 100 units:

100 * 5 = 500

Next 100 units:

100 * 7 = 700

Remaining units:

250 - 200 = 50

50 * 10 = 500

Total:

500 + 700 + 500 = 1700

Output:

Bill = 1700


Boundary Example:

units = 100

100 <= 100 → True

Bill:

100 * 5 = 500

Output:

Bill = 500


Boundary Example:

units = 200

200 <= 100 → False
200 <= 200 → True

First 100 units:

100 * 5 = 500

Next 100 units:

100 * 7 = 700

Total:

500 + 700 = 1200

Output:

Bill = 1200


Test Cases:

1. Input:
   units = 50

   Output:
   Bill = 250


2. Input:
   units = 100

   Output:
   Bill = 500


3. Input:
   units = 150

   Output:
   Bill = 850


4. Input:
   units = 200

   Output:
   Bill = 1200


5. Input:
   units = 250

   Output:
   Bill = 1700


6. Input:
   units = 300

   Output:
   Bill = 2200


Key Concepts:

`if` → Handles the first slab.

`elif` → Handles the second slab.

`else` → Handles usage above 200 units.

`*` → Multiplication.

`-` → Calculates the units remaining after a slab.

Important:

This is called SLAB-BASED calculation.

For 150 units, we do NOT calculate:

150 * 7

Instead:

First 100 units → 100 * 5
Remaining 50 units → 50 * 7

Total → 850


The general idea is:

First slab
    ↓
Second slab
    ↓
Third slab

Each portion is charged according to its own rate.
"""