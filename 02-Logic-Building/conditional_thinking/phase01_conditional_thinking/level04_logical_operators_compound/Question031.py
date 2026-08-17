def main():
    # Question 31: Take a character and check if it is a letter, a digit, or neither.
    ch = '9'

    if ch.isalpha():
        print("Letter")
    elif ch.isdigit():
        print("Digit")
    else:
        print("Neither")


if __name__ == "__main__":
    main()


"""
Explanation:

The question asks us to take a character and determine whether it is:

1. A letter
2. A digit
3. Neither a letter nor a digit


We check the conditions in order.

First:

ch.isalpha()

This checks whether the character is an alphabetic letter.

Example:

ch = 'A'

'A'.isalpha() → True

Therefore:

Letter


Second:

ch.isdigit()

This checks whether the character is a digit.

Example:

ch = '9'

'9'.isdigit() → True

Therefore:

Digit


If both conditions are False, the character is neither a letter
nor a digit.

For example:

ch = '@'

'@'.isalpha() → False
'@'.isdigit() → False

Therefore:

Neither


Dry Run:

Given:

ch = '9'


Step 1:

if ch.isalpha():

'9'.isalpha() → False

So this block is skipped.


Step 2:

elif ch.isdigit():

'9'.isdigit() → True

Therefore:

print("Digit")

Output:

Digit


Another Example:

ch = 'A'

Step 1:

'A'.isalpha() → True

Output:

Letter

The `elif` and `else` blocks are not checked because the first
condition was already True.


Another Example:

ch = '#'

'#'.isalpha() → False
'#'.isdigit() → False

Therefore:

Neither


Test Cases:

1. Input: 'A'
   Output: Letter

2. Input: 'z'
   Output: Letter

3. Input: '9'
   Output: Digit

4. Input: '0'
   Output: Digit

5. Input: '@'
   Output: Neither

6. Input: '#'
   Output: Neither

7. Input: ' '
   Output: Neither


Key Concepts:

`isalpha()`  → Checks whether a string contains alphabetic characters.

`isdigit()`  → Checks whether a string contains digits.

`if`         → Checks the first condition.

`elif`       → Checks another condition if the previous condition
               was False.

`else`       → Executes when all previous conditions are False.


Important Python Difference:

Python:

ch.isalpha()
ch.isdigit()

Java:

Character.isLetter(ch)
Character.isDigit(ch)

Since you are learning Python, remember the Python versions.
"""