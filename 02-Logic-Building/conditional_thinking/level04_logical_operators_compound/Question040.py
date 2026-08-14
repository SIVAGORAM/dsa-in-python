def main():
    # Question 40: Take a password string and check basic rules
    # (length >= 8 and contains at least one digit).
    password = "Code123not"

    has_digit = False

    for ch in password:
        if ch.isdigit():
            has_digit = True
            break

    if len(password) >= 8 and has_digit:
        print("Valid password")
    else:
        print("Invalid password")


if __name__ == "__main__":
    main()


"""
Explanation:

The question asks us to check two basic password rules:

1. The password must contain at least 8 characters.
2. The password must contain at least one digit.


We use a Boolean variable:

has_digit = False

Initially, we assume that the password does not contain a digit.

Then we check each character in the password.

If we find a digit:

has_digit = True

We can then stop checking because we already found a digit.


Example:

password = "Code123not"


Step 1: Check the length.

len(password)

The password contains 10 characters.

Therefore:

10 >= 8 → True


Step 2: Check whether the password contains a digit.

We inspect the characters one by one:

C → not a digit
o → not a digit
d → not a digit
e → not a digit
1 → digit found

So:

has_digit = True


Step 3: Check both conditions.

len(password) >= 8 and has_digit

True and True → True

Therefore:

Valid password


Dry Run:

Given:

password = "Code123not"

Initially:

has_digit = False


Loop:

ch = 'C'
'C'.isdigit() → False

ch = 'o'
'o'.isdigit() → False

ch = 'd'
'd'.isdigit() → False

ch = 'e'
'e'.isdigit() → False

ch = '1'
'1'.isdigit() → True

Therefore:

has_digit = True

Then `break` stops the loop because we already found a digit.


Now check:

len(password) >= 8
10 >= 8 → True

has_digit
True

Therefore:

True and True → True

Output:

Valid password


Another Example:

password = "Hello123"

Length:

len("Hello123") = 8

8 >= 8 → True

The password contains:

1, 2, 3

So:

has_digit = True

Therefore:

Valid password


Another Example:

password = "Password"

Length:

len("Password") = 8

8 >= 8 → True

But there is no digit.

Therefore:

has_digit = False

Final condition:

True and False → False

Output:

Invalid password


Another Example:

password = "Code1"

Length:

len("Code1") = 5

5 >= 8 → False

There is a digit:

has_digit = True

But:

False and True → False

Therefore:

Invalid password


Boundary Example:

password = "abcdefg1"

Length:

8 characters

8 >= 8 → True

Contains digit:

1 → True

Therefore:

Valid password


Test Cases:

1. Input:
   password = "Code123not"

   Output:
   Valid password


2. Input:
   password = "Hello123"

   Output:
   Valid password


3. Input:
   password = "Password"

   Output:
   Invalid password


4. Input:
   password = "Code1"

   Output:
   Invalid password


5. Input:
   password = "abcdefg1"

   Output:
   Valid password


6. Input:
   password = "12345678"

   Output:
   Valid password


7. Input:
   password = "abcdefgh"

   Output:
   Invalid password


8. Input:
   password = "abc1"

   Output:
   Invalid password


Key Concepts:

`len()` → Returns the length of a string.

`isdigit()` → Checks whether a character is a digit.

`for` → Used to inspect each character in the string.

Boolean variable → Stores True or False.

`break` → Stops the loop immediately.

`and` → Both conditions must be True.


Important:

The question asks only for:

1. Length >= 8
2. At least one digit

It does NOT require:

- Uppercase letter
- Lowercase letter
- Special character

So we don't need:

has_upper
has_lower
has_special


Python string loop:

for ch in password:

This directly gives us each character.

We don't need Java-style code such as:

int i = 0
password.length()
password.charAt(i)

In Python:

len(password) → Gets length

for ch in password → Gets each character


Main Logic:

Password length >= 8
        AND
Contains at least one digit
        ↓
Both True → Valid password
Any one False → Invalid password
"""