def main():
    # Question 49: Take two dates (day and month) and determine
    # which one comes first in the calendar.

    day1 = 12
    month1 = 5

    day2 = 10
    month2 = 6

    if month1 < month2 or (month1 == month2 and day1 < day2):
        print("First date comes first")
    elif month1 == month2 and day1 == day2:
        print("Both dates are same")
    else:
        print("Second date comes first")


if __name__ == "__main__":
    main()


"""
QUESTION:

Take two dates (day and month) and determine which one comes
first in the calendar.


WHAT DOES THE QUESTION MEAN?

We are given two dates.

Date 1:

day1
month1


Date 2:

day2
month2


We need to compare them and determine:

1. First date comes first
2. Both dates are the same
3. Second date comes first


--------------------------------------------------
IMPORTANT IDEA
--------------------------------------------------

When comparing dates without considering the year:

FIRST compare the MONTH.

If the months are different:

The smaller month comes first.


Example:

12 May
10 June

May = month 5
June = month 6

5 < 6

Therefore:

12 May comes before 10 June.


--------------------------------------------------
WHAT IF BOTH MONTHS ARE SAME?
--------------------------------------------------

Then we compare the DAY.

Example:

10 May
20 May

Months are equal:

5 == 5

So compare:

10 < 20

Therefore:

10 May comes first.


--------------------------------------------------
WHAT IF BOTH DAY AND MONTH ARE SAME?
--------------------------------------------------

Example:

12 May
12 May

Month:

5 == 5

Day:

12 == 12

Therefore:

Both dates are same.


--------------------------------------------------
SOLUTION LOGIC
--------------------------------------------------

We first check whether Date 1 comes before Date 2.

Condition:

month1 < month2

OR

month1 == month2 AND day1 < day2


In Python:

if month1 < month2 or (month1 == month2 and day1 < day2):


If this is True:

First date comes first.


--------------------------------------------------
STEP 2: CHECK SAME DATE
--------------------------------------------------

If Date 1 did not come first, we check:

month1 == month2 and day1 == day2


If both are equal:

Both dates are same.


--------------------------------------------------
STEP 3: OTHERWISE
--------------------------------------------------

If neither of the above conditions is true:

Second date comes first.


--------------------------------------------------
DRY RUN 1
--------------------------------------------------

Given:

day1 = 12
month1 = 5

day2 = 10
month2 = 6


Date 1:

12 May


Date 2:

10 June


STEP 1:

Check:

month1 < month2

5 < 6

True


Because the first condition is already True:

First date comes first.


Output:

First date comes first


--------------------------------------------------
DRY RUN 2 — SAME MONTH
--------------------------------------------------

Given:

day1 = 10
month1 = 5

day2 = 20
month2 = 5


First:

month1 < month2

5 < 5

False


Now:

month1 == month2 and day1 < day2


5 == 5 → True

10 < 20 → True

True and True → True


Therefore:

First date comes first.


--------------------------------------------------
DRY RUN 3 — SECOND DATE FIRST
--------------------------------------------------

Given:

day1 = 20
month1 = 5

day2 = 10
month2 = 5


Check:

month1 < month2

5 < 5 → False


Check:

month1 == month2 and day1 < day2

5 == 5 → True

20 < 10 → False

True and False → False


Check same date:

month1 == month2 and day1 == day2

5 == 5 → True

20 == 10 → False

True and False → False


Therefore:

else block executes.


Output:

Second date comes first.


--------------------------------------------------
DRY RUN 4 — SAME DATE
--------------------------------------------------

Given:

day1 = 12
month1 = 5

day2 = 12
month2 = 5


First condition:

month1 < month2

5 < 5 → False


Second part:

month1 == month2 and day1 < day2

5 == 5 → True

12 < 12 → False

True and False → False


Now check:

month1 == month2 and day1 == day2

5 == 5 → True

12 == 12 → True

True and True → True


Output:

Both dates are same.


--------------------------------------------------
EXAMPLE 5
--------------------------------------------------

Date 1:

1 January

Date 2:

31 December


Months:

1 < 12

True


Therefore:

First date comes first.


--------------------------------------------------
EXAMPLE 6
--------------------------------------------------

Date 1:

31 December

Date 2:

1 January


Months:

12 < 1

False


Same month?

12 == 1

False


Therefore:

Second date comes first.


--------------------------------------------------
EXAMPLE 7
--------------------------------------------------

Date 1:

5 August

Date 2:

10 August


Months:

8 == 8


Compare days:

5 < 10


Therefore:

First date comes first.


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Date 1:

12/5

Date 2:

10/6

Output:

First date comes first


TEST CASE 2:

Date 1:

10/5

Date 2:

20/5

Output:

First date comes first


TEST CASE 3:

Date 1:

20/5

Date 2:

10/5

Output:

Second date comes first


TEST CASE 4:

Date 1:

12/5

Date 2:

12/5

Output:

Both dates are same


TEST CASE 5:

Date 1:

1/1

Date 2:

31/12

Output:

First date comes first


TEST CASE 6:

Date 1:

31/12

Date 2:

1/1

Output:

Second date comes first


TEST CASE 7:

Date 1:

5/8

Date 2:

10/8

Output:

First date comes first


TEST CASE 8:

Date 1:

20/10

Date 2:

15/9

Output:

Second date comes first


--------------------------------------------------
TEST CASE TABLE
--------------------------------------------------

| Date 1 | Date 2 | Expected Output |
|--------|--------|------------------|
| 12/5 | 10/6 | First date comes first |
| 10/5 | 20/5 | First date comes first |
| 20/5 | 10/5 | Second date comes first |
| 12/5 | 12/5 | Both dates are same |
| 1/1 | 31/12 | First date comes first |
| 31/12 | 1/1 | Second date comes first |
| 5/8 | 10/8 | First date comes first |
| 20/10 | 15/9 | Second date comes first |


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Comparing months

If:

month1 < month2

Date 1 comes earlier.


2. Comparing days

If the months are equal, compare the days.


3. `and`

Both conditions must be True.

Example:

month1 == month2 and day1 < day2


4. `or`

At least one condition must be True.

Example:

month1 < month2 or ...


--------------------------------------------------
IMPORTANT LOGIC
--------------------------------------------------

Date 1
   ↓
Compare months
   ↓
Are months different?
   ↓
YES → Smaller month comes first
   ↓
NO
   ↓
Compare days
   ↓
Smaller day comes first


--------------------------------------------------
SIMPLE MEMORY TRICK
--------------------------------------------------

When comparing two dates:

MONTH FIRST
     ↓
DAY SECOND


Example:

12 May
10 June

Compare:

May → 5
June → 6

5 < 6

Therefore:

12 May comes first.


If months are equal:

10 May
20 May

Compare:

10 < 20

Therefore:

10 May comes first.


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How did you solve this problem?"

You can say:

"I first compare the months because the earlier month always
comes first. If both months are equal, I compare the days.
If both the month and day are equal, the dates are the same.
Otherwise, the second date comes first."


--------------------------------------------------
IMPORTANT NOTE
--------------------------------------------------

This problem only gives:

Day
Month

There is no year.

Therefore, we are only comparing the dates within the
same calendar year.

Also, this logic assumes the provided day and month values
are valid calendar dates.


--------------------------------------------------
MAIN LOGIC TO REMEMBER
--------------------------------------------------

if month1 < month2
   OR
   (same month AND day1 < day2)

        ↓

First date comes first


elif same month AND same day

        ↓

Both dates are same


else

        ↓

Second date comes first
"""