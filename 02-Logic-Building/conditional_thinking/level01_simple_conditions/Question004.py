def main():
    # Question 4: Check if a number is divisible by both 3 and 5.
    number = 45

    if number % 3 == 0 and number % 5 == 0:
        print("Divisible by both 3 and 5")
    else:
        print("Not divisible by both 3 and 5")


if __name__ == "__main__":
    main()


"""
Explanation:
The value stored in `number` is the input that the conditions work on.

The conditions `number % 3 == 0` and `number % 5 == 0`
check whether the number is divisible by both 3 and 5.

The `and` operator requires both conditions to be True.

Only the branch whose condition becomes true prints its message.
"""