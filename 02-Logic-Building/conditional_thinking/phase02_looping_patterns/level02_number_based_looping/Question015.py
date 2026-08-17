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
    # Question 15: Check if a number is an Armstrong number.
    number = 153
    print("Armstrong number" if isArmstrong(number) else "Not Armstrong number")


if __name__ == "__main__":
    main()


"""
QUESTION:

Check if a number is an Armstrong number.


--------------------------------------------------
WHAT DOES THE QUESTION MEAN?
--------------------------------------------------

An Armstrong number is a number where:

The sum of each digit raised to the power
of the total number of digits is equal
to the original number.


Example:

153


153 has 3 digits.


So we calculate:

1³ + 5³ + 3³


Which means:

1 × 1 × 1
+
5 × 5 × 5
+
3 × 3 × 3


= 1 + 125 + 27


= 153


The calculated result is:

153


The original number is:

153


Both are equal.


Therefore:

153 is an Armstrong number.


--------------------------------------------------
EXPECTED OUTPUT
--------------------------------------------------

Armstrong number


--------------------------------------------------
SOLUTION
--------------------------------------------------

To check whether a number is
an Armstrong number, we need to:


1. Count the number of digits.

2. Extract each digit.

3. Raise each digit to the power
   of the total number of digits.

4. Add all the calculated powers.

5. Compare the final sum with
   the original number.


The basic formula is:


For a number with `n` digits:


digit₁ⁿ + digit₂ⁿ + digit₃ⁿ + ...


If the result equals the original number:


ARMSTRONG NUMBER


Otherwise:


NOT ARMSTRONG NUMBER


--------------------------------------------------
STEP 1 — COUNT THE NUMBER OF DIGITS
--------------------------------------------------

Code:

value = number
digits = 0


We create a copy of the number
because we will change `value`
while counting its digits.


For:

number = 153


Initially:

value = 153

digits = 0


--------------------------------------------------
STEP 2 — COUNT EACH DIGIT
--------------------------------------------------

Code:

while True:
    digits += 1
    value //= 10


Every time we divide by 10,
one digit is removed.


For:

153


We get:


153 → 15 → 1 → 0


Therefore:

digits = 3


--------------------------------------------------
STEP 3 — RESET value
--------------------------------------------------

After counting the digits,
`value` has become 0.


So we need the original number
again to process its digits.


Code:

value = number


Now:

value = 153


--------------------------------------------------
STEP 4 — CREATE sum
--------------------------------------------------

Code:

sum = 0


This variable stores the total
of all digit powers.


Initially:

sum = 0


--------------------------------------------------
STEP 5 — GET EACH DIGIT
--------------------------------------------------

Code:

digit = value % 10


`% 10` gives the last digit.


For:

153


First:

153 % 10 = 3


So:

digit = 3


--------------------------------------------------
STEP 6 — CREATE power
--------------------------------------------------

Code:

power = 1


We use `power` to calculate:


digit ^ digits


For 153:


digit = 3

digits = 3


We need:


3³


So we start with:

power = 1


--------------------------------------------------
STEP 7 — CALCULATE THE POWER
--------------------------------------------------

Code:

for i in range(1, digits + 1):
    power *= digit


For:

digits = 3


The loop becomes:

range(1, 4)


which produces:

1
2
3


So the digit is multiplied
by itself three times.


For digit 3:


power = 1


Iteration 1:

power = 1 × 3

power = 3


Iteration 2:

power = 3 × 3

power = 9


Iteration 3:

power = 9 × 3

power = 27


Therefore:

3³ = 27


--------------------------------------------------
STEP 8 — ADD POWER TO sum
--------------------------------------------------

Code:

sum += power


This means:

sum = sum + power


For the first digit:


sum = 0 + 27

sum = 27


--------------------------------------------------
STEP 9 — REMOVE THE DIGIT
--------------------------------------------------

Code:

value //= 10


For:

153


We get:

153 // 10 = 15


Now:

value = 15


The next digit can be processed.


--------------------------------------------------
DRY RUN
--------------------------------------------------

Input:

number = 153


--------------------------------------------------
STEP 1 — COUNT DIGITS
--------------------------------------------------

Initial:

value = 153

digits = 0


Iteration 1:

digits = 1

153 // 10 = 15


Iteration 2:

digits = 2

15 // 10 = 1


Iteration 3:

digits = 3

1 // 10 = 0


The loop stops.


Therefore:

digits = 3


--------------------------------------------------
STEP 2 — RESET VALUE
--------------------------------------------------

Code:

value = number


Therefore:

value = 153


And:

sum = 0


--------------------------------------------------
PROCESS DIGIT 3
--------------------------------------------------

Get last digit:


153 % 10 = 3


Therefore:

digit = 3


Calculate:


3³


power starts at:

1


Then:


1 × 3 = 3

3 × 3 = 9

9 × 3 = 27


Therefore:

power = 27


Add to sum:


sum = 0 + 27

sum = 27


Remove digit:


153 // 10 = 15


Now:

value = 15


--------------------------------------------------
PROCESS DIGIT 5
--------------------------------------------------

Get last digit:


15 % 10 = 5


Therefore:

digit = 5


Calculate:


5³


power starts at:

1


Then:


1 × 5 = 5

5 × 5 = 25

25 × 5 = 125


Therefore:

power = 125


Add to sum:


sum = 27 + 125

sum = 152


Remove digit:


15 // 10 = 1


Now:

value = 1


--------------------------------------------------
PROCESS DIGIT 1
--------------------------------------------------

Get last digit:


1 % 10 = 1


Therefore:

digit = 1


Calculate:


1³


power starts at:

1


Then:


1 × 1 = 1

1 × 1 = 1

1 × 1 = 1


Therefore:

power = 1


Add to sum:


sum = 152 + 1

sum = 153


Remove digit:


1 // 10 = 0


Now:

value = 0


The loop stops.


--------------------------------------------------
FINAL COMPARISON
--------------------------------------------------

Original number:

153


Calculated sum:

153


Compare:


sum == number


153 == 153


This is:

True


Therefore:


153 is an Armstrong number.


--------------------------------------------------
OUTPUT
--------------------------------------------------

Armstrong number


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

This problem combines several
important concepts.


1. `% 10`

Gets the last digit.


Example:

153 % 10 = 3


Memory:


`% 10` → GET


--------------------------------------------------

2. `// 10`

Removes the last digit.


Example:

153 // 10 = 15


Memory:


`// 10` → REMOVE


--------------------------------------------------

3. `for` loop

Used to multiply a digit
the required number of times.


--------------------------------------------------

4. `power *= digit`

Means:


power = power * digit


This is used to calculate
the power manually.


--------------------------------------------------

5. `sum += power`

Adds the calculated power
to the total sum.


--------------------------------------------------

6. `==`

Compares the calculated sum
with the original number.


--------------------------------------------------
WHY DO WE NEED TO COUNT DIGITS FIRST?
--------------------------------------------------

This is one of the most important
parts of the problem.


For an Armstrong number, the power
depends on the total number of digits.


Example:

153


It has:

3 digits


Therefore:


1³ + 5³ + 3³


We cannot use a fixed power such as
3 for every number.


Consider:


1634


It has:

4 digits.


Therefore:


1⁴ + 6⁴ + 3⁴ + 4⁴


So we must first find:

digits


before processing the digits.


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Input:

370


Number of digits:

3


Calculation:


3³ + 7³ + 0³


= 27 + 343 + 0


= 370


Original:

370


Calculated:

370


Therefore:


Armstrong number


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Input:

371


Number of digits:

3


Calculation:


3³ + 7³ + 1³


= 27 + 343 + 1


= 371


Therefore:


Armstrong number


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

Input:

123


Number of digits:

3


Calculation:


1³ + 2³ + 3³


= 1 + 8 + 27


= 36


Original:

123


Calculated:

36


They are different.


Therefore:


Not Armstrong number


--------------------------------------------------
EXAMPLE 5 — FOUR DIGITS
--------------------------------------------------

Input:

1634


Number of digits:

4


Calculation:


1⁴ + 6⁴ + 3⁴ + 4⁴


= 1 + 1296 + 81 + 256


= 1634


Therefore:


Armstrong number


--------------------------------------------------
EXAMPLE 6 — SINGLE DIGIT
--------------------------------------------------

Input:

7


Number of digits:

1


Calculation:


7¹


= 7


Original:

7


Calculated:

7


Therefore:


Armstrong number


Every single-digit number
is an Armstrong number.


--------------------------------------------------
EXAMPLE 7 — ZERO
--------------------------------------------------

Input:

0


Number of digits:

1


Calculation:


0¹


= 0


Original:

0


Calculated:

0


Therefore:


Armstrong number


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

153


Expected:

Armstrong number


--------------------------------------------------

TEST CASE 2:

Input:

370


Expected:

Armstrong number


--------------------------------------------------

TEST CASE 3:

Input:

371


Expected:

Armstrong number


--------------------------------------------------

TEST CASE 4:

Input:

1634


Expected:

Armstrong number


--------------------------------------------------

TEST CASE 5:

Input:

123


Expected:

Not Armstrong number


--------------------------------------------------

TEST CASE 6:

Input:

7


Expected:

Armstrong number


--------------------------------------------------

TEST CASE 7:

Input:

0


Expected:

Armstrong number


--------------------------------------------------
COMMON MISTAKE 1
--------------------------------------------------

Using a fixed power of 3.


For example:

digit³


This only works for
three-digit Armstrong numbers.


The correct power is:

number of digits


So we first calculate:

digits


--------------------------------------------------
COMMON MISTAKE 2
--------------------------------------------------

Forgetting to reset `value`.


After counting digits:


value = 0


If we then try to extract
digits without resetting it,
there will be no digits left.


Therefore:


value = number


must be done before
processing the digits.


--------------------------------------------------
COMMON MISTAKE 3
--------------------------------------------------

Confusing `% 10` and `// 10`.


Remember:


`% 10`

→ GET last digit


`// 10`

→ REMOVE last digit


--------------------------------------------------
COMMON MISTAKE 4
--------------------------------------------------

Forgetting to add the calculated
power to the sum.


We need:


sum += power


Otherwise the final sum
will remain incorrect.


--------------------------------------------------
COMMON MISTAKE 5
--------------------------------------------------

Comparing the wrong values.


At the end, we need:


sum == number


If True:


Armstrong number


If False:


Not Armstrong number


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How do you check whether a number
is an Armstrong number?"


You can say:


"First, I count the number of digits.
Then I extract each digit using `% 10`.
For every digit, I calculate that digit
raised to the number of digits and add
the result to a running sum. Finally,
I compare the sum with the original
number. If they are equal, the number
is an Armstrong number."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. `% 10`

Gets the last digit.


2. `// 10`

Removes the last digit.


3. Digit counting

Finds the power to use.


4. `for` loop

Calculates the power.


5. `power *= digit`

Multiplies the digit repeatedly.


6. `sum += power`

Adds each digit's power.


7. `==`

Compares the final sum
with the original number.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

For Armstrong numbers:


COUNT DIGITS

↓

GET DIGIT

↓

RAISE DIGIT TO DIGIT COUNT

↓

ADD TO SUM

↓

REMOVE DIGIT

↓

REPEAT

↓

COMPARE SUM WITH NUMBER


Easy pattern:


COUNT → GET → POWER → ADD → REMOVE → COMPARE


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

Question:

Check whether 153 is
an Armstrong number.


        ↓


Count digits


        ↓


153 has 3 digits


        ↓


Get last digit


        ↓


3


        ↓


Calculate:

3³ = 27


        ↓


Add to sum


        ↓


sum = 27


        ↓


Remove 3


        ↓


15


        ↓


Get 5


        ↓


5³ = 125


        ↓


sum = 152


        ↓


Remove 5


        ↓


1


        ↓


Get 1


        ↓


1³ = 1


        ↓


sum = 153


        ↓


Compare:


153 == 153


        ↓


True


        ↓


Armstrong number


--------------------------------------------------
MAIN THING TO REMEMBER
--------------------------------------------------

An Armstrong number satisfies:


SUM OF EACH DIGIT RAISED TO
THE POWER OF TOTAL DIGITS


=


ORIGINAL NUMBER


For example:


153


has 3 digits.


Therefore:


1³ + 5³ + 3³


= 1 + 125 + 27


= 153


Since:


153 == 153


It is an Armstrong number.


MOST IMPORTANT PATTERN:


1. Count digits.

2. Get digit using `% 10`.

3. Calculate digit power.

4. Add power to `sum`.

5. Remove digit using `// 10`.

6. Repeat.

7. Compare:

   sum == number


MEMORY:


COUNT → GET → POWER → ADD → REMOVE → COMPARE
"""