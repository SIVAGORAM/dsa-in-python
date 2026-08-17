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
    # Question 12: Print the reverse of a given number.
    number = 12345
    print("Reverse = " + str(reverseNumber(number)))


if __name__ == "__main__":
    main()


"""
QUESTION:

Print the reverse of a given number.


WHAT DOES THE QUESTION MEAN?

We are given a number.

We need to reverse the order of its digits.

Example:

12345

The original number is:

1 2 3 4 5

After reversing:

5 4 3 2 1

Therefore:

Reverse = 54321


Expected output:

Reverse = 54321


--------------------------------------------------
SOLUTION
--------------------------------------------------

We use a helper function:

reverseNumber(number)


The function receives the given number
and returns its reversed value.


The main logic is:

1. Get the last digit.
2. Add the last digit to the reversed number.
3. Remove the last digit from the original value.
4. Repeat until all digits are processed.


The important line is:

reversed = reversed * 10 + value % 10


This line builds the reversed number
one digit at a time.


--------------------------------------------------
STEP 1 — STORE THE INPUT
--------------------------------------------------

Code:

number = 12345


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

abs(12345) = 12345

abs(-12345) = 12345


We use `abs()` because we want to
process only the digits.


The negative sign is handled separately
at the end.


--------------------------------------------------
STEP 3 — CREATE THE reversed VARIABLE
--------------------------------------------------

Code:

reversed = 0


This variable stores the reversed number
that we are building.


Initially:

reversed = 0


--------------------------------------------------
STEP 4 — START THE LOOP
--------------------------------------------------

Code:

while True:


The loop continues processing digits
until the value becomes 0.


We use `break` to stop the loop.


--------------------------------------------------
STEP 5 — GET THE LAST DIGIT
--------------------------------------------------

Code:

value % 10


The `%` operator gives the remainder.


When we use:

value % 10


we get the last digit.


Examples:

12345 % 10 = 5

1234 % 10 = 4

123 % 10 = 3

12 % 10 = 2

1 % 10 = 1


IMPORTANT:

`% 10` → GET THE LAST DIGIT


--------------------------------------------------
STEP 6 — BUILD THE REVERSED NUMBER
--------------------------------------------------

Code:

reversed = reversed * 10 + value % 10


This is the most important line
in this problem.


Suppose:

reversed = 54

and:

value % 10 = 3


Then:

reversed = 54 * 10 + 3

reversed = 540 + 3

reversed = 543


Therefore, multiplying `reversed`
by 10 creates space for the new digit.


--------------------------------------------------
STEP 7 — REMOVE THE LAST DIGIT
--------------------------------------------------

Code:

value //= 10


This means:

value = value // 10


Integer division by 10 removes
the last digit.


Examples:

12345 // 10 = 1234

1234 // 10 = 123

123 // 10 = 12

12 // 10 = 1

1 // 10 = 0


IMPORTANT:

`// 10` → REMOVE THE LAST DIGIT


--------------------------------------------------
DRY RUN
--------------------------------------------------

Input:

number = 12345


Initial values:

value = 12345

reversed = 0


--------------------------------------------------
ITERATION 1
--------------------------------------------------

value = 12345

Get last digit:

12345 % 10 = 5


Build reversed:

0 * 10 + 5 = 5


Therefore:

reversed = 5


Remove last digit:

12345 // 10 = 1234


Now:

value = 1234

reversed = 5


--------------------------------------------------
ITERATION 2
--------------------------------------------------

value = 1234

Get last digit:

1234 % 10 = 4


Build reversed:

5 * 10 + 4 = 54


Therefore:

reversed = 54


Remove last digit:

1234 // 10 = 123


Now:

value = 123

reversed = 54


--------------------------------------------------
ITERATION 3
--------------------------------------------------

value = 123

Get last digit:

123 % 10 = 3


Build reversed:

54 * 10 + 3 = 543


Therefore:

reversed = 543


Remove last digit:

123 // 10 = 12


Now:

value = 12

reversed = 543


--------------------------------------------------
ITERATION 4
--------------------------------------------------

value = 12

Get last digit:

12 % 10 = 2


Build reversed:

543 * 10 + 2 = 5432


Therefore:

reversed = 5432


Remove last digit:

12 // 10 = 1


Now:

value = 1

reversed = 5432


--------------------------------------------------
ITERATION 5
--------------------------------------------------

value = 1

Get last digit:

1 % 10 = 1


Build reversed:

5432 * 10 + 1 = 54321


Therefore:

reversed = 54321


Remove last digit:

1 // 10 = 0


Now:

value = 0

reversed = 54321


--------------------------------------------------
CHECK THE CONDITION
--------------------------------------------------

Code:

if not (value > 0):
    break


Now:

value = 0


Check:

0 > 0

This is:

False


Then:

not False

becomes:

True


Therefore:

break


The loop stops.


--------------------------------------------------
FINAL VALUE
--------------------------------------------------

reversed = 54321


Therefore:

Reverse = 54321


--------------------------------------------------
OUTPUT
--------------------------------------------------

Reverse = 54321


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

There are two very important
operators in number-based problems.


1. `% 10`

Gets the last digit.


Example:

12345 % 10 = 5


Memory:

`% 10` → GET


--------------------------------------------------

2. `// 10`

Removes the last digit.


Example:

12345 // 10 = 1234


Memory:

`// 10` → REMOVE


--------------------------------------------------
WHY DO WE USE reversed * 10?
--------------------------------------------------

Suppose:

reversed = 54


We want to add:

3


If we write:

54 + 3


we get:

57


That is wrong.


Instead:

54 * 10

= 540


Then:

540 + 3

= 543


Therefore:

reversed * 10 + digit


adds the new digit to the
right side of the reversed number.


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Input:

1234


Process:

1234 → 123 → 12 → 1 → 0


Last digits:

4 → 3 → 2 → 1


Build:

0

↓

4

↓

43

↓

432

↓

4321


Output:

Reverse = 4321


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Input:

987


Process:

987 → 98 → 9 → 0


Last digits:

7 → 8 → 9


Build:

0

↓

7

↓

78

↓

789


Output:

Reverse = 789


--------------------------------------------------
EXAMPLE 4 — NUMBER WITH ZERO
--------------------------------------------------

Input:

1200


Process:

1200 → 120 → 12 → 1 → 0


Last digits:

0 → 0 → 2 → 1


The reversed value becomes:

0021


But the result is stored as an integer.


Therefore:

0021

becomes:

21


Output:

Reverse = 21


IMPORTANT:

Leading zeros disappear when
the result is stored as an integer.


--------------------------------------------------
EXAMPLE 5 — NEGATIVE NUMBER
--------------------------------------------------

Input:

-12345


First:

abs(-12345)


becomes:

12345


Reverse:

12345 → 54321


Then the code checks:

number < 0


Since:

-12345 < 0


is True:


return:

-54321


Therefore:

Reverse = -54321


--------------------------------------------------
EXAMPLE 6 — SINGLE DIGIT
--------------------------------------------------

Input:

7


Get last digit:

7 % 10 = 7


Build:

0 * 10 + 7 = 7


Remove:

7 // 10 = 0


Output:

Reverse = 7


--------------------------------------------------
EXAMPLE 7 — ZERO
--------------------------------------------------

Input:

0


The number has one digit.


The code produces:

Reverse = 0


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

12345

Expected:

Reverse = 54321


--------------------------------------------------

TEST CASE 2:

Input:

987

Expected:

Reverse = 789


--------------------------------------------------

TEST CASE 3:

Input:

1200

Expected:

Reverse = 21


--------------------------------------------------

TEST CASE 4:

Input:

7

Expected:

Reverse = 7


--------------------------------------------------

TEST CASE 5:

Input:

-12345

Expected:

Reverse = -54321


--------------------------------------------------

TEST CASE 6:

Input:

0

Expected:

Reverse = 0


--------------------------------------------------
COMMON MISTAKE 1
--------------------------------------------------

Confusing `% 10` and `// 10`.


Remember:

`% 10` → GET last digit

`// 10` → REMOVE last digit


--------------------------------------------------
COMMON MISTAKE 2
--------------------------------------------------

Forgetting:

reversed * 10


Wrong:

reversed = reversed + value % 10


This will not correctly construct
the reversed number.


Correct:

reversed = reversed * 10 + value % 10


--------------------------------------------------
COMMON MISTAKE 3
--------------------------------------------------

Using `/` instead of `//`.


Wrong:

value /= 10


Correct:

value //= 10


For this logic, we need
integer division.


--------------------------------------------------
COMMON MISTAKE 4
--------------------------------------------------

Forgetting negative numbers.


For:

-12345


Expected:

-54321


The code correctly handles this using:

return -reversed if number < 0 else reversed


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How do you reverse a number?"


You can say:


"I repeatedly extract the last digit using
the modulo operator `% 10`. I add that digit
to the reversed number by multiplying the
current reversed value by 10 and adding the
digit. Then I remove the last digit from the
original value using integer division by 10.
I repeat this until the value becomes zero."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. `abs()`

Gets the absolute value.


2. `% 10`

Gets the last digit.


3. `// 10`

Removes the last digit.


4. `reversed * 10`

Creates space for the next digit.


5. `while True`

Repeats the digit-processing logic.


6. `break`

Stops the loop.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

For number-based problems:


`% 10`

→ GET LAST DIGIT


`// 10`

→ REMOVE LAST DIGIT


`reversed * 10 + digit`

→ BUILD REVERSED NUMBER


Remember:


GET

↓

BUILD

↓

REMOVE

↓

REPEAT


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

Question:

Reverse 12345


        ↓

Take absolute value

        ↓

12345


        ↓

Get last digit using `% 10`

        ↓

5


        ↓

Build reversed number

        ↓

5


        ↓

Remove last digit using `// 10`

        ↓

1234


        ↓

Repeat


12345 → 1234 → 123 → 12 → 1 → 0


        ↓


5 → 54 → 543 → 5432 → 54321


        ↓


Return:

54321


        ↓


Print:

Reverse = 54321


--------------------------------------------------
MAIN THING TO REMEMBER
--------------------------------------------------

For reversing a number:


1. `% 10` → GET the last digit.

2. `reversed * 10 + digit`
   → ADD the digit to the reversed number.

3. `// 10` → REMOVE the last digit.

4. Repeat until the value becomes 0.


MOST IMPORTANT PATTERN:


digit = number % 10

number = number // 10

reversed = reversed * 10 + digit


These three operations are
fundamental for number-based
logic-building problems.
"""