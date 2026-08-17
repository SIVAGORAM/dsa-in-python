def main():
    # Question 43: Take day and month and check if it forms
    # a valid calendar date (ignoring leap years).

    day = 29
    month = 2

    if month < 1 or month > 12:
        print("Invalid date")
    elif month == 2:
        if day >= 1 and day <= 28:
            print("Valid date")
        else:
            print("Invalid date")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day >= 1 and day <= 30:
            print("Valid date")
        else:
            print("Invalid date")
    else:
        if day >= 1 and day <= 31:
            print("Valid date")
        else:
            print("Invalid date")


if __name__ == "__main__":
    main()


"""
QUESTION:

Take day and month and check if it forms a valid calendar date
(ignoring leap years).


WHAT DOES THE QUESTION MEAN?

We are given:

1. Day
2. Month

We need to determine whether that combination represents a
valid calendar date.

For example:

day = 15
month = 8

August has 31 days.

Therefore:

15 August → Valid date


But:

day = 31
month = 4

April has only 30 days.

Therefore:

31 April → Invalid date


--------------------------------------------------
IMPORTANT:
--------------------------------------------------

The question says:

"ignoring leap years"

That means February always has:

28 days

We do NOT need to check whether the year is a leap year.

Therefore:

February 29 → Invalid date


--------------------------------------------------
NUMBER OF DAYS IN EACH MONTH
--------------------------------------------------

January   → 31
February  → 28
March     → 31
April     → 30
May       → 31
June      → 30
July      → 31
August    → 31
September → 30
October   → 31
November  → 30
December  → 31


--------------------------------------------------
SOLUTION LOGIC
--------------------------------------------------

We check the month first.

STEP 1:

Check whether the month is valid.

A valid month must be between:

1 and 12

Condition:

month < 1 or month > 12

If this is True:

Invalid date


--------------------------------------------------
STEP 2: FEBRUARY
--------------------------------------------------

If:

month == 2

February has 28 days because we are ignoring leap years.

Therefore:

day >= 1 and day <= 28

If True:

Valid date

Otherwise:

Invalid date


--------------------------------------------------
STEP 3: MONTHS WITH 30 DAYS
--------------------------------------------------

These months have 30 days:

April  → 4
June   → 6
September → 9
November → 11

So we check:

month == 4 or month == 6 or month == 9 or month == 11

For these months:

day must be between:

1 and 30


--------------------------------------------------
STEP 4: MONTHS WITH 31 DAYS
--------------------------------------------------

The remaining valid months have 31 days:

January
March
May
July
August
October
December

For these months:

day must be between:

1 and 31


--------------------------------------------------
DRY RUN 1: VALID DATE
--------------------------------------------------

Given:

day = 29
month = 2


STEP 1:

Check month:

month < 1 or month > 12

2 < 1 → False
2 > 12 → False

Therefore:

Month is valid.


STEP 2:

Check:

month == 2

2 == 2 → True

So this is February.


STEP 3:

Check:

day >= 1 and day <= 28

29 >= 1 → True
29 <= 28 → False

True and False → False

Therefore:

Invalid date


Output:

Invalid date


IMPORTANT:

29 February is invalid here because the question says
to ignore leap years.


--------------------------------------------------
DRY RUN 2: VALID FEBRUARY DATE
--------------------------------------------------

Given:

day = 28
month = 2


Month is valid.

month == 2 → True


Check:

28 >= 1 → True
28 <= 28 → True

True and True → True

Output:

Valid date


--------------------------------------------------
DRY RUN 3: 30-DAY MONTH
--------------------------------------------------

Given:

day = 30
month = 4


Month:

4 is valid.


Check:

month == 2

False


Check whether it is a 30-day month:

month == 4 → True

Therefore:

April has 30 days.


Check:

30 >= 1 → True
30 <= 30 → True

Therefore:

Valid date


Output:

Valid date


--------------------------------------------------
DRY RUN 4: INVALID 30-DAY MONTH
--------------------------------------------------

Given:

day = 31
month = 4


April has only 30 days.

Check:

31 >= 1 → True
31 <= 30 → False

Therefore:

Invalid date


Output:

Invalid date


--------------------------------------------------
DRY RUN 5: 31-DAY MONTH
--------------------------------------------------

Given:

day = 31
month = 8


August is a 31-day month.


Check:

31 >= 1 → True
31 <= 31 → True

Therefore:

Valid date


Output:

Valid date


--------------------------------------------------
DRY RUN 6: INVALID MONTH
--------------------------------------------------

Given:

day = 10
month = 13


Check:

month < 1 or month > 12

13 < 1 → False
13 > 12 → True

False or True → True

Therefore:

Invalid date


Output:

Invalid date


--------------------------------------------------
DRY RUN 7: INVALID DAY
--------------------------------------------------

Given:

day = 0
month = 5


May is a valid month.

May has 31 days.

But:

day >= 1

0 >= 1 → False

Therefore:

Invalid date


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

day = 15
month = 8

Output:

Valid date


TEST CASE 2:

Input:

day = 28
month = 2

Output:

Valid date


TEST CASE 3:

Input:

day = 29
month = 2

Output:

Invalid date


TEST CASE 4:

Input:

day = 30
month = 4

Output:

Valid date


TEST CASE 5:

Input:

day = 31
month = 4

Output:

Invalid date


TEST CASE 6:

Input:

day = 31
month = 8

Output:

Valid date


TEST CASE 7:

Input:

day = 31
month = 12

Output:

Valid date


TEST CASE 8:

Input:

day = 32
month = 12

Output:

Invalid date


TEST CASE 9:

Input:

day = 1
month = 1

Output:

Valid date


TEST CASE 10:

Input:

day = 0
month = 5

Output:

Invalid date


TEST CASE 11:

Input:

day = 10
month = 0

Output:

Invalid date


TEST CASE 12:

Input:

day = 10
month = 13

Output:

Invalid date


--------------------------------------------------
TEST CASE TABLE
--------------------------------------------------

| Day | Month | Expected Output |
|-----|-------|------------------|
| 15  | 8     | Valid date |
| 28  | 2     | Valid date |
| 29  | 2     | Invalid date |
| 30  | 4     | Valid date |
| 31  | 4     | Invalid date |
| 31  | 8     | Valid date |
| 31  | 12    | Valid date |
| 32  | 12    | Invalid date |
| 1   | 1     | Valid date |
| 0   | 5     | Invalid date |
| 10  | 0     | Invalid date |
| 10  | 13    | Invalid date |


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Month validation

A month must be:

1 <= month <= 12


2. Day validation

A day must be at least:

1


The maximum depends on the month.


3. February

Because leap years are ignored:

February → 28 days


4. 30-day months

April
June
September
November


5. 31-day months

January
March
May
July
August
October
December


--------------------------------------------------
IMPORTANT PYTHON OPERATORS
--------------------------------------------------

Python uses:

and

or

Not:

&&
||


For example:

Correct:

if day >= 1 and day <= 28:


Correct:

if month == 4 or month == 6:


Incorrect Python syntax:

if month == 4 || month == 6:


--------------------------------------------------
YOUR ORIGINAL CODE
--------------------------------------------------

Your original code was:

year = 2024

and then checked:

year % 400
year % 4
year % 100

That logic is for determining whether a YEAR is a leap year.

But Question 43 asks us to check:

day + month

So `year` is not needed for this question.


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How did you solve this problem?"

You can say:

"First, I validate that the month is between 1 and 12.
Then I handle February separately because it has 28 days when
leap years are ignored. Next, I handle the months with 30 days.
All remaining valid months have 31 days. Finally, I check whether
the given day falls within the allowed range for that month."


--------------------------------------------------
MAIN LOGIC TO REMEMBER
--------------------------------------------------

Day + Month
     ↓
Is month between 1 and 12?
     ↓
Is it February?
     ↓
Is it a 30-day month?
     ↓
Otherwise it is a 31-day month
     ↓
Check whether day is within the allowed range
     ↓
Valid / Invalid date
"""