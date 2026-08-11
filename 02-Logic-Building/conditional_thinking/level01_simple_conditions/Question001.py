def main():
    # Question 1: Take a number and print whether it's positive, negative, or zero.
    number = -7

    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")


if __name__ == "__main__":
    main()


"""
Explanation:
The value stored in `number` is the input that the conditions work on.

The `if`, `elif`, and `else` statements check the possible cases:
- `number > 0` → Positive
- `number < 0` → Negative
- Otherwise → Zero

Only the branch whose condition is true will execute and print the result.
"""