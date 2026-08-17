def main():
    # Question 24: Find HCF (GCD) of two numbers using loops.
    first = 48
    second = 18

    while second != 0:
        remainder = first % second
        first = second
        second = remainder

    print("GCD = " + str(abs(first)))


if __name__ == "__main__":
    main()


"""
QUESTION:

Find HCF (GCD) of two numbers using loops.


--------------------------------------------------
WHAT DOES THE QUESTION MEAN?
--------------------------------------------------

We are given two numbers.

We need to find their:

HCF → Highest Common Factor

or:

GCD → Greatest Common Divisor


Both HCF and GCD mean the same thing.


Example:


first = 48

second = 18


Factors of 48:


1, 2, 3, 4, 6, 8, 12, 16, 24, 48


Factors of 18:


1, 2, 3, 6, 9, 18


Common factors:


1, 2, 3, 6


The greatest common factor is:


6


Therefore:


GCD = 6


--------------------------------------------------
EXPECTED OUTPUT
--------------------------------------------------

GCD = 6


--------------------------------------------------
SOLUTION
--------------------------------------------------

We use the:

EUCLIDEAN ALGORITHM


The main idea is:


GCD(a, b) = GCD(b, a % b)


We repeatedly calculate
the remainder until the second
number becomes zero.


The final value of `first`
is the GCD.


--------------------------------------------------
EUCLIDEAN ALGORITHM
--------------------------------------------------

For:


48 and 18


Calculate:


48 % 18 = 12


Then replace:


first = 18

second = 12


Again:


18 % 12 = 6


Replace:


first = 12

second = 6


Again:


12 % 6 = 0


Replace:


first = 6

second = 0


Now:


second == 0


The loop stops.


Therefore:


GCD = 6


--------------------------------------------------
STEP 1 — STORE THE NUMBERS
--------------------------------------------------

Code:


first = 48

second = 18


These are the two numbers
whose GCD we want to find.


--------------------------------------------------
STEP 2 — START THE LOOP
--------------------------------------------------

Code:


while second != 0:


The loop continues as long as
the second number is not zero.


The loop stops when:


second == 0


--------------------------------------------------
STEP 3 — FIND THE REMAINDER
--------------------------------------------------

Code:


remainder = first % second


The `%` operator gives
the remainder after division.


For:


48 % 18


we get:


12


Therefore:


remainder = 12


--------------------------------------------------
STEP 4 — MOVE second INTO first
--------------------------------------------------

Code:


first = second


Before:


first = 48

second = 18


After:


first = 18


--------------------------------------------------
STEP 5 — MOVE remainder INTO second
--------------------------------------------------

Code:


second = remainder


Before:


remainder = 12


After:


second = 12


Now:


first = 18

second = 12


The same process repeats.


--------------------------------------------------
STEP 6 — STOP WHEN second IS 0
--------------------------------------------------

Eventually:


first = 6

second = 0


The condition:


while second != 0


becomes:


0 != 0


False.


The loop stops.


The value in `first` is:


6


Therefore:


GCD = 6


--------------------------------------------------
DRY RUN
--------------------------------------------------

Input:


first = 48

second = 18


--------------------------------------------------
ITERATION 1
--------------------------------------------------

Current values:


first = 48

second = 18


Calculate:


remainder = 48 % 18


18 × 2 = 36


48 - 36 = 12


Therefore:


remainder = 12


Update:


first = second


first = 18


Then:


second = remainder


second = 12


New values:


first = 18

second = 12


--------------------------------------------------
ITERATION 2
--------------------------------------------------

Current:


first = 18

second = 12


Calculate:


remainder = 18 % 12


12 × 1 = 12


18 - 12 = 6


Therefore:


remainder = 6


Update:


first = 12

second = 6


New values:


first = 12

second = 6


--------------------------------------------------
ITERATION 3
--------------------------------------------------

Current:


first = 12

second = 6


Calculate:


remainder = 12 % 6


= 0


Therefore:


remainder = 0


Update:


first = 6

second = 0


New values:


first = 6

second = 0


--------------------------------------------------
LOOP CONDITION
--------------------------------------------------

Check:


second != 0


0 != 0


False.


The loop stops.


--------------------------------------------------
FINAL RESULT
--------------------------------------------------

The value of `first` is:


6


Therefore:


GCD = 6


--------------------------------------------------
OUTPUT
--------------------------------------------------

GCD = 6


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

The most important concept
in this problem is:


%


The modulo operator gives
the remainder.


Example:


48 % 18 = 12


Then:


18 % 12 = 6


Then:


12 % 6 = 0


When the remainder becomes zero,
the previous non-zero value is
the GCD.


--------------------------------------------------
WHY DOES THE EUCLIDEAN ALGORITHM WORK?
--------------------------------------------------

The key rule is:


GCD(a, b) = GCD(b, a % b)


For example:


GCD(48, 18)


is the same as:


GCD(18, 12)


because:


48 % 18 = 12


Then:


GCD(18, 12)


becomes:


GCD(12, 6)


because:


18 % 12 = 6


Then:


GCD(12, 6)


becomes:


GCD(6, 0)


because:


12 % 6 = 0


And:


GCD(6, 0) = 6


Therefore:


GCD = 6


--------------------------------------------------
WHY DO WE USE while?
--------------------------------------------------

We don't know exactly how many
iterations will be required.


For some numbers, the loop may
run only a few times.


For other numbers, it may run
more times.


Therefore:


while second != 0:


is appropriate.


The loop continues until the
remainder becomes zero.


--------------------------------------------------
WHY DO WE USE abs()?
--------------------------------------------------

Code:


abs(first)


ensures the final GCD is positive.


For example:


abs(-6)


returns:


6


The GCD is normally represented
as a non-negative value.


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Input:


first = 18

second = 48


Dry run:


18 % 48 = 18


Then:


48 % 18 = 12


Then:


18 % 12 = 6


Then:


12 % 6 = 0


Therefore:


GCD = 6


The order of the two numbers
does not affect the final GCD.


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Input:


first = 20

second = 8


Calculate:


20 % 8 = 4


Then:


8 % 4 = 0


Therefore:


GCD = 4


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

Input:


first = 15

second = 10


Calculate:


15 % 10 = 5


Then:


10 % 5 = 0


Therefore:


GCD = 5


--------------------------------------------------
EXAMPLE 5
--------------------------------------------------

Input:


first = 7

second = 3


Calculate:


7 % 3 = 1


Then:


3 % 1 = 0


Therefore:


GCD = 1


This means 7 and 3
are coprime.


--------------------------------------------------
EXAMPLE 6
--------------------------------------------------

Input:


first = 12

second = 12


Calculate:


12 % 12 = 0


Then:


first = 12

second = 0


Loop stops.


Therefore:


GCD = 12


--------------------------------------------------
EXAMPLE 7
--------------------------------------------------

Input:


first = 0

second = 18


Calculate:


0 % 18 = 0


Then:


first = 18

second = 0


Therefore:


GCD = 18


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

48, 18


Expected:

GCD = 6


--------------------------------------------------

TEST CASE 2:

Input:

18, 48


Expected:

GCD = 6


--------------------------------------------------

TEST CASE 3:

Input:

20, 8


Expected:

GCD = 4


--------------------------------------------------

TEST CASE 4:

Input:

15, 10


Expected:

GCD = 5


--------------------------------------------------

TEST CASE 5:

Input:

7, 3


Expected:

GCD = 1


--------------------------------------------------

TEST CASE 6:

Input:

12, 12


Expected:

GCD = 12


--------------------------------------------------

TEST CASE 7:

Input:

0, 18


Expected:

GCD = 18


--------------------------------------------------
COMMON MISTAKE 1
--------------------------------------------------

Forgetting to update the values.


Wrong:


remainder = first % second


and then not updating:


first = second

second = remainder


The loop would not progress
correctly.


Correct:


remainder = first % second
first = second
second = remainder


--------------------------------------------------
COMMON MISTAKE 2
--------------------------------------------------

Using the wrong order of updates.


First calculate:


remainder = first % second


Then:


first = second


Then:


second = remainder


Do not calculate the remainder
after changing `first` and `second`.


--------------------------------------------------
COMMON MISTAKE 3
--------------------------------------------------

Using:


while second > 0:


This works for positive numbers,
but using:


while second != 0:


matches the Euclidean algorithm
more directly.


For handling negative inputs,
using absolute values at the start
can make the function more robust.


--------------------------------------------------
COMMON MISTAKE 4
--------------------------------------------------

Thinking the first common factor
is the GCD.


For:


48 and 18


Common factors:


1, 2, 3, 6


The GCD is the greatest one:


6


The Euclidean algorithm finds it
without manually listing factors.


--------------------------------------------------
COMMON MISTAKE 5
--------------------------------------------------

Forgetting the stopping condition.


The important condition is:


while second != 0:


Once:


second = 0


we stop.


The current `first` value
is the GCD.


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:


"How do you find the GCD of two
numbers efficiently?"


You can say:


"I use the Euclidean algorithm.
I repeatedly replace the pair
`(first, second)` with
`(second, first % second)`.
When the second value becomes zero,
the first value is the GCD."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. HCF


Highest Common Factor.


2. GCD


Greatest Common Divisor.


3. `%`


Returns the remainder.


4. Euclidean Algorithm


Uses:


GCD(a, b) = GCD(b, a % b)


5. `while` loop


Repeats until the remainder
becomes zero.


6. `abs()`


Keeps the final GCD non-negative.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

Remember:


REMAINDER → SHIFT → REPEAT


Specifically:


remainder = first % second


Then:


first = second

second = remainder


Stop when:


second == 0


The answer is:


first


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

Question:

Find GCD of 48 and 18.


        ↓


first = 48


second = 18


        ↓


48 % 18 = 12


        ↓


first = 18


second = 12


        ↓


18 % 12 = 6


        ↓


first = 12


second = 6


        ↓


12 % 6 = 0


        ↓


first = 6


second = 0


        ↓


STOP


        ↓


GCD = 6


--------------------------------------------------
MAIN THING TO REMEMBER
--------------------------------------------------

The Euclidean Algorithm:


remainder = first % second

first = second

second = remainder


Repeat until:


second == 0


Then:


GCD = first


For:


48 and 18:


48 % 18 = 12

18 % 12 = 6

12 % 6 = 0


Therefore:


GCD = 6


MOST IMPORTANT PATTERN:


GCD(a, b)

↓

GCD(b, a % b)

↓

REPEAT

↓

SECOND = 0

↓

FIRST = GCD


MEMORY:


DIVIDE → GET REMAINDER → SHIFT → REPEAT

"""