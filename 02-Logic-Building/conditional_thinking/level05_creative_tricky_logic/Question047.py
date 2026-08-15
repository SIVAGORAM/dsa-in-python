def main():
    # Question 47: Take a 3-digit number and check if the sum
    # of the first and last digit equals the middle digit.

    number = 582

    first = number // 100
    middle = (number // 10) % 10
    last = number % 10

    if first + last == middle:
        print("Sum of first and last digit equals middle digit")
    else:
        print("Sum of first and last digit does not equal middle digit")


if __name__ == "__main__":
    main()


"""
QUESTION:

Take a 3-digit number and check if the sum of the first and
last digit equals the middle digit.


WHAT DOES THE QUESTION MEAN?

We have a 3-digit number.

Example:

582

We need to extract its three digits:

First digit  → 5
Middle digit → 8
Last digit   → 2


Then calculate:

First digit + Last digit

5 + 2 = 7


Now compare the result with the middle digit:

7 == 8

False


Therefore:

The sum of the first and last digit does not equal
the middle digit.


--------------------------------------------------
HOW DO WE EXTRACT THE DIGITS?
--------------------------------------------------

For a 3-digit number:

number = 582


FIRST DIGIT:

number // 100

582 // 100 = 5


MIDDLE DIGIT:

(number // 10) % 10

582 // 10 = 58

58 % 10 = 8


LAST DIGIT:

number % 10

582 % 10 = 2


Therefore:

first = 5
middle = 8
last = 2


--------------------------------------------------
DRY RUN
--------------------------------------------------

Given:

number = 582


STEP 1: Extract first digit

first = number // 100

first = 582 // 100

first = 5


STEP 2: Extract middle digit

middle = (number // 10) % 10

middle = (582 // 10) % 10

middle = 58 % 10

middle = 8


STEP 3: Extract last digit

last = number % 10

last = 582 % 10

last = 2


STEP 4: Add first and last digits

first + last

5 + 2

= 7


STEP 5: Compare with middle digit

7 == 8

False


Therefore:

Sum of first and last digit does not equal middle digit.


OUTPUT:

Sum of first and last digit does not equal middle digit


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

number = 123


Extract digits:

first = 1
middle = 2
last = 3


Add first and last:

1 + 3 = 4


Compare:

4 == 2

False


Output:

Sum of first and last digit does not equal middle digit.


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

number = 121


Extract:

first = 1
middle = 2
last = 1


Add:

1 + 1 = 2


Compare:

2 == 2

True


Output:

Sum of first and last digit equals middle digit


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

number = 132


Extract:

first = 1
middle = 3
last = 2


Add:

1 + 2 = 3


Compare:

3 == 3

True


Output:

Sum of first and last digit equals middle digit


--------------------------------------------------
EXAMPLE 5
--------------------------------------------------

number = 456


Extract:

first = 4
middle = 5
last = 6


Add:

4 + 6 = 10


Compare:

10 == 5

False


Output:

Sum of first and last digit does not equal middle digit


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

582

First = 5
Middle = 8
Last = 2

5 + 2 = 7

7 != 8

Output:

Sum of first and last digit does not equal middle digit


TEST CASE 2:

Input:

121

First = 1
Middle = 2
Last = 1

1 + 1 = 2

2 == 2

Output:

Sum of first and last digit equals middle digit


TEST CASE 3:

Input:

132

First = 1
Middle = 3
Last = 2

1 + 2 = 3

Output:

Sum of first and last digit equals middle digit


TEST CASE 4:

Input:

123

First = 1
Middle = 2
Last = 3

1 + 3 = 4

4 != 2

Output:

Sum of first and last digit does not equal middle digit


TEST CASE 5:

Input:

456

First = 4
Middle = 5
Last = 6

4 + 6 = 10

10 != 5

Output:

Sum of first and last digit does not equal middle digit


--------------------------------------------------
TEST CASE TABLE
--------------------------------------------------

| Number | First | Middle | Last | First + Last | Expected |
|--------|------:|-------:|-----:|-------------:|----------|
| 582 | 5 | 8 | 2 | 7 | Not equal |
| 121 | 1 | 2 | 1 | 2 | Equal |
| 132 | 1 | 3 | 2 | 3 | Equal |
| 123 | 1 | 2 | 3 | 4 | Not equal |
| 456 | 4 | 5 | 6 | 10 | Not equal |
| 303 | 3 | 0 | 3 | 6 | Not equal |
| 414 | 4 | 1 | 4 | 8 | Not equal |


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Integer division `//`

Used to remove digits from the right side.

Example:

582 // 100 = 5


2. Modulo `%`

Used to extract the last digit.

Example:

582 % 10 = 2


3. Digit extraction

For a 3-digit number:

First digit:

number // 100


Middle digit:

(number // 10) % 10


Last digit:

number % 10


4. Addition

We add:

first + last


5. Comparison

Then check:

first + last == middle


--------------------------------------------------
IMPORTANT LOGIC
--------------------------------------------------

The entire problem can be remembered as:

3-digit number
      ↓
Extract first digit
      ↓
Extract middle digit
      ↓
Extract last digit
      ↓
Add first + last
      ↓
Compare with middle
      ↓
Equal / Not Equal


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How did you solve this problem?"

You can say:

"First, I extract the three digits using integer division and
modulo. The first digit is obtained using number // 100, the
middle digit using (number // 10) % 10, and the last digit using
number % 10. Then I add the first and last digits and compare
their sum with the middle digit."


--------------------------------------------------
IMPORTANT DIFFERENCE FROM QUESTION 22
--------------------------------------------------

Question 22 asked:

"Is the middle digit the largest, smallest, or neither?"


Question 47 asks:

"Does the sum of the first and last digits equal the middle digit?"


They are completely different problems.

Q22:

middle > first and middle > last


Q47:

first + last == middle


Your submitted code was using the logic for Q22,
so it needed to be changed for Q47.
"""