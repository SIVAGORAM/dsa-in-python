def main():
    # Question 3: Check if a number is divisible by 5.
    number = 25

    if number % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")


if __name__ == "__main__":
    main()


"""
Explanation:
The value stored in `number` is the input that the condition works on.

The condition `number % 5 == 0` checks whether the number is
divisible by 5 without a remainder.

Only the branch whose condition is true prints its message.
"""