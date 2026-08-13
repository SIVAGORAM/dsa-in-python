# Python Logic Building — Questions 21–30
## Level 3: Math and Number Logic

> **Revision purpose:** Use this README whenever you want to revise Questions 21–30.
>
> **Practice rule:** First read only the question and try to solve it yourself. Then compare your solution with the answer, understand the dry run, and test the listed cases.
>
> These are Questions 1–10 of **Level 3: Math and Number Logic** from the provided Logic Building PDF. fileciteturn1file0L21-L32

---

## Questions List

1. [Question 21 — Distinct Digits](#question-21--distinct-digits)
2. [Question 22 — Middle Digit](#question-22--middle-digit)
3. [Question 23 — First and Last Digits](#question-23--first-and-last-digits)
4. [Question 24 — Number of Digits](#question-24--number-of-digits)
5. [Question 25 — Multiple of 7 or Ends with 7](#question-25--multiple-of-7-or-ends-with-7)
6. [Question 26 — Quadrant](#question-26--quadrant)
7. [Question 27 — Currency Notes](#question-27--currency-notes)
8. [Question 28 — Range [100, 999]](#question-28--range-100-999)
9. [Question 29 — Third Angle](#question-29--third-angle)
10. [Question 30 — Perfect Square](#question-30--perfect-square)

---

# Question 21 — Distinct Digits

## Question

**Take a 3-digit number and check if all digits are distinct.**

## Solution

```python
def main():
    number = 427

    hundreds = number // 100
    tens = (number // 10) % 10
    ones = number % 10

    if hundreds != tens and tens != ones and hundreds != ones:
        print("All digits are distinct")
    else:
        print("Digits are not distinct")


if __name__ == "__main__":
    main()
```

## Explanation

A 3-digit number has hundreds, tens, and ones digits.

For `427`:

```text
hundreds = 427 // 100 = 4
tens = (427 // 10) % 10 = 42 % 10 = 2
ones = 427 % 10 = 7
```

So the digits are `4, 2, 7`.

We compare every pair:

```text
4 != 2 → True
2 != 7 → True
4 != 7 → True
```

All are True, so the digits are distinct.

### Dry Run Example

For `121`:

```text
hundreds = 1
tens = 2
ones = 1

1 != 2 → True
2 != 1 → True
1 != 1 → False
```

Output:

```text
Digits are not distinct
```

### Test Cases

| Input | Expected Output |
|---:|---|
| `427` | All digits are distinct |
| `123` | All digits are distinct |
| `121` | Digits are not distinct |
| `111` | Digits are not distinct |
| `455` | Digits are not distinct |
| `987` | All digits are distinct |

### Key Concepts

```text
//  → Integer division
%   → Remainder
!=  → Not equal
and → All conditions must be True
```

---

# Question 22 — Middle Digit

## Question

**Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither.**

## Solution

```python
def main():
    number = 582

    hundreds = number // 100
    middle = (number // 10) % 10
    ones = number % 10

    if middle > hundreds and middle > ones:
        print("Middle digit is largest")
    elif middle < hundreds and middle < ones:
        print("Middle digit is smallest")
    else:
        print("Middle digit is neither")


if __name__ == "__main__":
    main()
```

## Explanation

For `582`:

```text
hundreds = 5
middle = 8
ones = 2
```

Check if middle is largest:

```text
8 > 5 → True
8 > 2 → True
```

Therefore:

```text
Middle digit is largest
```

To check if it is smallest, both conditions must be true:

```python
middle < hundreds and middle < ones
```

If neither strict comparison is true, the result is `neither`.

### Dry Run Example

For `555`:

```text
hundreds = 5
middle = 5
ones = 5

5 > 5 → False
5 < 5 → False
```

Therefore:

```text
Middle digit is neither
```

### Test Cases

| Input | Expected Output |
|---:|---|
| `582` | Middle digit is largest |
| `318` | Middle digit is smallest |
| `555` | Middle digit is neither |
| `123` | Middle digit is largest |
| `321` | Middle digit is smallest |
| `585` | Middle digit is largest |
| `525` | Middle digit is smallest |

### Key Concepts

```text
//  → Integer division
%   → Remainder
>   → Greater than
<   → Less than
and → Both conditions must be True
```

---

# Question 23 — First and Last Digits

## Question

**Take a 4-digit number and check if the first and last digits are equal.**

## Solution

```python
def main():
    number = 4554

    first_digit = number // 1000
    last_digit = number % 10

    if first_digit == last_digit:
        print("First and last digits are equal")
    else:
        print("First and last digits are not equal")


if __name__ == "__main__":
    main()
```

## Explanation

For a 4-digit number:

```text
number // 1000 → first digit
number % 10    → last digit
```

For `4554`:

```text
4554 // 1000 = 4
4554 % 10 = 4
```

Then:

```text
4 == 4 → True
```

So the first and last digits are equal.

### Dry Run Example

For `1234`:

```text
first_digit = 1234 // 1000 = 1
last_digit = 1234 % 10 = 4

1 == 4 → False
```

Output:

```text
First and last digits are not equal
```

### Test Cases

| Input | Expected Output |
|---:|---|
| `4554` | First and last digits are equal |
| `1234` | First and last digits are not equal |
| `1001` | First and last digits are equal |
| `5678` | First and last digits are not equal |
| `9999` | First and last digits are equal |
| `4321` | First and last digits are not equal |

### Key Concepts

```text
// → Integer division
%  → Remainder
== → Equal to
```

---

# Question 24 — Number of Digits

## Question

**Check whether a given integer is single-digit, double-digit, or multi-digit.**

## Solution

```python
def main():
    number = 87

    value = abs(number)

    if value <= 9:
        print("Single-digit")
    elif value <= 99:
        print("Double-digit")
    else:
        print("Multi-digit")


if __name__ == "__main__":
    main()
```

## Explanation

We use `abs()` so the negative sign does not affect the digit count.

For `87`:

```text
abs(87) = 87

87 <= 9 → False
87 <= 99 → True
```

Therefore:

```text
Double-digit
```

For `-7`:

```text
abs(-7) = 7
7 <= 9 → True
```

Therefore:

```text
Single-digit
```

### Dry Run Example

For `-125`:

```text
value = abs(-125)
value = 125

125 <= 9 → False
125 <= 99 → False
```

Output:

```text
Multi-digit
```

### Test Cases

| Input | Expected Output |
|---:|---|
| `7` | Single-digit |
| `-7` | Single-digit |
| `87` | Double-digit |
| `-99` | Double-digit |
| `100` | Multi-digit |
| `-125` | Multi-digit |
| `0` | Single-digit |

### Key Concepts

```text
abs() → Absolute value
<=    → Less than or equal to
```

---

# Question 25 — Multiple of 7 or Ends with 7

## Question

**Check if a number is a multiple of 7 or ends with 7.**

## Solution

```python
def main():
    number = 147

    if number % 7 == 0 or abs(number) % 10 == 7:
        print("Matches condition")
    else:
        print("Does not match condition")


if __name__ == "__main__":
    main()
```

## Explanation

There are two conditions:

1. The number is a multiple of 7.
2. The number ends with 7.

We use `or` because at least one condition must be True.

For `147`:

```text
147 % 7 = 0
```

So it is a multiple of 7.

Also:

```text
147 % 10 = 7
```

So it ends with 7.

Therefore:

```text
Matches condition
```

### Dry Run Example

For `25`:

```text
25 % 7 = 4
25 % 10 = 5

25 % 7 == 0 → False
25 % 10 == 7 → False
```

Therefore:

```text
Does not match condition
```

### Test Cases

| Input | Expected Output |
|---:|---|
| `147` | Matches condition |
| `21` | Matches condition |
| `27` | Matches condition |
| `25` | Does not match condition |
| `77` | Matches condition |
| `70` | Matches condition |
| `-27` | Matches condition |

### Key Concepts

```text
%   → Remainder
or  → At least one condition must be True
abs → Absolute value
```

---

# Question 26 — Quadrant

## Question

**Take coordinates (x, y) and determine which quadrant the point lies in.**

## Solution

```python
def main():
    x = -4
    y = 6

    if x > 0 and y > 0:
        print("Quadrant I")
    elif x < 0 and y > 0:
        print("Quadrant II")
    elif x < 0 and y < 0:
        print("Quadrant III")
    elif x > 0 and y < 0:
        print("Quadrant IV")
    else:
        print("Point lies on an axis or origin")


if __name__ == "__main__":
    main()
```

## Explanation

The signs of `x` and `y` determine the quadrant:

```text
(+ , +) → Quadrant I
(- , +) → Quadrant II
(- , -) → Quadrant III
(+ , -) → Quadrant IV
```

For:

```text
x = -4
y = 6
```

```text
x < 0 → True
y > 0 → True
```

Therefore:

```text
Quadrant II
```

If `x` or `y` is zero, the point lies on an axis. If both are zero, it is the origin.

### Dry Run

```text
x = -4
y = 6

x > 0 and y > 0 → False
x < 0 and y > 0 → True
```

Output:

```text
Quadrant II
```

### Test Cases

| x | y | Expected Output |
|---:|---:|---|
| `4` | `6` | Quadrant I |
| `-4` | `6` | Quadrant II |
| `-4` | `-6` | Quadrant III |
| `4` | `-6` | Quadrant IV |
| `0` | `5` | Point lies on an axis or origin |
| `5` | `0` | Point lies on an axis or origin |
| `0` | `0` | Point lies on an axis or origin |

### Key Concepts

```text
>   → Greater than
<   → Less than
and → Both conditions must be True
```

---

# Question 27 — Currency Notes

## Question

**Check if an amount can be evenly divided into 2000, 500, and 100 currency notes.**

## Solution

```python
def main():
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
```

## Explanation

We use only:

```text
2000
500
100
```

For `7600`:

### Step 1 — 2000 notes

```text
7600 // 2000 = 3
7600 % 2000 = 1600
```

So:

```text
3 × 2000 = 6000
Remaining = 1600
```

### Step 2 — 500 notes

```text
1600 // 500 = 3
1600 % 500 = 100
```

So:

```text
3 × 500 = 1500
Remaining = 100
```

### Step 3 — 100 notes

```text
100 // 100 = 1
100 % 100 = 0
```

So:

```text
1 × 100 = 100
Remaining = 0
```

Nothing remains, therefore:

```text
2000: 3, 500: 3, 100: 1
```

### Dry Run Example

For `7650`:

```text
7650 // 2000 = 3
remaining = 1650

1650 // 500 = 3
remaining = 150

150 // 100 = 1
remaining = 50
```

`50` remains, so the amount cannot be fully divided.

### Test Cases

| Amount | Expected Output |
|---:|---|
| `7600` | `2000: 3, 500: 3, 100: 1` |
| `7500` | `2000: 3, 500: 3, 100: 0` |
| `1000` | `2000: 0, 500: 2, 100: 0` |
| `2000` | `2000: 1, 500: 0, 100: 0` |
| `7650` | Amount cannot be fully divided into these notes |
| `50` | Amount cannot be fully divided into these notes |
| `0` | `2000: 0, 500: 0, 100: 0` |

### Key Concepts

```text
// → Integer division
%  → Remainder
%= → Update variable with remainder
== → Equality comparison
```

Important:

Use `//` when counting whole notes.

---

# Question 28 — Range [100, 999]

## Question

**Check if a number lies within the range [100, 999].**

## Solution

```python
def main():
    number = 456

    if number >= 100 and number <= 999:
        print("Inside range")
    else:
        print("Outside range")


if __name__ == "__main__":
    main()
```

## Explanation

The range `[100, 999]` is inclusive.

That means:

```text
100 is included
999 is included
```

For `456`:

```text
456 >= 100 → True
456 <= 999 → True
```

Therefore:

```text
Inside range
```

### Dry Run

For `100`:

```text
100 >= 100 → True
100 <= 999 → True
```

So:

```text
Inside range
```

For `1000`:

```text
1000 >= 100 → True
1000 <= 999 → False
```

So:

```text
Outside range
```

### Test Cases

| Input | Expected Output |
|---:|---|
| `456` | Inside range |
| `100` | Inside range |
| `999` | Inside range |
| `99` | Outside range |
| `1000` | Outside range |
| `500` | Inside range |
| `0` | Outside range |

### Key Concepts

```text
>=  → Greater than or equal to
<=  → Less than or equal to
and → Both conditions must be True
```

Python also allows:

```python
100 <= number <= 999
```

---

# Question 29 — Third Angle

## Question

**Take two angles of a triangle and compute the third angle.**

## Solution

```python
def main():
    first_angle = 50
    second_angle = 60

    third_angle = 180 - first_angle - second_angle

    print("Third angle =", third_angle)


if __name__ == "__main__":
    main()
```

## Explanation

The three interior angles of a triangle add up to `180°`.

Formula:

```text
third angle = 180 - first angle - second angle
```

For:

```text
first_angle = 50
second_angle = 60
```

Calculate:

```text
180 - 50 = 130
130 - 60 = 70
```

Therefore:

```text
third_angle = 70
```

### Dry Run

For:

```text
first_angle = 90
second_angle = 45
```

```text
third_angle = 180 - 90 - 45
third_angle = 45
```

Output:

```text
Third angle = 45
```

### Test Cases

| First Angle | Second Angle | Expected Third Angle |
|---:|---:|---:|
| `50` | `60` | `70` |
| `90` | `45` | `45` |
| `30` | `80` | `70` |
| `60` | `60` | `60` |
| `100` | `30` | `50` |

### Key Concepts

```text
- → Subtraction
```

Important:

This question asks only to calculate the third angle. It does not ask us to validate the given angles.

---

# Question 30 — Perfect Square

## Question

**Check whether a number is a perfect square (without using the square root function).**

## Solution

```python
def main():
    number = 49

    perfect_square = False
    i = 1

    while i * i <= number:
        if i * i == number:
            perfect_square = True
            break

        i += 1

    print("Perfect square" if perfect_square else "Not a perfect square")


if __name__ == "__main__":
    main()
```

## Explanation

A perfect square is a number that can be obtained by multiplying a whole number by itself.

Examples:

```text
1 × 1 = 1
2 × 2 = 4
3 × 3 = 9
4 × 4 = 16
5 × 5 = 25
6 × 6 = 36
7 × 7 = 49
```

For `49`, we start with `i = 1` and check `i * i`.

```text
1 × 1 = 1  → Not 49
2 × 2 = 4  → Not 49
3 × 3 = 9  → Not 49
4 × 4 = 16 → Not 49
5 × 5 = 25 → Not 49
6 × 6 = 36 → Not 49
7 × 7 = 49 → Found
```

When `i * i == number`:

```text
perfect_square = True
```

Then `break` stops the loop.

Output:

```text
Perfect square
```

### Dry Run — Not a Perfect Square

For `20`:

```text
1 × 1 = 1
2 × 2 = 4
3 × 3 = 9
4 × 4 = 16
5 × 5 = 25
```

At `i = 5`:

```text
25 <= 20 → False
```

The loop stops.

We never found `i * i == 20`.

Therefore:

```text
Not a perfect square
```

### Why `i * i <= number`?

Once `i * i` becomes greater than the number, every larger square will also be greater.

So there is no need to continue.

### Why `break`?

`break` immediately stops the loop after finding the answer.

### Test Cases

| Input | Expected Output |
|---:|---|
| `49` | Perfect square |
| `25` | Perfect square |
| `1` | Perfect square |
| `16` | Perfect square |
| `20` | Not a perfect square |
| `50` | Not a perfect square |
| `81` | Perfect square |

> **Implementation note:** The exact solution above starts `i` at `1`, so `0` is not detected as a perfect square. Mathematically, `0` is a perfect square; handling it would require a small special case.

### Key Concepts

```text
while → Repeats while condition is True
i * i → Square of i
break → Immediately stops the loop
+= 1 → Increases i by 1
Boolean variable → Stores True or False
```

---

# Quick Revision Table

| Question | Main Skill |
|---:|---|
| 21 | Extracting digits + comparing |
| 22 | Extracting digits + finding relative position |
| 23 | First/last digit extraction |
| 24 | Range checking + `abs()` |
| 25 | `%` + `or` |
| 26 | Coordinate logic |
| 27 | `//` + `%` + remainder tracking |
| 28 | Inclusive range |
| 29 | Formula-based calculation |
| 30 | `while` + `break` + mathematical checking |

---

# Final Revision Checklist

Try to solve each question **without looking at the solution**:

- [ ] Q21 — All digits distinct
- [ ] Q22 — Middle digit largest/smallest/neither
- [ ] Q23 — First and last digits equal
- [ ] Q24 — Single/double/multi-digit
- [ ] Q25 — Multiple of 7 or ends with 7
- [ ] Q26 — Quadrant
- [ ] Q27 — Currency notes
- [ ] Q28 — Range `[100, 999]`
- [ ] Q29 — Third angle
- [ ] Q30 — Perfect square

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

Once you can do these 10 questions without looking at the answers, move forward to the next set of logic-building problems.
