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
    # Question 18: Check if a number is prime or not.
    number = 29
    print("Prime" if isPrime(number) else "Not prime")


if __name__ == "__main__":
    main()


"""
QUESTION:

Check if a number is prime or not.


--------------------------------------------------
WHAT DOES THE QUESTION MEAN?
--------------------------------------------------

We are given a number.

We need to determine whether
that number is a prime number.


A prime number is a number greater
than 1 that has exactly two factors:


1. 1

2. The number itself


Examples:


2 → factors: 1, 2

3 → factors: 1, 3

5 → factors: 1, 5

7 → factors: 1, 7


Therefore:

2, 3, 5, and 7 are prime numbers.


But:


4 → factors: 1, 2, 4


It has more than two factors.


Therefore:

4 is not a prime number.


--------------------------------------------------
EXAMPLE INPUT
--------------------------------------------------

number = 29


We need to check:

Is 29 prime?


--------------------------------------------------
EXPECTED OUTPUT
--------------------------------------------------

Prime


--------------------------------------------------
SOLUTION
--------------------------------------------------

We create a helper function:


isPrime(number)


The function checks whether
the given number has any divisor
other than 1 and itself.


The logic is:


1. If number is less than or equal
   to 1, return False.

2. Start checking divisors from 2.

3. Continue checking while:

   divisor * divisor <= number

4. If the number is exactly divisible
   by a divisor, return False.

5. If no divisor is found,
   return True.


--------------------------------------------------
STEP 1 — CHECK number <= 1
--------------------------------------------------

Code:

if number <= 1:
    return False


Numbers less than or equal to 1
are not prime.


Examples:


0 → Not prime

1 → Not prime

-5 → Not prime


Therefore:

if number <= 1


we immediately return:


False


--------------------------------------------------
STEP 2 — START divisor AT 2
--------------------------------------------------

Code:

divisor = 2


We start checking possible divisors
from 2.


Why not start from 1?


Every number is divisible by 1.


For example:


29 % 1 = 0


But this does not help us
determine whether 29 is prime.


So we start from:


2


--------------------------------------------------
STEP 3 — CHECK UP TO SQUARE ROOT
--------------------------------------------------

Code:

while divisor * divisor <= number:


This means we only check possible
divisors up to the square root
of the number.


For example:


29


We check:


2 × 2 = 4

3 × 3 = 9

4 × 4 = 16

5 × 5 = 25

6 × 6 = 36


When divisor becomes 6:


36 <= 29


is False.


So the loop stops.


We do not need to check
7, 8, 9, etc.


--------------------------------------------------
WHY DO WE ONLY CHECK UP TO
THE SQUARE ROOT?
--------------------------------------------------

Suppose:


a × b = number


If a number has a factor
greater than its square root,
there must be another factor
smaller than its square root.


Therefore, if there is any divisor,
we will find at least one divisor
at or below the square root.


Example:


36


Square root:

6


Factor pairs:


1 × 36

2 × 18

3 × 12

4 × 9

6 × 6


If we check up to 6,
we have enough information
to determine whether 36
has another divisor.


--------------------------------------------------
STEP 4 — CHECK DIVISIBILITY
--------------------------------------------------

Code:

if number % divisor == 0:
    return False


The `%` operator gives
the remainder.


If the remainder is 0:


number % divisor == 0


then the divisor divides
the number exactly.


Therefore, the number is not prime.


--------------------------------------------------
STEP 5 — MOVE TO NEXT DIVISOR
--------------------------------------------------

Code:

divisor += 1


This means:


divisor = divisor + 1


So the divisor changes:


2 → 3 → 4 → 5 → ...


We continue checking
possible divisors.


--------------------------------------------------
STEP 6 — RETURN TRUE
--------------------------------------------------

Code:

return True


If the loop finishes without
finding any divisor, then the
number is prime.


Therefore:

return True


--------------------------------------------------
DRY RUN
--------------------------------------------------

Input:


number = 29


--------------------------------------------------
STEP 1
--------------------------------------------------

Check:


29 <= 1


Result:


False


So we continue.


--------------------------------------------------
STEP 2
--------------------------------------------------

Initialize:


divisor = 2


--------------------------------------------------
ITERATION 1
--------------------------------------------------

Check loop:


divisor * divisor <= number


2 * 2 <= 29


4 <= 29


True


Now check:


29 % 2


= 1


Not equal to 0.


Therefore:

2 is not a divisor.


Increase:


divisor = 3


--------------------------------------------------
ITERATION 2
--------------------------------------------------

Check:


3 * 3 <= 29


9 <= 29


True


Check:


29 % 3


= 2


Not equal to 0.


Therefore:

3 is not a divisor.


Increase:


divisor = 4


--------------------------------------------------
ITERATION 3
--------------------------------------------------

Check:


4 * 4 <= 29


16 <= 29


True


Check:


29 % 4


= 1


Not divisible.


Increase:


divisor = 5


--------------------------------------------------
ITERATION 4
--------------------------------------------------

Check:


5 * 5 <= 29


25 <= 29


True


Check:


29 % 5


= 4


Not divisible.


Increase:


divisor = 6


--------------------------------------------------
ITERATION 5
--------------------------------------------------

Check:


6 * 6 <= 29


36 <= 29


False


The loop stops.


No divisor was found.


Therefore:


return True


--------------------------------------------------
FINAL RESULT
--------------------------------------------------

isPrime(29)


returns:


True


Therefore:


29 is a prime number.


--------------------------------------------------
OUTPUT
--------------------------------------------------

Prime


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

The most important concept
in this problem is:


number % divisor == 0


The `%` operator returns
the remainder.


Example:


29 % 2 = 1


So 2 does not divide 29.


29 % 3 = 2


So 3 does not divide 29.


29 % 5 = 4


So 5 does not divide 29.


If we find:


number % divisor == 0


then we know the number
has a divisor and is not prime.


--------------------------------------------------
EXAMPLE 2 — PRIME NUMBER
--------------------------------------------------

Input:


7


Check:


7 <= 1


False


Start:


divisor = 2


Check:


2 * 2 <= 7


4 <= 7


True


Then:


7 % 2 = 1


Not divisible.


Increase:


divisor = 3


Check:


3 * 3 <= 7


9 <= 7


False


No divisor found.


Therefore:


7 is prime.


Output:


Prime


--------------------------------------------------
EXAMPLE 3 — NOT PRIME
--------------------------------------------------

Input:


15


Start:


divisor = 2


Check:


15 % 2 = 1


Not divisible.


Increase:


divisor = 3


Check:


3 * 3 <= 15


9 <= 15


True


Now:


15 % 3 = 0


A divisor is found.


Therefore:


return False


Output:


Not prime


--------------------------------------------------
EXAMPLE 4 — EVEN NUMBER
--------------------------------------------------

Input:


10


Start:


divisor = 2


Check:


10 % 2 = 0


A divisor is found.


Therefore:


10 is not prime.


Output:


Not prime


--------------------------------------------------
EXAMPLE 5 — NUMBER 1
--------------------------------------------------

Input:


1


Check:


1 <= 1


True


Therefore:


return False


Output:


Not prime


--------------------------------------------------
EXAMPLE 6 — NUMBER 2
--------------------------------------------------

Input:


2


Check:


2 <= 1


False


Start:


divisor = 2


Check:


2 * 2 <= 2


4 <= 2


False


The loop does not execute.


No divisor is found.


Therefore:


return True


Output:


Prime


--------------------------------------------------
EXAMPLE 7 — NUMBER 0
--------------------------------------------------

Input:


0


Check:


0 <= 1


True


Therefore:


return False


Output:


Not prime


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

29


Expected:

Prime


--------------------------------------------------

TEST CASE 2:

Input:

7


Expected:

Prime


--------------------------------------------------

TEST CASE 3:

Input:

2


Expected:

Prime


--------------------------------------------------

TEST CASE 4:

Input:

15


Expected:

Not prime


--------------------------------------------------

TEST CASE 5:

Input:

10


Expected:

Not prime


--------------------------------------------------

TEST CASE 6:

Input:

1


Expected:

Not prime


--------------------------------------------------

TEST CASE 7:

Input:

0


Expected:

Not prime


--------------------------------------------------

TEST CASE 8:

Input:

97


Expected:

Prime


--------------------------------------------------

TEST CASE 9:

Input:

100


Expected:

Not prime


--------------------------------------------------
COMMON MISTAKE 1
--------------------------------------------------

Thinking that 1 is prime.


Wrong:


1 is prime.


Correct:


1 is NOT prime.


A prime number must have
exactly two factors.


1 has only one factor:


1


--------------------------------------------------
COMMON MISTAKE 2
--------------------------------------------------

Starting the divisor from 1.


Wrong:


divisor = 1


We start from:


divisor = 2


because 1 divides every number.


--------------------------------------------------
COMMON MISTAKE 3
--------------------------------------------------

Checking all the way up to
the number itself.


For example:


while divisor < number:


This works but performs
unnecessary checks.


A better approach is:


while divisor * divisor <= number:


This checks only up to
the square root.


--------------------------------------------------
COMMON MISTAKE 4
--------------------------------------------------

Forgetting:


number % divisor == 0


This is the condition that
tells us whether a divisor exists.


--------------------------------------------------
COMMON MISTAKE 5
--------------------------------------------------

Forgetting to increase
the divisor.


We need:


divisor += 1


Otherwise, the loop could
continue checking the same
divisor forever.


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:


"How do you check whether
a number is prime?"


You can say:


"I first check whether the number
is less than or equal to 1. If it is,
I return false. Otherwise, I check
possible divisors starting from 2
up to the square root of the number.
If any divisor divides the number
exactly, it is not prime. If no
divisor is found, the number is prime."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Prime number


A number greater than 1
with exactly two factors.


2. `%` operator


Used to check divisibility.


3. `number % divisor == 0`


Means a divisor was found.


4. `while` loop


Repeats the divisor checking.


5. `divisor * divisor <= number`


Checks only up to the square root.


6. `return False`


The number is not prime.


7. `return True`


The number is prime.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

For checking a prime:


NUMBER > 1?


        ↓


YES


        ↓


START divisor = 2


        ↓


CHECK:


number % divisor == 0?


        ↓


YES → NOT PRIME


        ↓


NO


        ↓


NEXT DIVISOR


        ↓


STOP AT √NUMBER


        ↓


NO DIVISOR FOUND


        ↓


PRIME


Easy rule:


CHECK → DIVIDE → FIND OR CONTINUE


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

Question:

Check whether 29 is prime.


        ↓


number = 29


        ↓


29 > 1


        ↓


Start:


divisor = 2


        ↓


Check 2:


29 % 2 ≠ 0


        ↓


Check 3:


29 % 3 ≠ 0


        ↓


Check 4:


29 % 4 ≠ 0


        ↓


Check 5:


29 % 5 ≠ 0


        ↓


Next divisor = 6


        ↓


6 × 6 > 29


        ↓


Stop


        ↓


No divisor found


        ↓


return True


        ↓


Prime


--------------------------------------------------
MAIN THING TO REMEMBER
--------------------------------------------------

A prime number:


1. Must be greater than 1.

2. Must have exactly two factors:
   1 and itself.

3. Start checking divisors from 2.

4. Check only up to the square root.

5. If a divisor is found:


   number % divisor == 0


   → NOT PRIME


6. If no divisor is found:


   → PRIME


MOST IMPORTANT CODE PATTERN:


if number <= 1:
    return False

divisor = 2

while divisor * divisor <= number:

    if number % divisor == 0:
        return False

    divisor += 1

return True


MEMORY:


GREATER THAN 1
        ↓
CHECK DIVISORS
        ↓
UP TO √NUMBER
        ↓
DIVISOR FOUND → NOT PRIME
        ↓
NO DIVISOR → PRIME
"""