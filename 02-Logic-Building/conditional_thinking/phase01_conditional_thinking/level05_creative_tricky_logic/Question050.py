def main():
    # Question 50: Take a year and print the corresponding century.
    year = 1998

    century = (year + 99) // 100

    print(str(century) + "th century")


if __name__ == "__main__":
    main()


"""
QUESTION:

Take a year and print the corresponding century.

Examples:

1998 → 20th century
1900 → 19th century
2000 → 20th century
2026 → 21st century


--------------------------------------------------
WHAT DOES THE QUESTION MEAN?
--------------------------------------------------

A century represents a period of 100 years.

The important thing is that the century number is NOT simply:

year // 100

because some years are at the beginning of a century.

For example:

1998 // 100 = 19

But:

1998 is actually in the 20th century.


Therefore, we need a formula that correctly handles
years that are not exactly divisible by 100.


--------------------------------------------------
FORMULA
--------------------------------------------------

century = (year + 99) // 100


This formula gives the correct century number.


--------------------------------------------------
WHY DO WE ADD 99?
--------------------------------------------------

Let's understand with:

year = 1998


If we simply use:

1998 // 100

we get:

19


But we need:

20


So we use:

(1998 + 99) // 100

= 2097 // 100

= 20


Therefore:

1998 → 20th century


--------------------------------------------------
DRY RUN 1
--------------------------------------------------

Given:

year = 1998


STEP 1:

Add 99:

1998 + 99 = 2097


STEP 2:

Integer division:

2097 // 100 = 20


Therefore:

century = 20


Output:

20th century


--------------------------------------------------
DRY RUN 2
--------------------------------------------------

Given:

year = 1900


Calculate:

(1900 + 99) // 100

= 1999 // 100

= 19


Therefore:

19th century


--------------------------------------------------
DRY RUN 3
--------------------------------------------------

Given:

year = 2000


Calculate:

(2000 + 99) // 100

= 2099 // 100

= 20


Therefore:

20th century


--------------------------------------------------
DRY RUN 4
--------------------------------------------------

Given:

year = 2001


Calculate:

(2001 + 99) // 100

= 2100 // 100

= 21


Therefore:

21st century


--------------------------------------------------
DRY RUN 5
--------------------------------------------------

Given:

year = 2026


Calculate:

(2026 + 99) // 100

= 2125 // 100

= 21


Therefore:

21st century


--------------------------------------------------
IMPORTANT PATTERN
--------------------------------------------------

Years:

1–100
   ↓
1st century

101–200
   ↓
2nd century

201–300
   ↓
3rd century

...

1801–1900
   ↓
19th century

1901–2000
   ↓
20th century

2001–2100
   ↓
21st century


--------------------------------------------------
WHY YEAR 2000 IS 20th CENTURY
--------------------------------------------------

This is an important boundary case.

The:

20th century = 1901 to 2000

The:

21st century = 2001 to 2100


Therefore:

2000 → 20th century

2001 → 21st century


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

1998

Calculation:

(1998 + 99) // 100

= 20

Output:

20th century


TEST CASE 2:

Input:

1900

Output:

19th century


TEST CASE 3:

Input:

1901

Output:

20th century


TEST CASE 4:

Input:

2000

Output:

20th century


TEST CASE 5:

Input:

2001

Output:

21st century


TEST CASE 6:

Input:

2026

Output:

21st century


TEST CASE 7:

Input:

1800

Output:

18th century


TEST CASE 8:

Input:

1801

Output:

19th century


--------------------------------------------------
TEST CASE TABLE
--------------------------------------------------

| Year | Century |
|-----:|---------|
| 100 | 1st century |
| 101 | 2nd century |
| 500 | 5th century |
| 1000 | 10th century |
| 1800 | 18th century |
| 1801 | 19th century |
| 1900 | 19th century |
| 1901 | 20th century |
| 1998 | 20th century |
| 2000 | 20th century |
| 2001 | 21st century |
| 2026 | 21st century |


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Integer Division `//`

It removes the decimal portion.

Example:

2097 // 100 = 20


2. Addition

We add:

99


3. Formula

(year + 99) // 100


4. Boundary Cases

The most important boundaries are:

100
101

1900
1901

2000
2001


--------------------------------------------------
SIMPLE MEMORY TRICK
--------------------------------------------------

To find the century:

(year + 99) // 100


Example:

1998

     +99
      ↓
2097

     //100
      ↓
20


Therefore:

1998 → 20th century


--------------------------------------------------
COMMON MISTAKE
--------------------------------------------------

Do NOT simply write:

century = year // 100


For:

1998

You would get:

19

But the correct answer is:

20th century


The `+99` handles this correctly.


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How did you solve this problem?"

You can say:

"I use the formula (year + 99) // 100 to calculate the century.
The addition of 99 ensures that years that are not exactly
divisible by 100 are assigned to the correct century. For
example, 1998 gives 20, while 2000 still gives 20."


--------------------------------------------------
MAIN LOGIC
--------------------------------------------------

Year
 ↓
Add 99
 ↓
Integer divide by 100
 ↓
Century number


Formula:

(year + 99) // 100


IMPORTANT:

1901 → 20th century
2000 → 20th century
2001 → 21st century


--------------------------------------------------
NOTE ABOUT YOUR CURRENT CODE
--------------------------------------------------

Your calculation is correct:

century = (year + 99) // 100


Your current output:

print(str(century) + "th century")

is perfectly fine for the examples like:

19th century
20th century


If you want grammatically correct ordinal endings for every
century, you would need additional logic for:

1st
2nd
3rd
4th
...
21st
22nd
23rd
24th
etc.

But that is NOT necessary for understanding the core
logic of this question.
"""