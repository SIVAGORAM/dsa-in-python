def main():
    # Question 11: Count the number of digits in a given number.

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

"""
--------------------------------------------------
QUESTION
--------------------------------------------------

Count the number of digits in a given number.


--------------------------------------------------
WHAT DOES THE QUESTION MEAN?
--------------------------------------------------

We are given a number.

We need to find how many digits
are present in that number.


Example:

98765


The digits are:

9
8
7
6
5


Therefore:

Number of digits = 5


--------------------------------------------------
EXPECTED OUTPUT
--------------------------------------------------

Digits = 5


--------------------------------------------------
SOLUTION
--------------------------------------------------

We can solve this problem using:

1. abs()
2. while loop
3. // operator
4. count variable


The important logic is:

value // 10


Integer division by 10 removes
the last digit of a number.


Example:

98765 // 10 = 9876

9876 // 10 = 987

987 // 10 = 98

98 // 10 = 9

9 // 10 = 0


Every time we remove one digit,
we increase the count by 1.


--------------------------------------------------
STEP 1 — STORE THE NUMBER
--------------------------------------------------

Code:

number = 98765


The variable `number` stores
the original number.


--------------------------------------------------
STEP 2 — USE abs()
--------------------------------------------------

Code:

value = abs(number)


`abs()` returns the absolute value
of a number.


Example:

abs(98765) = 98765

abs(-98765) = 98765


Why do we use `abs()`?

Because the negative sign `-`
is not considered a digit.


For example:

-98765


contains:

5 digits


not:

6 digits


Therefore, using:

value = abs(number)


allows the same logic to work
with both positive and negative numbers.


--------------------------------------------------
STEP 3 — CREATE THE COUNT VARIABLE
--------------------------------------------------

Code:

count = 0


The variable `count` keeps track
of how many digits we have processed.


Initially:

count = 0


Every time one digit is removed,
we increase `count` by 1.


--------------------------------------------------
STEP 4 — START THE LOOP
--------------------------------------------------

Code:

while True:


This creates a loop that continues
until we explicitly stop it
using `break`.


The loop will stop when
all digits have been removed.


--------------------------------------------------
STEP 5 — INCREASE THE COUNT
--------------------------------------------------

Code:

count += 1


This means:

count = count + 1


Every iteration represents
one digit.


Therefore, we increase
the count by 1.


--------------------------------------------------
STEP 6 — REMOVE THE LAST DIGIT
--------------------------------------------------

Code:

value //= 10


This is shorthand for:

value = value // 10


Integer division by 10 removes
the last digit.


Example:

98765 // 10 = 9876


Then:

9876 // 10 = 987


Then:

987 // 10 = 98


Then:

98 // 10 = 9


Then:

9 // 10 = 0


--------------------------------------------------
STEP 7 — CHECK WHETHER TO STOP
--------------------------------------------------

Code:

if not (value > 0):
    break


The condition:

value > 0


checks whether there are
still digits remaining.


`not` reverses the condition.


So:

not (value > 0)


means:

value is NOT greater than 0.


When:

value = 0


the condition becomes True,
so the loop stops.


--------------------------------------------------
DRY RUN
--------------------------------------------------

Initial values:

number = 98765

value = 98765

count = 0


--------------------------------------------------
ITERATION 1
--------------------------------------------------

Before:

value = 98765
count = 0


Increase count:

count = 1


Remove last digit:

98765 // 10 = 9876


Now:

value = 9876
count = 1


Check:

value > 0

9876 > 0 → True


So:

not True → False


Loop continues.


--------------------------------------------------
ITERATION 2
--------------------------------------------------

Before:

value = 9876
count = 1


Increase count:

count = 2


Remove last digit:

9876 // 10 = 987


Now:

value = 987
count = 2


Loop continues.


--------------------------------------------------
ITERATION 3
--------------------------------------------------

Before:

value = 987
count = 2


Increase count:

count = 3


Remove last digit:

987 // 10 = 98


Now:

value = 98
count = 3


Loop continues.


--------------------------------------------------
ITERATION 4
--------------------------------------------------

Before:

value = 98
count = 3


Increase count:

count = 4


Remove last digit:

98 // 10 = 9


Now:

value = 9
count = 4


Loop continues.


--------------------------------------------------
ITERATION 5
--------------------------------------------------

Before:

value = 9
count = 4


Increase count:

count = 5


Remove last digit:

9 // 10 = 0


Now:

value = 0
count = 5


Check:

value > 0

0 > 0 → False


Therefore:

not False → True


So:

break


The loop stops.


--------------------------------------------------
FINAL VALUES
--------------------------------------------------

value = 0

count = 5


Therefore:

Number of digits = 5


--------------------------------------------------
OUTPUT
--------------------------------------------------

Digits = 5


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

`//` is the floor division operator.


For positive integers:

98765 // 10 = 9876


It removes the last digit.


More examples:

1234 // 10 = 123

123 // 10 = 12

12 // 10 = 1

1 // 10 = 0


This is one of the most important
techniques for number-based
logic-building problems.


--------------------------------------------------
WHY DO WE USE // 10?
--------------------------------------------------

Consider:

98765


The last digit is:

5


If we divide by 10 using
integer division:

98765 // 10


we get:

9876


The last digit `5` is removed.


Again:

9876 // 10 = 987


The last digit `6` is removed.


Therefore, repeatedly using:

value // 10


allows us to process every digit
one by one.


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Number:

1234


Process:

1234 → 123 → 12 → 1 → 0


Count:

1 → 2 → 3 → 4


Answer:

Digits = 4


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Number:

987


Process:

987 → 98 → 9 → 0


Count:

1 → 2 → 3


Answer:

Digits = 3


--------------------------------------------------
EXAMPLE 4 — NEGATIVE NUMBER
--------------------------------------------------

Number:

-12345


First:

abs(-12345)


becomes:

12345


Then:

12345 → 1234 → 123 → 12 → 1 → 0


Answer:

Digits = 5


The negative sign is not counted
as a digit.


--------------------------------------------------
EXAMPLE 5 — ZERO
--------------------------------------------------

Number:

0


The number `0` has:

1 digit


Our current logic produces:

Digits = 1


which is correct.


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

98765


Expected:

Digits = 5


--------------------------------------------------

TEST CASE 2:

Input:

1234


Expected:

Digits = 4


--------------------------------------------------

TEST CASE 3:

Input:

-12345


Expected:

Digits = 5


--------------------------------------------------

TEST CASE 4:

Input:

7


Expected:

Digits = 1


--------------------------------------------------

TEST CASE 5:

Input:

0


Expected:

Digits = 1


--------------------------------------------------
COMMON MISTAKE 1
--------------------------------------------------

Forgetting `abs()`:


value = number


If:

number = -12345


then the negative number can
cause problems in digit-processing
logic.


Using:

value = abs(number)


makes the value positive.


--------------------------------------------------
COMMON MISTAKE 2
--------------------------------------------------

Using `/` instead of `//`:


value /= 10


This produces a floating-point value.


For digit-processing problems,
we generally want integer division:


value //= 10


--------------------------------------------------
COMMON MISTAKE 3
--------------------------------------------------

Forgetting to increase the count:


value //= 10


If we only remove digits but
don't update `count`, we won't
know how many digits were processed.


We need:

count += 1


--------------------------------------------------
COMMON MISTAKE 4
--------------------------------------------------

Using:

while value > 0:


without thinking about zero.


For:

number = 0


the loop would not execute,
and the answer could incorrectly
become 0.


Our current `while True` approach
handles zero correctly.


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How do you count the digits
of a number?"


You can say:


"I repeatedly divide the number by 10
using integer division. Each division
removes the last digit, so I increment
a counter for every division. When the
value becomes zero, all digits have
been processed and the counter gives
the number of digits."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. `abs()`

Removes the negative sign
by returning the absolute value.


2. `while True`

Creates a loop that continues
until `break` is executed.


3. `//`

Integer division.


4. `// 10`

Removes the last digit
of a positive integer.


5. `count += 1`

Increases the digit counter.


6. `break`

Stops the loop.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

For digit problems:

NUMBER

↓

`// 10`

↓

LAST DIGIT REMOVED

↓

`count += 1`

↓

Repeat

↓

NUMBER BECOMES 0

↓

ANSWER = count


Easy rule:


`number // 10`


means:


REMOVE THE LAST DIGIT


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

Given:

98765


        ↓


Use `abs()`


        ↓


98765


        ↓


Use `while` loop


        ↓


Increase `count`


        ↓


Remove last digit using `// 10`


        ↓


98765 → 9876 → 987 → 98 → 9 → 0


        ↓


Count = 5


        ↓


Print:

Digits = 5


--------------------------------------------------
MAIN THING TO REMEMBER
--------------------------------------------------

For counting digits using a loop:


1. Make the number positive using `abs()`.

2. Start `count = 0`.

3. Repeatedly use `// 10`.

4. Increase `count` for every digit removed.

5. Stop when the value becomes 0.

6. `count` is the number of digits.


MOST IMPORTANT CONCEPT:


`number // 10`


removes the last digit.


Example:


98765 → 9876 → 987 → 98 → 9 → 0


Therefore:


98765 has 5 digits.
"""