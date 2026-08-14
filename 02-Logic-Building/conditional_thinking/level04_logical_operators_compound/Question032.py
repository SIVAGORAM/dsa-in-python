def main():
    # Question 32: Take a number and print "Fizz" if divisible by 3,
    # "Buzz" if divisible by 5, and "FizzBuzz" if divisible by both.
    number = 25

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


if __name__ == "__main__":
    main()


"""
Explanation:

The question asks us to check a number for divisibility by 3 and 5.

There are four possible cases:

1. Divisible by both 3 and 5 → FizzBuzz
2. Divisible only by 3 → Fizz
3. Divisible only by 5 → Buzz
4. Divisible by neither → Print the number


Why do we check "both" first?

Suppose:

number = 15

15 is divisible by 3:
15 % 3 = 0

15 is also divisible by 5:
15 % 5 = 0

So it must print:

FizzBuzz

If we checked divisibility by 3 first, the program would print
"Fizz" and never reach the FizzBuzz case.

Therefore, the order should be:

1. Both
2. Only 3
3. Only 5
4. Neither


Dry Run:

Given:

number = 25


Step 1:

Check:

number % 3 == 0 and number % 5 == 0

25 % 3 = 1
25 % 5 = 0

So:

False and True → False

Move to the next condition.


Step 2:

Check:

number % 3 == 0

25 % 3 = 1

False

Move to the next condition.


Step 3:

Check:

number % 5 == 0

25 % 5 = 0

True

Therefore:

Buzz


Output:

Buzz


Another Example:

number = 9

9 % 3 = 0
9 % 5 = 4

So:

Divisible by 3 → True
Divisible by 5 → False

Output:

Fizz


Another Example:

number = 15

15 % 3 = 0
15 % 5 = 0

Both are True.

Output:

FizzBuzz


Another Example:

number = 7

7 % 3 = 1
7 % 5 = 2

Both are False.

Output:

7


Test Cases:

1. Input: 15
   Output: FizzBuzz

2. Input: 30
   Output: FizzBuzz

3. Input: 9
   Output: Fizz

4. Input: 12
   Output: Fizz

5. Input: 25
   Output: Buzz

6. Input: 10
   Output: Buzz

7. Input: 7
   Output: 7

8. Input: 11
   Output: 11

9. Input: 0
   Output: FizzBuzz


Key Concepts:

%  → Remainder

number % 3 == 0
→ Number is divisible by 3.

number % 5 == 0
→ Number is divisible by 5.

and
→ Both conditions must be True.

if
→ Checks the first condition.

elif
→ Checks the next condition if the previous one was False.

else
→ Runs when all previous conditions are False.


Important:

The most important logic in this problem is:

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")

The FizzBuzz condition must be checked BEFORE the individual
Fizz and Buzz conditions.
"""