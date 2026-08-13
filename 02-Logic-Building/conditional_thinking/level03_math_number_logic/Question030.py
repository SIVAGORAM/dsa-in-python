def main():
    # Question 30: Check whether a number is a perfect square
    # without using the square root function.
    number = 49

    perfect_square = False
    i = 1

    while i * i <= number:
        if i * i == number:
            perfect_square = True
            break

        i += 1

    print("Perfect square" if perfect_square else "Not a perfect square")


if __name__ == "__main__":
    main()


"""
Explanation:

The question asks us to check whether a number is a perfect square
without using the square root function.

A perfect square is a number that can be obtained by multiplying
a whole number by itself.

Examples:

1 × 1 = 1
2 × 2 = 4
3 × 3 = 9
4 × 4 = 16
5 × 5 = 25
6 × 6 = 36
7 × 7 = 49


Example:

number = 49


Step 1:

We start with:

i = 1

Then check:

i * i <= number

1 * 1 <= 49
1 <= 49 → True

So the loop runs.


Step 2:

Check:

i * i == number

1 * 1 == 49
1 == 49 → False

Increase `i`:

i = 2


Step 3:

Check:

2 * 2 == 49
4 == 49 → False

Increase `i`:

i = 3


The program continues:

3 * 3 = 9
4 * 4 = 16
5 * 5 = 25
6 * 6 = 36


Step 4:

When:

i = 7

Check:

7 * 7 == 49
49 == 49 → True

Therefore:

perfect_square = True

Then `break` stops the loop because we already found the answer.


Finally:

perfect_square = True

So the output is:

Perfect square


Example of a number that is NOT a perfect square:

number = 20

We check:

1 * 1 = 1
2 * 2 = 4
3 * 3 = 9
4 * 4 = 16
5 * 5 = 25

When `i = 5`:

25 <= 20 → False

The loop stops.

We never found:

i * i == 20

Therefore:

perfect_square = False

Output:

Not a perfect square


Why do we use `i * i <= number`?

There is no need to keep checking values after `i * i`
becomes greater than the number.

For example, if:

number = 20

When:

5 * 5 = 25

25 is already greater than 20.

Any larger value of `i` will produce an even larger square,
so the number cannot be a perfect square.


What does `break` do?

`break` immediately stops the loop.

Once we find:

i * i == number

there is no reason to continue searching.


Test Cases:

1. Input: 49
   Output: Perfect square

2. Input: 25
   Output: Perfect square

3. Input: 1
   Output: Perfect square

4. Input: 0
   Output: Not a perfect square

5. Input: 16
   Output: Perfect square

6. Input: 20
   Output: Not a perfect square

7. Input: 50
   Output: Not a perfect square

8. Input: 81
   Output: Perfect square


Key Concepts:

`while` → Repeats code while a condition is True.

`i * i` → Calculates the square of `i`.

`break` → Immediately stops the loop.

`+= 1` → Increases `i` by 1.

Boolean variable:
`perfect_square = False`

When a perfect square is found:

`perfect_square = True`

Important:

This solution does NOT use a square-root function.

Also remember that this is a Python `while` loop:

while condition:
    # code

Not a Java-style loop such as:

for (int i = 1; ...; i++)

The `print()` statement happens after the loop finishes.
"""