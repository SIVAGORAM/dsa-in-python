def main():
    # Question 5: Check if a given year is a leap year.
    year = 2024

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap year")
    else:
        print("Not a leap year")


if __name__ == "__main__":
    main()


"""
Explanation:
The value stored in `year` is the input that the condition works on.

A year is a leap year if:
- It is divisible by 400, OR
- It is divisible by 4 AND not divisible by 100.

Only the branch whose condition becomes true prints its message.
"""