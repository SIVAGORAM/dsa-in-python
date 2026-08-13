# Python Logic Building — Phase 1 Revision

> **Purpose:** Revision notes for the first 20 conditional-thinking problems from the Logic Building PDF.
>
> **Practice rule:** Before looking at the answer, try to solve each problem yourself. Then compare your logic, dry-run it, and test the edge cases.

---

## Table of Contents

1. [Positive, Negative, or Zero](#1-positive-negative-or-zero)
2. [Even or Odd](#2-even-or-odd)
3. [Divisible by 5](#3-divisible-by-5)
4. [Divisible by Both 3 and 5](#4-divisible-by-both-3-and-5)
5. [Leap Year](#5-leap-year)
6. [Larger of Two Numbers](#6-larger-of-two-numbers)
7. [Largest of Three Numbers](#7-largest-of-three-numbers)
8. [Temperature Classification](#8-temperature-classification)
9. [Vowel or Consonant](#9-vowel-or-consonant)
10. [Uppercase, Lowercase, Digit, or Special Character](#10-uppercase-lowercase-digit-or-special-character)
11. [Valid Triangle](#11-valid-triangle)
12. [Triangle Type](#12-triangle-type)
13. [Grade from Marks](#13-grade-from-marks)
14. [Multiple of the Other](#14-multiple-of-the-other)
15. [Greeting Based on Hour](#15-greeting-based-on-hour)
16. [Voting Eligibility](#16-voting-eligibility)
17. [Both Even, Both Odd, or One Each](#17-both-even-both-odd-or-one-each)
18. [Alphabet Range](#18-alphabet-range)
19. [Day Number to Day Name](#19-day-number-to-day-name)
20. [Days in a Month](#20-days-in-a-month)

---

# Phase 1 — Conditional Thinking

## 1. Positive, Negative, or Zero

### Question

Take a number and print whether it is positive, negative, or zero.

### Answer

```python
def main():
    number = -7

    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")


if __name__ == "__main__":
    main()
```

### Explanation

There are three possible cases:

- `number > 0` → Positive
- `number < 0` → Negative
- Otherwise → Zero

The `if`, `elif`, and `else` branches make sure only one result is printed.

### Test Cases

| Input | Expected Output |
|---:|---|
| `10` | `Positive` |
| `-7` | `Negative` |
| `0` | `Zero` |

### Key Concept

**Basic conditional statements**

---

## 2. Even or Odd

### Question

Check if a number is even or odd.

### Answer

```python
def main():
    number = 18

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == "__main__":
    main()
```

### Explanation

The `%` operator gives the remainder.

- `number % 2 == 0` → Even
- Otherwise → Odd

### Test Cases

| Input | Expected Output |
|---:|---|
| `18` | `Even` |
| `7` | `Odd` |
| `0` | `Even` |
| `-4` | `Even` |

### Key Concept

**Modulo operator `%`**

---

## 3. Divisible by 5

### Question

Check if a number is divisible by 5.

### Answer

```python
def main():
    number = 25

    if number % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")


if __name__ == "__main__":
    main()
```

### Explanation

If dividing the number by `5` leaves a remainder of `0`, the number is divisible by `5`.

### Test Cases

| Input | Expected Output |
|---:|---|
| `25` | `Divisible by 5` |
| `20` | `Divisible by 5` |
| `26` | `Not divisible by 5` |
| `0` | `Divisible by 5` |

### Key Concept

**Modulo + condition**

---

## 4. Divisible by Both 3 and 5

### Question

Check if a number is divisible by both 3 and 5.

### Answer

```python
def main():
    number = 45

    if number % 3 == 0 and number % 5 == 0:
        print("Divisible by both 3 and 5")
    else:
        print("Not divisible by both 3 and 5")


if __name__ == "__main__":
    main()
```

### Explanation

Both conditions must be true:

```text
number % 3 == 0
number % 5 == 0
```

Python uses `and` when **both conditions must be true**.

### Test Cases

| Input | Expected Output |
|---:|---|
| `45` | `Divisible by both 3 and 5` |
| `30` | `Divisible by both 3 and 5` |
| `15` | `Divisible by both 3 and 5` |
| `9` | `Not divisible by both 3 and 5` |
| `25` | `Not divisible by both 3 and 5` |

### Key Concept

**Logical `and` operator**

---

## 5. Leap Year

### Question

Check if a given year is a leap year.

### Answer

```python
def main():
    year = 2024

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap year")
    else:
        print("Not a leap year")


if __name__ == "__main__":
    main()
```

### Explanation

A year is a leap year when:

- It is divisible by `400`, **OR**
- It is divisible by `4` **and** not divisible by `100`

### Test Cases

| Input | Expected Output |
|---:|---|
| `2024` | `Leap year` |
| `2000` | `Leap year` |
| `1900` | `Not a leap year` |
| `2023` | `Not a leap year` |

### Key Concept

**Compound conditions using `and` and `or`**

---

## 6. Larger of Two Numbers

### Question

Take two numbers and print the larger one.

### Answer

```python
def main():
    first = 20
    second = 35

    if first > second:
        print(first)
    else:
        print(second)


if __name__ == "__main__":
    main()
```

### Explanation

Compare the two numbers.

- If `first > second`, print `first`.
- Otherwise, print `second`.

If both numbers are equal, either value is the same, so this solution still gives the correct larger value.

### Test Cases

| First | Second | Expected Output |
|---:|---:|---|
| `20` | `35` | `35` |
| `50` | `10` | `50` |
| `25` | `25` | `25` |
| `-5` | `-2` | `-2` |

### Key Concept

**Comparison operators**

---

## 7. Largest of Three Numbers

### Question

Take three numbers and print the largest.

### Answer

```python
def main():
    first = 20
    second = 35
    third = 12

    largest = first

    if second > largest:
        largest = second

    if third > largest:
        largest = third

    print("Largest =", largest)


if __name__ == "__main__":
    main()
```

### Explanation

Start by assuming `first` is the largest.

Then:

1. Compare `second` with `largest`.
2. Update `largest` if `second` is bigger.
3. Compare `third` with the current `largest`.
4. Update it if necessary.

### Test Cases

| First | Second | Third | Expected |
|---:|---:|---:|---:|
| `20` | `35` | `12` | `35` |
| `50` | `20` | `30` | `50` |
| `10` | `20` | `30` | `30` |
| `7` | `7` | `7` | `7` |
| `-5` | `-2` | `-10` | `-2` |

### Key Concept

**Tracking a current maximum**

---

## 8. Temperature Classification

### Question

Take a temperature value and print `Cold`, `Warm`, or `Hot` using range conditions.

### Answer

```python
def main():
    temperature = 31

    if temperature < 15:
        print("Cold")
    elif temperature <= 30:
        print("Warm")
    else:
        print("Hot")


if __name__ == "__main__":
    main()
```

### Explanation

The ranges used here are:

- Less than `15` → Cold
- `15` through `30` → Warm
- Greater than `30` → Hot

These ranges are the chosen interpretation for this practice question.

### Test Cases

| Temperature | Expected Output |
|---:|---|
| `10` | `Cold` |
| `15` | `Warm` |
| `25` | `Warm` |
| `30` | `Warm` |
| `31` | `Hot` |
| `40` | `Hot` |

### Key Concept

**Range-based conditions**

---

## 9. Vowel or Consonant

### Question

Take a character and check if it is a vowel or consonant.

### Answer

```python
def is_vowel(ch):
    lower = ch.lower()
    return (
        lower == "a"
        or lower == "e"
        or lower == "i"
        or lower == "o"
        or lower == "u"
    )


def main():
    ch = "e"

    if ch.isalpha():
        if is_vowel(ch):
            print("Vowel")
        else:
            print("Consonant")
    else:
        print("Not an alphabet")


if __name__ == "__main__":
    main()
```

### Explanation

First, `ch.isalpha()` checks whether the character is an alphabet.

Then `is_vowel()` converts the character to lowercase and checks whether it is one of:

```text
a, e, i, o, u
```

### Test Cases

| Input | Expected Output |
|---|---|
| `e` | `Vowel` |
| `A` | `Vowel` |
| `b` | `Consonant` |
| `Z` | `Consonant` |
| `7` | `Not an alphabet` |
| `@` | `Not an alphabet` |

### Key Concept

**Helper functions + Boolean return values**

---

## 10. Uppercase, Lowercase, Digit, or Special Character

### Question

Take a character and check whether it is uppercase, lowercase, a digit, or a special character.

### Answer

```python
def main():
    ch = "A"

    if ch.isupper():
        print("Uppercase")
    elif ch.islower():
        print("Lowercase")
    elif ch.isdigit():
        print("Digit")
    else:
        print("Special character")


if __name__ == "__main__":
    main()
```

### Explanation

The conditions are checked in order:

- `ch.isupper()` → Uppercase
- `ch.islower()` → Lowercase
- `ch.isdigit()` → Digit
- Otherwise → Special character

### Test Cases

| Input | Expected Output |
|---|---|
| `A` | `Uppercase` |
| `z` | `Lowercase` |
| `7` | `Digit` |
| `@` | `Special character` |
| `#` | `Special character` |

### Key Concept

**Python string methods**

---

## 11. Valid Triangle

### Question

Take three sides and check if they form a valid triangle.

### Answer

```python
def main():
    a = 3
    b = 4
    c = 5

    if a + b > c and a + c > b and b + c > a:
        print("Valid triangle")
    else:
        print("Invalid triangle")


if __name__ == "__main__":
    main()
```

### Explanation

Three sides form a valid triangle only when the sum of **any two sides is greater than the third side**.

We check:

```text
a + b > c
a + c > b
b + c > a
```

All three conditions must be true.

### Test Cases

| A | B | C | Expected |
|---:|---:|---:|---|
| `3` | `4` | `5` | `Valid triangle` |
| `5` | `5` | `8` | `Valid triangle` |
| `1` | `2` | `3` | `Invalid triangle` |
| `1` | `1` | `5` | `Invalid triangle` |

### Key Concept

**Multiple conditions with `and`**

---

## 12. Triangle Type

### Question

If the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene.

### Answer

```python
def main():
    a = 5
    b = 5
    c = 8

    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid triangle")


if __name__ == "__main__":
    main()
```

### Explanation

First validate the triangle.

Then classify it:

- All three sides equal → Equilateral
- Any two sides equal → Isosceles
- All three sides different → Scalene
- Invalid sides → Invalid triangle

### Test Cases

| A | B | C | Expected |
|---:|---:|---:|---|
| `5` | `5` | `5` | `Equilateral` |
| `5` | `5` | `8` | `Isosceles` |
| `3` | `4` | `5` | `Scalene` |
| `1` | `2` | `3` | `Invalid triangle` |

### Key Concept

**Nested `if` statements**

---

## 13. Grade from Marks

### Question

Take marks from `0–100` and print the corresponding grade (`A/B/C/D/F`).

### Answer

```python
def main():
    marks = 82

    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    elif marks >= 60:
        print("C")
    elif marks >= 40:
        print("D")
    else:
        print("F")


if __name__ == "__main__":
    main()
```

### Explanation

The ranges used here are:

- `90–100` → A
- `75–89` → B
- `60–74` → C
- `40–59` → D
- Below `40` → F

**Note:** The PDF specifies the grade categories but does not specify the exact mark boundaries. These boundaries are the ones used in our practice solution.

### Test Cases

| Marks | Expected |
|---:|---|
| `95` | `A` |
| `82` | `B` |
| `65` | `C` |
| `45` | `D` |
| `20` | `F` |
| `90` | `A` |
| `75` | `B` |
| `60` | `C` |
| `40` | `D` |

### Key Concept

**Ordered range checking**

---

## 14. Multiple of the Other

### Question

Check if one of two given numbers is a multiple of the other.

### Answer

```python
def main():
    first = 12
    second = 36

    if first != 0 and second % first == 0:
        print("Second is a multiple of first")
    elif second != 0 and first % second == 0:
        print("First is a multiple of second")
    else:
        print("No number is a multiple of the other")


if __name__ == "__main__":
    main()
```

### Explanation

A number is a multiple of another number when it can be divided by that number **without a remainder**.

For example:

```text
36 % 12 = 0
```

Therefore, `36` is a multiple of `12`.

The `!= 0` checks prevent division by zero.

### Test Cases

| First | Second | Expected |
|---:|---:|---|
| `12` | `36` | `Second is a multiple of first` |
| `5` | `20` | `Second is a multiple of first` |
| `20` | `5` | `First is a multiple of second` |
| `7` | `20` | `No number is a multiple of the other` |
| `0` | `5` | `First is a multiple of second` |
| `5` | `0` | `Second is a multiple of first` |

### Key Concept

**Modulo + divisibility**

---

## 15. Greeting Based on Hour

### Question

Take the hour of the day (`0–23`) and print `Good Morning`, `Good Afternoon`, `Good Evening`, or `Good Night`.

### Answer

```python
def main():
    hour = 16

    if 5 <= hour < 12:
        print("Good Morning")
    elif 12 <= hour < 17:
        print("Good Afternoon")
    elif 17 <= hour < 21:
        print("Good Evening")
    else:
        print("Good Night")


if __name__ == "__main__":
    main()
```

### Explanation

The ranges used here are:

- `5–11` → Good Morning
- `12–16` → Good Afternoon
- `17–20` → Good Evening
- Otherwise → Good Night

Python supports chained comparisons such as:

```python
5 <= hour < 12
```

### Test Cases

| Hour | Expected |
|---:|---|
| `0` | `Good Night` |
| `5` | `Good Morning` |
| `11` | `Good Morning` |
| `12` | `Good Afternoon` |
| `16` | `Good Afternoon` |
| `17` | `Good Evening` |
| `20` | `Good Evening` |
| `21` | `Good Night` |
| `23` | `Good Night` |

### Key Concept

**Range conditions + chained comparisons**

---

## 16. Voting Eligibility

### Question

Check voting eligibility for a given age (`18+`).

### Answer

```python
def main():
    age = 19

    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")


if __name__ == "__main__":
    main()
```

### Explanation

The condition checks whether the age is `18` or greater.

- `age >= 18` → Eligible
- Otherwise → Not eligible

### Test Cases

| Age | Expected |
|---:|---|
| `19` | `Eligible to vote` |
| `18` | `Eligible to vote` |
| `17` | `Not eligible to vote` |
| `10` | `Not eligible to vote` |

### Key Concept

**Comparison with a threshold**

---

## 17. Both Even, Both Odd, or One Each

### Question

Take two numbers and determine whether both are even, both are odd, or one is even and one is odd.

### Answer

```python
def main():
    first = 12
    second = 18

    if first % 2 == 0 and second % 2 == 0:
        print("Both are even")
    elif first % 2 != 0 and second % 2 != 0:
        print("Both are odd")
    else:
        print("One is even and one is odd")


if __name__ == "__main__":
    main()
```

### Explanation

There are three possible cases:

1. Both numbers are even.
2. Both numbers are odd.
3. One is even and the other is odd.

### Test Cases

| First | Second | Expected |
|---:|---:|---|
| `12` | `18` | `Both are even` |
| `5` | `9` | `Both are odd` |
| `4` | `7` | `One is even and one is odd` |
| `8` | `3` | `One is even and one is odd` |

### Key Concept

**Combining modulo and logical operators**

---

## 18. Alphabet Range

### Question

Take an alphabet character and check if it lies between `a` and `m` or `n` and `z`.

### Answer

```python
def main():
    ch = "h"

    if "a" <= ch <= "m":
        print("Between a and m")
    elif "n" <= ch <= "z":
        print("Between n and z")
    else:
        print("Not a lowercase alphabet")


if __name__ == "__main__":
    main()
```

### Explanation

The character is compared with the lowercase alphabet ranges:

- `a–m` → Between a and m
- `n–z` → Between n and z
- Otherwise → Not a lowercase alphabet

### Test Cases

| Input | Expected |
|---|---|
| `a` | `Between a and m` |
| `h` | `Between a and m` |
| `m` | `Between a and m` |
| `n` | `Between n and z` |
| `z` | `Between n and z` |
| `A` | `Not a lowercase alphabet` |
| `7` | `Not a lowercase alphabet` |

### Key Concept

**Character comparison + chained comparisons**

---

## 19. Day Number to Day Name

### Question

Take a day number (`1–7`) and print the corresponding day name.

### Answer

```python
def main():
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

### Explanation

The list indexes start at `0`, but the question numbers the days from `1`.

Therefore:

```text
Day 1 → index 0 → Monday
Day 2 → index 1 → Tuesday
Day 3 → index 2 → Wednesday
...
Day 7 → index 6 → Sunday
```

That's why we use:

```python
days[day - 1]
```

### Test Cases

| Day | Expected |
|---:|---|
| `1` | `Monday` |
| `2` | `Tuesday` |
| `3` | `Wednesday` |
| `5` | `Friday` |
| `7` | `Sunday` |
| `0` | `Invalid day` |
| `8` | `Invalid day` |

### Key Concept

**List indexing**

---

## 20. Days in a Month

### Question

Take a month number (`1–12`) and print the number of days in that month. Ignore leap years.

### Answer

```python
def main():
    month = 2

    if month == 2:
        print("28 days")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("30 days")
    elif 1 <= month <= 12:
        print("31 days")
    else:
        print("Invalid month")


if __name__ == "__main__":
    main()
```

### Explanation

The months are divided into three groups:

```text
February                  → 28 days
April, June, September,
November                  → 30 days
All remaining valid months → 31 days
```

The question explicitly says to **ignore leap years**, so February is treated as having 28 days.

### Test Cases

| Month | Expected |
|---:|---|
| `1` | `31 days` |
| `2` | `28 days` |
| `3` | `31 days` |
| `4` | `30 days` |
| `6` | `30 days` |
| `9` | `30 days` |
| `11` | `30 days` |
| `12` | `31 days` |
| `0` | `Invalid month` |
| `13` | `Invalid month` |

### Key Concept

**Grouping cases with conditions**

---

# Quick Revision — What You Learned

After these 20 questions, you should be comfortable with:

- `if`
- `elif`
- `else`
- Comparison operators: `>`, `<`, `>=`, `<=`, `==`, `!=`
- Modulo operator `%`
- Logical operators: `and`, `or`
- Nested conditions
- Range conditions
- Chained comparisons
- String methods such as `.isupper()`, `.islower()`, `.isdigit()`, `.isalpha()`
- Helper functions
- Boolean return values
- List indexing
- Tracking a current maximum
- Validating input ranges
- Breaking a problem into smaller conditions

---

# Python Operators — Quick Revision

| Meaning | Python |
|---|---|
| Equal | `==` |
| Not equal | `!=` |
| Greater than | `>` |
| Less than | `<` |
| Greater than or equal | `>=` |
| Less than or equal | `<=` |
| AND | `and` |
| OR | `or` |
| NOT | `not` |
| Remainder | `%` |

> **Important:** Python uses `and` and `or`, not `&&` and `||`.

---

# Problem-Solving Method

For every new problem, follow this process:

```text
1. Read the question carefully.
        ↓
2. Identify the input.
        ↓
3. Identify the possible cases.
        ↓
4. Write the conditions in plain English.
        ↓
5. Convert the logic into Python.
        ↓
6. Dry-run with a small example.
        ↓
7. Test normal + boundary + invalid cases.
        ↓
8. Only then look for a cleaner solution.
```

## Example

For:

> Check if a number is even or odd.

Think:

```text
Input → number

Question:
Is number divisible by 2?

Logic:
number % 2 == 0

True  → Even
False → Odd
```

Then write the code.

---

# Final Revision Checklist

Before moving to the next level, make sure you can solve these without looking at the answers:

- [ ] Positive / Negative / Zero
- [ ] Even / Odd
- [ ] Divisible by 5
- [ ] Divisible by 3 and 5
- [ ] Leap Year
- [ ] Larger of Two Numbers
- [ ] Largest of Three Numbers
- [ ] Temperature Classification
- [ ] Vowel / Consonant
- [ ] Character Type
- [ ] Valid Triangle
- [ ] Triangle Type
- [ ] Grade from Marks
- [ ] Multiple of Other Number
- [ ] Greeting Based on Hour
- [ ] Voting Eligibility
- [ ] Even / Odd Combination
- [ ] Alphabet Range
- [ ] Day Number
- [ ] Days in Month

---

# Important Practice Rule

Do **not** memorize the code.

For revision, try to remember:

> **What is the input?**  
> **What are the possible cases?**  
> **What condition separates those cases?**  
> **What should happen for each case?**

If you can answer those four questions, you can write the code.

---

## Next Step

After becoming comfortable with these 20 conditional problems, continue with the remaining Conditional Thinking problems from the PDF. Then move to **Looping & Patterns**, where the focus shifts from decision-making to iteration and dry-run thinking.
