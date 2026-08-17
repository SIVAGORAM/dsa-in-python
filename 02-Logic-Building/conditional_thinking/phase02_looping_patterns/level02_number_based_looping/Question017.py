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
    # Question 17: Print all prime numbers between 1 and 100.
    n = 100

    for number in range(2, n + 1):
        if isPrime(number):
            print(number)


if __name__ == "__main__":
    main()


"""
QUESTION:

Print all prime numbers between 1 and 100.


--------------------------------------------------
WHAT DOES THE QUESTION MEAN?
--------------------------------------------------

We need to find and print every prime
number between 1 and 100.


A prime number is a number greater than 1
that has exactly two factors:


1. 1
2. The number itself


Examples:

2 → factors: 1, 2

3 → factors: 1, 3

5 → factors: 1, 5

7 → factors: 1, 7


Therefore:

2, 3, 5, 7 are prime numbers.


But:

4


has factors:

1, 2, 4


It has more than two factors.


Therefore:

4 is NOT a prime number.


--------------------------------------------------
EXPECTED OUTPUT
--------------------------------------------------

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


--------------------------------------------------
SOLUTION
--------------------------------------------------

We use two parts:


1. `isPrime(number)`

Checks whether one number
is prime or not.


2. `for` loop

Checks every number from
2 to 100.


The main logic is:


for number in range(2, n + 1):


For every number:


if isPrime(number):


If the number is prime,
we print it.


--------------------------------------------------
WHY DO WE START FROM 2?
--------------------------------------------------

We start from:

2


because:

0 and 1 are not prime numbers.


The smallest prime number is:

2


Therefore:


range(2, n + 1)


is used.


--------------------------------------------------
STEP 1 — CHECK number <= 1
--------------------------------------------------

Code:

if number <= 1:
    return False


Any number less than or equal to 1
is not prime.


Examples:


0 → Not prime

1 → Not prime

-5 → Not prime


Therefore, we immediately return:

False


--------------------------------------------------
STEP 2 — START divisor AT 2
--------------------------------------------------

Code:

divisor = 2


We start checking possible divisors
from 2.


Why?


Because every number is divisible by 1,
so checking 1 does not help us determine
whether the number is prime.


For example:


7 % 1 = 0


That doesn't tell us whether 7
is prime.


So we start with:

2


--------------------------------------------------
STEP 3 — CHECK divisor * divisor
--------------------------------------------------

Code:

while divisor * divisor <= number:


This is an important optimization.


Instead of checking every number
up to `number - 1`, we only check
possible divisors up to the square root
of the number.


For example:


For 100:


10 * 10 = 100


So we only need to check divisors
up to 10.


--------------------------------------------------
WHY ONLY UP TO THE SQUARE ROOT?
--------------------------------------------------

Suppose a number has two factors:


a × b = number


If both `a` and `b` were greater
than the square root of the number,
their product would be greater
than the number.


Therefore, if a number has a divisor,
at least one divisor must be less than
or equal to its square root.


Example:


36


Square root of 36:


6


Factor pairs:


1 × 36

2 × 18

3 × 12

4 × 9

6 × 6


We only need to check up to:

6


Once we reach 6, we have checked
everything necessary.


--------------------------------------------------
STEP 4 — CHECK DIVISIBILITY
--------------------------------------------------

Code:

if number % divisor == 0:
    return False


The `%` operator gives the remainder.


If:


number % divisor == 0


then `divisor` divides the number
exactly.


Therefore, the number has a divisor
other than 1 and itself.


So it cannot be prime.


We immediately return:

False


--------------------------------------------------
STEP 5 — MOVE TO THE NEXT DIVISOR
--------------------------------------------------

Code:

divisor += 1


This means:


divisor = divisor + 1


Example:


2 → 3 → 4 → 5 → 6 ...


We continue checking possible
divisors.


--------------------------------------------------
STEP 6 — RETURN TRUE
--------------------------------------------------

Code:

return True


If the loop finishes without finding
any divisor, the number is prime.


Therefore:


return True


--------------------------------------------------
DRY RUN — isPrime(7)
--------------------------------------------------

Input:

number = 7


Check:


7 <= 1


False


So continue.


Initial:

divisor = 2


--------------------------------------------------
CHECK LOOP
--------------------------------------------------

Condition:


divisor * divisor <= number


2 * 2 <= 7


4 <= 7


True


Continue.


--------------------------------------------------
CHECK DIVISIBILITY
--------------------------------------------------

7 % 2


= 1


Not equal to 0.


Therefore:

2 is not a divisor.


Increase:

divisor = 3


--------------------------------------------------
CHECK LOOP AGAIN
--------------------------------------------------

3 * 3 <= 7


9 <= 7


False


The loop stops.


No divisor was found.


Therefore:


return True


So:

7 is prime.


--------------------------------------------------
DRY RUN — isPrime(9)
--------------------------------------------------

Input:

number = 9


Initial:

divisor = 2


Check:


2 * 2 <= 9


4 <= 9


True


Check:


9 % 2


= 1


Not divisible.


Increase:

divisor = 3


Check:


3 * 3 <= 9


9 <= 9


True


Check:


9 % 3


= 0


Divisible.


Therefore:

9 is NOT prime.


The function immediately returns:


False


--------------------------------------------------
MAIN LOOP DRY RUN
--------------------------------------------------

Code:


for number in range(2, n + 1):


Here:


n = 100


Therefore:


range(2, 101)


generates:


2, 3, 4, 5, ... 100


Each number is passed to:


isPrime(number)


--------------------------------------------------
NUMBER = 2
--------------------------------------------------

isPrime(2)


Check:


2 <= 1


False


divisor = 2


Check:


2 * 2 <= 2


4 <= 2


False


No divisor found.


Return:

True


Therefore:

print(2)


--------------------------------------------------
NUMBER = 3
--------------------------------------------------

isPrime(3)


Check:


2 * 2 <= 3


4 <= 3


False


No divisor found.


Return:

True


Print:


3


--------------------------------------------------
NUMBER = 4
--------------------------------------------------

isPrime(4)


Check:


2 * 2 <= 4


4 <= 4


True


Check:


4 % 2 == 0


True


Therefore:

return False


4 is not printed.


--------------------------------------------------
NUMBER = 5
--------------------------------------------------

isPrime(5)


2 * 2 <= 5


True


5 % 2


= 1


No divisor found.


Return:

True


Print:


5


--------------------------------------------------
PROCESS CONTINUES
--------------------------------------------------

The same logic is applied
to every number from 2 to 100.


Prime numbers are printed.


Non-prime numbers are skipped.


--------------------------------------------------
OUTPUT
--------------------------------------------------

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


--------------------------------------------------
IMPORTANT PYTHON CONCEPT
--------------------------------------------------

The most important concept
is the `%` operator.


Example:


10 % 2 = 0


So 2 divides 10 exactly.


But:


10 % 3 = 1


So 3 does not divide 10 exactly.


Therefore:


number % divisor == 0


means:


DIVISOR FOUND


--------------------------------------------------
IMPORTANT CONCEPT — SQUARE ROOT
--------------------------------------------------

This condition:


divisor * divisor <= number


allows us to check divisors only
up to the square root.


Instead of:


divisor <= number


we use:


divisor * divisor <= number


This makes the prime-checking
function more efficient.


For example:


To check 97:


2 × 2 = 4

3 × 3 = 9

4 × 4 = 16

5 × 5 = 25

6 × 6 = 36

7 × 7 = 49

8 × 8 = 64

9 × 9 = 81

10 × 10 = 100


When divisor becomes 10:


100 <= 97


False.


So we stop.


We don't need to check:

11, 12, 13, ... 96


--------------------------------------------------
WHY IS 1 NOT PRIME?
--------------------------------------------------

A prime number must have
exactly two factors:


1. 1
2. Itself


The number 1 has only one factor:


1


Therefore:

1 is NOT prime.


--------------------------------------------------
WHY IS 2 PRIME?
--------------------------------------------------

2 has exactly two factors:


1

2


Therefore:

2 is prime.


Also:

2 is the only even prime number.


Every other even number
is not prime because it is
divisible by 2.


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

Check:

11


Possible divisor:


2


11 % 2 = 1


No divisor found.


Next:


3 × 3 = 9


9 <= 11


Check:

11 % 3 = 2


No divisor.


Next:


4 × 4 = 16


16 > 11


Stop.


Therefore:


11 is prime.


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

Check:

15


Try divisor 2:


15 % 2 = 1


Try divisor 3:


15 % 3 = 0


A divisor was found.


Therefore:


15 is not prime.


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

Check:

25


Try:


2


25 % 2 = 1


Try:


3


25 % 3 = 1


Try:


4


25 % 4 = 1


Try:


5


25 % 5 = 0


Therefore:


25 is not prime.


--------------------------------------------------
EXAMPLE 5
--------------------------------------------------

Check:

29


Possible divisors only need
to be checked up to √29.


√29 is approximately:


5.38


So we check:


2, 3, 4, 5


29 is not divisible by any of them.


Therefore:


29 is prime.


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

2


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

11


Expected:

Prime


--------------------------------------------------

TEST CASE 4:

Input:

9


Expected:

Not prime


--------------------------------------------------

TEST CASE 5:

Input:

15


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
COMMON MISTAKE 1
--------------------------------------------------

Considering 1 as a prime number.


Wrong:


1 is prime.


Correct:


1 is NOT prime.


A prime number must have
exactly two factors.


--------------------------------------------------
COMMON MISTAKE 2
--------------------------------------------------

Checking divisors using:


while divisor <= number:


This works logically, but it performs
more checks than necessary.


Better:


while divisor * divisor <= number:


This checks only up to the
square root.


--------------------------------------------------
COMMON MISTAKE 3
--------------------------------------------------

Forgetting:


number % divisor == 0


This is the main condition
for checking whether a divisor
exists.


--------------------------------------------------
COMMON MISTAKE 4
--------------------------------------------------

Starting the main loop from 1.


Wrong:


range(1, n + 1)


We start from:


range(2, n + 1)


because 0 and 1 are not prime.


--------------------------------------------------
COMMON MISTAKE 5
--------------------------------------------------

Using `/` when integer division
is required.


For example:


number / 2


returns a float.


When integer division is required,
use:


number // 2


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:


"How do you check whether a number
is prime?"


You can say:


"I first handle numbers less than or
equal to 1 because they are not prime.
Then I check possible divisors starting
from 2 up to the square root of the
number. If any divisor divides the
number exactly, it is not prime.
If no divisor is found, the number
is prime."


If they ask:


"Why do you only check up to
the square root?"


You can say:


"If a number has a factor greater than
its square root, it must have a
corresponding factor smaller than
the square root. Therefore, checking
up to the square root is sufficient."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Prime number

A number greater than 1
with exactly two factors.


2. `%`

Used to check divisibility.


3. `number % divisor == 0`

Means a divisor was found.


4. `divisor * divisor <= number`

Checks only up to the square root.


5. `return False`

Immediately says the number
is not prime.


6. `return True`

Means no divisor was found,
so the number is prime.


7. `for` loop

Used to check every number
from 2 to 100.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

For checking a prime number:


START FROM 2


↓

CHECK DIVISIBILITY


↓

`number % divisor == 0`?


↓

YES → NOT PRIME


↓

NO → NEXT DIVISOR


↓

CHECK UP TO √NUMBER


↓

NO DIVISOR FOUND


↓

PRIME


Easy pattern:


CHECK → DIVIDE → STOP OR CONTINUE


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

Question:

Print all prime numbers
between 1 and 100.


        ↓


Start from 2


        ↓


Check:

2


        ↓


Prime → Print


        ↓


Check:

3


        ↓


Prime → Print


        ↓


Check:

4


        ↓


Divisible by 2


        ↓


Not prime → Skip


        ↓


Continue until 100


        ↓


Print only numbers for which:


isPrime(number) == True


        ↓


Final output:


2, 3, 5, 7, 11, 13, 17, 19,
23, 29, 31, 37, 41, 43, 47,
53, 59, 61, 67, 71, 73, 79,
83, 89, 97


--------------------------------------------------
MAIN THING TO REMEMBER
--------------------------------------------------

A prime number:


1. Must be greater than 1.

2. Must have exactly two factors:
   1 and itself.

3. We can check divisors starting
   from 2.

4. We only need to check up to
   the square root.

5. If any divisor is found:


   number % divisor == 0


   → NOT PRIME


6. If no divisor is found:


   → PRIME


MOST IMPORTANT PATTERN:


if number <= 1:
    return False


divisor = 2


while divisor * divisor <= number:

    if number % divisor == 0:
        return False

    divisor += 1


return True


For printing all primes:


for number in range(2, n + 1):

    if isPrime(number):
        print(number)


MEMORY:


GREATER THAN 1 → CHECK DIVISORS → √NUMBER → PRIME
"""