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


"""
QUESTION:

Print the factorial of a given number.


WHAT DOES THE QUESTION MEAN?

The factorial of a number means multiplying that number
by every positive integer smaller than it down to 1.

For example:

5 factorial

is written as:

5!

And:

5! = 5 × 4 × 3 × 2 × 1

= 120


Therefore:

5! = 120


--------------------------------------------------
WHAT IS FACTORIAL?
--------------------------------------------------

For a positive number n:

n! = n × (n - 1) × (n - 2) × ... × 2 × 1


Examples:

1! = 1

2! = 2 × 1
   = 2

3! = 3 × 2 × 1
   = 6

4! = 4 × 3 × 2 × 1
   = 24

5! = 5 × 4 × 3 × 2 × 1
   = 120


--------------------------------------------------
IMPORTANT FACT
--------------------------------------------------

0! = 1


This is an important factorial rule.


So:

0! = 1

1! = 1


--------------------------------------------------
SOLUTION LOGIC
--------------------------------------------------

Given:

number = 5


We create:

result = 1


Why?

Because we are going to multiply values together.


Then:

for value in range(2, number + 1):


For:

number = 5


this becomes:

range(2, 6)


which generates:

2
3
4
5


Then we multiply each value into `result`.


--------------------------------------------------
WHY result = 1?
--------------------------------------------------

We are performing multiplication.

We should start with:

result = 1


Then:

1 × 2 = 2

2 × 3 = 6

6 × 4 = 24

24 × 5 = 120


If we started with:

result = 0


then:

0 × 2 = 0

0 × 3 = 0

0 × 4 = 0

...


The final result would always be 0.


Therefore, for multiplication accumulators,
we start with:

result = 1


--------------------------------------------------
DRY RUN
--------------------------------------------------

Given:

number = 5


Initial:

result = 1


--------------------------------------------------

ITERATION 1:

value = 2


Execute:

result *= value


This means:

result = result * value


So:

result = 1 * 2

result = 2


--------------------------------------------------

ITERATION 2:

value = 3


result = 2 * 3

result = 6


--------------------------------------------------

ITERATION 3:

value = 4


result = 6 * 4

result = 24


--------------------------------------------------

ITERATION 4:

value = 5


result = 24 * 5

result = 120


--------------------------------------------------

Loop finishes.


Return:

120


--------------------------------------------------
DRY RUN TABLE
--------------------------------------------------

| Iteration | value | Previous result | Calculation | New result |
|----------:|------:|-----------------:|-------------|------------:|
| Start | - | - | Initial value | 1 |
| 1 | 2 | 1 | 1 × 2 | 2 |
| 2 | 3 | 2 | 2 × 3 | 6 |
| 3 | 4 | 6 | 6 × 4 | 24 |
| 4 | 5 | 24 | 24 × 5 | 120 |


--------------------------------------------------
FINAL CALCULATION
--------------------------------------------------

5!

= 5 × 4 × 3 × 2 × 1

= 120


Output:

5! = 120


--------------------------------------------------
HOW range() WORKS
--------------------------------------------------

The code uses:

range(2, number + 1)


For:

number = 5


it becomes:

range(2, 6)


Python includes:

2


and excludes:

6


Therefore:

2
3
4
5


These are exactly the numbers we need to multiply.


--------------------------------------------------
WHY DO WE START FROM 2?
--------------------------------------------------

Factorial is:

5 × 4 × 3 × 2 × 1


But we start:

result = 1


So multiplying by 1 is unnecessary:

1 × 1 = 1


Therefore we can start the loop from:

2


This gives:

2
3
4
5


and produces:

1 × 2 × 3 × 4 × 5

= 120


This is the same factorial result.


--------------------------------------------------
EXAMPLE 2
--------------------------------------------------

number = 3


Factorial:

3!

= 3 × 2 × 1

= 6


Dry run:

result = 1

1 × 2 = 2

2 × 3 = 6


Output:

3! = 6


--------------------------------------------------
EXAMPLE 3
--------------------------------------------------

number = 4


Factorial:

4!

= 4 × 3 × 2 × 1

= 24


Output:

4! = 24


--------------------------------------------------
EXAMPLE 4
--------------------------------------------------

number = 1


Factorial:

1!

= 1


The loop:

range(2, 2)


has no values.

So:

result = 1


Output:

1! = 1


--------------------------------------------------
EXAMPLE 5
--------------------------------------------------

number = 0


Factorial rule:

0! = 1


With the current function:

result = 1

range(2, 1)


has no values.

Therefore:

result = 1


Output:

0! = 1


--------------------------------------------------
TEST CASES
--------------------------------------------------

TEST CASE 1:

Input:

number = 5

Expected:

5! = 120


TEST CASE 2:

Input:

number = 3

Expected:

3! = 6


TEST CASE 3:

Input:

number = 4

Expected:

4! = 24


TEST CASE 4:

Input:

number = 1

Expected:

1! = 1


TEST CASE 5:

Input:

number = 0

Expected:

0! = 1


TEST CASE 6:

Input:

number = 6

Calculation:

6 × 5 × 4 × 3 × 2 × 1

= 720

Expected:

6! = 720


--------------------------------------------------
COMMON MISTAKE #1
--------------------------------------------------

Starting with:

result = 0


is WRONG for multiplication.


Because:

0 × anything = 0


Correct:

result = 1


--------------------------------------------------
COMMON MISTAKE #2
--------------------------------------------------

Forgetting to return the result.

The function calculates:

result = 120


But we need to send that value back to `main()`.

Therefore:

return result


is required.


--------------------------------------------------
COMMON MISTAKE #3
--------------------------------------------------

Wrong:

range(1, number)


For:

number = 5


this generates:

1
2
3
4


It does not include 5.


Correct:

range(2, number + 1)


which generates:

2
3
4
5


--------------------------------------------------
COMMON MISTAKE #4
--------------------------------------------------

Your original output was:

str(number) + "not  = " + ...


This would produce:

5not = 120


That is not the expected factorial notation.


Correct:

str(number) + "! = " + str(factorial(number))


Output:

5! = 120


--------------------------------------------------
IMPORTANT PYTHON CONCEPT:
FUNCTION
--------------------------------------------------

You created a separate function:

factorial(number)


Its job is:

Calculate factorial
    ↓
Return the result


Then `main()` calls it:

factorial(number)


For:

number = 5


the function returns:

120


Then `main()` prints it.


--------------------------------------------------
FUNCTION FLOW
--------------------------------------------------

main()
  ↓
number = 5
  ↓
factorial(5)
  ↓
result = 1
  ↓
multiply 2
  ↓
multiply 3
  ↓
multiply 4
  ↓
multiply 5
  ↓
return 120
  ↓
print 5! = 120


--------------------------------------------------
IMPORTANT ACCUMULATOR PATTERN
--------------------------------------------------

In Q6-Q8, we used an accumulator for addition:

total = 0

total += number


Here we use an accumulator for multiplication:

result = 1

result *= value


This is an extremely important pattern.


--------------------------------------------------
ADDITION VS MULTIPLICATION
--------------------------------------------------

SUM:

total = 0

for number in ...:
    total += number


PRODUCT:

result = 1

for value in ...:
    result *= value


Remember:

Addition → start with 0

Multiplication → start with 1


--------------------------------------------------
WHAT DOES *= MEAN?
--------------------------------------------------

This:

result *= value


means:

result = result * value


Example:

result = 6
value = 4


Then:

result *= value


means:

result = 6 * 4

result = 24


--------------------------------------------------
INTERVIEW EXPLANATION
--------------------------------------------------

If an interviewer asks:

"How did you calculate the factorial?"

You can say:

"I initialize the result to 1 and iterate from 2 through
the given number. During each iteration, I multiply the
current result by the loop variable. After the loop,
I return the accumulated result."


--------------------------------------------------
KEY CONCEPTS
--------------------------------------------------

1. Function

`factorial()` performs the calculation.


2. for loop

Used to iterate from 2 to n.


3. Accumulator

`result` stores the running product.


4. Multiplication assignment

`result *= value`

means:

`result = result * value`


5. return

Sends the calculated factorial back to the caller.


6. range()

`range(2, number + 1)` includes 2 through number.


--------------------------------------------------
MEMORY TRICK
--------------------------------------------------

For SUM:

Start with:

0


For PRODUCT / FACTORIAL:

Start with:

1


Factorial pattern:

result = 1

for value in range(2, number + 1):
    result *= value

return result


Think:

START WITH 1
     ↓
MULTIPLY
     ↓
MULTIPLY
     ↓
MULTIPLY
     ↓
FINAL PRODUCT


--------------------------------------------------
Q6-Q9 CONNECTION
--------------------------------------------------

Q6:

Sum of first n numbers

Uses:

total = 0

total += number


Q7:

Sum of even numbers

Uses:

total = 0

if number % 2 == 0:
    total += number


Q8:

Sum of odd numbers

Uses:

total = 0

if number % 2 != 0:
    total += number


Q9:

Factorial

Uses:

result = 1

result *= value


The important new concept is:

MULTIPLICATION ACCUMULATOR.


--------------------------------------------------
FINAL LOGIC
--------------------------------------------------

number = 5

        ↓

factorial(5)

        ↓

result = 1

        ↓

1 × 2 = 2

        ↓

2 × 3 = 6

        ↓

6 × 4 = 24

        ↓

24 × 5 = 120

        ↓

return 120

        ↓

5! = 120


MAIN THINGS TO REMEMBER:

1. Factorial means multiplying all positive integers
   from 1 through n.
2. `0! = 1`.
3. Start multiplication accumulator with `1`.
4. Use `result *= value`.
5. Use `range(2, number + 1)`.
6. Return the calculated result.
7. `number++` is not used in Python.
"""