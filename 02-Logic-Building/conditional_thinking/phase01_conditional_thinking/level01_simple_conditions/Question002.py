def main():
    # Question 2: Check if a number is even or odd.
    number = 18

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == "__main__":
    main()


"""
Explanation:
The value stored in `number` is the input that the condition works on.

The condition `number % 2 == 0` checks whether the number is
even. If the remainder is 0, the number is even; otherwise, it is odd.

Only the branch whose condition is true prints its message.
"""