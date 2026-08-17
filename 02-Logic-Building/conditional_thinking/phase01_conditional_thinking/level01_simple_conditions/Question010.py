def main():
    # Question 10: Take a character and check whether it's uppercase,
    # lowercase, a digit, or a special character.
    ch = 'A'

    if ch.isupper():
        print("Uppercase")
    elif ch.islower():
        print("Lowercase")
    elif ch.isdigit():
        print("Digit")
    else:
        print("Special character")


if __name__ == "__main__":
    main()


"""
Explanation:
The value stored in `ch` is the input that the conditions work on.

The conditions check the character in order:
- `ch.isupper()` → Uppercase
- `ch.islower()` → Lowercase
- `ch.isdigit()` → Digit
- Otherwise → Special character

Only the branch whose condition becomes true prints its message.
"""