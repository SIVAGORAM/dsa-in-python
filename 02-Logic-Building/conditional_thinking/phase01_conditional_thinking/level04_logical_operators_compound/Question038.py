def main():
    # Question 38: Take a day number (1-7) and print the corresponding day name.
    day = 3

    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    if 1 <= day <= 7:
        print(days[day - 1])
    else:
        print("Invalid day")


if __name__ == "__main__":
    main()


"""
Explanation:

The question asks us to take a day number from 1 to 7 and print
the corresponding day name.

The days are stored in a list:

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]


Important:

Python lists use zero-based indexing.

That means:

Index 0 → Monday
Index 1 → Tuesday
Index 2 → Wednesday
Index 3 → Thursday
Index 4 → Friday
Index 5 → Saturday
Index 6 → Sunday


But the question gives day numbers from 1 to 7.

Therefore, we need to subtract 1 from the day number:

day - 1


Mapping:

Day 1 → days[0] → Monday
Day 2 → days[1] → Tuesday
Day 3 → days[2] → Wednesday
Day 4 → days[3] → Thursday
Day 5 → days[4] → Friday
Day 6 → days[5] → Saturday
Day 7 → days[6] → Sunday


Dry Run:

Given:

day = 3


Step 1:

Check whether the day is valid:

1 <= day <= 7

1 <= 3 → True
3 <= 7 → True

Therefore:

The day is valid.


Step 2:

Calculate the list index:

day - 1

3 - 1 = 2


Step 3:

Access the list:

days[2]

Because Python starts indexing from 0:

days[2] = "Wednesday"


Output:

Wednesday


Another Example:

day = 1

Check:

1 <= 1 <= 7 → True

Index:

1 - 1 = 0

days[0] → "Monday"

Output:

Monday


Boundary Example:

day = 7

Check:

1 <= 7 <= 7 → True

Index:

7 - 1 = 6

days[6] → "Sunday"

Output:

Sunday


Invalid Example:

day = 8

Check:

1 <= 8 <= 7 → False

Therefore:

Invalid day


Another Invalid Example:

day = 0

Check:

1 <= 0 → False

Therefore:

Invalid day


Test Cases:

1. Input:
   day = 1

   Output:
   Monday


2. Input:
   day = 2

   Output:
   Tuesday


3. Input:
   day = 3

   Output:
   Wednesday


4. Input:
   day = 4

   Output:
   Thursday


5. Input:
   day = 5

   Output:
   Friday


6. Input:
   day = 6

   Output:
   Saturday


7. Input:
   day = 7

   Output:
   Sunday


8. Input:
   day = 0

   Output:
   Invalid day


9. Input:
   day = 8

   Output:
   Invalid day


Key Concepts:

List → Ordered collection of values.

Index → Position of an item in a list.

Python uses zero-based indexing:

days[0] → Monday
days[1] → Tuesday
days[2] → Wednesday

The important conversion is:

day - 1

because the question uses:

1 → Monday
2 → Tuesday
...
7 → Sunday

while Python uses:

0 → Monday
1 → Tuesday
...
6 → Sunday


Important:

The condition:

1 <= day <= 7

is Python's chained comparison.

It means:

day >= 1 and day <= 7

Both are equivalent.
"""