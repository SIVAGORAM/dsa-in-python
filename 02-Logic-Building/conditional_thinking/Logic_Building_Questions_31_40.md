# Python Logic Building — Questions 31–40
## Level 4: Logical Operators & Compound Statements

> **Revision purpose:** Use this README to revise Questions 31–40.
>
> **Practice rule:** First read only the question and try to solve it yourself. Then compare your solution, understand the dry run, and run the test cases.
>
> **Source note:** The provided PDF's Level 4 Question 38 is phrased as a weekday/weekend classification, while the Question 38 you practiced here is the day-number → day-name problem. This README keeps the version you actually practiced and notes the difference clearly.

---

## Questions List

1. [Question 31 — Letter, Digit, or Neither](#question-31--letter-digit-or-neither)
2. [Question 32 — FizzBuzz](#question-32--fizzbuzz)
3. [Question 33 — Median of Three Numbers](#question-33--median-of-three-numbers)
4. [Question 34 — AM or PM](#question-34--am-or-pm)
5. [Question 35 — Tax Eligibility](#question-35--tax-eligibility)
6. [Question 36 — Positive Numbers and Sum](#question-36--positive-numbers-and-sum)
7. [Question 37 — Digit to Word](#question-37--digit-to-word)
8. [Question 38 — Day Number to Day Name](#question-38--day-number-to-day-name)
9. [Question 39 — Electricity Bill](#question-39--electricity-bill)
10. [Question 40 — Basic Password Validation](#question-40--basic-password-validation)

---

# Question 31 — Letter, Digit, or Neither

## Question

**Take a character and check if it is a letter, a digit, or neither.**

## Solution

```python
def main():
    # Question 31: Take a character and check if it is a letter, a digit, or neither.
    ch = '9'

    if ch.isalpha():
        print("Letter")
    elif ch.isdigit():
        print("Digit")
    else:
        print("Neither")


if __name__ == "__main__":
    main()
```

## Explanation

The question gives one character and asks us to classify it as:

1. Letter
2. Digit
3. Neither

First, `isalpha()` checks whether it is a letter.

If that is False, `isdigit()` checks whether it is a digit.

If both are False, the character is neither.

### Example

```text
ch = '9'

'9'.isalpha() → False
'9'.isdigit() → True

Output:
Digit
```

For:

```text
ch = 'A'
```

```text
'A'.isalpha() → True

Output:
Letter
```

For:

```text
ch = '@'
```

```text
'@'.isalpha() → False
'@'.isdigit() → False

Output:
Neither
```

## Dry Run

```text
ch = '9'

Step 1:
'9'.isalpha() → False

Step 2:
'9'.isdigit() → True

Therefore:
Digit
```

## Test Cases

| Input | Expected Output |
|---|---|
| `'A'` | Letter |
| `'z'` | Letter |
| `'9'` | Digit |
| `'0'` | Digit |
| `'@'` | Neither |
| `'#'` | Neither |
| `' '` | Neither |

## Key Concepts

```text
isalpha() → Checks for alphabetic characters
isdigit() → Checks for digits
if        → First condition
elif      → Another condition
else      → When previous conditions are False
```

---

# Question 32 — FizzBuzz

## Question

**Take a number and print "Fizz" if divisible by 3, "Buzz" if divisible by 5, and "FizzBuzz" if divisible by both.**

## Solution

```python
def main():
    # Question 32: Take a number and print Fizz, Buzz, or FizzBuzz.
    number = 25

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


if __name__ == "__main__":
    main()
```

## Explanation

There are four possible outcomes:

```text
Divisible by both 3 and 5 → FizzBuzz
Divisible only by 3       → Fizz
Divisible only by 5       → Buzz
Divisible by neither      → Print the number
```

We use `%` to check divisibility.

For:

```text
number = 25
```

```text
25 % 3 = 1
25 % 5 = 0
```

So it is divisible by 5 only.

Output:

```text
Buzz
```

### Why check both first?

For `15`:

```text
15 % 3 = 0
15 % 5 = 0
```

If we checked 3 first, we could incorrectly print `Fizz`.

Therefore, check the combined condition first:

```python
if number % 3 == 0 and number % 5 == 0:
```

## Dry Run

```text
number = 15

15 % 3 == 0 → True
15 % 5 == 0 → True

True and True → True

Output:
FizzBuzz
```

For `9`:

```text
9 % 3 == 0 → True
9 % 5 == 0 → False

Output:
Fizz
```

For `7`:

```text
7 % 3 == 0 → False
7 % 5 == 0 → False

Output:
7
```

## Test Cases

| Input | Expected Output |
|---:|---|
| `15` | FizzBuzz |
| `30` | FizzBuzz |
| `9` | Fizz |
| `12` | Fizz |
| `25` | Buzz |
| `10` | Buzz |
| `7` | `7` |
| `11` | `11` |
| `0` | FizzBuzz |

## Key Concepts

```text
%   → Remainder
==  → Equal to
and → Both conditions must be True
elif → Check another condition
else → Neither condition was True
```

---

# Question 33 — Median of Three Numbers

## Question

**Take three numbers and print the median value (neither maximum nor minimum).**

## Solution

```python
def main():
    # Question 33: Take three numbers and print the median value.
    a = 12
    b = 5
    c = 20

    median = 0

    if (a >= b and a <= c) or (a >= c and a <= b):
        median = a
    elif (b >= a and b <= c) or (b >= c and b <= a):
        median = b
    else:
        median = c

    print("Median =", median)


if __name__ == "__main__":
    main()
```

## Explanation

The median of three numbers is the value that lies between the other two.

Example:

```text
5, 12, 20
```

Therefore:

```text
Minimum = 5
Median  = 12
Maximum = 20
```

The first condition checks whether `a` lies between `b` and `c`.

```python
(a >= b and a <= c) or (a >= c and a <= b)
```

If `a` is not the median, we check `b`.

If neither `a` nor `b` is the median, `c` must be the median.

## Dry Run

```text
a = 12
b = 5
c = 20

12 >= 5  → True
12 <= 20 → True

True and True → True

median = 12
```

Output:

```text
Median = 12
```

Another example:

```text
a = 30
b = 10
c = 20
```

Sorted:

```text
10, 20, 30
```

So:

```text
Median = 20
```

## Test Cases

| a | b | c | Expected Median |
|---:|---:|---:|---:|
| `12` | `5` | `20` | `12` |
| `30` | `10` | `20` | `20` |
| `7` | `3` | `5` | `5` |
| `1` | `2` | `3` | `2` |
| `20` | `10` | `15` | `15` |
| `5` | `5` | `10` | `5` |
| `10` | `20` | `20` | `20` |

## Key Concepts

```text
>=  → Greater than or equal to
<=  → Less than or equal to
and → Both conditions must be True
or  → At least one condition must be True
```

---

# Question 34 — AM or PM

## Question

**Take 24-hour time (hours and minutes) and print whether it is AM or PM.**

## Solution

```python
def main():
    # Question 34: Take 24-hour time and print AM or PM.
    hour = 14
    minutes = 30

    if hour < 12:
        print("AM")
    else:
        print("PM")


if __name__ == "__main__":
    main()
```

## Explanation

In 24-hour time:

```text
00:00–11:59 → AM
12:00–23:59 → PM
```

Only the hour is required to determine AM or PM.

For:

```text
hour = 14
minutes = 30
```

```text
14 < 12 → False
```

Therefore:

```text
PM
```

## Dry Run

```text
hour = 14

14 < 12 → False

else block executes.

Output:
PM
```

Boundary examples:

```text
00:30 → AM
11:59 → AM
12:00 → PM
23:59 → PM
```

## Test Cases

| Hour | Minutes | Expected Output |
|---:|---:|---|
| `0` | `0` | AM |
| `9` | `30` | AM |
| `11` | `59` | AM |
| `12` | `0` | PM |
| `14` | `30` | PM |
| `18` | `45` | PM |
| `23` | `59` | PM |

## Key Concepts

```text
<    → Less than
if   → Condition
else → Opposite case
```

---

# Question 35 — Tax Eligibility

## Question

**Take income and age, and check if eligible for tax (age > 18 and income > 5 L).**

## Solution

```python
def main():
    # Question 35: Take income and age, and check tax eligibility.
    age = 25
    income = 600000

    if age > 18 and income > 500000:
        print("Eligible for tax")
    else:
        print("Not eligible for tax")


if __name__ == "__main__":
    main()
```

## Explanation

Both conditions must be satisfied:

1. `age > 18`
2. `income > 500000`

Therefore we use `and`.

For:

```text
age = 25
income = 600000
```

```text
25 > 18 → True
600000 > 500000 → True

True and True → True
```

Output:

```text
Eligible for tax
```

## Dry Run

```text
age = 25
income = 600000

25 > 18 → True
600000 > 500000 → True

Both are True.

Output:
Eligible for tax
```

Boundary example:

```text
age = 18
income = 600000

18 > 18 → False
```

Therefore:

```text
Not eligible for tax
```

Likewise, income exactly `500000` does not satisfy `income > 500000`.

## Test Cases

| Age | Income | Expected Output |
|---:|---:|---|
| `25` | `600000` | Eligible for tax |
| `17` | `600000` | Not eligible for tax |
| `25` | `400000` | Not eligible for tax |
| `18` | `600000` | Not eligible for tax |
| `25` | `500000` | Not eligible for tax |
| `30` | `1000000` | Eligible for tax |

## Key Concepts

```text
>   → Greater than
and → Both conditions must be True
```

---

# Question 36 — Positive Numbers and Sum

## Question

**Take two numbers and check if both are positive and their sum is less than 100.**

## Solution

```python
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
```

## Explanation

There are three conditions:

1. `first > 0`
2. `second > 0`
3. `first + second < 100`

All three must be True.

For:

```text
first = 30
second = 40
```

```text
30 > 0 → True
40 > 0 → True
30 + 40 = 70
70 < 100 → True
```

Therefore:

```text
Condition satisfied
```

## Dry Run

```text
first = 30
second = 40

30 > 0 → True
40 > 0 → True
30 + 40 = 70
70 < 100 → True

True and True and True → True
```

Output:

```text
Condition satisfied
```

Boundary example:

```text
first = 50
second = 50

50 + 50 = 100
100 < 100 → False
```

Therefore:

```text
Condition not satisfied
```

## Test Cases

| First | Second | Expected Output |
|---:|---:|---|
| `30` | `40` | Condition satisfied |
| `10` | `20` | Condition satisfied |
| `50` | `50` | Condition not satisfied |
| `60` | `40` | Condition not satisfied |
| `-10` | `20` | Condition not satisfied |
| `0` | `20` | Condition not satisfied |
| `99` | `1` | Condition not satisfied |

## Key Concepts

```text
>   → Greater than
<   → Less than
+   → Addition
and → All conditions must be True
```

---

# Question 37 — Digit to Word

## Question

**Take a single digit (0–9) and print its word form ("Zero" to "Nine").**

## Solution

```python
def main():
    # Question 37: Take a single digit (0-9) and print its word form.
    digit = 7

    words = [
        "Zero",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine"
    ]

    if digit >= 0 and digit <= 9:
        print(words[digit])
    else:
        print("Invalid digit")


if __name__ == "__main__":
    main()
```

## Explanation

We store the word for each digit in a list.

```text
Index 0 → Zero
Index 1 → One
Index 2 → Two
Index 3 → Three
Index 4 → Four
Index 5 → Five
Index 6 → Six
Index 7 → Seven
Index 8 → Eight
Index 9 → Nine
```

Python uses zero-based indexing.

Therefore, the digit itself can be used as the list index.

For:

```text
digit = 7
```

```text
words[7] → Seven
```

## Dry Run

```text
digit = 7

7 >= 0 → True
7 <= 9 → True

words[7] → "Seven"

Output:
Seven
```

Boundary cases:

```text
digit = 0
words[0] → Zero

digit = 9
words[9] → Nine
```

Invalid:

```text
digit = 12

12 >= 0 → True
12 <= 9 → False

Output:
Invalid digit
```

## Test Cases

| Input | Expected Output |
|---:|---|
| `0` | Zero |
| `1` | One |
| `5` | Five |
| `7` | Seven |
| `9` | Nine |
| `10` | Invalid digit |
| `-1` | Invalid digit |

## Key Concepts

```text
List  → Ordered collection
Index → Position in a list
```

Important:

Use a list:

```python
words = ["Zero", "One", "Two"]
```

not a set:

```python
words = {"Zero", "One", "Two"}
```

because we need index-based access.

---

# Question 38 — Day Number to Day Name

## Question

**Take a day number (1–7) and print the corresponding day name.**

> **Source note:** The provided PDF's Level 4 Question 38 is worded as “Take a weekday number (1–7) and determine if it is a weekday or weekend.” The version below is the **day-name problem you practiced**.

## Solution

```python
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
```

## Explanation

The question gives numbers `1–7`.

The list uses zero-based indexes:

```text
Index 0 → Monday
Index 1 → Tuesday
Index 2 → Wednesday
Index 3 → Thursday
Index 4 → Friday
Index 5 → Saturday
Index 6 → Sunday
```

So we convert:

```text
day → day - 1
```

Mapping:

```text
1 → days[0] → Monday
2 → days[1] → Tuesday
3 → days[2] → Wednesday
4 → days[3] → Thursday
5 → days[4] → Friday
6 → days[5] → Saturday
7 → days[6] → Sunday
```

## Dry Run

```text
day = 3

1 <= 3 <= 7 → True

day - 1 = 2

days[2] → Wednesday
```

Output:

```text
Wednesday
```

Boundary:

```text
day = 7
7 - 1 = 6
days[6] → Sunday
```

Invalid:

```text
day = 8
1 <= 8 <= 7 → False

Output:
Invalid day
```

## Test Cases

| Input | Expected Output |
|---:|---|
| `1` | Monday |
| `2` | Tuesday |
| `3` | Wednesday |
| `4` | Thursday |
| `5` | Friday |
| `6` | Saturday |
| `7` | Sunday |
| `0` | Invalid day |
| `8` | Invalid day |

## Key Concepts

```text
List indexing
Zero-based indexing
Range validation
day - 1
```

Also:

```python
1 <= day <= 7
```

is equivalent to:

```python
day >= 1 and day <= 7
```

---

# Question 39 — Electricity Bill

## Question

**Calculate electricity bill based on units using slab rates.**

The practiced slab rates are:

```text
First 100 units → ₹5 per unit
Next 100 units  → ₹7 per unit
Above 200 units → ₹10 per unit
```

## Solution

```python
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
```

## Explanation

This is a slab-based calculation.

The important rule is:

> Earlier units keep their earlier rate when usage enters a higher slab.

For `150` units:

```text
First 100 units → ₹5 each
Remaining 50   → ₹7 each
```

Do NOT calculate:

```text
150 × ₹7
```

Instead:

```text
100 × 5 = 500
50 × 7 = 350

Total = 850
```

Therefore:

```text
Bill = 850
```

## Dry Run

```text
units = 150

150 <= 100 → False

150 <= 200 → True
```

Use:

```text
100 × 5 = 500
150 - 100 = 50
50 × 7 = 350

500 + 350 = 850
```

Output:

```text
Bill = 850
```

### Example: 250 Units

```text
First 100:
100 × 5 = 500

Next 100:
100 × 7 = 700

Remaining:
250 - 200 = 50

50 × 10 = 500

Total:
500 + 700 + 500 = 1700
```

Output:

```text
Bill = 1700
```

### Boundary Examples

For `100`:

```text
100 × 5 = 500
```

For `200`:

```text
100 × 5 = 500
100 × 7 = 700

Total = 1200
```

## Test Cases

| Units | Expected Bill |
|---:|---:|
| `50` | `250` |
| `100` | `500` |
| `150` | `850` |
| `200` | `1200` |
| `250` | `1700` |
| `300` | `2200` |

## Key Concepts

```text
if   → First slab
elif → Second slab
else → Above 200
*    → Multiplication
-    → Remaining units
```

Main pattern:

```text
First slab
    ↓
Second slab
    ↓
Third slab
```

---

# Question 40 — Basic Password Validation

## Question

**Take a password string and check basic rules (length >= 8 and contains at least one digit).**

## Solution

```python
def main():
    # Question 40: Take a password string and check basic rules.
    password = "Code123not"

    has_digit = False

    for ch in password:
        if ch.isdigit():
            has_digit = True
            break

    if len(password) >= 8 and has_digit:
        print("Valid password")
    else:
        print("Invalid password")


if __name__ == "__main__":
    main()
```

## Explanation

The question requires TWO rules:

1. Password length must be at least 8 characters.
2. Password must contain at least one digit.

We start with:

```python
has_digit = False
```

This means we have not found a digit yet.

Then:

```python
for ch in password:
```

checks each character.

When a digit is found:

```python
has_digit = True
```

We then use:

```python
break
```

because we do not need to continue searching after finding one digit.

Finally:

```python
len(password) >= 8 and has_digit
```

checks both requirements.

## Dry Run

Given:

```text
password = "Code123not"
```

Length:

```text
len(password) = 10
10 >= 8 → True
```

Now inspect characters:

```text
C → not digit
o → not digit
d → not digit
e → not digit
1 → digit
```

At `1`:

```text
has_digit = True
break
```

Final check:

```text
True and True → True
```

Output:

```text
Valid password
```

### Example: No Digit

```text
password = "Password"

Length:
8 >= 8 → True

No digit found:
has_digit = False

True and False → False

Output:
Invalid password
```

### Example: Too Short

```text
password = "Code1"

Length:
5 >= 8 → False

Even though a digit exists, the password is invalid.

Output:
Invalid password
```

### Boundary Example

```text
password = "abcdefg1"

Length = 8
8 >= 8 → True

Digit `1` found → True

Therefore:
Valid password
```

## Test Cases

| Password | Expected Output |
|---|---|
| `"Code123not"` | Valid password |
| `"Hello123"` | Valid password |
| `"Password"` | Invalid password |
| `"Code1"` | Invalid password |
| `"abcdefg1"` | Valid password |
| `"12345678"` | Valid password |
| `"abcdefgh"` | Invalid password |
| `"abc1"` | Invalid password |

## Key Concepts

```text
len()     → Length of a string
isdigit() → Checks whether a character is a digit
for       → Iterates through characters
Boolean   → True / False
break     → Stops the loop
and       → Both conditions must be True
```

Important:

This question does NOT require:

```text
Uppercase
Lowercase
Special character
```

Only:

```text
Length >= 8
AND
At least one digit
```

---

# Quick Revision Table — Questions 31–40

| # | Problem | Main Concept |
|---:|---|---|
| 31 | Letter, digit, or neither | `isalpha()`, `isdigit()` |
| 32 | FizzBuzz | `%`, `and`, `elif` |
| 33 | Median of 3 numbers | Compound conditions |
| 34 | AM or PM | Time condition |
| 35 | Tax eligibility | `and` |
| 36 | Positive numbers + sum | Multiple conditions |
| 37 | Digit to word | List + indexing |
| 38 | Day number to day name | List + zero-based indexing |
| 39 | Electricity bill | Slab logic |
| 40 | Password validation | String iteration + Boolean flag |

---

# Core Concepts to Revise

## `and`

Both conditions must be True.

```text
True and True   → True
True and False  → False
False and True  → False
False and False → False
```

## `or`

At least one condition must be True.

```text
True or True   → True
True or False  → True
False or True  → True
False or False → False
```

## `%` Modulo

Used for remainder and divisibility.

```python
15 % 3
```

Result:

```text
0
```

Therefore 15 is divisible by 3.

## Boolean Flag

```python
has_digit = False
```

Later:

```python
has_digit = True
```

This lets the program remember whether something was found.

## `break`

```python
break
```

Immediately stops the current loop.

## List Indexing

Python uses zero-based indexing:

```text
Index 0 → First item
Index 1 → Second item
Index 2 → Third item
```

## Slab Logic

When different portions have different rates:

```text
First portion  → Rate 1
Second portion → Rate 2
Remaining      → Rate 3
```

Do not apply the highest rate to the entire amount.

---

# Final Revision Checklist

Try solving each question **without looking at the solution**:

- [ ] Q31 — Letter, digit, or neither
- [ ] Q32 — FizzBuzz
- [ ] Q33 — Median of three numbers
- [ ] Q34 — AM or PM
- [ ] Q35 — Tax eligibility
- [ ] Q36 — Positive numbers + sum
- [ ] Q37 — Digit to word
- [ ] Q38 — Day number to day name
- [ ] Q39 — Electricity bill
- [ ] Q40 — Password validation

## Mastery Rule

For every question, you should be able to:

```text
1. Explain the question in your own words.
2. Identify the input.
3. Identify the expected output.
4. Write the logic in plain English.
5. Write the Python code.
6. Dry-run the code manually.
7. Test normal cases.
8. Test boundary cases.
9. Test edge cases.
10. Explain why the solution works.
```

Do not memorize the code.

Instead, ask yourself:

```text
WHAT is the problem?
        ↓
WHAT are the possible cases?
        ↓
WHAT condition identifies each case?
        ↓
WHY did I use and/or?
        ↓
WHAT happens in the dry run?
        ↓
WHAT happens for boundary/edge cases?
```

Once you can solve and explain Questions 31–40 independently, continue to the next logical set.
