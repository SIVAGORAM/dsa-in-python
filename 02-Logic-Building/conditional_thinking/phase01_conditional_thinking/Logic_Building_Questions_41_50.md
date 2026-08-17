# Python Logic Building — Questions 41–50

## Revision Guide

This document contains Questions **41–50** in a revision-friendly format.

For every question:
- Question
- Correct solution
- What the question means
- Step-by-step explanation
- Dry run
- Examples
- Test cases
- Key concepts
- Interview explanation
- Important points to remember

> **Practice rule:** First read only the question and try to solve it yourself. Then compare your answer with the solution and dry-run it manually.

---

# Questions List

1. Question 41 — Point on X-axis, Y-axis, or Origin
2. Question 42 — Pythagorean Triplet
3. Question 43 — Valid Calendar Date
4. Question 44 — Smaller Clock-Hand Angle
5. Question 45 — Arithmetic Progression
6. Question 46 — Geometric Progression
7. Question 47 — First + Last Digit Equals Middle
8. Question 48 — Digit Sum vs Digit Product
9. Question 49 — Compare Two Dates
10. Question 50 — Find the Century

---

# Question 41 — Point on X-axis, Y-axis, or Origin

## Question

**Take coordinates `(x, y)` and check if the point lies on the X-axis, Y-axis, or at the origin.**

## Solution

```python
def main():
    x = 0
    y = 5

    if x == 0 and y == 0:
        print("Origin")
    elif y == 0:
        print("X-axis")
    elif x == 0:
        print("Y-axis")
    else:
        print("Not on an axis")


if __name__ == "__main__":
    main()
```

## Explanation

A point is represented as `(x, y)`.

Rules:

```text
x == 0 and y == 0 → Origin
y == 0            → X-axis
x == 0            → Y-axis
otherwise         → Not on an axis
```

### Dry Run

For:

```text
x = 0
y = 5
```

```text
x == 0 and y == 0
True and False → False

y == 0
False

x == 0
True
```

Output:

```text
Y-axis
```

### Why check Origin first?

`(0, 0)` satisfies both `x == 0` and `y == 0`, but it is specifically the Origin. Therefore, check the Origin first.

### Test Cases

| x | y | Expected Output |
|---:|---:|---|
| 0 | 0 | Origin |
| 0 | 5 | Y-axis |
| 0 | -5 | Y-axis |
| 5 | 0 | X-axis |
| -5 | 0 | X-axis |
| 5 | 3 | Not on an axis |
| -5 | -3 | Not on an axis |

### Interview Explanation

> "I first check whether both x and y are zero because that represents the origin. Then I check y for the X-axis and x for the Y-axis. Otherwise, the point is not on an axis."

---

# Question 42 — Pythagorean Triplet

## Question

**Take three numbers and check if they can form a Pythagorean triplet.**

## Solution

```python
def main():
    a = 3
    b = 4
    c = 5

    if a * a + b * b == c * c or        a * a + c * c == b * b or        b * b + c * c == a * a:
        print("Pythagorean triplet")
    else:
        print("Not a Pythagorean triplet")


if __name__ == "__main__":
    main()
```

## Explanation

Three numbers form a Pythagorean triplet when:

```text
a² + b² = c²
```

Example:

```text
3² + 4² = 5²
9 + 16 = 25
```

Because the numbers can be supplied in any order, all three arrangements are checked.

### Dry Run

```text
a = 3
b = 4
c = 5

3 * 3 + 4 * 4 == 5 * 5
9 + 16 == 25
25 == 25
True
```

Output:

```text
Pythagorean triplet
```

### Test Cases

| a | b | c | Expected Output |
|---:|---:|---:|---|
| 3 | 4 | 5 | Pythagorean triplet |
| 5 | 3 | 4 | Pythagorean triplet |
| 4 | 5 | 3 | Pythagorean triplet |
| 5 | 12 | 13 | Pythagorean triplet |
| 8 | 15 | 17 | Pythagorean triplet |
| 2 | 3 | 4 | Not a Pythagorean triplet |
| 5 | 5 | 5 | Not a Pythagorean triplet |

### Key Concept

```text
Pythagorean theorem
Squaring
or
==
```

### Interview Explanation

> "I use the Pythagorean theorem. Since the three numbers can appear in any order, I check all three possible squared relationships using `or`."

---

# Question 43 — Valid Calendar Date

## Question

**Take day and month and check if it forms a valid calendar date, ignoring leap years.**

## Solution

```python
def main():
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
```

## Explanation

Because leap years are ignored:

```text
January    → 31
February   → 28
March      → 31
April      → 30
May        → 31
June       → 30
July       → 31
August     → 31
September  → 30
October    → 31
November   → 30
December   → 31
```

First validate the month:

```python
month < 1 or month > 12
```

Then handle February, the 30-day months, and finally the 31-day months.

### Dry Run

For:

```text
day = 29
month = 2
```

February is selected.

```text
29 >= 1 → True
29 <= 28 → False
```

Therefore:

```text
Invalid date
```

### Test Cases

| Day | Month | Expected Output |
|---:|---:|---|
| 15 | 8 | Valid date |
| 28 | 2 | Valid date |
| 29 | 2 | Invalid date |
| 30 | 4 | Valid date |
| 31 | 4 | Invalid date |
| 31 | 8 | Valid date |
| 31 | 12 | Valid date |
| 32 | 12 | Invalid date |
| 1 | 1 | Valid date |
| 0 | 5 | Invalid date |
| 10 | 0 | Invalid date |
| 10 | 13 | Invalid date |

### Interview Explanation

> "First I validate the month. Then I handle February as 28 days because leap years are ignored, followed by the 30-day months and then the 31-day months."

---

# Question 44 — Smaller Clock-Hand Angle

## Question

**Take time (hours and minutes) and print the smaller angle between the hour and minute hands.**

## Solution

```python
def main():
    hours = 3
    minutes = 30

    hour_angle = (hours % 12) * 30 + minutes * 0.5
    minute_angle = minutes * 6

    angle = abs(hour_angle - minute_angle)

    if angle > 180:
        angle = 360 - angle

    print("Smaller angle =", angle)


if __name__ == "__main__":
    main()
```

## Explanation

A clock has 360 degrees.

```text
12 hours → 360°
1 hour   → 30°
60 min   → 360°
1 minute → 6°
```

The hour hand also moves during the minutes:

```text
30° / 60 = 0.5° per minute
```

Formulas:

```python
hour_angle = (hours % 12) * 30 + minutes * 0.5
minute_angle = minutes * 6
angle = abs(hour_angle - minute_angle)
```

If the difference is greater than 180:

```python
angle = 360 - angle
```

### Dry Run — 3:30

Hour hand:

```text
(3 % 12) * 30 + 30 * 0.5
= 90 + 15
= 105°
```

Minute hand:

```text
30 * 6 = 180°
```

Difference:

```text
abs(105 - 180) = 75°
```

Output:

```text
Smaller angle = 75.0
```

### Important Example — 9:00

```text
Hour angle = 270°
Minute angle = 0°
Difference = 270°
```

Since:

```text
270 > 180
```

use:

```text
360 - 270 = 90°
```

### Test Cases

| Hours | Minutes | Expected Angle |
|---:|---:|---:|
| 3 | 30 | 75.0° |
| 12 | 0 | 0.0° |
| 6 | 0 | 180.0° |
| 9 | 0 | 90.0° |
| 1 | 5 | 2.5° |
| 3 | 0 | 90.0° |
| 12 | 30 | 165.0° |
| 6 | 30 | 15.0° |

### Interview Explanation

> "I calculate the hour-hand angle using 30 degrees per hour and 0.5 degrees per minute. Then I calculate the minute-hand angle using 6 degrees per minute, find the absolute difference, and convert it to the smaller angle if it is greater than 180 degrees."

---

# Question 45 — Arithmetic Progression

## Question

**Take three numbers and check if they are in arithmetic progression.**

## Solution

```python
def main():
    a = 4
    b = 8
    c = 12

    if b - a == c - b:
        print("Arithmetic progression")
    else:
        print("Not an arithmetic progression")


if __name__ == "__main__":
    main()
```

## Explanation

An Arithmetic Progression (AP) has the same difference between consecutive terms.

For:

```text
a, b, c
```

check:

```python
b - a == c - b
```

### Dry Run

```text
8 - 4 = 4
12 - 8 = 4

4 == 4 → True
```

Output:

```text
Arithmetic progression
```

### Example

```text
20, 15, 10

15 - 20 = -5
10 - 15 = -5
```

This is also an AP.

### Test Cases

| a | b | c | Expected Output |
|---:|---:|---:|---|
| 4 | 8 | 12 | Arithmetic progression |
| 2 | 5 | 8 | Arithmetic progression |
| 2 | 5 | 10 | Not an arithmetic progression |
| 20 | 15 | 10 | Arithmetic progression |
| -5 | -2 | 1 | Arithmetic progression |
| 7 | 7 | 7 | Arithmetic progression |
| 1 | 4 | 7 | Arithmetic progression |
| 10 | 20 | 31 | Not an arithmetic progression |

### Memory Trick

```text
AP → Same difference

4 → 8 → 12
   +4   +4
```

### Interview Explanation

> "An arithmetic progression has a constant difference. I compare the difference between the second and first numbers with the difference between the third and second numbers."

---

# Question 46 — Geometric Progression

## Question

**Take three numbers and check if they are in geometric progression.**

## Solution

```python
def main():
    a = 3
    b = 9
    c = 27

    if b * b == a * c:
        print("Geometric progression")
    else:
        print("Not a geometric progression")


if __name__ == "__main__":
    main()
```

## Explanation

A Geometric Progression (GP) has the same ratio between consecutive terms.

Normally:

```text
b / a == c / b
```

Cross multiplication gives:

```text
b * b == a * c
```

That is the condition used.

### Dry Run

For:

```text
3, 9, 27
```

```text
b * b = 9 * 9 = 81
a * c = 3 * 27 = 81

81 == 81 → True
```

Output:

```text
Geometric progression
```

### Not GP Example

```text
2, 6, 20
```

```text
6 * 6 = 36
2 * 20 = 40

36 == 40 → False
```

### Test Cases

| a | b | c | Expected Output |
|---:|---:|---:|---|
| 3 | 9 | 27 | Geometric progression |
| 2 | 6 | 18 | Geometric progression |
| 4 | 2 | 1 | Geometric progression |
| 2 | 6 | 20 | Not a geometric progression |
| 5 | 10 | 20 | Geometric progression |
| 10 | 20 | 30 | Not a geometric progression |
| 2 | -6 | 18 | Geometric progression |
| 7 | 7 | 7 | Geometric progression |

### AP vs GP

```text
AP → Same difference

4 → 8 → 12
   +4   +4
```

```text
GP → Same ratio

3 → 9 → 27
   ×3   ×3
```

### Interview Explanation

> "A geometric progression has a constant ratio. I use the cross-multiplied form `b*b == a*c` so I can check the relationship without division."

---

# Question 47 — First + Last Digit Equals Middle

## Question

**Take a 3-digit number and check if the sum of the first and last digit equals the middle digit.**

## Solution

```python
def main():
    number = 582

    first = number // 100
    middle = (number // 10) % 10
    last = number % 10

    if first + last == middle:
        print("Sum of first and last digit equals middle digit")
    else:
        print("Sum of first and last digit does not equal middle digit")


if __name__ == "__main__":
    main()
```

## Explanation

For:

```text
582
```

digits are:

```text
First  = 5
Middle = 8
Last   = 2
```

Calculate:

```text
5 + 2 = 7
```

Compare:

```text
7 == 8 → False
```

Therefore the sum does not equal the middle digit.

### Digit Extraction

First:

```python
number // 100
```

Middle:

```python
(number // 10) % 10
```

Last:

```python
number % 10
```

### Dry Run

```text
582 // 100 = 5

(582 // 10) % 10
= 58 % 10
= 8

582 % 10 = 2

5 + 2 = 7

7 == 8 → False
```

### Example Where It Is True

```text
121

1 + 1 = 2

Middle = 2

2 == 2 → True
```

### Test Cases

| Number | First | Middle | Last | First + Last | Expected |
|---:|---:|---:|---:|---:|---|
| 582 | 5 | 8 | 2 | 7 | Not equal |
| 121 | 1 | 2 | 1 | 2 | Equal |
| 132 | 1 | 3 | 2 | 3 | Equal |
| 123 | 1 | 2 | 3 | 4 | Not equal |
| 456 | 4 | 5 | 6 | 10 | Not equal |

### Important Difference from Q22

Q22 checks whether the middle digit is largest, smallest, or neither.

Q47 checks:

```python
first + last == middle
```

### Interview Explanation

> "First I extract the three digits using integer division and modulo. Then I add the first and last digits and compare their sum with the middle digit."

---

# Question 48 — Digit Sum vs Digit Product

## Question

**Take an integer (1–9999) and check if the sum of its digits is greater than the product of its digits.**

## Solution

```python
def sum_digits(number):
    value = abs(number)
    digit_sum = 0

    while True:
        digit_sum += value % 10
        value //= 10

        if not (value > 0):
            break

    return digit_sum


def product_digits(number):
    value = abs(number)
    digit_product = 1

    if value == 0:
        return 0

    while value > 0:
        digit_product *= value % 10
        value //= 10

    return digit_product


def main():
    number = 1234

    digit_sum = sum_digits(number)
    digit_product = product_digits(number)

    if digit_sum > digit_product:
        print("Digit sum is greater")
    else:
        print("Digit product is greater or equal")


if __name__ == "__main__":
    main()
```

## Explanation

For:

```text
1234
```

Sum:

```text
1 + 2 + 3 + 4 = 10
```

Product:

```text
1 * 2 * 3 * 4 = 24
```

Comparison:

```text
10 > 24 → False
```

Output:

```text
Digit product is greater or equal
```

## Important Digit Pattern

```python
digit = number % 10
number //= 10
```

Remember:

```text
% 10  → TAKE last digit
// 10 → REMOVE last digit
```

### Dry Run — Sum

```text
1234 → digit 4 → sum 4
123  → digit 3 → sum 7
12   → digit 2 → sum 9
1    → digit 1 → sum 10
0    → stop
```

### Dry Run — Product

```text
1 × 4 = 4
4 × 3 = 12
12 × 2 = 24
24 × 1 = 24
```

Final product:

```text
24
```

### Example with Zero

For `120`:

```text
Sum = 1 + 2 + 0 = 3
Product = 1 * 2 * 0 = 0
```

Therefore:

```text
Digit sum is greater
```

### Test Cases

| Number | Digit Sum | Digit Product | Expected Output |
|---:|---:|---:|---|
| 1234 | 10 | 24 | Digit product is greater or equal |
| 123 | 6 | 6 | Digit product is greater or equal |
| 111 | 3 | 1 | Digit sum is greater |
| 222 | 6 | 8 | Digit product is greater or equal |
| 120 | 3 | 0 | Digit sum is greater |
| 101 | 2 | 0 | Digit sum is greater |
| 999 | 27 | 729 | Digit product is greater or equal |
| 1000 | 1 | 0 | Digit sum is greater |

### Key Concepts

```text
% 10
// 10
while
Accumulator
Functions
```

### Python Note

Avoid:

```python
sum = 0
```

because `sum` is a Python built-in function.

Prefer:

```python
digit_sum = 0
```

### Interview Explanation

> "I process the number digit by digit. I use modulo 10 to extract the last digit and integer division by 10 to remove it. I maintain one accumulator for the sum and another for the product, then compare them."

---

# Question 49 — Compare Two Dates

## Question

**Take two dates (day and month) and determine which one comes first in the calendar.**

## Solution

```python
def main():
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
```

## Explanation

When comparing dates:

```text
MONTH FIRST
    ↓
DAY SECOND
```

If the months are different, the smaller month comes first.

If the months are equal, compare the days.

If both month and day are equal, the dates are the same.

### Dry Run

Given:

```text
Date 1 = 12/5
Date 2 = 10/6
```

Compare months:

```text
5 < 6 → True
```

Therefore:

```text
First date comes first
```

### Same Month Example

```text
10/5
20/5
```

Months:

```text
5 == 5
```

Days:

```text
10 < 20
```

Therefore:

```text
First date comes first
```

### Same Date

```text
12/5
12/5
```

Both month and day are equal.

Therefore:

```text
Both dates are same
```

### Test Cases

| Date 1 | Date 2 | Expected Output |
|---|---|---|
| 12/5 | 10/6 | First date comes first |
| 10/5 | 20/5 | First date comes first |
| 20/5 | 10/5 | Second date comes first |
| 12/5 | 12/5 | Both dates are same |
| 1/1 | 31/12 | First date comes first |
| 31/12 | 1/1 | Second date comes first |
| 5/8 | 10/8 | First date comes first |
| 20/10 | 15/9 | Second date comes first |

### Interview Explanation

> "I first compare the months because an earlier month comes first. If the months are equal, I compare the days. If both month and day are equal, the dates are the same."

### Memory Trick

```text
MONTH FIRST
    ↓
If same month:
    ↓
DAY SECOND
```

---

# Question 50 — Find the Century

## Question

**Take a year and print the corresponding century.**

Examples:

```text
1998 → 20th century
1900 → 19th century
2000 → 20th century
2001 → 21st century
```

## Solution

```python
def main():
    year = 1998

    century = (year + 99) // 100

    print(str(century) + "th century")


if __name__ == "__main__":
    main()
```

## Explanation

A century contains 100 years.

Important boundaries:

```text
1–100       → 1st century
101–200     → 2nd century
1901–2000   → 20th century
2001–2100   → 21st century
```

Do not simply use:

```python
year // 100
```

because:

```text
1998 // 100 = 19
```

but:

```text
1998 → 20th century
```

Use:

```python
century = (year + 99) // 100
```

### Why add 99?

For `1998`:

```text
1998 + 99 = 2097
2097 // 100 = 20
```

Therefore:

```text
1998 → 20th century
```

### Dry Run

For:

```text
year = 1998
```

```text
year + 99
= 2097

2097 // 100
= 20
```

Output:

```text
20th century
```

### Boundary Cases

#### 1900

```text
(1900 + 99) // 100
= 19
```

So:

```text
1900 → 19th century
```

#### 1901

```text
(1901 + 99) // 100
= 20
```

So:

```text
1901 → 20th century
```

#### 2000

```text
(2000 + 99) // 100
= 20
```

So:

```text
2000 → 20th century
```

#### 2001

```text
(2001 + 99) // 100
= 21
```

So:

```text
2001 → 21st century
```

### Test Cases

| Year | Expected Century |
|---:|---|
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

### Key Concepts

```text
Integer division //
Formula
Boundary cases
Year ranges
```

### Common Mistake

Incorrect:

```python
century = year // 100
```

Correct:

```python
century = (year + 99) // 100
```

### Interview Explanation

> "I use the formula `(year + 99) // 100`. Adding 99 ensures that years that are not exactly divisible by 100 are assigned to the correct century. For example, 1998 gives 20, while 2000 still gives 20."

---

# Quick Revision Table — Questions 41–50

| # | Problem | Main Concept |
|---:|---|---|
| 41 | Coordinate position | `and`, axis logic |
| 42 | Pythagorean triplet | Squaring, `or` |
| 43 | Valid date | Range and nested conditions |
| 44 | Clock-hand angle | Formula, modulo, `abs()` |
| 45 | Arithmetic progression | Same difference |
| 46 | Geometric progression | Same ratio |
| 47 | First + last digit | `% 10`, `// 10` |
| 48 | Digit sum vs product | Loops + digit extraction |
| 49 | Compare dates | Month then day |
| 50 | Find century | Integer division + boundaries |

---

# Most Important Patterns

## Coordinates

```python
if x == 0 and y == 0:
    # Origin
elif y == 0:
    # X-axis
elif x == 0:
    # Y-axis
else:
    # Not on axis
```

## Pythagorean Triplet

```text
a² + b² = c²
```

Check all possible arrangements when the numbers can be in any order.

## Digit Extraction

```python
digit = number % 10
number //= 10
```

Remember:

```text
% 10  → TAKE last digit
// 10 → REMOVE last digit
```

## AP

```python
b - a == c - b
```

```text
AP → Same difference
```

## GP

```python
b * b == a * c
```

```text
GP → Same ratio
```

## Date Comparison

```text
MONTH FIRST
    ↓
DAY SECOND
```

## Century

```python
(year + 99) // 100
```

---

# Final Mastery Checklist

Before moving to the next set, solve each question without looking at the solution:

- [ ] Q41 — Coordinate axis/origin
- [ ] Q42 — Pythagorean triplet
- [ ] Q43 — Valid calendar date
- [ ] Q44 — Smaller clock-hand angle
- [ ] Q45 — Arithmetic progression
- [ ] Q46 — Geometric progression
- [ ] Q47 — First + last digit
- [ ] Q48 — Digit sum vs product
- [ ] Q49 — Compare two dates
- [ ] Q50 — Find century

For every question, you should be able to:

```text
1. Explain the question in your own words.
2. Identify the input.
3. Identify the output.
4. Explain the logic before coding.
5. Write the solution without copying.
6. Dry-run the code manually.
7. Test normal cases.
8. Test boundary cases.
9. Test edge cases.
10. Explain the solution in an interview.
```

## Final Memory Map

```text
Q41 → Coordinates
       ↓
Q42 → Pythagorean theorem
       ↓
Q43 → Date validation
       ↓
Q44 → Clock angles
       ↓
Q45 → AP = Same difference
       ↓
Q46 → GP = Same ratio
       ↓
Q47 → Extract 3 digits
       ↓
Q48 → Process every digit
       ↓
Q49 → Compare month → day
       ↓
Q50 → Century formula
```

> **Don't memorize the code. Understand the pattern behind each problem.**
