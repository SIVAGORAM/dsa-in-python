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
    # Question 13: Check if a number is a palindrome.
    number = 12321
    print("Palindrome" if isPalindromeNumber(number) else "Not palindrome")


if __name__ == "__main__":
    main()


"""
QUESTION:

Check if a number is a palindrome.


--------------------------------------------------
WHAT DOES THE QUESTION MEAN?
--------------------------------------------------

A palindrome number is a number that
reads the same from left to right
and from right to left.


Example:

12321


From left to right:

1 2 3 2 1


From right to left:

1 2 3 2 1


Both are the same.


Therefore:

12321 is a palindrome.


Another example:

12345


Original:

12345


Reverse:

54321


They are different.


Therefore:

12345 is NOT a palindrome.


--------------------------------------------------
EXPECTED OUTPUT
--------------------------------------------------

For:

number = 12321


Output:

Palindrome


--------------------------------------------------
SOLUTION
--------------------------------------------------

To check whether a number is a palindrome:

1. Reverse the number.
2. Compare the original number
   with the reversed number.
3. If both are the same,
   the number is a palindrome.
4. Otherwise, it is not a palindrome.


We already created a helper function:

reverseNumber(number)


This function reverses the given number.


Then we created:

isPalindromeNumber(number)


This function compares the original
number with its reversed form.


--------------------------------------------------
MAIN LOGIC
--------------------------------------------------

The important line is:

return abs(number) == abs(reverseNumber(number))


This means:


Original number

        ==

Reversed number


If they are equal:

Palindrome


If they are different:

Not palindrome


--------------------------------------------------
STEP 1 — REVERSE THE NUMBER
--------------------------------------------------

We use:

reverseNumber(number)


For:

12321


The reverse is:

12321


because:

12321 → 1232 → 123 → 12 → 1 → 0


The digits are collected as:

1 → 12 → 123 → 1232 → 12321


Therefore:

reverseNumber(12321)

returns:

12321


--------------------------------------------------
STEP 2 — COMPARE ORIGINAL AND REVERSE
--------------------------------------------------

Code:

abs(number) == abs(reverseNumber(number))


For:

number = 12321


Original:

abs(12321) = 12321


Reverse:

reverseNumber(12321) = 12321


Therefore:

12321 == 12321


This is:

True


So the function returns:

True


--------------------------------------------------
STEP 3 — PRINT THE RESULT
--------------------------------------------------

Code:

print("Palindrome" if isPalindromeNumber(number)
      else "Not palindrome")


This is a Python conditional expression.


It means:


If:

isPalindromeNumber(number)

is True:


print:

Palindrome


Otherwise:


print:

Not palindrome


--------------------------------------------------
DRY RUN
--------------------------------------------------

Input:

number = 12321


--------------------------------------------------
STEP 1
--------------------------------------------------

Call:

isPalindromeNumber(12321)


Inside the function:

abs(12321) == abs(reverseNumber(12321))


--------------------------------------------------
STEP 2
--------------------------------------------------

Reverse the number:


number = 12321


Initial:

value = 12321

reversed = 0


--------------------------------------------------
ITERATION 1
--------------------------------------------------

Last digit:

12321 % 10 = 1


Build:

0 * 10 + 1 = 1


reversed = 1


Remove last digit:

12321 // 10 = 1232


--------------------------------------------------
ITERATION 2
--------------------------------------------------

Last digit:

1232 % 10 = 2


Build:

1 * 10 + 2 = 12


reversed = 12


Remove:

1232 // 10 = 123


--------------------------------------------------
ITERATION 3
--------------------------------------------------

Last digit:

123 % 10 = 3


Build:

12 * 10 + 3 = 123


reversed = 123


Remove:

123 // 10 = 12


--------------------------------------------------
ITERATION 4
--------------------------------------------------

Last digit:

12 % 10 = 2


Build:

123 * 10 + 2 = 1232


reversed = 1232


Remove:

12 // 10 = 1


--------------------------------------------------
ITERATION 5
--------------------------------------------------

Last digit:

1 % 10 = 1


Build:

1232 * 10 + 1 = 12321


reversed = 12321


Remove:

1 // 10 = 0


The loop stops.


Therefore:

reverseNumber(12321)

returns:

12321


--------------------------------------------------
STEP 3 — COMPARE
--------------------------------------------------

Original:

12321


Reversed:

12321


Comparison:

12321 == 12321


Result:

True


Therefore:

Palindrome


--------------------------------------------------
OUTPUT
--------------------------------------------------

Palindrome


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

The main concept is:

COMPARING A NUMBER WITH ITS REVERSE


Example:


12321

Reverse:

12321


Same:

YES


Therefore:

Palindrome


--------------------------------------------------

Another example:


12345

Reverse:

54321


Same:

NO


Therefore:

Not palindrome


--------------------------------------------------
WHY DO WE USE abs()?
--------------------------------------------------

Code:

abs(number) == abs(reverseNumber(number))


`abs()` returns the positive
version of a number.


Example:

abs(-12321)

becomes:

12321


This allows the comparison to ignore
the negative sign.


For example:

number = -12321


Its reverse is:

-12321


Using `abs()`:

abs(-12321) = 12321

abs(-12321) = 12321


Therefore:

12321 == 12321


Result:

True


So this implementation considers
negative palindrome numbers as palindromes
based on their digits.


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Input:

121


Reverse:

121


Comparison:

121 == 121


Result:

Palindrome


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Input:

123


Reverse:

321


Comparison:

123 == 321


Result:

Not palindrome


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

Input:

1221


Reverse:

1221


Comparison:

1221 == 1221


Result:

Palindrome


--------------------------------------------------
EXAMPLE 5
--------------------------------------------------

Input:

1234


Reverse:

4321


Comparison:

1234 == 4321


Result:

Not palindrome


--------------------------------------------------
EXAMPLE 6 — SINGLE DIGIT
--------------------------------------------------

Input:

7


Reverse:

7


Comparison:

7 == 7


Result:

Palindrome


Every single-digit number
is a palindrome.


--------------------------------------------------
EXAMPLE 7 — ZERO
--------------------------------------------------

Input:

0


Reverse:

0


Comparison:

0 == 0


Result:

Palindrome


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

12321


Expected:

Palindrome


--------------------------------------------------

TEST CASE 2:

Input:

121


Expected:

Palindrome


--------------------------------------------------

TEST CASE 3:

Input:

12321


Expected:

Palindrome


--------------------------------------------------

TEST CASE 4:

Input:

12345


Expected:

Not palindrome


--------------------------------------------------

TEST CASE 5:

Input:

1221


Expected:

Palindrome


--------------------------------------------------

TEST CASE 6:

Input:

7


Expected:

Palindrome


--------------------------------------------------

TEST CASE 7:

Input:

0


Expected:

Palindrome


--------------------------------------------------

TEST CASE 8:

Input:

-12321


Expected:

Palindrome


--------------------------------------------------
COMMON MISTAKE 1
--------------------------------------------------

Only checking whether the number
contains repeated digits.


That is not enough.


For example:

1123


has repeated digits,


but:

1123

reverse:

3211


They are different.


Therefore:

Not palindrome


--------------------------------------------------
COMMON MISTAKE 2
--------------------------------------------------

Forgetting to reverse the number.


A palindrome must be checked
by comparing the number with
its reverse.


The core logic is:

number == reverse(number)


--------------------------------------------------
COMMON MISTAKE 3
--------------------------------------------------

Confusing `% 10` and `// 10`.


Remember:


`% 10`

→ GET the last digit


`// 10`

→ REMOVE the last digit


These are important for
number-based problems.


--------------------------------------------------
COMMON MISTAKE 4
--------------------------------------------------

Forgetting the difference between:

=

and:

==


`=` means assignment.


Example:

number = 12321


`==` means comparison.


Example:

number == reversed


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How do you check whether a number
is a palindrome?"


You can say:


"I reverse the number using modulo
and integer division. Then I compare
the reversed number with the original
number. If both values are equal,
the number is a palindrome; otherwise,
it is not."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Palindrome

A value that reads the same
forward and backward.


2. `% 10`

Gets the last digit.


3. `// 10`

Removes the last digit.


4. Reverse logic

Builds the reversed number.


5. `==`

Compares two values.


6. `abs()`

Returns the absolute value.


7. Conditional expression

Chooses between two outputs.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

For palindrome numbers:


NUMBER

↓

REVERSE NUMBER

↓

COMPARE


If:


NUMBER == REVERSE


↓

PALINDROME


Otherwise:


NUMBER != REVERSE


↓

NOT PALINDROME


Easy rule:


SAME FORWARD + BACKWARD

=

PALINDROME


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

Question:

Check whether 12321 is a palindrome.


        ↓


Take the number


        ↓


12321


        ↓


Reverse the number


        ↓


12321


        ↓


Compare:


12321 == 12321


        ↓


True


        ↓


Print:


Palindrome


--------------------------------------------------
MAIN THING TO REMEMBER
--------------------------------------------------

A palindrome number is a number
that remains the same after reversal.


The basic logic is:


1. Reverse the number.

2. Compare the original number
   with the reversed number.

3. If both are equal:

   Palindrome


4. Otherwise:

   Not palindrome


MOST IMPORTANT PATTERN:


reversed = reverse(number)

number == reversed


If equal:

PALINDROME


If not equal:

NOT PALINDROME


For this question, the main idea
is very simple:


REVERSE → COMPARE → DECIDE
"""