# Python Logic Building --- Questions 11 to 20

## Quick Revision README

This README contains Questions **11 to 20** from the Python Logic
Building practice set.

For every question:

-   Question
-   What the question means
-   Answer / solution
-   Step-by-step explanation
-   Dry run
-   Important Python concepts
-   Examples
-   Test cases
-   Common mistakes
-   Interview explanation
-   Memory trick
-   Final logic
-   Main thing to remember

------------------------------------------------------------------------

# Question 11 --- Count the Number of Digits

## Question

Count the number of digits in a given number.

### Example

``` text
Input: 98765
Output: Digits = 5
```

## What Does the Question Mean?

We need to find how many digits are present in a number.

For:

``` text
98765
```

The digits are:

``` text
9 8 7 6 5
```

Therefore:

``` text
Number of digits = 5
```

## Answer

``` python
def main():
    number = 98765
    value = abs(number)
    count = 0

    while True:
        count += 1
        value //= 10

        if not (value > 0):
            break

    print("Digits = " + str(count))


if __name__ == "__main__":
    main()
```

## Step-by-Step Explanation

### 1. Store the number

``` python
number = 98765
```

### 2. Use `abs()`

``` python
value = abs(number)
```

This handles negative numbers.

``` text
abs(-98765) = 98765
```

The negative sign is not a digit.

### 3. Start the counter

``` python
count = 0
```

### 4. Remove one digit at a time

``` python
value //= 10
```

Examples:

``` text
98765 → 9876 → 987 → 98 → 9 → 0
```

Each time a digit is removed:

``` python
count += 1
```

## Dry Run

Input:

``` text
number = 98765
value = 98765
count = 0
```

  Iteration     Value Before   Count   Value After
  ----------- -------------- ------- -------------
  1                    98765       1          9876
  2                     9876       2           987
  3                      987       3            98
  4                       98       4             9
  5                        9       5             0

When `value` becomes `0`, the loop stops.

Final:

``` text
count = 5
```

## Output

``` text
Digits = 5
```

## Important Concept

``` python
number // 10
```

removes the last digit.

Memory:

``` text
// 10 → REMOVE LAST DIGIT
```

## Test Cases

``` text
98765 → 5
1234 → 4
-12345 → 5
7 → 1
0 → 1
```

## Common Mistakes

-   Forgetting `abs()` for negative numbers.
-   Using `/` instead of `//`.
-   Forgetting `count += 1`.
-   Not handling `0` correctly.

## Interview Explanation

> Repeatedly divide the number by 10 using integer division. Each
> division removes one digit, so I increment a counter for every
> division. When the value becomes zero, the counter contains the number
> of digits.

## Memory Trick

``` text
NUMBER
  ↓
 // 10
  ↓
REMOVE LAST DIGIT
  ↓
COUNT
  ↓
REPEAT
```

## Main Thing to Remember

``` text
// 10 → removes the last digit
count += 1 → counts the removed digit
```

------------------------------------------------------------------------

# Question 12 --- Reverse a Number

## Question

Print the reverse of a given number.

### Example

``` text
Input: 12345
Output: Reverse = 54321
```

## What Does the Question Mean?

We need to reverse the order of the digits.

``` text
12345
 ↓
54321
```

## Answer

``` python
def reverseNumber(number):
    value = abs(number)
    reversed = 0

    while True:
        reversed = reversed * 10 + value % 10
        value //= 10

        if not (value > 0):
            break

    return -reversed if number < 0 else reversed


def main():
    number = 12345
    print("Reverse = " + str(reverseNumber(number)))


if __name__ == "__main__":
    main()
```

## Step-by-Step Explanation

### Get the last digit

``` python
value % 10
```

Example:

``` text
12345 % 10 = 5
```

### Add it to the reversed number

``` python
reversed = reversed * 10 + value % 10
```

### Remove the last digit

``` python
value //= 10
```

### Repeat

``` text
12345 → 1234 → 123 → 12 → 1 → 0
```

## Dry Run

Initial:

``` text
value = 12345
reversed = 0
```

  Iteration     Last Digit   Reversed   Value After
  ----------- ------------ ---------- -------------
  1                      5          5          1234
  2                      4         54           123
  3                      3        543            12
  4                      2       5432             1
  5                      1      54321             0

Final:

``` text
54321
```

## Output

``` text
Reverse = 54321
```

## Important Concepts

``` python
value % 10
```

gets the last digit.

``` python
value // 10
```

removes the last digit.

``` python
reversed * 10 + digit
```

builds the reversed number.

## Examples

``` text
1234 → 4321
987 → 789
1200 → 21
7 → 7
-12345 → -54321
```

Leading zeros disappear when the result is stored as an integer:

``` text
1200 → 0021 → 21
```

## Test Cases

``` text
12345 → 54321
987 → 789
1200 → 21
7 → 7
-12345 → -54321
0 → 0
```

## Common Mistakes

-   Confusing `% 10` and `// 10`.
-   Forgetting `reversed * 10`.
-   Using `/` instead of `//`.
-   Forgetting negative numbers.

## Interview Explanation

> I repeatedly extract the last digit using `% 10`, append it to the
> reversed number by multiplying the current reversed value by 10, and
> then remove the last digit using `// 10`.

## Memory Trick

``` text
% 10  → GET
// 10 → REMOVE
reversed * 10 + digit → BUILD
```

## Main Thing to Remember

``` text
GET → BUILD → REMOVE → REPEAT
```

------------------------------------------------------------------------

# Question 13 --- Check if a Number is a Palindrome

## Question

Check if a number is a palindrome.

### Example

``` text
Input: 12321
Output: Palindrome
```

## What Does the Question Mean?

A palindrome reads the same forward and backward.

``` text
12321
```

Reverse:

``` text
12321
```

Both are equal.

Therefore:

``` text
12321 is a palindrome.
```

## Answer

``` python
def reverseNumber(number):
    value = abs(number)
    reversed = 0

    while True:
        reversed = reversed * 10 + value % 10
        value //= 10

        if not (value > 0):
            break

    return -reversed if number < 0 else reversed


def isPalindromeNumber(number):
    return abs(number) == abs(reverseNumber(number))


def main():
    number = 12321
    print("Palindrome" if isPalindromeNumber(number) else "Not palindrome")


if __name__ == "__main__":
    main()
```

## Step-by-Step Explanation

### Step 1

Reverse the number.

``` text
12321 → 12321
```

### Step 2

Compare:

``` text
original == reversed
```

### Step 3

If equal:

``` text
Palindrome
```

Otherwise:

``` text
Not palindrome
```

## Dry Run

Input:

``` text
12321
```

Reverse process:

``` text
12321 → 1232 → 123 → 12 → 1 → 0
```

Digits obtained:

``` text
1 → 2 → 3 → 2 → 1
```

Reversed:

``` text
12321
```

Comparison:

``` text
12321 == 12321
```

Result:

``` text
True
```

Therefore:

``` text
Palindrome
```

## Output

``` text
Palindrome
```

## Examples

``` text
121 → Palindrome
1221 → Palindrome
12321 → Palindrome
12345 → Not palindrome
7 → Palindrome
0 → Palindrome
```

## Test Cases

``` text
12321 → Palindrome
121 → Palindrome
1221 → Palindrome
12345 → Not palindrome
7 → Palindrome
0 → Palindrome
-12321 → Palindrome
```

## Important Concept

The basic palindrome pattern is:

``` text
NUMBER
   ↓
REVERSE
   ↓
COMPARE
```

If:

``` text
number == reversed
```

then it is a palindrome.

## Common Mistakes

-   Only checking repeated digits.
-   Forgetting to reverse the number.
-   Confusing `=` with `==`.
-   Forgetting `% 10` and `// 10`.

## Interview Explanation

> I reverse the number and compare the reversed value with the original
> value. If both are equal, the number is a palindrome.

## Memory Trick

``` text
REVERSE → COMPARE → DECIDE
```

## Main Thing to Remember

``` text
Same forward + backward = Palindrome
```

------------------------------------------------------------------------

# Question 14 --- Find the Sum of Digits

## Question

Find the sum of digits of a number.

### Example

``` text
Input: 9876
Output: Sum of digits = 30
```

## What Does the Question Mean?

Add every digit of the number.

``` text
9 + 8 + 7 + 6 = 30
```

## Answer

``` python
def sumDigits(number):
    value = abs(number)
    sum = 0

    while True:
        sum += value % 10
        value //= 10

        if not (value > 0):
            break

    return sum


def main():
    number = 9876
    print("Sum of digits = " + str(sumDigits(number)))


if __name__ == "__main__":
    main()
```

## Step-by-Step Explanation

### Start

``` python
sum = 0
```

### Get the last digit

``` python
value % 10
```

### Add it

``` python
sum += value % 10
```

### Remove it

``` python
value //= 10
```

## Dry Run

Input:

``` text
9876
```

  Iteration     Last Digit   Sum   Value After
  ----------- ------------ ----- -------------
  1                      6     6           987
  2                      7    13            98
  3                      8    21             9
  4                      9    30             0

Final:

``` text
30
```

## Output

``` text
Sum of digits = 30
```

## Examples

``` text
1234 → 10
555 → 15
1000 → 1
-1234 → 10
7 → 7
0 → 0
```

## Test Cases

``` text
9876 → 30
1234 → 10
555 → 15
1000 → 1
-1234 → 10
7 → 7
0 → 0
```

## Important Concept

``` text
% 10 → GET
// 10 → REMOVE
sum += digit → ADD
```

## Common Mistakes

-   Forgetting `sum +=`.
-   Forgetting `value //= 10`.
-   Using `/` instead of `//`.
-   Not handling negative numbers.

## Interview Explanation

> I repeatedly extract the last digit using `% 10`, add it to a running
> sum, and remove the last digit using `// 10` until the number becomes
> zero.

## Memory Trick

``` text
GET → ADD → REMOVE → REPEAT
```

## Main Thing to Remember

``` python
sum += number % 10
number //= 10
```

------------------------------------------------------------------------

# Question 15 --- Check if a Number is an Armstrong Number

## Question

Check if a number is an Armstrong number.

### Example

``` text
Input: 153
Output: Armstrong number
```

## What Does the Question Mean?

An Armstrong number is a number where the sum of each digit raised to
the power of the total number of digits equals the original number.

For:

``` text
153
```

There are 3 digits.

Calculate:

``` text
1³ + 5³ + 3³
= 1 + 125 + 27
= 153
```

Therefore:

``` text
153 is an Armstrong number.
```

## Answer

``` python
def isArmstrong(number):
    value = number
    digits = 0

    while True:
        digits += 1
        value //= 10

        if not (value > 0):
            break

    sum = 0
    value = number

    while True:
        digit = value % 10
        power = 1

        for i in range(1, digits + 1):
            power *= digit

        sum += power
        value //= 10

        if not (value > 0):
            break

    return sum == number


def main():
    number = 153
    print("Armstrong number" if isArmstrong(number) else "Not Armstrong number")


if __name__ == "__main__":
    main()
```

## Step-by-Step Explanation

### Step 1 --- Count digits

For:

``` text
153
```

Process:

``` text
153 → 15 → 1 → 0
```

Therefore:

``` text
digits = 3
```

### Step 2 --- Reset the value

After counting, `value` is 0.

So:

``` python
value = number
```

restores:

``` text
value = 153
```

### Step 3 --- Extract each digit

``` python
digit = value % 10
```

### Step 4 --- Calculate digit power

``` python
power = 1

for i in range(1, digits + 1):
    power *= digit
```

For digit 3 and 3 digits:

``` text
3 × 3 × 3 = 27
```

### Step 5 --- Add to sum

``` python
sum += power
```

## Dry Run

Input:

``` text
153
```

### Count digits

``` text
153 → 15 → 1 → 0
```

``` text
digits = 3
```

### Process digit 3

``` text
3³ = 27
sum = 27
```

### Process digit 5

``` text
5³ = 125
sum = 27 + 125 = 152
```

### Process digit 1

``` text
1³ = 1
sum = 152 + 1 = 153
```

Final:

``` text
sum = 153
number = 153
```

Comparison:

``` text
153 == 153
```

Result:

``` text
True
```

## Output

``` text
Armstrong number
```

## Examples

``` text
153 → Armstrong
370 → Armstrong
371 → Armstrong
1634 → Armstrong
123 → Not Armstrong
7 → Armstrong
0 → Armstrong
```

## Test Cases

``` text
153 → Armstrong number
370 → Armstrong number
371 → Armstrong number
1634 → Armstrong number
123 → Not Armstrong number
7 → Armstrong number
0 → Armstrong number
```

## Important Concept

The power depends on the number of digits.

For 3 digits:

``` text
digit³
```

For 4 digits:

``` text
digit⁴
```

## Common Mistakes

-   Always using power 3.
-   Forgetting to reset `value = number`.
-   Confusing `% 10` and `// 10`.
-   Forgetting `sum += power`.

## Interview Explanation

> First I count the number of digits. Then I extract each digit, raise
> it to the power of the digit count, and add the results. Finally, I
> compare the sum with the original number.

## Memory Trick

``` text
COUNT → GET → POWER → ADD → REMOVE → COMPARE
```

## Main Thing to Remember

``` text
Sum of each digit^number_of_digits == original number
```

------------------------------------------------------------------------

# Question 16 --- Check if a Number is a Perfect Number

## Question

Check if a number is a perfect number.

### Example

``` text
Input: 28
Output: Perfect number
```

## What Does the Question Mean?

A perfect number equals the sum of all its proper positive divisors.

For:

``` text
28
```

Proper divisors:

``` text
1, 2, 4, 7, 14
```

Sum:

``` text
1 + 2 + 4 + 7 + 14 = 28
```

Therefore:

``` text
28 is a perfect number.
```

## Answer

``` python
def isPerfect(number):
    if number <= 1:
        return False

    sum = 1

    for factor in range(2, number // 2 + 1):
        if number % factor == 0:
            sum += factor

    return sum == number


def main():
    number = 28
    print("Perfect number" if isPerfect(number) else "Not perfect number")


if __name__ == "__main__":
    main()
```

## Important Correction

The original code used:

``` python
range(2, number / 2 + 1)
```

This is incorrect in Python because `/` produces a float.

For:

``` text
28 / 2 = 14.0
```

`range()` needs integers.

Correct:

``` python
range(2, number // 2 + 1)
```

## Step-by-Step Explanation

### 1. Handle numbers \<= 1

``` python
if number <= 1:
    return False
```

### 2. Start sum at 1

``` python
sum = 1
```

Because 1 is a proper divisor of every number greater than 1.

### 3. Check factors

``` python
for factor in range(2, number // 2 + 1):
```

### 4. Check divisibility

``` python
if number % factor == 0:
```

If remainder is 0, the factor divides the number exactly.

### 5. Add the factor

``` python
sum += factor
```

### 6. Compare

``` python
return sum == number
```

## Dry Run

Input:

``` text
28
```

Initial:

``` text
sum = 1
```

Factors checked:

``` text
2 → divisor → sum = 3
3 → not divisor
4 → divisor → sum = 7
5 → not divisor
6 → not divisor
7 → divisor → sum = 14
8 → not divisor
...
14 → divisor → sum = 28
```

Proper divisors:

``` text
1, 2, 4, 7, 14
```

Final:

``` text
sum = 28
number = 28
```

Comparison:

``` text
28 == 28
```

Result:

``` text
True
```

## Output

``` text
Perfect number
```

## Examples

``` text
6 → Perfect
28 → Perfect
10 → Not perfect
12 → Not perfect
1 → Not perfect
0 → Not perfect
496 → Perfect
```

## Test Cases

``` text
28 → Perfect number
6 → Perfect number
10 → Not perfect number
12 → Not perfect number
1 → Not perfect number
0 → Not perfect number
496 → Perfect number
```

## Important Concept

A divisor satisfies:

``` python
number % factor == 0
```

This means the division leaves no remainder.

## Common Mistakes

-   Using `/` instead of `//` inside `range()`.
-   Including the number itself in the sum.
-   Forgetting `number <= 1`.
-   Using `number % factor == 1`.

## Interview Explanation

> I find all proper divisors of the number and add them. If the sum of
> the proper divisors equals the original number, the number is perfect.

## Memory Trick

``` text
FIND DIVISORS → ADD THEM → COMPARE
```

## Main Thing to Remember

``` text
Perfect number:
sum of proper divisors == original number
```

------------------------------------------------------------------------

# Question 17 --- Print All Prime Numbers Between 1 and 100

## Question

Print all prime numbers between 1 and 100.

## What Does the Question Mean?

We need to check every number from 2 to 100 and print only the prime
numbers.

A prime number:

-   Is greater than 1.
-   Has exactly two factors: 1 and itself.

## Answer

``` python
def isPrime(number):
    if number <= 1:
        return False

    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False

        divisor += 1

    return True


def main():
    n = 100

    for number in range(2, n + 1):
        if isPrime(number):
            print(number)


if __name__ == "__main__":
    main()
```

## Step-by-Step Explanation

### 1. Ignore numbers \<= 1

``` python
if number <= 1:
    return False
```

### 2. Start divisor at 2

``` python
divisor = 2
```

### 3. Check up to square root

``` python
while divisor * divisor <= number:
```

### 4. Check divisibility

``` python
if number % divisor == 0:
    return False
```

### 5. Move to next divisor

``` python
divisor += 1
```

### 6. If no divisor is found

``` python
return True
```

## Dry Run --- `isPrime(7)`

``` text
number = 7
divisor = 2
```

Check:

``` text
2 × 2 <= 7
4 <= 7 → True
```

Then:

``` text
7 % 2 = 1
```

Not divisible.

Next:

``` text
divisor = 3
```

Check:

``` text
3 × 3 <= 7
9 <= 7 → False
```

No divisor found.

Therefore:

``` text
7 is prime
```

## Dry Run --- `isPrime(9)`

``` text
number = 9
divisor = 2
```

``` text
9 % 2 = 1
```

Next divisor:

``` text
3
```

``` text
3 × 3 <= 9 → True
9 % 3 = 0
```

Divisor found.

Therefore:

``` text
9 is not prime
```

## Output

``` text
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
```

## Why Only Check Up to Square Root?

If:

``` text
a × b = number
```

and one factor is greater than the square root, the other factor must be
smaller than the square root.

Therefore, checking up to the square root is sufficient.

## Test Cases

``` text
2 → Prime
7 → Prime
11 → Prime
9 → Not prime
15 → Not prime
1 → Not prime
0 → Not prime
97 → Prime
100 → Not prime
```

## Common Mistakes

-   Treating 1 as prime.
-   Starting from divisor 1.
-   Checking all the way to the number unnecessarily.
-   Forgetting `%`.
-   Forgetting `divisor += 1`.

## Interview Explanation

> I first reject numbers less than or equal to 1. Then I check possible
> divisors from 2 up to the square root. If any divisor divides the
> number exactly, it is not prime. Otherwise it is prime.

## Memory Trick

``` text
NUMBER > 1
     ↓
CHECK DIVISORS
     ↓
UP TO √NUMBER
     ↓
DIVISOR FOUND → NOT PRIME
NO DIVISOR → PRIME
```

## Main Thing to Remember

``` python
while divisor * divisor <= number:
    if number % divisor == 0:
        return False
    divisor += 1

return True
```

------------------------------------------------------------------------

# Question 18 --- Check if a Number is Prime or Not

## Question

Check if a number is prime or not.

### Example

``` text
Input: 29
Output: Prime
```

## What Does the Question Mean?

We need to determine whether the given number has exactly two factors:

``` text
1
number itself
```

For:

``` text
29
```

possible divisors up to √29 are:

``` text
2, 3, 4, 5
```

None divides 29 exactly.

Therefore:

``` text
29 is prime.
```

## Answer

``` python
def isPrime(number):
    if number <= 1:
        return False

    divisor = 2

    while divisor * divisor <= number:
        if number % divisor == 0:
            return False

        divisor += 1

    return True


def main():
    number = 29
    print("Prime" if isPrime(number) else "Not prime")


if __name__ == "__main__":
    main()
```

## Step-by-Step Explanation

### Check invalid values

``` python
if number <= 1:
    return False
```

### Start divisor

``` python
divisor = 2
```

### Check up to square root

``` python
while divisor * divisor <= number:
```

### Check divisibility

``` python
if number % divisor == 0:
    return False
```

### Move forward

``` python
divisor += 1
```

### No divisor found

``` python
return True
```

## Dry Run --- 29

Initial:

``` text
number = 29
divisor = 2
```

Check 2:

``` text
29 % 2 = 1
```

Check 3:

``` text
29 % 3 = 2
```

Check 4:

``` text
29 % 4 = 1
```

Check 5:

``` text
29 % 5 = 4
```

Next divisor:

``` text
6
```

Check:

``` text
6 × 6 = 36
36 > 29
```

Stop.

No divisor found.

Therefore:

``` text
Prime
```

## Output

``` text
Prime
```

## Examples

``` text
29 → Prime
7 → Prime
2 → Prime
15 → Not prime
10 → Not prime
1 → Not prime
0 → Not prime
97 → Prime
```

## Test Cases

``` text
29 → Prime
7 → Prime
2 → Prime
15 → Not prime
10 → Not prime
1 → Not prime
0 → Not prime
97 → Prime
100 → Not prime
```

## Common Mistakes

-   Treating 1 as prime.
-   Starting from divisor 1.
-   Forgetting the square-root optimization.
-   Forgetting `%`.
-   Forgetting to increment the divisor.

## Interview Explanation

> I check whether the number is greater than 1, then test divisors from
> 2 up to its square root. If any divisor divides it exactly, it is not
> prime. Otherwise it is prime.

## Memory Trick

``` text
> 1 → CHECK → √NUMBER → DIVISOR?
```

## Main Thing to Remember

``` text
DIVISOR FOUND → NOT PRIME
NO DIVISOR → PRIME
```

------------------------------------------------------------------------

# Question 19 --- Print Fibonacci Series up to n Terms

## Question

Print Fibonacci series up to `n` terms.

### Example

``` text
Input: 10
Output:
0 1 1 2 3 5 8 13 21 34
```

## What Does the Question Mean?

The Fibonacci series starts with:

``` text
0 1
```

Every next number is the sum of the previous two.

``` text
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
```

Therefore:

``` text
0 1 1 2 3 5 8 13 21 34 ...
```

## Answer

``` python
def main():
    terms = 10
    first = 0
    second = 1

    for count in range(1, terms + 1):
        print(str(first) + " ", end="")

        next = first + second
        first = second
        second = next

    print()


if __name__ == "__main__":
    main()
```

## Step-by-Step Explanation

### Initialize

``` python
first = 0
second = 1
```

### Loop

``` python
for count in range(1, terms + 1):
```

For 10 terms:

``` text
range(1, 11)
```

runs 10 times.

### Print current term

``` python
print(first, end=" ")
```

### Calculate next

``` python
next = first + second
```

### Shift

``` python
first = second
second = next
```

## Dry Run

  Iteration     First Printed   Next   New First   New Second
  ----------- --------------- ------ ----------- ------------
  1                         0      1           1            1
  2                         1      2           1            2
  3                         1      3           2            3
  4                         2      5           3            5
  5                         3      8           5            8
  6                         5     13           8           13
  7                         8     21          13           21
  8                        13     34          21           34
  9                        21     55          34           55
  10                       34     89          55           89

## Output

``` text
0 1 1 2 3 5 8 13 21 34
```

## Important Concept

``` text
NEXT = FIRST + SECOND
```

Then:

``` text
FIRST = SECOND
SECOND = NEXT
```

## Examples

``` text
5 terms → 0 1 1 2 3
7 terms → 0 1 1 2 3 5 8
2 terms → 0 1
1 term → 0
```

## Test Cases

``` text
10 → 0 1 1 2 3 5 8 13 21 34
5 → 0 1 1 2 3
7 → 0 1 1 2 3 5 8
2 → 0 1
1 → 0
```

## Common Mistakes

-   Forgetting to update `first` and `second`.
-   Updating in the wrong order.
-   Using the wrong starting values.
-   Using `range(1, terms)` instead of `range(1, terms + 1)`.
-   Forgetting `end=" "` when one-line output is required.

## Interview Explanation

> I initialize the sequence with 0 and 1. In each iteration I print the
> current value, calculate the next value by adding the previous two
> values, and then shift the variables forward.

## Memory Trick

``` text
FIRST + SECOND = NEXT
FIRST = SECOND
SECOND = NEXT
```

## Main Thing to Remember

``` text
ADD → SHIFT → REPEAT
```

------------------------------------------------------------------------

# Question 20 --- Find the Sum of the First n Fibonacci Terms

## Question

Find the sum of the first `n` terms of the Fibonacci series.

### Example

For 10 terms:

``` text
0 1 1 2 3 5 8 13 21 34
```

Sum:

``` text
0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34
= 88
```

## What Does the Question Mean?

We need to:

1.  Generate the first `n` Fibonacci terms.
2.  Add every generated term.
3.  Print the final sum.

## Answer

``` python
def main():
    terms = 10
    first = 0
    second = 1
    total = 0

    for count in range(1, terms + 1):
        total += first

        next = first + second
        first = second
        second = next

    print("Sum of Fibonacci series = " + str(total))


if __name__ == "__main__":
    main()
```

## Important Correction

The original Question 20 code only printed the Fibonacci series. It did
not calculate the sum.

We need an accumulator:

``` python
total = 0
```

and:

``` python
total += first
```

## Step-by-Step Explanation

### 1. Initialize Fibonacci values

``` python
first = 0
second = 1
```

### 2. Initialize the sum

``` python
total = 0
```

### 3. Add the current Fibonacci term

``` python
total += first
```

### 4. Calculate next term

``` python
next = first + second
```

### 5. Shift values

``` python
first = second
second = next
```

### 6. Repeat `n` times

## Dry Run

Input:

``` text
terms = 10
```

Initial:

``` text
first = 0
second = 1
total = 0
```

  Iteration     Current First   Total After Add   Next
  ----------- --------------- ----------------- ------
  1                         0                 0      1
  2                         1                 1      2
  3                         1                 2      3
  4                         2                 4      5
  5                         3                 7      8
  6                         5                12     13
  7                         8                20     21
  8                        13                33     34
  9                        21                54     55
  10                       34                88     89

Final:

``` text
total = 88
```

## Output

``` text
Sum of Fibonacci series = 88
```

## Examples

``` text
1 term → 0
2 terms → 1
5 terms → 7
7 terms → 20
10 terms → 88
```

## Test Cases

``` text
terms = 10 → 88
terms = 5 → 7
terms = 7 → 20
terms = 2 → 1
terms = 1 → 0
```

## Important Concept --- Accumulator

An accumulator stores a running result.

Example:

``` python
total = 0
total += first
```

If the values are:

``` text
0, 1, 1, 2
```

then:

``` text
total = 0
total = 0 + 1 = 1
total = 1 + 1 = 2
total = 2 + 2 = 4
```

## Common Mistakes

-   Only printing Fibonacci terms instead of summing them.
-   Forgetting `total = 0`.
-   Adding `next` instead of the current `first`.
-   Updating values before adding the current term.
-   Using the wrong range.

## Interview Explanation

> I generate the Fibonacci sequence using two variables and maintain a
> running sum. In each iteration I add the current Fibonacci term to the
> total, calculate the next term, shift the variables, and repeat for
> `n` terms.

## Memory Trick

Fibonacci:

``` text
NEXT = FIRST + SECOND
```

Sum:

``` text
TOTAL = TOTAL + FIRST
```

Overall:

``` text
ADD → CALCULATE → SHIFT → REPEAT
```

## Final Logic

``` text
terms = 10

first = 0
second = 1
total = 0

        ↓

Add first

        ↓

Calculate next

        ↓

Shift first and second

        ↓

Repeat 10 times

        ↓

0 + 1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34

        ↓

88
```

## Main Thing to Remember

The two most important patterns are:

``` python
total += first
```

and:

``` python
next = first + second
first = second
second = next
```

Memory:

``` text
FIBONACCI + ACCUMULATOR

GENERATE → ADD → SHIFT → REPEAT
```

------------------------------------------------------------------------

# Quick Revision Cheat Sheet --- Questions 11 to 20

  Q    Problem               Core Pattern
  ---- --------------------- ------------------------------------
  11   Count digits          `// 10` + counter
  12   Reverse number        `% 10` + `// 10` + `reversed * 10`
  13   Palindrome number     Reverse → Compare
  14   Sum of digits         `% 10` + accumulator
  15   Armstrong number      Count → Power → Sum → Compare
  16   Perfect number        Find divisors → Sum → Compare
  17   Print primes 1--100   Prime check + loop
  18   Check prime           Divisors up to √n
  19   Fibonacci series      `next = first + second`
  20   Sum Fibonacci terms   Fibonacci + accumulator

------------------------------------------------------------------------

# Most Important Patterns to Remember

## Number Digit Pattern

``` python
digit = number % 10
number //= 10
```

Remember:

``` text
% 10  → GET LAST DIGIT
// 10 → REMOVE LAST DIGIT
```

## Reverse Number

``` python
reversed = reversed * 10 + digit
```

Remember:

``` text
GET → BUILD → REMOVE
```

## Palindrome

``` text
NUMBER == REVERSE
```

Remember:

``` text
REVERSE → COMPARE
```

## Sum of Digits

``` python
sum += number % 10
number //= 10
```

Remember:

``` text
GET → ADD → REMOVE
```

## Armstrong

``` text
COUNT DIGITS
→ GET DIGIT
→ RAISE TO DIGIT COUNT
→ ADD
→ REMOVE
→ COMPARE
```

## Perfect Number

``` text
FIND DIVISORS
→ ADD PROPER DIVISORS
→ COMPARE WITH NUMBER
```

## Prime

``` python
if number % divisor == 0:
    return False
```

Check divisors only while:

``` python
divisor * divisor <= number
```

Remember:

``` text
DIVISOR FOUND → NOT PRIME
NO DIVISOR → PRIME
```

## Fibonacci

``` python
next = first + second
first = second
second = next
```

Remember:

``` text
ADD → SHIFT → REPEAT
```

## Fibonacci Sum

``` python
total += first
```

Remember:

``` text
GENERATE → ADD → SHIFT → REPEAT
```

------------------------------------------------------------------------

# Final Revision Strategy

Before moving to the next set of problems, make sure you can explain
these patterns without looking at the solution:

### Number Problems

-   `% 10`
-   `// 10`
-   `abs()`
-   Building a reversed number
-   Counting digits
-   Sum of digits

### Mathematical Logic

-   Palindrome
-   Armstrong number
-   Perfect number
-   Prime number

### Sequence Logic

-   Fibonacci generation
-   Fibonacci sum
-   Accumulator pattern

### Interview-Level Thinking

For every question, ask yourself:

``` text
1. What is the input?
2. What exactly is the output?
3. What changes every iteration?
4. What condition stops the loop?
5. What variable stores the answer?
6. What happens for edge cases?
7. Can I explain the logic without looking at the code?
```

------------------------------------------------------------------------

# Questions 11--20 Completion Checklist

-   [x] Question 11 --- Count digits
-   [x] Question 12 --- Reverse number
-   [x] Question 13 --- Palindrome number
-   [x] Question 14 --- Sum of digits
-   [x] Question 15 --- Armstrong number
-   [x] Question 16 --- Perfect number
-   [x] Question 17 --- Print primes from 1 to 100
-   [x] Question 18 --- Check prime
-   [x] Question 19 --- Fibonacci series
-   [x] Question 20 --- Sum of Fibonacci terms

------------------------------------------------------------------------

# Final Goal

Do not memorize the answers.

Understand the patterns.

``` text
DIGITS
  ↓
% 10 / // 10
  ↓
NUMBER LOGIC
  ↓
PRIME / PALINDROME / ARMSTRONG / PERFECT
  ↓
FIBONACCI
  ↓
ACCUMULATORS
  ↓
DSA
```

Once these patterns become comfortable, we can move toward the next
level of logic-building and eventually into core DSA topics such as:

``` text
Arrays
Strings
Hashing
Two Pointers
Sliding Window
Stack
Queue
Linked List
Recursion
Binary Search
Trees
Graphs
Dynamic Programming
```
