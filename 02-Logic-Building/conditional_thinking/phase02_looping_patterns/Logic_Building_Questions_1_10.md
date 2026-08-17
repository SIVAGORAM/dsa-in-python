# Python Logic Building — Questions 1 to 10

Complete revision guide for Questions 1–10 with questions, solutions, explanations, dry runs, examples, test cases, common mistakes, and key concepts.

---

## Question 1 — Print Numbers from 1 to 10

### Question
Print numbers from 1 to 10.

### Solution

```python
def main():
    # Question 1: Print numbers from 1 to 10.
    for number in range(1, 10 + 1):
        print(number)


if __name__ == "__main__":
    main()
```

### Explanation

We need to print every number starting from `1` and ending at `10`.

Python's `range(start, stop)` includes the start value but excludes the stop value.

Therefore:

```python
range(1, 10 + 1)
```

becomes:

```python
range(1, 11)
```

This generates numbers from `1` through `10`.

### Dry Run

| Iteration | number | Action |
|---:|---:|---|
| 1 | 1 | Print 1 |
| 2 | 2 | Print 2 |
| 3 | 3 | Print 3 |
| 4 | 4 | Print 4 |
| 5 | 5 | Print 5 |
| 6 | 6 | Print 6 |
| 7 | 7 | Print 7 |
| 8 | 8 | Print 8 |
| 9 | 9 | Print 9 |
| 10 | 10 | Print 10 |

### Output

```text
1
2
3
4
5
6
7
8
9
10
```

### Test Cases

| Requirement | Expected |
|---|---|
| Print 1 to 10 | `1` through `10` |
| Print 1 to 5 | `1 2 3 4 5` |
| Print 5 to 10 | `5 6 7 8 9 10` |
| Print only 1 | `1` |

### Common Mistake

```python
range(1, 10)
```

does not print `10`.

Use:

```python
range(1, 11)
```

### Key Concept

**`range()` → start included, stop excluded.**

---

## Question 2 — Print All Even Numbers Between 1 and 100

### Question
Print all even numbers between 1 and 100.

### Solution

```python
def main():
    # Question 2: Print all even numbers between 1 and 100.
    for number in range(1, 100 + 1):
        if number % 2 == 0:
            print(number)


if __name__ == "__main__":
    main()
```

### Explanation

An even number is completely divisible by `2`.

We check this using:

```python
number % 2 == 0
```

The `%` operator gives the remainder.

Examples:

```text
10 % 2 = 0 → Even
11 % 2 = 1 → Odd
12 % 2 = 0 → Even
```

The loop checks every number from `1` to `100`, and the `if` condition prints only even numbers.

### Dry Run

| number | `number % 2` | Condition | Action |
|---:|---:|---|---|
| 1 | 1 | False | Skip |
| 2 | 0 | True | Print 2 |
| 3 | 1 | False | Skip |
| 4 | 0 | True | Print 4 |
| 5 | 1 | False | Skip |
| 6 | 0 | True | Print 6 |
| 7 | 1 | False | Skip |
| 8 | 0 | True | Print 8 |
| 9 | 1 | False | Skip |
| 10 | 0 | True | Print 10 |

The same process continues until `100`.

### Output

```text
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
```

### Alternative Solution

```python
for number in range(2, 101, 2):
    print(number)
```

### Test Cases

| Range | Expected |
|---|---|
| 1–10 | `2 4 6 8 10` |
| 1–20 | `2 4 6 8 10 12 14 16 18 20` |
| 1–100 | `2 4 6 ... 100` |
| Only 1 | No output |
| Only 2 | `2` |

### Key Concept

```python
number % 2 == 0
```

means **even number**.

---

## Question 3 — Print All Odd Numbers Between 1 and 100

### Question
Print all odd numbers between 1 and 100.

### Solution

```python
def main():
    # Question 3: Print all odd numbers between 1 and 100.
    for number in range(1, 100 + 1):
        if number % 2 != 0:
            print(number)


if __name__ == "__main__":
    main()
```

### Explanation

An odd number leaves a non-zero remainder when divided by `2`.

We use:

```python
number % 2 != 0
```

Examples:

```text
1 % 2 = 1 → Odd
2 % 2 = 0 → Even
3 % 2 = 1 → Odd
4 % 2 = 0 → Even
```

### Dry Run

| number | `number % 2` | Condition | Action |
|---:|---:|---|---|
| 1 | 1 | True | Print 1 |
| 2 | 0 | False | Skip |
| 3 | 1 | True | Print 3 |
| 4 | 0 | False | Skip |
| 5 | 1 | True | Print 5 |
| 6 | 0 | False | Skip |
| 7 | 1 | True | Print 7 |
| 8 | 0 | False | Skip |
| 9 | 1 | True | Print 9 |
| 10 | 0 | False | Skip |

### Output

```text
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99
```

### Alternative Solution

```python
for number in range(1, 101, 2):
    print(number)
```

### Test Cases

| Range | Expected |
|---|---|
| 1–10 | `1 3 5 7 9` |
| 1–20 | `1 3 5 7 9 11 13 15 17 19` |
| 1–100 | `1 3 5 ... 99` |
| Only 1 | `1` |
| Only 2 | No output |

### Key Concept

```python
number % 2 != 0
```

means **odd number**.

---

## Question 4 — Print Numbers from 10 Down to 1

### Question
Print numbers from 10 down to 1.

### Solution

```python
def main():
    # Question 4: Print numbers from 10 down to 1.
    for number in range(10, 1 - 1, -1):
        print(number)


if __name__ == "__main__":
    main()
```

### Explanation

We need to move backward:

```text
10 → 9 → 8 → 7 → 6 → 5 → 4 → 3 → 2 → 1
```

The loop can be written as:

```python
range(10, 0, -1)
```

Here:

- Start = `10`
- Stop = `0`
- Step = `-1`

The negative step decreases the value by `1`.

The stop value `0` is excluded, so `1` is the last printed number.

### Dry Run

| Iteration | number | Action |
|---:|---:|---|
| 1 | 10 | Print 10 |
| 2 | 9 | Print 9 |
| 3 | 8 | Print 8 |
| 4 | 7 | Print 7 |
| 5 | 6 | Print 6 |
| 6 | 5 | Print 5 |
| 7 | 4 | Print 4 |
| 8 | 3 | Print 3 |
| 9 | 2 | Print 2 |
| 10 | 1 | Print 1 |

### Output

```text
10
9
8
7
6
5
4
3
2
1
```

### Test Cases

| Requirement | Expected |
|---|---|
| 10 to 1 | `10 9 8 ... 1` |
| 5 to 1 | `5 4 3 2 1` |
| 10 to 5 | `10 9 8 7 6 5` |
| 1 to 1 | `1` |

### Common Mistake

```python
range(10, 1, -1)
```

does not include `1`.

Use:

```python
range(10, 0, -1)
```

### Key Concept

**Negative step → move backward.**

---

## Question 5 — Print the Multiplication Table

### Question
Print the table of a given number from `n × 1` to `n × 10`.

### Solution

```python
def main():
    # Question 5: Print the table of a given number.
    n = 7

    for multiplier in range(1, 10 + 1):
        print(str(n) + " x " + str(multiplier) + " = " + str(n * multiplier))


if __name__ == "__main__":
    main()
```

### Explanation

For:

```text
n = 7
```

we need:

```text
7 × 1
7 × 2
7 × 3
...
7 × 10
```

`n` stays fixed.

`multiplier` changes from `1` to `10`.

For every iteration:

```python
n * multiplier
```

is calculated.

### Dry Run

| n | multiplier | Calculation | Output |
|---:|---:|---:|---|
| 7 | 1 | 7 × 1 = 7 | 7 x 1 = 7 |
| 7 | 2 | 7 × 2 = 14 | 7 x 2 = 14 |
| 7 | 3 | 7 × 3 = 21 | 7 x 3 = 21 |
| 7 | 4 | 7 × 4 = 28 | 7 x 4 = 28 |
| 7 | 5 | 7 × 5 = 35 | 7 x 5 = 35 |
| 7 | 6 | 7 × 6 = 42 | 7 x 6 = 42 |
| 7 | 7 | 7 × 7 = 49 | 7 x 7 = 49 |
| 7 | 8 | 7 × 8 = 56 | 7 x 8 = 56 |
| 7 | 9 | 7 × 9 = 63 | 7 x 9 = 63 |
| 7 | 10 | 7 × 10 = 70 | 7 x 10 = 70 |

### Output

```text
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

### Test Cases

| Input | Expected final line |
|---:|---|
| 7 | `7 x 10 = 70` |
| 5 | `5 x 10 = 50` |
| 10 | `10 x 10 = 100` |
| 0 | `0 x 10 = 0` |
| -5 | `-5 x 10 = -50` |

### Key Concepts

- `for` loop
- `range(1, 11)`
- multiplication
- loop variable
- string conversion

---

## Question 6 — Sum of First n Natural Numbers

### Question
Print the sum of the first `n` natural numbers.

### Solution

```python
def main():
    # Question 6: Print the sum of first n natural numbers.
    n = 10
    total = 0

    for number in range(1, n + 1):
        total += number

    print("Sum = " + str(total))


if __name__ == "__main__":
    main()
```

### Explanation

For:

```text
n = 10
```

we calculate:

```text
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
```

`total` is an accumulator.

Start:

```python
total = 0
```

Then:

```python
total += number
```

means:

```python
total = total + number
```

### Dry Run

| number | Previous total | Calculation | New total |
|---:|---:|---|---:|
| 1 | 0 | 0 + 1 | 1 |
| 2 | 1 | 1 + 2 | 3 |
| 3 | 3 | 3 + 3 | 6 |
| 4 | 6 | 6 + 4 | 10 |
| 5 | 10 | 10 + 5 | 15 |
| 6 | 15 | 15 + 6 | 21 |
| 7 | 21 | 21 + 7 | 28 |
| 8 | 28 | 28 + 8 | 36 |
| 9 | 36 | 36 + 9 | 45 |
| 10 | 45 | 45 + 10 | 55 |

### Output

```text
Sum = 55
```

### Test Cases

| Input | Expected |
|---:|---:|
| 10 | `55` |
| 5 | `15` |
| 3 | `6` |
| 1 | `1` |
| 0 | `0` |
| 100 | `5050` |

### Important Concept — Accumulator

For a sum:

```python
total = 0

for number in range(...):
    total += number
```

Start addition with `0`.

### Common Mistake

Prefer:

```python
total = 0
```

instead of:

```python
sum = 0
```

because `sum()` is already a Python built-in function.

---

## Question 7 — Sum of All Even Numbers up to n

### Question
Print the sum of all even numbers up to `n`.

### Solution

```python
def main():
    # Question 7: Print the sum of all even numbers up to n.
    n = 20
    total = 0

    for number in range(1, n + 1):
        if number % 2 == 0:
            total += number

    print("Even sum = " + str(total))


if __name__ == "__main__":
    main()
```

### Explanation

For:

```text
n = 20
```

the even numbers are:

```text
2, 4, 6, 8, 10, 12, 14, 16, 18, 20
```

Their sum is:

```text
110
```

We check even numbers using:

```python
number % 2 == 0
```

Only numbers satisfying the condition are added.

### Dry Run

| number | Even? | total |
|---:|:---:|---:|
| 1 | No | 0 |
| 2 | Yes | 2 |
| 3 | No | 2 |
| 4 | Yes | 6 |
| 5 | No | 6 |
| 6 | Yes | 12 |
| 7 | No | 12 |
| 8 | Yes | 20 |
| 9 | No | 20 |
| 10 | Yes | 30 |
| 11 | No | 30 |
| 12 | Yes | 42 |
| 13 | No | 42 |
| 14 | Yes | 56 |
| 15 | No | 56 |
| 16 | Yes | 72 |
| 17 | No | 72 |
| 18 | Yes | 90 |
| 19 | No | 90 |
| 20 | Yes | 110 |

### Output

```text
Even sum = 110
```

### Alternative Solution

```python
for number in range(2, n + 1, 2):
    total += number
```

This directly generates even numbers.

### Test Cases

| Input | Expected |
|---:|---:|
| 20 | `110` |
| 10 | `30` |
| 5 | `6` |
| 2 | `2` |
| 1 | `0` |
| 0 | `0` |
| 100 | `2550` |

### Key Pattern

```python
if number % 2 == 0:
    total += number
```

This combines:

**loop + condition + modulo + accumulator**

---

## Question 8 — Sum of All Odd Numbers up to n

### Question
Print the sum of all odd numbers up to `n`.

### Solution

```python
def main():
    # Question 8: Print the sum of all odd numbers up to n.
    n = 20
    total = 0

    for number in range(1, n + 1):
        if number % 2 != 0:
            total += number

    print("Odd sum = " + str(total))


if __name__ == "__main__":
    main()
```

### Explanation

For:

```text
n = 20
```

the odd numbers are:

```text
1, 3, 5, 7, 9, 11, 13, 15, 17, 19
```

Their sum is:

```text
100
```

We identify odd numbers using:

```python
number % 2 != 0
```

### Dry Run

| number | Odd? | total |
|---:|:---:|---:|
| 1 | Yes | 1 |
| 2 | No | 1 |
| 3 | Yes | 4 |
| 4 | No | 4 |
| 5 | Yes | 9 |
| 6 | No | 9 |
| 7 | Yes | 16 |
| 8 | No | 16 |
| 9 | Yes | 25 |
| 10 | No | 25 |
| 11 | Yes | 36 |
| 12 | No | 36 |
| 13 | Yes | 49 |
| 14 | No | 49 |
| 15 | Yes | 64 |
| 16 | No | 64 |
| 17 | Yes | 81 |
| 18 | No | 81 |
| 19 | Yes | 100 |
| 20 | No | 100 |

### Output

```text
Odd sum = 100
```

### Alternative Solution

```python
for number in range(1, n + 1, 2):
    total += number
```

### Test Cases

| Input | Expected |
|---:|---:|
| 20 | `100` |
| 10 | `25` |
| 5 | `9` |
| 3 | `4` |
| 1 | `1` |
| 2 | `1` |
| 0 | `0` |

### Q7 vs Q8

| Requirement | Condition |
|---|---|
| Even | `number % 2 == 0` |
| Odd | `number % 2 != 0` |

---

## Question 9 — Factorial of a Given Number

### Question
Print the factorial of a given number.

### Solution

```python
def factorial(number):
    result = 1

    for value in range(2, number + 1):
        result *= value

    return result


def main():
    # Question 9: Print the factorial of a given number.
    number = 5

    print(str(number) + "! = " + str(factorial(number)))


if __name__ == "__main__":
    main()
```

### Important Correction

The correct output format is:

```text
5! = 120
```

not:

```text
5not = 120
```

### Explanation

Factorial means multiplying all positive integers from `1` through the given number.

```text
5! = 5 × 4 × 3 × 2 × 1
   = 120
```

Important:

```text
0! = 1
```

We start:

```python
result = 1
```

because this is a multiplication accumulator.

Then:

```python
range(2, number + 1)
```

for `number = 5` produces:

```text
2, 3, 4, 5
```

### Dry Run

| value | Previous result | Calculation | New result |
|---:|---:|---|---:|
| 2 | 1 | 1 × 2 | 2 |
| 3 | 2 | 2 × 3 | 6 |
| 4 | 6 | 6 × 4 | 24 |
| 5 | 24 | 24 × 5 | 120 |

### Output

```text
5! = 120
```

### Examples

```text
3! = 6
4! = 24
5! = 120
6! = 720
0! = 1
```

### Test Cases

| Input | Expected |
|---:|---:|
| 0 | `1` |
| 1 | `1` |
| 3 | `6` |
| 4 | `24` |
| 5 | `120` |
| 6 | `720` |

### Common Mistakes

Do not start multiplication with:

```python
result = 0
```

because anything multiplied by zero becomes zero.

Use:

```python
result = 1
```

Also, Python does not use:

```text
number++
```

The `range()` function supplies the next value.

### Key Concept

**Addition accumulator starts at 0; multiplication accumulator starts at 1.**

---

## Question 10 — Product of Digits of a Given Number

### Question
Print the product of digits of a given number.

### Solution

```python
def productDigits(number):
    value = abs(number)
    product = 1

    if value == 0:
        return 0

    while value > 0:
        product *= value % 10
        value //= 10

    return product


def main():
    # Question 10: Print the product of digits of a given number.
    number = 2345

    print("Product of digits = " + str(productDigits(number)))


if __name__ == "__main__":
    main()
```

### Explanation

For:

```text
2345
```

the digits are:

```text
2, 3, 4, 5
```

Multiply them:

```text
2 × 3 × 4 × 5 = 120
```

The important digit-extraction pattern is:

```python
digit = value % 10
value //= 10
```

Meaning:

```text
% 10  → get the last digit
// 10 → remove the last digit
```

### Dry Run

Initial:

```text
value = 2345
product = 1
```

| Iteration | value before | Last digit | Product | value after |
|---:|---:|---:|---:|---:|
| 1 | 2345 | 5 | 5 | 234 |
| 2 | 234 | 4 | 20 | 23 |
| 3 | 23 | 3 | 60 | 2 |
| 4 | 2 | 2 | 120 | 0 |

Final product:

```text
120
```

### Detailed Calculation

```text
1 × 5 = 5
5 × 4 = 20
20 × 3 = 60
60 × 2 = 120
```

### Why `product = 1`?

We are multiplying.

```text
1 × 5 = 5
```

If we started with `0`, the result would always remain `0`.

### Why `abs()`?

For a negative number such as:

```text
-234
```

`abs()` converts it to:

```text
234
```

Then:

```text
2 × 3 × 4 = 24
```

### Why Handle Zero Separately?

For:

```text
number = 0
```

the product of the digit is `0`.

The loop would not execute because `value > 0` is false, so the function explicitly returns `0`.

### Examples

```text
123 → 1 × 2 × 3 = 6
456 → 4 × 5 × 6 = 120
1111 → 1 × 1 × 1 × 1 = 1
25 → 2 × 5 = 10
0 → 0
-234 → 2 × 3 × 4 = 24
203 → 2 × 0 × 3 = 0
```

### Test Cases

| Input | Calculation | Expected |
|---:|---|---:|
| 2345 | `2×3×4×5` | `120` |
| 123 | `1×2×3` | `6` |
| 456 | `4×5×6` | `120` |
| 1111 | `1×1×1×1` | `1` |
| 25 | `2×5` | `10` |
| 0 | `0` | `0` |
| -234 | `2×3×4` | `24` |
| 203 | `2×0×3` | `0` |

### Important Pattern

```python
digit = value % 10
value //= 10
```

This pattern is extremely important for number-based problems.

### Sum of Digits vs Product of Digits

Sum:

```python
total = 0

while value > 0:
    digit = value % 10
    total += digit
    value //= 10
```

Product:

```python
product = 1

while value > 0:
    digit = value % 10
    product *= digit
    value //= 10
```

The digit extraction is the same. Only the accumulator operation changes.

### Key Concepts

- `while` loop
- `% 10`
- `// 10`
- digit extraction
- multiplication accumulator
- `abs()`
- zero edge case

---

# Quick Revision — Questions 1 to 10

| Q | Topic | Main Concept |
|---:|---|---|
| 1 | Print 1 to 10 | `for` + `range()` |
| 2 | Even numbers 1–100 | `% 2 == 0` |
| 3 | Odd numbers 1–100 | `% 2 != 0` |
| 4 | 10 down to 1 | negative `range()` step |
| 5 | Multiplication table | loop + multiplication |
| 6 | Sum of first n numbers | accumulator |
| 7 | Sum of even numbers | condition + accumulator |
| 8 | Sum of odd numbers | condition + accumulator |
| 9 | Factorial | multiplication accumulator |
| 10 | Product of digits | `% 10` + `// 10` |

---

# Most Important Patterns to Remember

## 1. Forward Loop

```python
for number in range(1, 11):
    print(number)
```

## 2. Backward Loop

```python
for number in range(10, 0, -1):
    print(number)
```

## 3. Even Number

```python
number % 2 == 0
```

## 4. Odd Number

```python
number % 2 != 0
```

## 5. Sum Accumulator

```python
total = 0

for number in range(...):
    total += number
```

## 6. Multiplication Accumulator

```python
result = 1

for number in range(...):
    result *= number
```

## 7. Get Last Digit

```python
digit = number % 10
```

## 8. Remove Last Digit

```python
number //= 10
```

---

# Final Revision Checklist

- [ ] Understand how `range()` works.
- [ ] Understand that the stop value is excluded.
- [ ] Create a forward loop.
- [ ] Create a backward loop.
- [ ] Check even numbers.
- [ ] Check odd numbers.
- [ ] Use an accumulator.
- [ ] Know why addition starts at `0`.
- [ ] Know why multiplication starts at `1`.
- [ ] Understand factorial.
- [ ] Understand `% 10` for extracting digits.
- [ ] Understand `// 10` for removing digits.
- [ ] Handle zero in product-of-digits problems.
- [ ] Prefer `total` instead of `sum` as a variable name.
- [ ] Remember that Python does not use `number++` or `number--`.

---

# Core Mental Model

```text
Q1
FOR LOOP
    ↓
Print numbers

Q2–Q3
FOR LOOP
    ↓
CONDITION
    ↓
Even / Odd

Q4
FOR LOOP
    ↓
NEGATIVE STEP
    ↓
Backward

Q5
FOR LOOP
    ↓
MULTIPLICATION
    ↓
Table

Q6
FOR LOOP
    ↓
ACCUMULATOR
    ↓
Sum

Q7–Q8
FOR LOOP
    ↓
CONDITION
    ↓
ACCUMULATOR
    ↓
Even/Odd Sum

Q9
FOR LOOP
    ↓
MULTIPLICATION ACCUMULATOR
    ↓
Factorial

Q10
WHILE LOOP
    ↓
% 10
    ↓
Get digit
    ↓
 // 10
    ↓
Remove digit
    ↓
Product
```

These ten questions establish the core loop, condition, accumulator, and digit-processing patterns needed for the next set of Python logic-building problems.
