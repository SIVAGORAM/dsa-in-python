def main():
    # Question 27: Check if an amount can be evenly divided into
    # 2000, 500, and 100 currency notes.
    amount = 7600

    notes_2000 = amount // 2000
    amount %= 2000

    notes_500 = amount // 500
    amount %= 500

    notes_100 = amount // 100
    amount %= 100

    if amount == 0:
        print(
            "2000:", notes_2000,
            ", 500:", notes_500,
            ", 100:", notes_100
        )
    else:
        print("Amount cannot be fully divided into these notes")


if __name__ == "__main__":
    main()


"""
Explanation:

The question asks us to divide an amount using only these
currency notes:

2000
500
100

We need to find how many notes of each denomination are required
and check whether the entire amount can be divided without any
remaining amount.


Example:

amount = 7600


Step 1: Find the number of 2000 notes.

notes_2000 = amount // 2000

7600 // 2000 = 3

So:
notes_2000 = 3

Three 2000 notes give:

3 × 2000 = 6000

Now remove those 6000 from the amount:

7600 % 2000 = 1600

Remaining amount:
1600


Step 2: Find the number of 500 notes.

notes_500 = amount // 500

1600 // 500 = 3

So:
notes_500 = 3

Three 500 notes give:

3 × 500 = 1500

Remaining amount:

1600 % 500 = 100


Step 3: Find the number of 100 notes.

notes_100 = amount // 100

100 // 100 = 1

So:
notes_100 = 1

Remaining amount:

100 % 100 = 0


Since the remaining amount is 0:

amount == 0 → True

Therefore:

2000: 3
500: 3
100: 1


The total is:

3 × 2000 = 6000
3 × 500  = 1500
1 × 100  = 100

Total = 7600


Another Example:

amount = 7500

2000 notes:
7500 // 2000 = 3
Remaining = 1500

500 notes:
1500 // 500 = 3
Remaining = 0

100 notes:
0 // 100 = 0

Therefore:

2000: 3
500: 3
100: 0


Example where the amount cannot be fully divided:

amount = 7650

2000 notes:
7650 // 2000 = 3
Remaining = 1650

500 notes:
1650 // 500 = 3
Remaining = 150

100 notes:
150 // 100 = 1
Remaining = 50

The remaining amount is 50.

Since:

amount == 0 → False

Therefore:

Amount cannot be fully divided into these notes


Test Cases:

1. Input: 7600
   Output:
   2000: 3, 500: 3, 100: 1

2. Input: 7500
   Output:
   2000: 3, 500: 3, 100: 0

3. Input: 1000
   Output:
   2000: 0, 500: 2, 100: 0

4. Input: 2000
   Output:
   2000: 1, 500: 0, 100: 0

5. Input: 7650
   Output:
   Amount cannot be fully divided into these notes

6. Input: 50
   Output:
   Amount cannot be fully divided into these notes

7. Input: 0
   Output:
   2000: 0, 500: 0, 100: 0


Key Concepts:

// → Integer division
%  → Remainder
== → Equality comparison

Example:

7600 // 2000 → 3
7600 % 2000  → 1600

Important:

Use `//` when you want the whole-number count of notes.

Do not use `/` here because:

7600 / 2000 → 3.8

while:

7600 // 2000 → 3

Also remember:

`amount %= 2000`

is shorthand for:

`amount = amount % 2000`

It updates the remaining amount after taking the larger notes.
"""